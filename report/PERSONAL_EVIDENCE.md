# Bằng chứng thực nghiệm cá nhân

Tái lập: `python scripts/run_personal.py`. Cần scikit-learn (requirements-personal.txt).

TF-IDF word 1-2 grams, L2; fitted on 10 source bodies only

Answerer chỉ trích lại ngữ cảnh, không phải LLM.

## sentence3

32 chunks; trung bình 322.28125 ký tự.

### Q1: Tại Trường Y Dược - Đại học Trà Vinh, sinh viên được rút học phần trong thời hạn nào và nếu tự ý bỏ học từ tuần thứ ba thì bị xử lý ra sao?

Gold: Sinh viên được rút học phần trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn được giữ trong phiếu đăng ký; nếu không đi học thì bị xem là tự ý bỏ học và nhận điểm F.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tvu-course-registration::c03 — 0.347481**

## Rút bớt học phần

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F. ## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa.

**Top 2: tnut-advanced-withdrawal-assessment::c01 — 0.303248**

# Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z. Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí.

**Top 3: tvu-course-registration::c01 — 0.217838**

# Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo. Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt.

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tvu-course-registration::c03] ## Rút bớt học phần

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F. ## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa.
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tnut-advanced-withdrawal-assessment::c01] # Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z. Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c01] # Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo. Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt.
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q2: Sinh viên Đại học Thủ Dầu Một phải nộp đơn phúc khảo ở đâu, trong bao lâu và phải thực hiện quy định lệ phí như thế nào?

Gold: Sinh viên nộp đơn BM.01 về bộ môn quản lý đề cương học phần trong vòng bảy ngày từ ngày công bố điểm và phải đóng lệ phí phúc khảo theo quy định.

Filter: `{'audience': 'student'}`; đúng tài liệu: True; đủ cụm bằng chứng: False.

**Top 1: tdmu-grade-appeal::c01 — 0.378111**

# Quy trình phúc khảo bài kiểm tra tại Trường Đại học Thủ Dầu Một

Quy trình áp dụng cho sinh viên các hệ đào tạo, học viên cao học, đơn vị đào tạo và các đơn vị phối hợp tại Trường Đại học Thủ Dầu Một. Tài liệu tham chiếu Quyết định số 714/QĐ-ĐHTDM ngày 13 tháng 6 năm 2024 về khảo thí và đo lường kết quả học tập. ## Sinh viên nộp đơn

Sinh viên có yêu cầu phúc khảo phải lập đơn theo biểu mẫu BM.01 và nộp về bộ môn quản lý đề cương học phần trong vòng bảy ngày kể từ ngày công bố điểm kiểm tra.

**Top 2: tvu-grade-appeal::c01 — 0.262853**

# Phúc khảo và điều chỉnh điểm tại Trường Y Dược - Đại học Trà Vinh

## Phúc khảo

Sinh viên có nhu cầu phúc khảo phải làm đề nghị theo biểu mẫu chung, gửi Phòng Khảo thí trong vòng 15 ngày kể từ ngày niêm yết kết quả và đóng lệ phí theo quy định. Khoa chịu trách nhiệm tổ chức chấm phúc khảo. Các học phần có hình thức đánh giá kết thúc bằng báo cáo, vấn đáp hoặc thực hành không thuộc diện được yêu cầu phúc khảo.

**Top 3: tnut-advanced-withdrawal-assessment::c01 — 0.207222**

# Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z. Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí.

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tdmu-grade-appeal::c01] # Quy trình phúc khảo bài kiểm tra tại Trường Đại học Thủ Dầu Một

Quy trình áp dụng cho sinh viên các hệ đào tạo, học viên cao học, đơn vị đào tạo và các đơn vị phối hợp tại Trường Đại học Thủ Dầu Một. Tài liệu tham chiếu Quyết định số 714/QĐ-ĐHTDM ngày 13 tháng 6 năm 2024 về khảo thí và đo lường kết quả học tập. ## Sinh viên nộp đơn

Sinh viên có yêu cầu phúc khảo phải lập đơn theo biểu mẫu BM.01 và nộp về bộ môn quản lý đề cương học phần trong vòng bảy ngày kể từ ngày công bố điểm kiểm tra.
Nguồn: https://tdmu.edu.vn/hinh/thuvien/taptin/2-6-2025-4-42-24-pm06-BKTKDDBCL-QT.09-Phuc%20khao%20Bai%20KTr.pdf

[tvu-grade-appeal::c01] # Phúc khảo và điều chỉnh điểm tại Trường Y Dược - Đại học Trà Vinh

## Phúc khảo

Sinh viên có nhu cầu phúc khảo phải làm đề nghị theo biểu mẫu chung, gửi Phòng Khảo thí trong vòng 15 ngày kể từ ngày niêm yết kết quả và đóng lệ phí theo quy định. Khoa chịu trách nhiệm tổ chức chấm phúc khảo. Các học phần có hình thức đánh giá kết thúc bằng báo cáo, vấn đáp hoặc thực hành không thuộc diện được yêu cầu phúc khảo.
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tnut-advanced-withdrawal-assessment::c01] # Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z. Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

