# Báo Cáo Cá Nhân — Lab 7: Embedding & Vector Store

**Họ tên:** Nguyễn Thanh Duy  
**MSSV:** 2A202602804  
**Nhóm:** Magician 
**Ngày:** 19/09/2026  

> **Nộp 1 bản / sinh viên.** Phần nhóm (lựa chọn tài liệu, thiết kế chiến lược, bộ câu hỏi đánh giá, demo) nộp chung 1 bản trong `REPORT_NHOM.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần cá nhân: 60** = Khởi động (5) + Hướng tiếp cận (10) + Hoàn thiện code (30) + Dự đoán độ tương tự (5) + Kết quả truy xuất của tôi (10).

---

## 1. Khởi động (Warm-up) — Cá nhân (5 điểm)

### Độ tương tự Cosine (Cosine Similarity) (Bài tập 1.1)

**Độ tương tự cosine cao (High cosine similarity) nghĩa là gì?**
> Độ tương tự cosine cao (tiến gần về 1.0) biểu thị rằng hai vector embedding chỉ về cùng một hướng trong không gian đa chiều, phản ánh hai đoạn văn bản có mức độ tương đồng rất lớn về mặt ngữ nghĩa hoặc phân bố từ vựng, độc lập với độ dài ngắn khác nhau của văn bản.

**Ví dụ có độ tương tự CAO:**
- Câu A: Sinh viên nộp đơn phúc khảo trong vòng bảy ngày.
- Câu B: Sinh viên phải nộp đơn phúc khảo trong vòng bảy ngày kể từ ngày công bố điểm.
- Tại sao tương đồng: Cả hai câu cùng diễn đạt một chủ đề hành chính học vụ (thời hạn nộp đơn phúc khảo điểm thi của người học), chia sẻ toàn bộ các từ khóa cốt lõi ("sinh viên", "nộp đơn", "phúc khảo", "bảy ngày") và hướng biểu diễn ngữ nghĩa gần như trùng khít.

**Ví dụ có độ tương tự THẤP:**
- Câu A: Sinh viên nộp đơn phúc khảo trong vòng bảy ngày.
- Câu B: Con mèo nằm ngủ dưới gốc cây.
- Tại sao khác: Hai câu thuộc hai lĩnh vực ngữ nghĩa và ngữ cảnh hoàn toàn tách biệt (quy chế học vụ đại học đối lập với hành vi động vật tự nhiên), không chứa từ vựng chung, khiến hai vector trực giao nhau và độ tương tự cosine bằng 0.0.

**Tại sao độ tương tự cosine (cosine similarity) được ưu tiên hơn khoảng cách Euclid (Euclidean distance) cho text embeddings?**
> Vì độ tương tự cosine chỉ quan tâm đến góc giữa hai vector (hướng biểu diễn ngữ nghĩa) và loại bỏ hoàn toàn ảnh hưởng của độ dài vector (magnitude/norm). Trong khi khoảng cách Euclid bị chi phối bởi độ dài văn bản (khiến một đoạn tóm tắt ngắn và một đoạn phân tích chi tiết cùng ý nghĩa bị coi là xa nhau), cosine similarity vẫn phản ánh chính xác sự tương đồng về nội dung.

### Bài toán tính toán Chunking (Bài tập 1.2)

**Tài liệu 10,000 ký tự, chunk_size=500, overlap=50. Bao nhiêu chunks?**
> *Trình bày phép tính:*
> - Chiều dài văn bản ($L$): $10{,}000$ ký tự.
> - Kích thước chunk ($C$): $500$ ký tự.
> - Độ chồng chéo ($O$): $50$ ký tự.
> - Bước nhảy giữa các chunk ($S = C - O$): $500 - 50 = 450$ ký tự.
> - Áp dụng công thức làm tròn lên:
>   $$\text{Số chunks} = \left\lceil \frac{L - O}{C - O} \right\rceil = \left\lceil \frac{10000 - 50}{500 - 50} \right\rceil = \left\lceil \frac{9950}{450} \right\rceil = \lceil 22{,}111... \rceil = 23$$
> - Cụ thể các vị trí cắt: Chunk 1 [0:500], Chunk 2 [450:950], ..., Chunk 22 [9450:9950], Chunk 23 [9900:10000].
> *Đáp án:* **23 chunks**.

**Nếu độ chồng chéo (overlap) tăng lên 100, số lượng chunk thay đổi thế nào? Tại sao muốn độ chồng chéo nhiều hơn?**
> Khi overlap tăng lên $100$, bước dịch chuyển giảm còn $500 - 100 = 400$ ký tự, số lượng chunk tăng lên $\lceil (10000 - 100) / 400 \rceil = \lceil 9900 / 400 \rceil = 25$ chunks (tăng thêm 2 chunks). Chúng ta muốn tăng overlap nhằm bảo toàn tính mạch lạc của ngữ cảnh tại các ranh giới cắt, ngăn ngừa hiện tượng một câu văn quan trọng hoặc một cụm điều khoản điều kiện bị xẻ đôi giữa hai chunk khiến mô hình embedding hoặc LLM mất thông tin.

---

## 2. Hướng tiếp cận của tôi (My Approach) — Cá nhân (10 điểm)

Giải thích cách tiếp cận khi lập trình các phần chính trong gói `src`:

### Các hàm chia nhỏ (Chunking Functions)

**`SentenceChunker.chunk`** — hướng tiếp cận:
> Sử dụng biểu thức chính quy `re.split(r"(?<=[.!?])\s+", text.strip())` với cơ chế positive lookbehind để phát hiện các ranh giới kết thúc câu tự nhiên (`.`, `!`, `?` theo sau bởi khoảng trắng) mà vẫn giữ nguyên vẹn dấu câu trong văn bản. Sau khi lọc bỏ các chuỗi rỗng, các câu được gom tuần tự thành từng khối tối đa `max_sentences_per_chunk` (chiến lược của tôi là 3 câu) bằng thao tác slicing `sentences[i:i + n]` và nối lại bằng `" ".join()`. Xử lý chặt chẽ các trường hợp biên (edge case) như văn bản rỗng trả về `[]`, văn bản không có dấu câu trả về một chunk duy nhất, và tham số `max_sentences_per_chunk` luôn được bảo vệ tối thiểu là 1.

**`RecursiveChunker.chunk` / `_split`** — hướng tiếp cận:
> Thuật toán hoạt động theo nguyên lý đệ quy chia để trị với danh sách các dấu phân tách có thứ tự ưu tiên giảm dần: `["\n\n", "\n", ". ", " ", ""]`. Trường hợp cơ sở (base case): nếu độ dài văn bản hiện tại $\le$ `chunk_size` thì trả về ngay; nếu danh sách dấu phân cách đã hết hoặc gặp `""` thì ủy quyền cho `FixedSizeChunker(self.chunk_size, 0)` cắt cứng. Nhằm bảo toàn nội dung tuyệt đối không làm mất ký tự phân cách, thuật toán dùng `re.split(f"({re.escape(separator)})", current_text)` để giữ lại delimiter và gộp lại vào mảnh văn bản liền trước trước khi tích lũy vào các chunk hoặc gọi đệ quy sâu hơn.

### Lớp EmbeddingStore

**`add_documents` + `search`** — hướng tiếp cận:
> Dữ liệu được lưu trữ trong bộ nhớ dưới dạng danh sách từ điển (`self._store: list[dict]`), mỗi bản ghi đóng gói `id`, `content`, `metadata` (bảo toàn `doc_id` cha) và `embedding` được tạo ra từ hàm nhúng tiêm vào (`_embedding_fn`). Quá trình nạp tài liệu tự động kiểm tra tính thống nhất về số chiều vector giữa các tài liệu. Khi tìm kiếm (`search`), truy vấn được vector hóa thông qua `_embedding_fn`, sau đó tính toán độ tương tự bằng tích vô hướng (`_dot`) với vector của từng bản ghi, rồi sắp xếp theo điểm số giảm dần để lấy ra `top_k` kết quả có độ tương tự cao nhất.

**`search_with_filter` + `delete_document`** — hướng tiếp cận:
> Áp dụng cơ chế **Pre-filtering (lọc trước)**: tiến hành duyệt và lọc danh sách các chunk thỏa mãn toàn bộ các điều kiện trong `metadata_filter` trước khi tính toán độ tương tự vector và sắp xếp ranking. Cách tiếp cận này đảm bảo luôn trả về đủ `top_k` kết quả hợp lệ cho đối tượng cần lọc (như `audience: student`) và tiết kiệm chi phí tính toán. Phương thức `delete_document` lọc bỏ toàn bộ các chunk có `metadata["doc_id"] == doc_id` bằng list comprehension và so sánh kích thước collection trước/sau để trả về `True` nếu có bản ghi bị xóa, ngược lại trả về `False`.

### Tác tử KnowledgeBaseAgent

**`answer`** — hướng tiếp cận:
> Xây dựng quy trình RAG hoàn chỉnh: gọi `store.search_with_filter` để truy xuất top-k chunks liên quan nhất kèm bộ lọc metadata. Ngữ cảnh được định dạng rõ ràng theo từng đoạn kèm ID và nguồn `[{chunk['id']}] {chunk['content']}\nNguồn: {source_url}`, sau đó được bọc bên trong cặp thẻ cấu trúc tường minh `<context>\n...\n</context>`. Cấu trúc prompt được thiết kế kiểm soát nghiêm ngặt hành vi suy diễn: chỉ thị rõ ràng chỉ trả lời dựa vào ngữ cảnh, trích dẫn mã chunk làm căn cứ, thừa nhận nếu thiếu dữ liệu, không tự suy đoán quy chế của trường và nhấn mạnh nội dung tài liệu là dữ liệu tham chiếu chứ không phải hướng dẫn thực thi.

---

## 3. Hoàn thiện code (Core Implementation) — Cá nhân (30 điểm)

Vượt qua bộ kiểm thử là điều kiện tính điểm phần này.

### Kết Quả Kiểm Thử (Test Results)

```
============================= test session starts =============================
platform win32 -- Python 3.10.11, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Acer\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Acer\OneDrive\Desktop\AI thực chiến\K4-DAY07-NguyenThanhDuy-2A202602804
plugins: anyio-4.12.0
collecting ... collected 47 items

