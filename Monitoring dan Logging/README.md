Model Monitoring & Logging System

Sistem ini merupakan bagian dari alur kerja MLOps yang bertujuan untuk memantau performa model machine learning secara real-time. Sistem ini menggunakan Prometheus untuk menarik data metrik dan Grafana untuk visualisasi dashboard.

🛠️ Arsitektur Teknologi
-Python/Flask: Sebagai penyedia metrik kustom (Exporter).
-Prometheus: Database deret waktu (time-series database) untuk mengumpulkan metrik.
-Grafana: Antarmuka visualisasi data.
-Docker: Orkestrasi kontainer menggunakan `docker-compose`.

⚙️Cara Menjalankan Sistem

1. Pastikan Anda berada di dalam direktori proyek ini.
2. Jalankan orkestrasi kontainer untuk Prometheus dan Grafana:
   ```bash
   docker compose up -d
3. Jalankan script penyedia metrik:   
    python 3.prometheus_exporter.py
4. Akses Grafana melalui web browser pada http://localhost:3000    