### Q3: Sinh viên chương trình tiên tiến TNUT được đăng ký tối thiểu và tối đa bao nhiêu tín chỉ trong học kỳ chính?

Gold: Với năm học có ba học kỳ chính, giới hạn là 8–16 tín chỉ mỗi kỳ; với năm học có hai học kỳ chính, giới hạn là 10–24 tín chỉ mỗi kỳ.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tnut-advanced-registration::c02 — 0.534524**

Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ. ## Số tín chỉ ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

**Top 2: tnut-advanced-registration::c01 — 0.294781**

# Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký.

**Top 3: tvu-course-registration::c03 — 0.226152**

## Rút bớt học phần

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F. ## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa.

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tnut-advanced-registration::c02] Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ. ## Số tín chỉ ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tnut-advanced-registration::c01] # Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c03] ## Rút bớt học phần

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F. ## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa.
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q4: Ở UFM, khi lập kế hoạch đăng ký học phần, sinh viên cần tìm hiểu những gì và có thể nhờ ai tư vấn?

Gold: Sinh viên cần tìm hiểu chương trình đào tạo, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và điều kiện cá nhân; có thể liên hệ cố vấn học tập khi cần tư vấn.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: ufm-course-registration::c02 — 0.415276**

Trước khi đăng ký, sinh viên cần tìm hiểu chương trình, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và cân nhắc điều kiện cá nhân. Sinh viên có thể liên hệ cố vấn học tập khi cần tư vấn. Học kỳ đầu tiên, sinh viên học theo thời khóa biểu do Trường ấn định.

**Top 2: tnut-advanced-registration::c01 — 0.293197**

# Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký.

**Top 3: tvu-course-registration::c01 — 0.263396**

# Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo. Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt.

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[ufm-course-registration::c02] Trước khi đăng ký, sinh viên cần tìm hiểu chương trình, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và cân nhắc điều kiện cá nhân. Sinh viên có thể liên hệ cố vấn học tập khi cần tư vấn. Học kỳ đầu tiên, sinh viên học theo thời khóa biểu do Trường ấn định.
Nguồn: https://pdt.ufm.edu.vn/dulieu/quiche/1329_Quy_che_dao_tao_tin_chi_tu_khoa_2021.htm

[tnut-advanced-registration::c01] # Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c01] # Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo. Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt.
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q5: Các ngưỡng điểm trung bình tích lũy nào khiến sinh viên TVU bị cảnh báo học vụ theo từng năm và số tín chỉ F tồn đọng tối đa là bao nhiêu?

Gold: Ngưỡng cảnh báo là dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; dưới 1,80 ở các năm tiếp theo và cuối khóa. Một căn cứ khác là số tín chỉ F tồn đọng vượt quá 24 tín chỉ.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tvu-academic-warning::c01 — 0.394582**

# Cảnh báo học vụ và buộc thôi học tại Trường Y Dược - Đại học Trà Vinh

## Điều kiện cảnh báo

Sinh viên có thể bị cảnh báo kết quả học tập khi thuộc một trong các trường hợp sau:

- Điểm trung bình chung tích lũy dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; hoặc dưới 1,80 ở các năm tiếp theo và cuối khóa. - Điểm trung bình chung học kỳ dưới 0,80 ở học kỳ đầu tiên của khóa học hoặc dưới 1,00 ở các học kỳ tiếp theo. - Tổng số tín chỉ của các học phần điểm F còn tồn đọng vượt quá 24 tín chỉ.

**Top 2: tnut-advanced-registration::c02 — 0.251755**

Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ. ## Số tín chỉ ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

**Top 3: qtu-academic-affairs-overview::c01 — 0.163911**

# Phạm vi Quy định công tác học vụ

Quy định công tác học vụ của Trường Đại học Quang Trung được ban hành theo Quyết định số 95/QĐ-ĐHQT ngày 24 tháng 6 năm 2021 và áp dụng trong toàn trường. ## Các nhóm nội dung

Quy định bao quát việc đăng ký, học lại, học cải thiện và rút học phần; kiểm tra, đánh giá kết quả, điều kiện dự thi và phúc khảo; cảnh báo học tập, buộc nghỉ học, tạm dừng và tiếp nhận học lại; cùng các thủ tục xác nhận sinh viên, chuyển ngành, chuyển cơ sở đào tạo và cấp văn bằng, chứng chỉ. Văn bản xác định trách nhiệm của sinh viên, giảng viên, cố vấn học tập và các đơn vị chức năng trong việc thực hiện và hỗ trợ công tác học vụ.

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tvu-academic-warning::c01] # Cảnh báo học vụ và buộc thôi học tại Trường Y Dược - Đại học Trà Vinh

## Điều kiện cảnh báo

Sinh viên có thể bị cảnh báo kết quả học tập khi thuộc một trong các trường hợp sau:

- Điểm trung bình chung tích lũy dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; hoặc dưới 1,80 ở các năm tiếp theo và cuối khóa. - Điểm trung bình chung học kỳ dưới 0,80 ở học kỳ đầu tiên của khóa học hoặc dưới 1,00 ở các học kỳ tiếp theo. - Tổng số tín chỉ của các học phần điểm F còn tồn đọng vượt quá 24 tín chỉ.
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tnut-advanced-registration::c02] Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ. ## Số tín chỉ ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[qtu-academic-affairs-overview::c01] # Phạm vi Quy định công tác học vụ