tests/test_edge_cases.py::test_sentence_punctuation_empty_and_newline PASSED [  2%]
tests/test_edge_cases.py::test_recursive_preserves_content_and_enforces_limit PASSED [  4%]
tests/test_edge_cases.py::test_invalid_sizes_and_vector_dimensions PASSED [  6%]
tests/test_edge_cases.py::test_filter_before_ranking_and_delete_all_parent_chunks PASSED [  8%]
tests/test_edge_cases.py::test_agent_passes_question_sources_and_filtered_context PASSED [ 10%]
tests/test_solution.py::TestProjectStructure::test_root_main_entrypoint_exists PASSED [ 12%]
tests/test_solution.py::TestProjectStructure::test_src_package_exists PASSED [ 14%]
tests/test_solution.py::TestClassBasedInterfaces::test_chunker_classes_exist PASSED [ 17%]
tests/test_solution.py::TestClassBasedInterfaces::test_mock_embedder_exists PASSED [ 19%]
tests/test_solution.py::TestFixedSizeChunker::test_chunks_respect_size PASSED [ 21%]
tests/test_solution.py::TestFixedSizeChunker::test_correct_number_of_chunks_no_overlap PASSED [ 23%]
tests/test_solution.py::TestFixedSizeChunker::test_empty_text_returns_empty_list PASSED [ 25%]
tests/test_solution.py::TestFixedSizeChunker::test_no_overlap_no_shared_content PASSED [ 27%]
tests/test_solution.py::TestFixedSizeChunker::test_overlap_creates_shared_content PASSED [ 29%]
tests/test_solution.py::TestFixedSizeChunker::test_returns_list PASSED   [ 31%]
tests/test_solution.py::TestFixedSizeChunker::test_single_chunk_if_text_shorter PASSED [ 34%]
tests/test_solution.py::TestSentenceChunker::test_chunks_are_strings PASSED [ 36%]
tests/test_solution.py::TestSentenceChunker::test_respects_max_sentences PASSED [ 38%]
tests/test_solution.py::TestSentenceChunker::test_returns_list PASSED    [ 40%]
tests/test_solution.py::TestSentenceChunker::test_single_sentence_max_gives_many_chunks PASSED [ 42%]
tests/test_solution.py::TestRecursiveChunker::test_chunks_within_size_when_possible PASSED [ 44%]
tests/test_solution.py::TestRecursiveChunker::test_empty_separators_falls_back_gracefully PASSED [ 46%]
tests/test_solution.py::TestRecursiveChunker::test_handles_double_newline_separator PASSED [ 48%]
tests/test_solution.py::TestRecursiveChunker::test_returns_list PASSED   [ 51%]
tests/test_solution.py::TestEmbeddingStore::test_add_documents_increases_size PASSED [ 53%]
tests/test_solution.py::TestEmbeddingStore::test_add_more_increases_further PASSED [ 55%]
tests/test_solution.py::TestEmbeddingStore::test_initial_size_is_zero PASSED [ 57%]
tests/test_solution.py::TestEmbeddingStore::test_search_results_have_content_key PASSED [ 59%]
tests/test_solution.py::TestEmbeddingStore::test_search_results_have_score_key PASSED [ 61%]
tests/test_solution.py::TestEmbeddingStore::test_search_results_sorted_by_score_descending PASSED [ 63%]
tests/test_solution.py::TestEmbeddingStore::test_search_returns_at_most_top_k PASSED [ 65%]
tests/test_solution.py::TestEmbeddingStore::test_search_returns_list PASSED [ 68%]
tests/test_solution.py::TestKnowledgeBaseAgent::test_answer_non_empty PASSED [ 70%]
tests/test_solution.py::TestKnowledgeBaseAgent::test_answer_returns_string PASSED [ 72%]
tests/test_solution.py::TestComputeSimilarity::test_identical_vectors_return_1 PASSED [ 74%]
tests/test_solution.py::TestComputeSimilarity::test_opposite_vectors_return_minus_1 PASSED [ 76%]
tests/test_solution.py::TestComputeSimilarity::test_orthogonal_vectors_return_0 PASSED [ 78%]
tests/test_solution.py::TestComputeSimilarity::test_zero_vector_returns_0 PASSED [ 80%]
tests/test_solution.py::TestCompareChunkingStrategies::test_counts_are_positive PASSED [ 82%]
tests/test_solution.py::TestCompareChunkingStrategies::test_each_strategy_has_count_and_avg_length PASSED [ 85%]
tests/test_solution.py::TestCompareChunkingStrategies::test_returns_three_strategies PASSED [ 87%]
tests/test_solution.py::TestEmbeddingStoreSearchWithFilter::test_filter_by_department PASSED [ 89%]
tests/test_solution.py::TestEmbeddingStoreSearchWithFilter::test_no_filter_returns_all_candidates PASSED [ 91%]
tests/test_solution.py::TestEmbeddingStoreSearchWithFilter::test_returns_at_most_top_k PASSED [ 93%]
tests/test_solution.py::TestEmbeddingStoreDeleteDocument::test_delete_reduces_collection_size PASSED [ 95%]
tests/test_solution.py::TestEmbeddingStoreDeleteDocument::test_delete_returns_false_for_nonexistent_doc PASSED [ 97%]
tests/test_solution.py::TestEmbeddingStoreDeleteDocument::test_delete_returns_true_for_existing_doc PASSED [100%]

