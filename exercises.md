# Ngày 7 — Bài tập
## Nền tảng Dữ liệu: Embedding & Vector Store | Bài tập thực hành

**Họ và tên:** Nguyễn Thanh Duy  
**MSSV:** 2A202602804  
**Nhóm:** Nhóm Biến thể K4-L3A (Quy chế & Dịch vụ Đại học)  
**Chiến lược cá nhân:** `SentenceChunker(max_sentences_per_chunk=3)`  

---

## Phần 1 — Khởi động (Cá nhân)

### Bài tập 1.1 — Cosine Similarity (Độ tương tự Cosine) bằng ngôn ngữ đời thường

Không yêu cầu toán học — hãy giải thích về mặt khái niệm:

- **Điều gì xảy ra khi hai đoạn văn bản có độ tương tự cosine cao?**  
  > Khi hai đoạn văn bản có độ tương tự cosine cao (tiến gần về 1.0), hai vector đại diện chỉ về cùng một hướng trong không gian ngữ nghĩa nhiều chiều. Điều này có nghĩa là hai văn bản có mức độ tương đồng rất lớn về mặt nội dung, ý nghĩa hoặc phân bố từ vựng chủ đề, bất kể hai đoạn văn dài ngắn khác nhau.

- **Đưa ra một ví dụ cụ thể về hai câu sẽ có độ tương tự CAO và hai câu sẽ có độ tương tự THẤP:**  
  > - **Ví dụ CAO:**  
  >   - Câu A: *"Sinh viên nộp đơn phúc khảo trong vòng bảy ngày."*  
  >   - Câu B: *"Sinh viên phải nộp đơn phúc khảo trong vòng bảy ngày kể từ ngày công bố điểm."*  
  >   - *Lý do:* Cả hai câu cùng mô tả quy định học vụ về thời hạn nộp đơn phúc khảo điểm, dùng chung các từ khóa cốt lõi ("sinh viên", "nộp đơn", "phúc khảo", "bảy ngày"). Độ tương tự cosine đạt **0.6841**.  
  > - **Ví dụ THẤP:**  
  >   - Câu A: *"Sinh viên nộp đơn phúc khảo trong vòng bảy ngày."*  
  >   - Câu B: *"Con mèo nằm ngủ dưới gốc cây."*  
  >   - *Lý do:* Hai câu thuộc hai ngữ cảnh hoàn toàn tách biệt (thủ tục học vụ đại học vs hành vi động vật tự nhiên), không có từ vựng giao nhau. Hai vector trực giao, cosine similarity bằng **0.0000**.

- **Tại sao độ tương tự cosine lại được ưu tiên hơn khoảng cách Euclid (Euclidean distance) đối với text embeddings?**  
  > Vì độ tương tự cosine chỉ đo **hướng** (góc giữa hai vector) và loại bỏ hoàn toàn ảnh hưởng của **độ lớn** (độ dài văn bản / norm vector). Khoảng cách Euclid bị chi phối bởi độ dài văn bản: nếu một câu ngắn tóm tắt và một đoạn văn dài diễn giải cùng một nội dung, Euclid sẽ đánh giá chúng cách rất xa nhau, trong khi Cosine vẫn phản ánh đúng chúng có cùng ngữ nghĩa.