Quy định công tác học vụ của Trường Đại học Quang Trung được ban hành theo Quyết định số 95/QĐ-ĐHQT ngày 24 tháng 6 năm 2021 và áp dụng trong toàn trường. ## Các nhóm nội dung

Quy định bao quát việc đăng ký, học lại, học cải thiện và rút học phần; kiểm tra, đánh giá kết quả, điều kiện dự thi và phúc khảo; cảnh báo học tập, buộc nghỉ học, tạm dừng và tiếp nhận học lại; cùng các thủ tục xác nhận sinh viên, chuyển ngành, chuyển cơ sở đào tạo và cấp văn bằng, chứng chỉ. Văn bản xác định trách nhiệm của sinh viên, giảng viên, cố vấn học tập và các đơn vị chức năng trong việc thực hiện và hỗ trợ công tác học vụ.
Nguồn: https://qtu.edu.vn/qd-95-ban-hanh-quy-dinh-ve-cong-tac-hoc-vu-tai-truong-dai-hoc-quang-trung/

## fixed500_overlap50

26 chunks; trung bình 429.34615 ký tự.

### Q1: Tại Trường Y Dược - Đại học Trà Vinh, sinh viên được rút học phần trong thời hạn nào và nếu tự ý bỏ học từ tuần thứ ba thì bị xử lý ra sao?

Gold: Sinh viên được rút học phần trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn được giữ trong phiếu đăng ký; nếu không đi học thì bị xem là tự ý bỏ học và nhận điểm F.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tnut-advanced-withdrawal-assessment::c01 — 0.293033**

# Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z.

Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí. Việc rút được thực hiện trực tuyến trên cổng đăng ký học hoặc bằng đơn gửi

**Top 2: tvu-course-registration::c02 — 0.291454**

ột tuần kể từ ngày kết thúc đăng ký, sinh viên phải kiểm tra lớp có được mở hay không. Nếu lớp không được chấp nhận, sinh viên đăng ký sang lớp khác. Trường hợp hệ thống khóa, lớp đủ sĩ số hoặc có khó khăn khác, sinh viên dùng mẫu đơn và nộp trực tiếp cho Phòng Đào tạo.

## Rút bớt học phần

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F

**Top 3: tvu-course-registration::c01 — 0.219811**

# Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.

Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt. Sau một tuần kể từ ngày kết thúc đăng ký, sinh viên phả

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tnut-advanced-withdrawal-assessment::c01] # Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z.

Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí. Việc rút được thực hiện trực tuyến trên cổng đăng ký học hoặc bằng đơn gửi
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c02] ột tuần kể từ ngày kết thúc đăng ký, sinh viên phải kiểm tra lớp có được mở hay không. Nếu lớp không được chấp nhận, sinh viên đăng ký sang lớp khác. Trường hợp hệ thống khóa, lớp đủ sĩ số hoặc có khó khăn khác, sinh viên dùng mẫu đơn và nộp trực tiếp cho Phòng Đào tạo.

## Rút bớt học phần

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tvu-course-registration::c01] # Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.

Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt. Sau một tuần kể từ ngày kết thúc đăng ký, sinh viên phả
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q2: Sinh viên Đại học Thủ Dầu Một phải nộp đơn phúc khảo ở đâu, trong bao lâu và phải thực hiện quy định lệ phí như thế nào?

Gold: Sinh viên nộp đơn BM.01 về bộ môn quản lý đề cương học phần trong vòng bảy ngày từ ngày công bố điểm và phải đóng lệ phí phúc khảo theo quy định.

Filter: `{'audience': 'student'}`; đúng tài liệu: True; đủ cụm bằng chứng: False.

**Top 1: tdmu-grade-appeal::c01 — 0.378111**

# Quy trình phúc khảo bài kiểm tra tại Trường Đại học Thủ Dầu Một

Quy trình áp dụng cho sinh viên các hệ đào tạo, học viên cao học, đơn vị đào tạo và các đơn vị phối hợp tại Trường Đại học Thủ Dầu Một. Tài liệu tham chiếu Quyết định số 714/QĐ-ĐHTDM ngày 13 tháng 6 năm 2024 về khảo thí và đo lường kết quả học tập.

## Sinh viên nộp đơn

Sinh viên có yêu cầu phúc khảo phải lập đơn theo biểu mẫu BM.01 và nộp về bộ môn quản lý đề cương học phần trong vòng bảy ngày kể từ ngày công bố điểm kiểm tra. 

**Top 2: tvu-grade-appeal::c01 — 0.234131**

# Phúc khảo và điều chỉnh điểm tại Trường Y Dược - Đại học Trà Vinh

## Phúc khảo

Sinh viên có nhu cầu phúc khảo phải làm đề nghị theo biểu mẫu chung, gửi Phòng Khảo thí trong vòng 15 ngày kể từ ngày niêm yết kết quả và đóng lệ phí theo quy định. Khoa chịu trách nhiệm tổ chức chấm phúc khảo.