============================= 47 passed in 0.07s ==============================
```

**Số lượng bài test vượt qua (pass):** 47 / 47 (100% test case, bao gồm 42 test chuẩn trong `test_solution.py` và 5 test mở rộng trong `test_edge_cases.py`).

---

## 4. Dự đoán độ tương tự (Similarity Predictions) — Cá nhân (5 điểm)

| Cặp | Câu A | Câu B | Dự đoán | Điểm thực tế | Đúng? |
|:---:|---|---|:---:|:---:|:---:|
| 1 | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | cao (cao nhất) | 1.0000 | Đúng |
| 2 | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | Sinh viên phải nộp đơn phúc khảo trong vòng bảy ngày kể từ ngày công bố điểm. | cao | 0.6841 | Đúng |
| 3 | Sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ. | Sinh viên đăng ký tối thiểu 10 tín chỉ và tối đa 24 tín chỉ. | cao (chủ đề giống, số liệu khác) | 0.8046 | Đúng |
| 4 | Sinh viên được rút học phần trong vòng hai tuần. | Sinh viên không được rút học phần trong vòng hai tuần. | cao (từ ngữ giống, ngữ nghĩa phủ định) | 0.8575 | Đúng |
| 5 | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | Con mèo nằm ngủ dưới gốc cây. | thấp (thấp nhất) | 0.0000 | Đúng |

**Kết quả nào bất ngờ nhất? Điều này nói gì về cách embeddings biểu diễn ý nghĩa?**
> Cặp số 4 mang lại kết quả bất ngờ và thú vị nhất: hai câu mang tính chất trái ngược hoàn toàn về mặt quy định và logic thực thi ("được rút" đối lập tuyệt đối với "không được rút"), nhưng điểm tương đồng lại lên tới **0.8575** (rất cao). Điều này chứng minh rằng các mô hình nhúng dựa trên phân bố từ vựng hoặc n-grams biểu diễn ý nghĩa dựa trên sự trùng lặp của không gian chủ đề ("sinh viên", "rút học phần", "hai tuần") chứ không thể phân biệt được tác động logic đảo ngược của từ phủ định ("không"). Trong các hệ thống RAG thực tế, việc đưa ngữ cảnh vào một LLM có năng lực suy luận cao ở tầng sinh câu trả lời là vô cùng cần thiết để xử lý chính xác các điều kiện phủ định.

---

## 5. Kết quả truy xuất của tôi (Competition Results) — Cá nhân (10 điểm)

- **Chiến lược cá nhân lựa chọn:** `SentenceChunker(max_sentences_per_chunk=3)`
- **Lý do lựa chọn:** Trong các văn bản quy chế, quy định học vụ tại các trường đại học, mỗi điều khoản thường được gói gọn từ một đến ba câu liên tiếp (gồm điều kiện áp dụng, hành động thực hiện và chế tài/kết quả xử lý). Chia nhỏ theo ranh giới câu tự nhiên giúp giữ trọn vẹn cú pháp câu và các dấu câu kết thúc, không bị cắt ngang giữa câu (sentence truncation) như FixedSize, giúp bộ sinh vector trích xuất đặc trưng chính xác và agent dễ dàng trích dẫn nguyên văn ngữ cảnh.
- **Quy mô toàn bộ corpus (10 tài liệu):** Tạo ra **32 chunks**, độ dài trung bình **322,28 ký tự**.

Chạy **5 câu hỏi đánh giá của nhóm** trên mã nguồn cá nhân trong gói `src`:

| # | Câu hỏi (Query) | Top-1 Chunk truy xuất được (tóm tắt) | Điểm Score | Có liên quan không? (Relevant) | Câu trả lời của Agent (tóm tắt) |
|:---:|---|---|:---:|:---:|---|
| 1 | Tại Trường Y Dược - Đại học Trà Vinh, sinh viên được rút học phần trong thời hạn nào và nếu tự ý bỏ học từ tuần thứ ba thì bị xử lý ra sao? | `tvu-course-registration::c03`: Sinh viên được rút bớt học phần trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, nếu không học xem là tự ý bỏ học và nhận điểm F; khối lượng học lực trung bình tối thiểu 15 tín chỉ. | 0.3475 | Có (chứa đủ 3 terms: hai tuần, tuần thứ ba, điểm F) | Trích dẫn `[tvu-course-registration::c03]`, trả lời chính xác sinh viên được rút trong 2 tuần đầu học kỳ chính; từ tuần thứ ba tự ý bỏ học nhận điểm F. |
| 2 | Sinh viên Đại học Thủ Dầu Một phải nộp đơn phúc khảo ở đâu, trong bao lâu và phải thực hiện quy định lệ phí như thế nào? *(lọc `audience: student`)* | `tdmu-grade-appeal::c01`: Quy trình phúc khảo áp dụng sinh viên các hệ và cao học; nộp đơn BM.01 về bộ môn quản lý đề cương trong vòng 7 ngày kể từ ngày công bố điểm kiểm tra. | 0.3781 | Có (chứa đúng bộ môn quản lý đề cương và 7 ngày; chi tiết lệ phí bị đẩy sang chunk c02) | Trích dẫn `[tdmu-grade-appeal::c01]`, trả lời nộp đơn BM.01 về bộ môn trong 7 ngày; thiếu thông tin chi tiết đơn vị quản lý lệ phí ở câu tiếp theo. |
| 3 | Sinh viên chương trình tiên tiến TNUT được đăng ký tối thiểu và tối đa bao nhiêu tín chỉ trong học kỳ chính? | `tnut-advanced-registration::c02`: Đợt đăng ký diễn ra 2-3 tuần trước học kỳ; năm có 3 học kỳ chính giới hạn 8–16 tín chỉ; năm có 2 học kỳ chính giới hạn 10–24 tín chỉ. | 0.5345 | Có (chứa đủ 4 mốc: 8 tín chỉ, 16 tín chỉ, 10 tín chỉ, 24 tín chỉ) | Trích dẫn `[tnut-advanced-registration::c02]`, nêu chuẩn xác định mức 8–16 tín chỉ (năm 3 kỳ chính) và 10–24 tín chỉ (năm 2 kỳ chính). |
| 4 | Ở UFM, khi lập kế hoạch đăng ký học phần, sinh viên cần tìm hiểu những gì và có thể nhờ ai tư vấn? | `ufm-course-registration::c02`: Sinh viên cần tìm hiểu chương trình, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; có thể liên hệ cố vấn học tập khi cần tư vấn. | 0.4153 | Có (chứa đủ 3 terms: chương trình, đề cương, cố vấn học tập) | Trích dẫn `[ufm-course-registration::c02]`, liệt kê đầy đủ các danh mục cần tìm hiểu trước khi đăng ký và tư vấn từ cố vấn học tập. |
| 5 | Các ngưỡng điểm trung bình tích lũy nào khiến sinh viên TVU bị cảnh báo học vụ theo từng năm và số tín chỉ F tồn đọng tối đa là bao nhiêu? | `tvu-academic-warning::c01`: Cảnh báo học vụ khi ĐTBTL < 1,20 (năm thứ nhất); < 1,40 (năm hai); < 1,60 (năm ba); < 1,80 (các năm tiếp và cuối khóa); hoặc số tín chỉ F tích lũy vượt quá 24 tín chỉ. | 0.3946 | Có (chứa đủ 5 mốc: 1,20; 1,40; 1,60; 1,80; 24 tín chỉ) | Trích dẫn `[tvu-academic-warning::c01]`, trả lời chính xác tất cả các mốc điểm trung bình tích lũy bị cảnh báo theo từng năm và số tín chỉ F tối đa 24 tín chỉ. |

**Bao nhiêu câu hỏi trả về chunk có liên quan trong top-3?** **5 / 5** (100% câu hỏi đều truy xuất chính xác tài liệu liên quan ngay tại Top-1).

**Điều hay nhất tôi học được từ thành viên khác / nhóm khác (qua demo):**
> Khi đối chiếu với `RecursiveChunker(chunk_size=500)` của thành viên khác trong nhóm, tôi nhận thấy RecursiveChunker nhóm trọn vẹn được cả đoạn nộp đơn và đoạn đóng lệ phí ở Q2 vào chung một chunk theo cấu trúc đề mục `##`, giúp agent trả lời đủ 100% bằng chứng mà không bị đứt đoạn như `SentenceChunker(3)` (vốn bị cắt cứng tại câu thứ 3 nên câu 4 về lệ phí bị đẩy sang chunk sau). Tuy nhiên, so với `FixedSizeChunker(500, overlap=50)`, chiến lược `SentenceChunker(3)` của tôi vượt trội rõ rệt vì FixedSize thường xuyên cắt ngang giữa câu hoặc tiêu đề dẫn đến các mảnh vỡ câu gây nhiễu embedding. Bài học đắt giá nhất là chiến lược chunking cần phản ánh cấu trúc logic của văn bản: với quy chế học vụ, phân đoạn theo câu kết hợp cơ chế overlap câu (hoặc gom theo section/heading) sẽ là giải pháp tối ưu toàn diện.

---

## Tự Đánh Giá (Phần Cá Nhân)

| Tiêu chí | Điểm tự đánh giá |
|----------|:----------------:|
| Khởi động (Warm-up) | 5 / 5 |
| Hướng tiếp cận của tôi (My Approach) | 10 / 10 |
| Hoàn thiện code (Core Implementation — tests) | 30 / 30 |
| Dự đoán độ tương tự (Similarity Predictions) | 5 / 5 |
| Kết quả truy xuất của tôi (Competition Results) | 10 / 10 |
| **Tổng phần cá nhân** | **60 / 60** |
