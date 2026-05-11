# 📰 Tự Động Lấy Tin Tức Dân Trí (Auto Fetch News)

Dự án này là một công cụ tự động lấy tin tức mới nhất từ RSS của báo Dân Trí, lưu trữ dưới dạng file JSON và hiển thị lên một trang web tĩnh (Static Web). Toàn bộ quá trình chạy hoàn toàn tự động và miễn phí dựa trên **GitHub Actions** và **GitHub Pages**.

## 🚀 Tính năng nổi bật

- **Tự động hóa hoàn toàn:** Sử dụng GitHub Actions để chạy script Python tự động **10 phút một lần**.
- **Không cần Database:** Dữ liệu được lưu trực tiếp thành file `dantri_news.json`.
- **Giao diện tối giản:** Đọc tin nhanh chóng qua trang `index.html` với HTML/CSS/JS thuần, không chứa quảng cáo.
- **Tránh bị cache:** Tự động nạp file JSON mới nhất mỗi khi load lại trang.

## 📂 Cấu trúc thư mục

\`\`\`text
├── fetch_news.py          # Script Python lấy dữ liệu từ RSS Dân Trí
├── dantri_news.json       # File dữ liệu được tự động sinh ra (Bot tự push lên)
├── index.html             # Giao diện web hiển thị tin tức
├── README.md              # Tài liệu hướng dẫn
└── .github/
    └── workflows/
        └── update_news.yml # Cấu hình GitHub Actions tự động chạy mỗi 10 phút
\`\`\`

## 🛠️ Hướng dẫn cài đặt (Dành cho người mới clone/fork project)

Nếu bạn muốn tạo một dự án tương tự trên tài khoản GitHub của mình, hãy làm theo các bước sau:

### Bước 1: Cấp quyền cho GitHub Actions
Mặc định GitHub Actions không được phép ghi đè file. Để bot có thể tạo và cập nhật file `dantri_news.json`, bạn cần:
1. Vào **Settings** > **Actions** > **General**.
2. Kéo xuống mục **Workflow permissions**.
3. Tích chọn **Read and write permissions** và bấm **Save**.

### Bước 2: Kích hoạt lần đầu tiên (Tạo file JSON)
1. Chuyển sang tab **Actions**.
2. Bấm vào workflow **Tự động cập nhật tin Dân Trí** ở bên trái.
3. Chọn **Run workflow** để kịch bản chạy lần đầu tiên. Chờ khoảng 30s bạn sẽ thấy file `dantri_news.json` xuất hiện trong thư mục mã nguồn.

### Bước 3: Bật trang web hiển thị (GitHub Pages)
1. Vào **Settings** > **Pages**.
2. Tại mục **Build and deployment** (Source), chọn `Deploy from a branch`.
3. Tại phần **Branch**, chọn nhánh `main` (hoặc `master`) và lưu lại.
4. Đợi vài phút, GitHub sẽ cấp cho bạn một đường link web để truy cập (Ví dụ: `https://<tên-của-bạn>.github.io/<tên-repo>/`).

## 💻 Công nghệ sử dụng
- **Python 3**: Lấy và phân tích dữ liệu XML/RSS.
- **HTML/CSS/Vanilla JS**: Thiết kế giao diện và parse dữ liệu JSON lên DOM.
- **GitHub Actions**: Lập lịch chạy (Cron Job) và tự động Commit.
- **GitHub Pages**: Hosting tĩnh miễn phí.
