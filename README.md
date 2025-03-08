# Bike Sharing Data Analysis

## 📌 Project Overview

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan **Bike Sharing Dataset**. Analisis ini mencakup eksplorasi dataset, analisis statistik, serta pengelompokan data untuk mendapatkan insight yang lebih mendalam.

## 📂 Dataset

Dataset yang digunakan berisi informasi harian tentang jumlah penyewaan sepeda, kondisi cuaca, musim, dan faktor lain yang memengaruhi peminjaman.

### 🔹 Fitur Dataset

- `season` : Musim (1: spring, 2: summer, 3: fall, 4: winter)
- `yr` : Tahun (0 = 2011, 1 = 2012)
- `mnth` : Bulan (1-12)
- `weekday` : Hari dalam seminggu (0-6)
- `workingday` : Hari kerja (1 = hari kerja, 0 = bukan hari kerja)
- `weathersit` : Kondisi cuaca dalam bentuk kode
- `temp` : Suhu normalisasi
- `atemp` : Suhu yang dirasakan
- `hum` : Kelembaban normalisasi
- `windspeed` : Kecepatan angin normalisasi
- `casual` : Jumlah pengguna yang tidak terdaftar
- `registered` : Jumlah pengguna yang terdaftar
- `cnt` : Total peminjaman sepeda

## 📊 Analisis yang Dilakukan

1. **Exploratory Data Analysis (EDA)**

   - Melihat distribusi data
   - Menganalisis hubungan antar variabel
   - Visualisasi tren penyewaan sepeda

2. **Manual Clustering (Tanpa Machine Learning)**

   - **Manual Grouping** berdasarkan jumlah peminjaman (`cnt`)
     - **Low Usage**: Jika `cnt` < Q1
     - **Medium Usage**: Jika Q1 ≤ `cnt` ≤ Q3
     - **High Usage**: Jika `cnt` > Q3
   - Melihat bagaimana kategori ini berhubungan dengan faktor lain (musim, hari kerja, dll.)

## 🚀 Teknologi yang Digunakan

- **Python** (pandas, numpy, matplotlib, seaborn, plotly)
- **Jupyter Notebook / Google Colab**
- **Streamlit** (untuk dashboard interaktif)

## 📌 Cara Menjalankan Proyek

1. Jalankan notebook di Jupyter/Colab atau jalankan dashboard Streamlit:
   ```bash
   ```
   ```bash
   python -m streamlit run dashboard.py
   ```

## 📈 Insight dan Kesimpulan

- Penyewaan sepeda cenderung lebih tinggi pada musim tertentu.
- Cuaca dan suhu memiliki pengaruh signifikan terhadap jumlah peminjaman.
- Pengelompokan manual membantu dalam memahami pola penyewaan dengan lebih mudah.

## 🛠 Pengembangan Lebih Lanjut

- Menambahkan model prediksi penyewaan sepeda berdasarkan faktor lingkungan.
- Mengembangkan analisis waktu yang lebih mendalam (time series analysis).
- Mengintegrasikan data geospasial untuk analisis lokasi penyewaan.

---

💡 **Author**: Dewi Yuliana

**     Email: **[dewiyulianaa938@gmail.com](mailto\:dewiyulianaa938@gmail.com)\
📌 **LinkedIn**: [Dewi Yuliana](https://www.linkedin.com/in/dewiyuliana1507)\
📅 **Project Date**: February, 2025