> **Ghi kết quả vào:** [`report/REPORT_CANHAN.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_CANHAN.md) — Phần 1 (Khởi động)

---

### Bài tập 1.2 — Bài toán tính toán Chunking

- **Một tài liệu có độ dài 10,000 ký tự. Bạn tiến hành chia nhỏ (chunk) với `chunk_size=500` (kích thước chunk), `overlap=50` (độ chồng chéo). Bạn dự kiến sẽ có bao nhiêu chunks?**  
  > - Chiều dài văn bản ($L$): $10{,}000$ ký tự  
  > - Kích thước chunk ($C$): $500$ ký tự  
  > - Độ chồng chéo ($O$): $50$ ký tự  
  > - Bước nhảy giữa các chunk ($S = C - O$): $500 - 50 = 450$ ký tự  
  > - Công thức: $\text{Số lượng chunk} = \left\lceil \frac{L - O}{C - O} \right\rceil = \left\lceil \frac{10000 - 50}{500 - 50} \right\rceil = \left\lceil \frac{9950}{450} \right\rceil = \lceil 22{,}111... \rceil = 23$  
  > - **Đáp án:** **23 chunks**.  
  >   *(Chi tiết vị trí: Chunk 1 [0:500], Chunk 2 [450:950], ..., Chunk 22 [9450:9950], Chunk 23 [9900:10000]).*

- **Nếu độ chồng chéo (overlap) tăng lên 100, số lượng chunk sẽ thay đổi như thế nào? Tại sao bạn lại muốn tăng độ chồng chéo?**  
  > - Khi overlap tăng lên $100$, bước dịch chuyển giảm còn $500 - 100 = 400$ ký tự.  
  > - Số chunks mới = $\lceil (10000 - 100) / 400 \rceil = \lceil 9900 / 400 \rceil = \lceil 24{,}75 \rceil = 25$ chunks (**tăng thêm 2 chunks**).  
  > - **Lý do muốn tăng độ chồng chéo:** Giúp bảo toàn tính liền mạch của ngữ cảnh tại các điểm ranh giới cắt, ngăn ngừa hiện tượng một câu văn quan trọng hoặc một cụm điều khoản điều kiện bị xẻ đôi giữa hai chunk khiến mô hình embedding hoặc LLM bị mất thông tin.

> **Ghi kết quả vào:** [`report/REPORT_CANHAN.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_CANHAN.md) — Phần 1 (Khởi động)

---

## Phần 2 — Lập trình cốt lõi (Cá nhân)

Hoàn thành tất cả các TODOs trong `src/chunking.py`, `src/store.py`, và `src/agent.py`. `Document` dataclass và `FixedSizeChunker` đã được triển khai sẵn làm ví dụ — hãy đọc kỹ để hiểu cấu trúc trước khi lập trình phần còn lại.

Chạy `pytest tests/` để kiểm tra tiến độ: **Đã đạt 47 / 47 tests passed (100%)**.

### Danh sách cần làm (Checklist)
- [x] `Document` dataclass — ĐÃ TRIỂN KHAI SẴN trong [`src/models.py`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/src/models.py)
- [x] `FixedSizeChunker` — ĐÃ TRIỂN KHAI SẴN trong [`src/chunking.py`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/src/chunking.py)
- [x] `SentenceChunker` — tách dựa trên ranh giới câu bằng regex positive lookbehind, nhóm tối đa N câu.
- [x] `RecursiveChunker` — thử nghiệm các dấu phân cách `["\n\n", "\n", ". ", " ", ""]`, đệ quy khi vượt kích thước và bảo toàn dấu phân cách.
- [x] `compute_similarity` — tính cosine similarity bằng dot product và norm, có bảo vệ chia cho 0.
- [x] `ChunkingStrategyComparator` — chạy cả 3 chiến lược (`fixed_size`, `by_sentences`, `recursive`), thống kê số lượng và độ dài trung bình.
- [x] `EmbeddingStore.__init__` — khởi tạo kho lưu trữ isolated in-memory.
- [x] `EmbeddingStore.add_documents` — nhúng vector và lưu trữ từng chunk, bảo toàn `doc_id` gốc trong metadata.
- [x] `EmbeddingStore.search` — nhúng truy vấn, xếp hạng theo tích vô hướng (dot product) và trả về top_k.
- [x] `EmbeddingStore.get_collection_size` — trả về tổng số chunks đang lưu trữ.
- [x] `EmbeddingStore.search_with_filter` — cơ chế pre-filtering theo metadata rồi mới xếp hạng độ tương tự.
- [x] `EmbeddingStore.delete_document` — xóa toàn bộ các chunks thuộc về một doc_id cha.
- [x] `KnowledgeBaseAgent.answer` — truy xuất top-k chunks liên quan + bọc `<context>` + prompt grounding nghiêm ngặt.

