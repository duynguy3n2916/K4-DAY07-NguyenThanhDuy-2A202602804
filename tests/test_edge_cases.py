import pytest

from src import (Document, EmbeddingStore, KnowledgeBaseAgent, RecursiveChunker,
                 SentenceChunker, FixedSizeChunker, compute_similarity)


def test_sentence_punctuation_empty_and_newline():
    assert SentenceChunker(3).chunk("  ") == []
    assert SentenceChunker(3).chunk("Một.\nHai! Ba? Bốn.") == ["Một. Hai! Ba?", "Bốn."]


def test_recursive_preserves_content_and_enforces_limit():
    text = "Đoạn một.\n\nĐoạn hai! " + "x" * 50
    for separators in (None, [], ["\n\n"]):
        chunks = RecursiveChunker(separators, 12).chunk(text)
        assert "".join(chunks) == text
        assert all(0 < len(c) <= 12 for c in chunks)


def test_invalid_sizes_and_vector_dimensions():
    with pytest.raises(ValueError):
        FixedSizeChunker(10, 10)
    with pytest.raises(ValueError):
        RecursiveChunker(chunk_size=0)
    with pytest.raises(ValueError):
        compute_similarity([1], [1, 2])


def test_filter_before_ranking_and_delete_all_parent_chunks():
    store = EmbeddingStore(embedding_fn=lambda text: [float(text), 1.0])
    store.add_documents([
        Document("p-1", "1", {"doc_id": "p", "audience": "student"}),
        Document("p-2", "2", {"doc_id": "p", "audience": "student"}),
        Document("q-1", "9", {"doc_id": "q", "audience": "staff"}),
    ])
    assert store.search("1", 0) == []
    assert store.search("1", -1) == []
    assert store.search_with_filter("1", 1, {"audience": "student"})[0]["id"] == "p-2"
    assert store.search_with_filter("1", 3, {"missing": None}) == []
    assert store.delete_document("p")
    assert store.get_collection_size() == 1
    assert not store.delete_document("p")


def test_agent_passes_question_sources_and_filtered_context():
    store = EmbeddingStore(embedding_fn=lambda _: [1.0])
    store.add_documents([
        Document("s", "student content", {"audience": "student", "source_url": "source-s"}),
        Document("f", "staff content", {"audience": "staff"}),
    ])
    prompts = []
    agent = KnowledgeBaseAgent(store, lambda prompt: prompts.append(prompt) or "answer")
    assert agent.answer("question", metadata_filter={"audience": "student"}) == "answer"
    assert all(part in prompts[0] for part in ["question", "student content", "source-s", "[s]"])
    assert "staff content" not in prompts[0]
    agent.answer("empty", metadata_filter={"audience": "absent"})
    assert len(prompts) == 1