Các học phần có hình thức đánh giá kết thúc bằng báo cáo, vấn đáp hoặc thực hành không thuộc diện được yêu cầu phúc khảo.

## Điều chỉnh điểm

Khi có sai sót về điểm đánh giá kết thúc hoặc điểm tổng kết họ

**Top 3: tnut-advanced-withdrawal-assessment::c01 — 0.218994**

# Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z.

Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí. Việc rút được thực hiện trực tuyến trên cổng đăng ký học hoặc bằng đơn gửi

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tdmu-grade-appeal::c01] # Quy trình phúc khảo bài kiểm tra tại Trường Đại học Thủ Dầu Một

Quy trình áp dụng cho sinh viên các hệ đào tạo, học viên cao học, đơn vị đào tạo và các đơn vị phối hợp tại Trường Đại học Thủ Dầu Một. Tài liệu tham chiếu Quyết định số 714/QĐ-ĐHTDM ngày 13 tháng 6 năm 2024 về khảo thí và đo lường kết quả học tập.

## Sinh viên nộp đơn

Sinh viên có yêu cầu phúc khảo phải lập đơn theo biểu mẫu BM.01 và nộp về bộ môn quản lý đề cương học phần trong vòng bảy ngày kể từ ngày công bố điểm kiểm tra. 
Nguồn: https://tdmu.edu.vn/hinh/thuvien/taptin/2-6-2025-4-42-24-pm06-BKTKDDBCL-QT.09-Phuc%20khao%20Bai%20KTr.pdf

[tvu-grade-appeal::c01] # Phúc khảo và điều chỉnh điểm tại Trường Y Dược - Đại học Trà Vinh

## Phúc khảo

Sinh viên có nhu cầu phúc khảo phải làm đề nghị theo biểu mẫu chung, gửi Phòng Khảo thí trong vòng 15 ngày kể từ ngày niêm yết kết quả và đóng lệ phí theo quy định. Khoa chịu trách nhiệm tổ chức chấm phúc khảo.

Các học phần có hình thức đánh giá kết thúc bằng báo cáo, vấn đáp hoặc thực hành không thuộc diện được yêu cầu phúc khảo.

## Điều chỉnh điểm

Khi có sai sót về điểm đánh giá kết thúc hoặc điểm tổng kết họ
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tnut-advanced-withdrawal-assessment::c01] # Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z.

Sinh viên không làm thủ tục rút mà tự ý bỏ học phải nhận điểm F và vẫn phải nộp học phí. Việc rút được thực hiện trực tuyến trên cổng đăng ký học hoặc bằng đơn gửi
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

### Q3: Sinh viên chương trình tiên tiến TNUT được đăng ký tối thiểu và tối đa bao nhiêu tín chỉ trong học kỳ chính?

Gold: Với năm học có ba học kỳ chính, giới hạn là 8–16 tín chỉ mỗi kỳ; với năm học có hai học kỳ chính, giới hạn là 10–24 tín chỉ mỗi kỳ.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tnut-advanced-registration::c02 — 0.512724**

ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.

**Top 2: tnut-advanced-registration::c01 — 0.349507**

# Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký. Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ.

## Số tín chỉ ở học kỳ chính

Nếu năm học có ba học kỳ chính, si

**Top 3: tvu-course-registration::c03 — 0.232553**

ông học thì được xem là tự ý bỏ học và nhận điểm F.

## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa. Sinh viên đang bị xếp hạng học lực yếu đăng ký ít nhất 10 tín chỉ, trừ học kỳ cuối khóa. Học kỳ hè không quy định khối lượng tối thiểu.

> Ghi chú nguồn: Nội dung được nhóm rút gọn và diễn đạt lại từ mục “Tổ chức đào tạo” của Sổ tay sinh viên 2026; không bao gồm menu và các liên kết không liên quan trên trang.

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tnut-advanced-registration::c02] ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tnut-advanced-registration::c01] # Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký. Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ.

## Số tín chỉ ở học kỳ chính

Nếu năm học có ba học kỳ chính, si
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c03] ông học thì được xem là tự ý bỏ học và nhận điểm F.

## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa. Sinh viên đang bị xếp hạng học lực yếu đăng ký ít nhất 10 tín chỉ, trừ học kỳ cuối khóa. Học kỳ hè không quy định khối lượng tối thiểu.

> Ghi chú nguồn: Nội dung được nhóm rút gọn và diễn đạt lại từ mục “Tổ chức đào tạo” của Sổ tay sinh viên 2026; không bao gồm menu và các liên kết không liên quan trên trang.
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q4: Ở UFM, khi lập kế hoạch đăng ký học phần, sinh viên cần tìm hiểu những gì và có thể nhờ ai tư vấn?

Gold: Sinh viên cần tìm hiểu chương trình đào tạo, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và điều kiện cá nhân; có thể liên hệ cố vấn học tập khi cần tư vấn.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: ufm-course-registration::c01 — 0.315269**

# Tổ chức đăng ký học tập tại Đại học Tài chính - Marketing (UFM)

Đăng ký học phần là quy trình bắt buộc trước mỗi học kỳ. Sinh viên chọn học phần mới, học phần chưa đạt để học lại và học phần đã đạt để cải thiện điểm trên hệ thống quản lý đào tạo bằng tài khoản cá nhân.