> **Nộp code:** thư mục [`src/`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/src)  
> **Ghi lại hướng tiếp cận vào:** [`report/REPORT_CANHAN.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_CANHAN.md) — Phần 2 (Hướng tiếp cận của tôi)

---

## Phần 3 — So Sánh Chiến Lược Truy Xuất (Nhóm)

### Bài tập 3.0 — Chuẩn Bị Tài Liệu (Giờ đầu tiên)

Mỗi nhóm chọn một chủ đề (domain) và chuẩn bị bộ tài liệu:

**Bước 1 — Chọn chủ đề:** Biến thể K4-L3A: Quy chế đào tạo và quy định công tác học vụ tại các trường Đại học (ĐH Trà Vinh TVU, ĐH Thủ Dầu Một TDMU, ĐH Kỹ thuật Công nghiệp Thái Nguyên TNUT, ĐH Tài chính - Marketing UFM, ĐH Quang Trung QTU).

**Bước 2 — Thu thập 5-10 tài liệu.** Đã thu thập đủ **10 tài liệu chuẩn**, lưu trữ tại [`data/academic_regulations/`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/data/academic_regulations):

| # | Tên tài liệu | Nguồn (Source URL) | Ngày lấy / Phiên bản | Số ký tự | Metadata đã gán |
|:---:|--------------|------------|--------------------|:--------:|-----------------|
| 1 | `tvu-course-registration` | https://cmp.tvu.edu.vn/so-tay-sinh-vien/ | 2026-09-19 / Sổ tay SV 2026 | 1,380 | `audience: student`, `category: registration` |
| 2 | `tvu-academic-warning` | https://cmp.tvu.edu.vn/so-tay-sinh-vien/ | 2026-09-19 / Sổ tay SV 2026 | 1,004 | `audience: student`, `category: academic-warning` |
| 3 | `tvu-grade-appeal` | https://cmp.tvu.edu.vn/so-tay-sinh-vien/ | 2026-09-19 / Sổ tay SV 2026 | 905 | `audience: student`, `category: grade-appeal` |
| 4 | `qtu-academic-affairs-overview` | https://qtu.edu.vn/qd-95-... | 2026-09-19 / 95/QĐ-ĐHQT | 836 | `audience: all`, `category: academic-policy` |
| 5 | `tdmu-grade-appeal` | https://tdmu.edu.vn/.../Phuc%20khao...pdf | 2026-09-19 / QT/09 lần 01 | 1,434 | `audience: student`, `category: grade-appeal` |
| 6 | `tdmu-grade-appeal-operations` | https://tdmu.edu.vn/.../Phuc%20khao...pdf | 2026-09-19 / QT/09 lần 01 | 1,194 | `audience: staff`, `category: grade-appeal` |
| 7 | `tnut-advanced-registration` | https://fit.tnut.edu.vn/bai-viet/quy-che... | 2026-09-19 / 3571/QĐ-ĐHKTCN | 883 | `audience: student`, `category: registration` |
| 8 | `tnut-advanced-withdrawal-assessment`| https://fit.tnut.edu.vn/bai-viet/quy-che... | 2026-09-19 / 3571/QĐ-ĐHKTCN | 928 | `audience: student`, `category: withdrawal-and-assessment` |
| 9 | `ufm-course-registration` | https://pdt.ufm.edu.vn/dulieu/quiche/... | 2026-09-19 / 1329/QĐ-ĐHTCM | 1,104 | `audience: student`, `category: registration` |
| 10 | `ufm-assessment` | https://pdt.ufm.edu.vn/dulieu/quiche/... | 2026-09-19 / 1329/QĐ-ĐHTCM | 695 | `audience: student`, `category: assessment` |

**Bước 3 — Thiết kế cấu trúc metadata (metadata schema):**
- `audience`: `student` / `staff` / `all` (Phân định nhóm đối tượng, phục vụ lọc ở Q2).
- `institution`: Tên trường đại học ban hành.
- `department`: Phòng/ban quản lý học vụ (`academic-affairs`, `examination-affairs`).
- `category`: Chuyên mục (`registration`, `grade-appeal`, `academic-warning`).
- `source_url`, `retrieved_at`, `document_version`: Truy xuất nguồn gốc và phiên bản.

> **Ghi kết quả vào:** [`report/REPORT_NHOM.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_NHOM.md) — Phần 1 (Lựa chọn tài liệu)

