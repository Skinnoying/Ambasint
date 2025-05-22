
# 🔍 Ambasint

![badge](https://img.shields.io/badge/OSINT-Tool-blueviolet?style=for-the-badge)
![python](https://img.shields.io/badge/Python-3.9%2B-yellow?style=for-the-badge)
![flask](https://img.shields.io/badge/Flask-Web%20App-green?style=for-the-badge)
![status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**Ambasint** adalah tool OSINT (Open-Source Intelligence) berbasis web untuk melacak keberadaan username di berbagai jejaring sosial dan platform online. Cocok digunakan untuk investigasi digital, cyber security, dan riset open-source.

---

## 🚀 Fitur

- 🔁 **Hybrid Pencarian (async + cloudscraper)** — cepat & mampu melewati proteksi seperti Cloudflare
- 🧠 **Auto Integrasi Database Sherlock** — mendukung ratusan situs tanpa penambahan manual
- ✅ **Validasi Akun Otomatis** — cek status akun aktif/tidak + link profil langsung
- 📊 **Dashboard Modern** — UI interaktif untuk hasil pencarian yang jelas dan menarik
- 🔄 **Update Otomatis data.json** — sinkron dengan repositori resmi Sherlock Project

---

## 📦 Instalasi

```bash
# 1. Clone repo ini
git clone https://github.com/Skinnoying/Ambasint.git
cd Ambasint

# 2. (Opsional) Aktifkan virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install semua dependensi
pip install -r requirements.txt

# 4. Jalankan aplikasi
python app.py
```

---

## 🌐 Cara Menggunakan

1. Jalankan `python app.py`.
2. Buka browser ke `http://127.0.0.1:5000`.
3. Masukkan username yang ingin dicari.
4. Lihat hasil: akun valid/invalid lengkap dengan link ke profil.

---

## 📁 Struktur Direktori

```
Ambasint/
├── app.py
├── checker/
│   ├── __init__.py
│   ├── config.py
│   ├── async_checker.py
│   ├── sync_checker.py
│   ├── hybrid_checker.py
│   └── data.json
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   ├── index.html
│   └── result.html
└── requirements.txt
```

---

## ⚠️ Disclaimer

> Tool ini hanya untuk **riset & edukasi**. Jangan digunakan untuk aktivitas ilegal.

---

## 📜 Lisensi

Dirilis di bawah [MIT License](LICENSE).