Nếu không đăng ký được trên hệ thống, sinh viên phải trực tiếp liên hệ Phòng Quản lý đào tạo trong thời gian đăng ký để được hướng dẫn. Trước khi đăng ký, sinh viên cần tìm hiểu chương trình, đề cương học phần, điều kiện đăng 

**Top 2: ufm-course-registration::c02 — 0.306767**

u chương trình, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và cân nhắc điều kiện cá nhân. Sinh viên có thể liên hệ cố vấn học tập khi cần tư vấn.

Học kỳ đầu tiên, sinh viên học theo thời khóa biểu do Trường ấn định. Từ học kỳ thứ hai, sinh viên đăng ký học phần và khối lượng học tập theo kế hoạch được công bố. Trường có thể đăng ký sẵn học phần bắt buộc; sinh viên vẫn phải truy cập tài khoản để kiểm tra và điều chỉnh phù hợp.

Hai tháng trư

**Top 3: tvu-course-registration::c01 — 0.269228**

# Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.

Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt. Sau một tuần kể từ ngày kết thúc đăng ký, sinh viên phả

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[ufm-course-registration::c01] # Tổ chức đăng ký học tập tại Đại học Tài chính - Marketing (UFM)

Đăng ký học phần là quy trình bắt buộc trước mỗi học kỳ. Sinh viên chọn học phần mới, học phần chưa đạt để học lại và học phần đã đạt để cải thiện điểm trên hệ thống quản lý đào tạo bằng tài khoản cá nhân.

Nếu không đăng ký được trên hệ thống, sinh viên phải trực tiếp liên hệ Phòng Quản lý đào tạo trong thời gian đăng ký để được hướng dẫn. Trước khi đăng ký, sinh viên cần tìm hiểu chương trình, đề cương học phần, điều kiện đăng 
Nguồn: https://pdt.ufm.edu.vn/dulieu/quiche/1329_Quy_che_dao_tao_tin_chi_tu_khoa_2021.htm

[ufm-course-registration::c02] u chương trình, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và cân nhắc điều kiện cá nhân. Sinh viên có thể liên hệ cố vấn học tập khi cần tư vấn.

Học kỳ đầu tiên, sinh viên học theo thời khóa biểu do Trường ấn định. Từ học kỳ thứ hai, sinh viên đăng ký học phần và khối lượng học tập theo kế hoạch được công bố. Trường có thể đăng ký sẵn học phần bắt buộc; sinh viên vẫn phải truy cập tài khoản để kiểm tra và điều chỉnh phù hợp.

Hai tháng trư
Nguồn: https://pdt.ufm.edu.vn/dulieu/quiche/1329_Quy_che_dao_tao_tin_chi_tu_khoa_2021.htm

[tvu-course-registration::c01] # Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.

Ở giai đoạn chọn lớp, sinh viên đăng ký lớp và lịch học dựa trên kế hoạch đã được duyệt. Sau một tuần kể từ ngày kết thúc đăng ký, sinh viên phả
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q5: Các ngưỡng điểm trung bình tích lũy nào khiến sinh viên TVU bị cảnh báo học vụ theo từng năm và số tín chỉ F tồn đọng tối đa là bao nhiêu?

Gold: Ngưỡng cảnh báo là dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; dưới 1,80 ở các năm tiếp theo và cuối khóa. Một căn cứ khác là số tín chỉ F tồn đọng vượt quá 24 tín chỉ.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tvu-academic-warning::c01 — 0.361047**

# Cảnh báo học vụ và buộc thôi học tại Trường Y Dược - Đại học Trà Vinh

## Điều kiện cảnh báo

Sinh viên có thể bị cảnh báo kết quả học tập khi thuộc một trong các trường hợp sau:

- Điểm trung bình chung tích lũy dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; hoặc dưới 1,80 ở các năm tiếp theo và cuối khóa.
- Điểm trung bình chung học kỳ dưới 0,80 ở học kỳ đầu tiên của khóa học hoặc dưới 1,00 ở các học kỳ tiếp theo.
- Tổng số tín chỉ của các học phần điểm F còn tồn 

**Top 2: tnut-advanced-registration::c02 — 0.267171**

ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.

**Top 3: tvu-academic-warning::c02 — 0.208268**

- Tổng số tín chỉ của các học phần điểm F còn tồn đọng vượt quá 24 tín chỉ.
- Không đóng học phí một học kỳ.

## Trường hợp buộc thôi học

Sau mỗi học kỳ, sinh viên có thể bị buộc thôi học nếu bị kỷ luật ở mức buộc thôi học, có số lần cảnh báo kết quả học tập vượt quá hai lần, không đóng học phí hai học kỳ liên tiếp, có điểm rèn luyện cả năm loại kém lần thứ hai, vi phạm thi hộ lần thứ hai hoặc đã hết thời gian học tối đa.

> Ghi chú nguồn: Nội dung được nhóm rút gọn và diễn đạt lại từ mục “Cảnh

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tvu-academic-warning::c01] # Cảnh báo học vụ và buộc thôi học tại Trường Y Dược - Đại học Trà Vinh

## Điều kiện cảnh báo