---

### Bài tập 3.1 — Thiết Kế Chiến Lược Truy Xuất (Mỗi người thử riêng)

**Bước 1 — Đường cơ sở (Baseline):** Chạy `ChunkingStrategyComparator().compare()` trên 3 tài liệu:
- `qtu-academic-affairs-overview`: `fixed_size` (2 chunks, avg 443), `by_sentences` (2 chunks, avg 416), `recursive` (3 chunks, avg 278.7).
- `tdmu-grade-appeal-operations`: `fixed_size` (3 chunks, avg 431.3), `by_sentences` (4 chunks, avg 297), `recursive` (4 chunks, avg 298.5).
- `tdmu-grade-appeal`: `fixed_size` (4 chunks, avg 396), `by_sentences` (4 chunks, avg 356.8), `recursive` (4 chunks, avg 358.5).

**Bước 2 — Chiến lược cá nhân:** `SentenceChunker(max_sentences_per_chunk=3)`  
- **Lý do thiết kế:** Điều khoản quy định học vụ thường được diễn đạt hoàn chỉnh bằng một đến ba câu liên tiếp (quy định điều kiện, hành vi thực hiện và hệ quả/chế tài). Giữ nguyên ranh giới câu và dấu câu giúp câu văn trọn vẹn, không bị cắt cụt từ như FixedSize, giúp answerer trích xuất ngữ cảnh dễ dàng.  
- **Quy mô toàn bộ corpus (10 tài liệu):** **32 chunks**, trung bình **322,28 ký tự**.

```python
class SentenceChunker:
    """Chiến lược chia nhỏ theo ranh giới câu cho quy chế đại học."""

    def __init__(self, max_sentences_per_chunk: int = 3) -> None:
        self.max_sentences_per_chunk = max(1, max_sentences_per_chunk)

    def chunk(self, text: str) -> list[str]:
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
        n = self.max_sentences_per_chunk
        return [" ".join(sentences[i:i + n]) for i in range(0, len(sentences), n)]
```

**Bước 3 — So sánh:** So với đường cơ sở `fixed_size` (26 chunks, trung bình 429 ký tự), `SentenceChunker(3)` không làm rách từ ở ranh giới cắt, giúp điểm tương đồng vector tập trung hơn và không sinh rác ngữ nghĩa.

> **Ghi kết quả vào:** [`report/REPORT_CANHAN.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_CANHAN.md) — Phần 5 & [`report/REPORT_NHOM.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_NHOM.md) — Phần 2

---

### Bài tập 3.2 — Chuẩn Bị Câu Hỏi Đánh Giá (Benchmark Queries)

5 câu hỏi chuẩn xác, có thể kiểm chứng được lưu tại [`data/academic_regulations/benchmark.json`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/data/academic_regulations/benchmark.json):

