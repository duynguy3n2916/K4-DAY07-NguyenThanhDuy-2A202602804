"""Reproduce the personal experiment offline: python scripts/run_personal.py.

TF-IDF is a lexical baseline, not a semantic embedding model. No gold answers
or expected document IDs are used during retrieval or answer generation.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from sklearn.feature_extraction.text import TfidfVectorizer
from src import (ChunkingStrategyComparator, Document, EmbeddingStore,
                 FixedSizeChunker, KnowledgeBaseAgent, RecursiveChunker,
                 SentenceChunker, compute_similarity, _mock_embed)


def load_corpus():
    docs = []
    for path in sorted((ROOT / "data/academic_regulations").glob("*.md")):
        _, header, body = path.read_text(encoding="utf-8-sig").split("---", 2)
        metadata = dict(line.split(": ", 1) for line in header.strip().splitlines())
        required = {"doc_id", "audience", "source_url", "retrieved_at", "document_version"}
        if not required <= metadata.keys():
            raise ValueError(f"Missing metadata: {path}")
        docs.append(Document(metadata["doc_id"], body.strip(), metadata))
    return docs


def extract_context(prompt):
    """Offline answerer: quote retrieved context, without inventing an LLM answer."""
    context = prompt.split("<context>\n", 1)[1].split("\n</context>", 1)[0]
    return "[Trích xuất ngữ cảnh; không dùng LLM]\n" + context


def main():
    docs = load_corpus()
    queries = json.loads((ROOT / "data/academic_regulations/benchmark.json").read_text(encoding="utf-8"))
    predictions = json.loads((ROOT / "report/similarity_predictions.json").read_text(encoding="utf-8"))
    # Fit only on the corpus, never on benchmark queries or gold answers.
    vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1, 2), norm="l2")
    vectorizer.fit([d.content for d in docs])
    embed = lambda text: vectorizer.transform([text]).toarray()[0].tolist()
    output = {"backend": "TF-IDF word 1-2 grams, L2; fitted on 10 source bodies only",
              "answerer": "extract_context (offline, no LLM)", "inventory": [],
              "baseline": {}, "strategies": {}, "predictions": []}
    for doc in docs:
        chunks = SentenceChunker(max_sentences_per_chunk=3).chunk(doc.content)
        output["inventory"].append({"doc_id": doc.id, "chunks": len(chunks),
                                    "characters": sum(map(len, chunks))})
    for doc in docs[:3]:
        output["baseline"][doc.id] = ChunkingStrategyComparator().compare(doc.content, 500)
    for name, chunker in {"sentence3": SentenceChunker(max_sentences_per_chunk=3),
                          "fixed500_overlap50": FixedSizeChunker(500, 50),
                          "recursive500": RecursiveChunker(chunk_size=500)}.items():
        chunks = [Document(f"{doc.id}::c{i:02}", chunk, {**doc.metadata, "chunk_index": i})
                  for doc in docs for i, chunk in enumerate(chunker.chunk(doc.content), 1)]
        store = EmbeddingStore(embedding_fn=embed)
        store.add_documents(chunks)
        agent = KnowledgeBaseAgent(store, extract_context)
        results = []
        for query in queries:
            filters = query.get("metadata_filter")
            top = store.search_with_filter(query["query"], 3, filters)
            unfiltered = store.search(query["query"], 3)
            relevant = [r for r in top if r["metadata"]["doc_id"] in query["expected_doc_ids"]]
            evidence = " ".join(r["content"].lower() for r in relevant)
            terms = {term: term.lower() in evidence for term in query["answer_terms"]}
            results.append({**query, "top3": top, "unfiltered_top3": unfiltered,
                            "document_hit": bool(relevant), "answer_terms_found": terms,
                            "full_evidence": all(terms.values()),
                            "agent_answer": agent.answer(query["query"], 3, filters)})
        output["strategies"][name] = {"count": len(chunks),
            "avg_length": sum(len(c.content) for c in chunks) / len(chunks), "results": results}
    for pair in predictions:
        score = compute_similarity(embed(pair["a"]), embed(pair["b"]))
        output["predictions"].append({**pair, "score": score,
            "mock_score": compute_similarity(_mock_embed(pair["a"]), _mock_embed(pair["b"])),
            "matches": (score >= 0.5) == (pair["expected"] == "high")})
    (ROOT / "report/personal_results.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Bằng chứng thực nghiệm cá nhân", "",
             "Tái lập: `python scripts/run_personal.py`. Cần scikit-learn (requirements-personal.txt).",
             "", output["backend"], "", "Answerer chỉ trích lại ngữ cảnh, không phải LLM.", ""]
    for name, result in output["strategies"].items():
        lines += [f"## {name}", "", f"{result['count']} chunks; trung bình {result['avg_length']:.5f} ký tự.", ""]
        for query in result["results"]:
            lines += [f"### {query['id']}: {query['query']}", "",
                      f"Gold: {query['gold_answer']}", "",
                      f"Filter: `{query.get('metadata_filter')}`; đúng tài liệu: {query['document_hit']}; đủ cụm bằng chứng: {query['full_evidence']}.", ""]
            for rank, hit in enumerate(query["top3"], 1):
                lines += [f"**Top {rank}: {hit['id']} — {hit['score']:.6f}**", "", hit["content"], ""]
            lines += ["**Đầu ra Agent (nguyên văn):**", "", query["agent_answer"], ""]
    (ROOT / "report/PERSONAL_EVIDENCE.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({name: {"count": r["count"], "avg": r["avg_length"],
        "document_hits": sum(q["document_hit"] for q in r["results"]),
        "full_evidence": sum(q["full_evidence"] for q in r["results"])}
        for name, r in output["strategies"].items()}, indent=2))


if __name__ == "__main__":
    main()
