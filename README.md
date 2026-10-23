# BÁO CÁO TRIỂN KHAI HỆ THỐNG QUẢN LÝ NHÂN SỰ (HRM)
- **Môn học:** Triển khai và Quản trị Hệ thống Phần mềm
- **Sinh viên thực hiện:** Ma Khánh Tùng 
- **Mã số sinh viên (MSV)** DTC245180014
- **Đề tài:** Đề 10 - Hệ thống Quản lý Nhân sự (HRM)
- **Môi trường triển khai:** Ubuntu Server 18.04 LTS, Docker Compose

---

## 1. Kiến trúc tổng thể hệ thống

Hệ thống bao gồm các thành phần được đóng gói và vận hành qua Docker Compose:
- **Web App HRM:** Ứng dụng Flask/Python quản lý nhân viên, phòng ban, chấm công.
- **Database:** PostgreSQL 15 lưu trữ dữ liệu nghiệp vụ.
- **Quản trị Database:** pgAdmin 4 giao diện trực quan.
- **Reverse Proxy:** Nginx cấu hình SSL tự ký (HTTPS) và các Security Headers.
- **Giám sát Metrics:** Prometheus + Grafana (tích hợp cAdvisor, postgres-exporter, nginx-prometheus-exporter).
- **Thu thập Log tập trung:** Loki + Promtail.

Hệ thống được cô lập qua 3 Docker Bridge Network:
- `frontend_net`: Nginx, pgAdmin, App, Nginx-exporter.
- `backend_net`: App, PostgreSQL, pgAdmin, Postgres-exporter.
- `monitoring_net`: Prometheus, Grafana, Loki, Promtail, cAdvisor, các Exporter.

---

## 2. Hướng dẫn khởi chạy hệ thống

### Yêu cầu tiên quyết:
- Máy chủ Ubuntu Server 18.04 LTS đã cài Docker Engine và Docker Compose plugin.
- Quyền thực thi lệnh Docker (`sudo usermod -aG docker $USER`).

### Các bước triển khai:
```bash
# 1. Clone repository về máy
git clone https://github.com/khanhtung14/He-thong-qun-ly-nhan-su.git
cd hrm-project

# 2. Khởi tạo file biến môi trường từ file mẫu
cp .env.example .env

# 3. Tạo chứng chỉ SSL tự ký cho Nginx (nếu chưa có)
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout nginx/certs/selfsigned.key \
  -out nginx/certs/selfsigned.crt \
  -subj "/C=VN/ST=Hanoi/L=Hanoi/O=IT/CN=localhost"

# 4. Build image cho ứng dụng web HRM
docker build -t hrm-project-app:latest ./app

# 5. Khởi chạy toàn bộ hệ thống bằng Docker Compose
docker compose up -d

# 6. Kiểm tra trạng thái toàn bộ containers
docker compose ps