| # | Câu hỏi (Query) | Câu trả lời chuẩn (Gold Answer) | Chunk nào chứa thông tin? |
|:---:|---|---|:---:|
| 1 | Tại Trường Y Dược - TVU, sinh viên được rút học phần trong thời hạn nào và nếu tự ý bỏ học từ tuần thứ ba thì bị xử lý ra sao? | Sinh viên được rút học phần trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn được giữ trong phiếu đăng ký; nếu không đi học thì bị xem là tự ý bỏ học và nhận điểm F. | `tvu-course-registration::c03` |
| 2 | Sinh viên ĐH Thủ Dầu Một phải nộp đơn phúc khảo ở đâu, trong bao lâu và phải thực hiện quy định lệ phí như thế nào? *(lọc `audience: student`)* | Sinh viên nộp đơn BM.01 về bộ môn quản lý đề cương học phần trong vòng bảy ngày từ ngày công bố điểm và phải đóng lệ phí phúc khảo theo quy định. | `tdmu-grade-appeal::c01` & `c02` |
| 3 | Sinh viên chương trình tiên tiến TNUT được đăng ký tối thiểu và tối đa bao nhiêu tín chỉ trong học kỳ chính? | Với năm học có ba học kỳ chính, giới hạn là 8–16 tín chỉ mỗi kỳ; với năm học có hai học kỳ chính, giới hạn là 10–24 tín chỉ mỗi kỳ. | `tnut-advanced-registration::c02` |
| 4 | Ở UFM, khi lập kế hoạch đăng ký học phần, sinh viên cần tìm hiểu những gì và có thể nhờ ai tư vấn? | Sinh viên cần tìm hiểu chương trình đào tạo, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và điều kiện cá nhân; có thể liên hệ cố vấn học tập khi cần tư vấn. | `ufm-course-registration::c02` |
| 5 | Các ngưỡng điểm trung bình tích lũy nào khiến sinh viên TVU bị cảnh báo học vụ theo từng năm và số tín chỉ F tồn đọng tối đa là bao nhiêu? | Ngưỡng cảnh báo là dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; dưới 1,80 ở các năm tiếp theo và cuối khóa. Một căn cứ khác là số tín chỉ F tồn đọng vượt quá 24 tín chỉ. | `tvu-academic-warning::c01` |

> **Ghi kết quả vào:** [`report/REPORT_NHOM.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_NHOM.md) — Phần 3

---

### Bài tập 3.3 — Dự Đoán Độ Tương Tự Cosine (Cá nhân)

Thực thi `compute_similarity` trên 5 cặp câu (dữ liệu trong [`report/similarity_predictions.json`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/similarity_predictions.json)):

| Cặp | Câu A | Câu B | Dự đoán | Điểm thực tế | Đúng? |
|:---:|---|---|:---:|:---:|:---:|
| 1 | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | cao nhất | **1.0000** | Đúng |
| 2 | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | Sinh viên phải nộp đơn phúc khảo trong vòng bảy ngày kể từ ngày công bố điểm. | cao | **0.6841** | Đúng |
| 3 | Sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ. | Sinh viên đăng ký tối thiểu 10 tín chỉ và tối đa 24 tín chỉ. | cao (khác số liệu) | **0.8046** | Đúng |
| 4 | Sinh viên được rút học phần trong vòng hai tuần. | Sinh viên không được rút học phần trong vòng hai tuần. | cao (ngữ nghĩa phủ định) | **0.8575** | Đúng |
| 5 | Sinh viên nộp đơn phúc khảo trong vòng bảy ngày. | Con mèo nằm ngủ dưới gốc cây. | thấp nhất | **0.0000** | Đúng |

- **Phản ngẫm:** Cặp 4 đem lại bài học bất ngờ nhất: dù mang ý nghĩa phủ định trái ngược ("được rút" vs "không được rút"), điểm tương đồng cosine vẫn đạt tới **0.8575**. Điều này minh chứng embedding từ vựng/n-gram chỉ bắt sự trùng lặp từ ngữ chủ đề chứ không nhận biết được logic phủ định, do đó cần kết hợp LLM để suy luận chính xác quy chế.

> **Ghi kết quả vào:** [`report/REPORT_CANHAN.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_CANHAN.md) — Phần 4 (Dự đoán độ tương tự)