Sinh viên có thể bị cảnh báo kết quả học tập khi thuộc một trong các trường hợp sau:

- Điểm trung bình chung tích lũy dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; hoặc dưới 1,80 ở các năm tiếp theo và cuối khóa.
- Điểm trung bình chung học kỳ dưới 0,80 ở học kỳ đầu tiên của khóa học hoặc dưới 1,00 ở các học kỳ tiếp theo.
- Tổng số tín chỉ của các học phần điểm F còn tồn 
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tnut-advanced-registration::c02] ở học kỳ chính

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-academic-warning::c02] - Tổng số tín chỉ của các học phần điểm F còn tồn đọng vượt quá 24 tín chỉ.
- Không đóng học phí một học kỳ.

## Trường hợp buộc thôi học

Sau mỗi học kỳ, sinh viên có thể bị buộc thôi học nếu bị kỷ luật ở mức buộc thôi học, có số lần cảnh báo kết quả học tập vượt quá hai lần, không đóng học phí hai học kỳ liên tiếp, có điểm rèn luyện cả năm loại kém lần thứ hai, vi phạm thi hộ lần thứ hai hoặc đã hết thời gian học tối đa.

> Ghi chú nguồn: Nội dung được nhóm rút gọn và diễn đạt lại từ mục “Cảnh
Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

## recursive500

30 chunks; trung bình 345.43333 ký tự.

### Q1: Tại Trường Y Dược - Đại học Trà Vinh, sinh viên được rút học phần trong thời hạn nào và nếu tự ý bỏ học từ tuần thứ ba thì bị xử lý ra sao?

Gold: Sinh viên được rút học phần trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn được giữ trong phiếu đăng ký; nếu không đi học thì bị xem là tự ý bỏ học và nhận điểm F.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tvu-course-registration::c03 — 0.292075**

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F.

## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa. Sinh viên đang bị xếp hạng học lực yếu đăng ký ít nhất 10 tín chỉ, trừ học kỳ cuối khóa. Học kỳ hè không quy định khối lượng tối thiểu.



**Top 2: tnut-advanced-withdrawal-assessment::c01 — 0.274507**

# Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z.



**Top 3: tvu-course-registration::c01 — 0.240976**

# Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.



**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tvu-course-registration::c03] Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F.

## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa. Sinh viên đang bị xếp hạng học lực yếu đăng ký ít nhất 10 tín chỉ, trừ học kỳ cuối khóa. Học kỳ hè không quy định khối lượng tối thiểu.


Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tnut-advanced-withdrawal-assessment::c01] # Rút học phần và đánh giá

## Rút học phần

Sinh viên rút học phần trong tuần đầu của học kỳ thì không phải nộp học phí cho học phần đó. Sau thời điểm này, sinh viên vẫn có thể rút nhưng không được rút học phí nếu thực hiện trước kỳ thi kết thúc bốn tuần đối với học kỳ chính hoặc ba tuần đối với học kỳ phụ; học phần được ghi điểm Z.


Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c01] # Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.


Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q2: Sinh viên Đại học Thủ Dầu Một phải nộp đơn phúc khảo ở đâu, trong bao lâu và phải thực hiện quy định lệ phí như thế nào?

Gold: Sinh viên nộp đơn BM.01 về bộ môn quản lý đề cương học phần trong vòng bảy ngày từ ngày công bố điểm và phải đóng lệ phí phúc khảo theo quy định.

Filter: `{'audience': 'student'}`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tdmu-grade-appeal::c01 — 0.379673**

# Quy trình phúc khảo bài kiểm tra tại Trường Đại học Thủ Dầu Một

Quy trình áp dụng cho sinh viên các hệ đào tạo, học viên cao học, đơn vị đào tạo và các đơn vị phối hợp tại Trường Đại học Thủ Dầu Một. Tài liệu tham chiếu Quyết định số 714/QĐ-ĐHTDM ngày 13 tháng 6 năm 2024 về khảo thí và đo lường kết quả học tập.

## Sinh viên nộp đơn



**Top 2: tvu-grade-appeal::c01 — 0.256417**

# Phúc khảo và điều chỉnh điểm tại Trường Y Dược - Đại học Trà Vinh

## Phúc khảo

Sinh viên có nhu cầu phúc khảo phải làm đề nghị theo biểu mẫu chung, gửi Phòng Khảo thí trong vòng 15 ngày kể từ ngày niêm yết kết quả và đóng lệ phí theo quy định. Khoa chịu trách nhiệm tổ chức chấm phúc khảo.

Các học phần có hình thức đánh giá kết thúc bằng báo cáo, vấn đáp hoặc thực hành không thuộc diện được yêu cầu phúc khảo.

## Điều chỉnh điểm



**Top 3: tdmu-grade-appeal::c02 — 0.206892**

Sinh viên có yêu cầu phúc khảo phải lập đơn theo biểu mẫu BM.01 và nộp về bộ môn quản lý đề cương học phần trong vòng bảy ngày kể từ ngày công bố điểm kiểm tra. Thư ký hỗ trợ khảo thí tiếp nhận đơn, trình lãnh đạo duyệt; sinh viên đóng lệ phí theo quy định của Ban Tài chính - Kế toán.