---

### Bài tập 3.4 — Chạy Đánh Giá & So Sánh Trong Nhóm

- **Bước 1 — Kết quả của `SentenceChunker(3)`:**
  - 100% câu hỏi (5/5) đều truy xuất trúng tài liệu liên quan ngay tại vị trí **Top-1**.
  - Điểm tương đồng: Q1 = 0.3475, Q2 = 0.3781, Q3 = 0.5345, Q4 = 0.4153, Q5 = 0.3946.
- **Bước 2 — So sánh trong nhóm:**
  - So với `FixedSizeChunker(500, 50)`: `SentenceChunker` vượt trội vì không làm đứt gãy câu, giúp vector biểu diễn cô đọng, điểm Top-1 cao hơn.
  - So với `RecursiveChunker(500)`: Recursive đạt đủ 5/5 full evidence vì gom được toàn bộ đoạn nộp đơn + lệ phí ở Q2 theo đề mục `##`, trong khi SentenceChunker bị cắt ở câu số 3.
- **Bước 3 — Vai trò của metadata filtering:**
  - Cực kỳ hữu hiệu ở Q2: Lọc `audience: student` loại bỏ ngay tài liệu `tdmu-grade-appeal-operations.md` dành cho cán bộ chấm thi, tránh trả lời nhầm quy trình nội bộ cho sinh viên.

> **Ghi kết quả vào:** [`report/REPORT_CANHAN.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_CANHAN.md) — Phần 5 & [`report/REPORT_NHOM.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_NHOM.md) — Phần 3

---

### Bài tập 3.5 — Phân Tích Lỗi (Failure Analysis)

- **Câu hỏi gặp vấn đề:** Câu hỏi **Q2** (Quy trình phúc khảo và lệ phí tại ĐH Thủ Dầu Một).
- **Hiện tượng:** Truy xuất đúng tài liệu `tdmu-grade-appeal::c01` ở vị trí Top-1, trả lời đúng đơn BM.01 nộp về bộ môn quản lý đề cương trong 7 ngày, nhưng câu trả lời thiếu thông tin đóng lệ phí tại Ban Tài chính - Kế toán.
- **Nguyên nhân:** `SentenceChunker(max_sentences_per_chunk=3)` gom 3 câu đầu tiên thành chunk `c01`. Câu thứ 4 về lệ phí bị đẩy sang chunk `c02`. Vì không có cơ chế chồng lặp câu (sentence overlap), thông tin bị chia cắt qua ranh giới chunk.
- **Đề xuất cải thiện:** Áp dụng **Sliding Sentence Window (ví dụ: chunk 3 câu, trượt 1 câu chồng lặp)** hoặc kết hợp **Heading-based Chunking** để các bước trong cùng một quy trình thủ tục luôn được gom chung một khối ngữ cảnh.

> **Ghi kết quả vào:** [`report/REPORT_CANHAN.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_CANHAN.md) — Phần 5 & [`report/REPORT_NHOM.md`](file:///C:/Users/Acer/OneDrive/Desktop/AI%20th%E1%BB%B1c%20chi%E1%BA%BFn/K4-DAY07-NguyenThanhDuy-2A202602804/report/REPORT_NHOM.md) — Phần 4

---

## Danh Sách Kiểm Tra Nộp Bài (Submission Checklist)

- [x] Vượt qua tất cả các bài kiểm thử (tests): `pytest tests/ -v` (**47 / 47 PASSED**)
- [x] Cập nhật thư mục `src/` (cá nhân hoàn thiện `chunking.py`, `store.py`, `agent.py`)
- [x] Hoàn thành báo cáo nhóm (`report/REPORT_NHOM.md` — 1 file/nhóm)
- [x] Hoàn thành báo cáo cá nhân (`report/REPORT_CANHAN.md` — 1 file/sinh viên)