## Thành lập và tổ chức chấm



**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tdmu-grade-appeal::c01] # Quy trình phúc khảo bài kiểm tra tại Trường Đại học Thủ Dầu Một

Quy trình áp dụng cho sinh viên các hệ đào tạo, học viên cao học, đơn vị đào tạo và các đơn vị phối hợp tại Trường Đại học Thủ Dầu Một. Tài liệu tham chiếu Quyết định số 714/QĐ-ĐHTDM ngày 13 tháng 6 năm 2024 về khảo thí và đo lường kết quả học tập.

## Sinh viên nộp đơn


Nguồn: https://tdmu.edu.vn/hinh/thuvien/taptin/2-6-2025-4-42-24-pm06-BKTKDDBCL-QT.09-Phuc%20khao%20Bai%20KTr.pdf

[tvu-grade-appeal::c01] # Phúc khảo và điều chỉnh điểm tại Trường Y Dược - Đại học Trà Vinh

## Phúc khảo

Sinh viên có nhu cầu phúc khảo phải làm đề nghị theo biểu mẫu chung, gửi Phòng Khảo thí trong vòng 15 ngày kể từ ngày niêm yết kết quả và đóng lệ phí theo quy định. Khoa chịu trách nhiệm tổ chức chấm phúc khảo.

Các học phần có hình thức đánh giá kết thúc bằng báo cáo, vấn đáp hoặc thực hành không thuộc diện được yêu cầu phúc khảo.

## Điều chỉnh điểm


Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tdmu-grade-appeal::c02] Sinh viên có yêu cầu phúc khảo phải lập đơn theo biểu mẫu BM.01 và nộp về bộ môn quản lý đề cương học phần trong vòng bảy ngày kể từ ngày công bố điểm kiểm tra. Thư ký hỗ trợ khảo thí tiếp nhận đơn, trình lãnh đạo duyệt; sinh viên đóng lệ phí theo quy định của Ban Tài chính - Kế toán.

## Thành lập và tổ chức chấm


Nguồn: https://tdmu.edu.vn/hinh/thuvien/taptin/2-6-2025-4-42-24-pm06-BKTKDDBCL-QT.09-Phuc%20khao%20Bai%20KTr.pdf

### Q3: Sinh viên chương trình tiên tiến TNUT được đăng ký tối thiểu và tối đa bao nhiêu tín chỉ trong học kỳ chính?

Gold: Với năm học có ba học kỳ chính, giới hạn là 8–16 tín chỉ mỗi kỳ; với năm học có hai học kỳ chính, giới hạn là 10–24 tín chỉ mỗi kỳ.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tnut-advanced-registration::c02 — 0.502466**

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.

**Top 2: tnut-advanced-registration::c01 — 0.337259**

# Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký. Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ.

## Số tín chỉ ở học kỳ chính



**Top 3: tvu-course-registration::c03 — 0.277978**

Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F.

## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa. Sinh viên đang bị xếp hạng học lực yếu đăng ký ít nhất 10 tín chỉ, trừ học kỳ cuối khóa. Học kỳ hè không quy định khối lượng tối thiểu.



**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tnut-advanced-registration::c02] Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tnut-advanced-registration::c01] # Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký. Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ.

## Số tín chỉ ở học kỳ chính


Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c03] Sinh viên được rút bớt học phần đã đăng ký trong vòng hai tuần kể từ đầu học kỳ chính. Từ tuần thứ ba, học phần vẫn nằm trong phiếu đăng ký; nếu sinh viên không học thì được xem là tự ý bỏ học và nhận điểm F.

## Khối lượng học tập

Sinh viên có học lực trung bình đăng ký ít nhất 15 tín chỉ mỗi học kỳ, trừ học kỳ cuối khóa. Sinh viên đang bị xếp hạng học lực yếu đăng ký ít nhất 10 tín chỉ, trừ học kỳ cuối khóa. Học kỳ hè không quy định khối lượng tối thiểu.


Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q4: Ở UFM, khi lập kế hoạch đăng ký học phần, sinh viên cần tìm hiểu những gì và có thể nhờ ai tư vấn?

Gold: Sinh viên cần tìm hiểu chương trình đào tạo, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và điều kiện cá nhân; có thể liên hệ cố vấn học tập khi cần tư vấn.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: ufm-course-registration::c02 — 0.412723**

Nếu không đăng ký được trên hệ thống, sinh viên phải trực tiếp liên hệ Phòng Quản lý đào tạo trong thời gian đăng ký để được hướng dẫn. Trước khi đăng ký, sinh viên cần tìm hiểu chương trình, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và cân nhắc điều kiện cá nhân. Sinh viên có thể liên hệ cố vấn học tập khi cần tư vấn.



**Top 2: tnut-advanced-registration::c01 — 0.271597**

# Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký. Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ.

## Số tín chỉ ở học kỳ chính



**Top 3: tvu-course-registration::c01 — 0.245659**

# Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.



**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[ufm-course-registration::c02] Nếu không đăng ký được trên hệ thống, sinh viên phải trực tiếp liên hệ Phòng Quản lý đào tạo trong thời gian đăng ký để được hướng dẫn. Trước khi đăng ký, sinh viên cần tìm hiểu chương trình, đề cương học phần, điều kiện đăng ký, kế hoạch đào tạo và thời khóa biểu; kiểm tra kết quả đã học và cân nhắc điều kiện cá nhân. Sinh viên có thể liên hệ cố vấn học tập khi cần tư vấn.


Nguồn: https://pdt.ufm.edu.vn/dulieu/quiche/1329_Quy_che_dao_tao_tin_chi_tu_khoa_2021.htm

[tnut-advanced-registration::c01] # Đăng ký học phần chương trình tiên tiến

## Trách nhiệm và thời gian đăng ký

Trước mỗi học kỳ, Nhà trường thông báo kế hoạch và hướng dẫn sinh viên đăng ký trên hệ thống. Cố vấn học tập tư vấn kế hoạch phù hợp với năng lực và điều kiện của sinh viên. Sinh viên phải đăng ký trước khi học kỳ mới bắt đầu, tự bảo mật tài khoản và chịu trách nhiệm về kết quả đăng ký. Đợt đăng ký diễn ra trong khoảng hai đến ba tuần trước mỗi học kỳ.

## Số tín chỉ ở học kỳ chính


Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176

[tvu-course-registration::c01] # Đăng ký và rút học phần tại Trường Y Dược - Đại học Trà Vinh

## Quy trình đăng ký

Sinh viên xây dựng kế hoạch học tập cho học kỳ mới bằng cách chọn học phần trong chương trình đào tạo và ghi vào sổ đăng ký học tập. Kế hoạch này được trình cố vấn học tập phê duyệt trước khi sinh viên đăng ký trên phần mềm quản lý đào tạo theo lịch của Phòng Đào tạo.


Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

### Q5: Các ngưỡng điểm trung bình tích lũy nào khiến sinh viên TVU bị cảnh báo học vụ theo từng năm và số tín chỉ F tồn đọng tối đa là bao nhiêu?

Gold: Ngưỡng cảnh báo là dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; dưới 1,80 ở các năm tiếp theo và cuối khóa. Một căn cứ khác là số tín chỉ F tồn đọng vượt quá 24 tín chỉ.

Filter: `None`; đúng tài liệu: True; đủ cụm bằng chứng: True.

**Top 1: tvu-academic-warning::c02 — 0.288456**

- Điểm trung bình chung tích lũy dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; hoặc dưới 1,80 ở các năm tiếp theo và cuối khóa.
- Điểm trung bình chung học kỳ dưới 0,80 ở học kỳ đầu tiên của khóa học hoặc dưới 1,00 ở các học kỳ tiếp theo.
- Tổng số tín chỉ của các học phần điểm F còn tồn đọng vượt quá 24 tín chỉ.
- Không đóng học phí một học kỳ.

## Trường hợp buộc thôi học



**Top 2: tvu-academic-warning::c01 — 0.283980**

# Cảnh báo học vụ và buộc thôi học tại Trường Y Dược - Đại học Trà Vinh

## Điều kiện cảnh báo

Sinh viên có thể bị cảnh báo kết quả học tập khi thuộc một trong các trường hợp sau:



**Top 3: tnut-advanced-registration::c02 — 0.274161**

Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.

**Đầu ra Agent (nguyên văn):**

[Trích xuất ngữ cảnh; không dùng LLM]
[tvu-academic-warning::c02] - Điểm trung bình chung tích lũy dưới 1,20 ở năm thứ nhất; dưới 1,40 ở năm thứ hai; dưới 1,60 ở năm thứ ba; hoặc dưới 1,80 ở các năm tiếp theo và cuối khóa.
- Điểm trung bình chung học kỳ dưới 0,80 ở học kỳ đầu tiên của khóa học hoặc dưới 1,00 ở các học kỳ tiếp theo.
- Tổng số tín chỉ của các học phần điểm F còn tồn đọng vượt quá 24 tín chỉ.
- Không đóng học phí một học kỳ.

## Trường hợp buộc thôi học


Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tvu-academic-warning::c01] # Cảnh báo học vụ và buộc thôi học tại Trường Y Dược - Đại học Trà Vinh

## Điều kiện cảnh báo

Sinh viên có thể bị cảnh báo kết quả học tập khi thuộc một trong các trường hợp sau:


Nguồn: https://cmp.tvu.edu.vn/so-tay-sinh-vien/

[tnut-advanced-registration::c02] Nếu năm học có ba học kỳ chính, sinh viên đăng ký tối thiểu 8 tín chỉ và tối đa 16 tín chỉ trong một kỳ. Nếu năm học có hai học kỳ chính, mức tối thiểu là 10 tín chỉ và tối đa là 24 tín chỉ.

Không áp dụng khối lượng tối thiểu cho sinh viên năm cuối đang thực tập hoặc làm đồ án tốt nghiệp và cho sinh viên đăng ký học kỳ phụ. Khối lượng tối đa của học kỳ phụ được Nhà trường thông báo theo điều kiện mở lớp từng năm.
Nguồn: https://fit.tnut.edu.vn/bai-viet/quy-che-dao-tao-trinh-do-dai-hoc-cho-chuong-trinh-tien-tien-nam-2022-176
