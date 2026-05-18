# ML-fraud_detection
# Smart Bank Fraud Detection System

Proyek ini adalah aplikasi *dashboard* interaktif berbasis *Machine Learning* yang dirancang untuk mendeteksi potensi transaksi penipuan (*fraud*) di sektor perbankan secara *real-time*. Aplikasi ini menggunakan **Streamlit** dan algoritma **Random Forest Classifier**.

app : [AI Fraud Detection App](https://ml-frauddetectionv10-e3fqsqdetueptfhfnjwef2.streamlit.app/)

---

## 🚀 Fitur Utama
- **Prediksi Real-Time:** Pengguna dapat memasukkan parameter jejak digital transaksi melalui *sidebar* interaktif untuk mendapatkan hasil deteksi instan.
- **Tingkat Keyakinan model (Confidence Level):** Menggunakan fungsi probabilitas untuk menampilkan persentase tingkat keyakinan model terhadap indikasi penipuan dilengkapi dengan visualisasi *progress bar* .
- **Arsitektur End-to-End:** Alur kerja proyek mencakup analisis data eksploratif (EDA), pelatihan model (*training*), evaluasi metrik, hingga tahap deployment.

---

## 🛠️ Arsitektur Teknologi (Tech Stack)
- **Bahasa Pemrograman:** Python
- **Framework Dashboard:** Streamlit
- **Manipulasi Data:** Pandas & NumPy
- **Machine Learning Library:** Scikit-Learn (Sklearn)
- **Visualisasi Data:** Seaborn & Matplotlib
- **Model Serialization:** Joblib

---

## Evaluasi Performa Model (Versi 1.0)
Berdasarkan hasil pengujian pada 2.000 data uji (*test set*), model Random Forest pertama memberikan performa terbaik dengan hasil *Confusion Matrix* sebagai berikut:
- **True Negative (1710):** Nasabah normal yang berhasil dideteksi dengan benar sebagai Aman.
- **True Positive (196):** Penipu yang berhasil dideteksi dan diblokir dengan tepat oleh sistem.
- **False Positive (40):** Nasabah normal yang salah dituduh sebagai Penipu (Alarm Palsu).
- **False Negative (54):** Penipu yang gagal dideteksi oleh sistem dan berhasil lolos (Kebobolan).

---

## Kekurangan & Batasan Project ini

Meskipun model memiliki akurasi keseluruhan yang tinggi, evaluasi mendalam, saya menemukan beberapa celah yang perlu diperbaiki pada perkembangan project ini selanjutnya:

### 1. Dominasi Mutlak *Anomaly Score* (*Lazy Learning*)
Berdasarkan analisis *Feature Importance*, fitur `anomaly_score` memiliki bobot kepentingan lebih dari **60-70%** di dalam model. Hal ini memicu fenomena *Lazy Learning*, di mana model terlalu bergantung pada satu indikator utama. 
- **Dampaknya:** Jika seorang penipu yang cerdas berhasil memanipulasi transaksi sehingga mendapatkan `anomaly_score` yang rendah (misal: 0.20), model akan langsung menganggap transaksi tersebut aman, meskipun indikator lain sangat mencurigakan (seperti jarak lokasi yang sangat jauh atau nominal transfer yang ekstrem).

### 2. Ketiadaan Logika Keuangan Dasar (*Lack of Financial Logic*)
Algoritma *Random Forest* bekerja dengan mencari pola statistik angka secara mandiri, bukan menggunakan logika matematika keuangan terstruktur.
- **Dampaknya:** Model tidak memahami korelasi bawaan bahwa sebuah akun dengan rata-rata saldo bulanan (`avg_monthly_balance`) sebesar **$1,000** secara logis tidak mungkin melakukan transfer nominal (`transaction_amount`) sebesar **$90,000** tanpa memicu kecurigaan. Tanpa adanya rekayasa fitur khusus, model menganggap kedua angka tersebut sebagai variabel independen yang terpisah.

---

## Rencana Pengembangan Selanjutnya (Model Versi 2.0)
Untuk mengatasi kelemahan di atas dan menekan angka kebobolan (*False Negative*) dari 54 kasus menjadi sekecil mungkin, langkah-langkah berikut akan diterapkan pada model berikutnya:
1. **Rekayasa Fitur (Feature Engineering):** Membuat kolom metrik baru hasil kalkulasi rasio logika keuangan, seperti `spending_to_balance_ratio` (Nominal Transaksi dibagi Rata-rata Saldo). Fitur ini akan memaksa AI melihat kejanggalan daya beli nasabah.
2. **Penyaringan Fitur Dominan (Feature Dropping):** Mencoba melatih model baru tanpa memasukkan kolom `anomaly_score`. Tujuannya adalah memaksa pasukan pohon keputusan (*Decision Trees*) untuk menggali pola tersembunyi yang lebih kompleks dari kombinasi fitur sekunder seperti koordinat geografis, waktu transaksi, dan saldo bulanan.
3. **Penerapan Algoritma Tingkat Lanjut:** Menguji algoritma berbasis *Boosting* seperti XGBoost atau LightGBM untuk membandingkan performa penanganan data yang tidak seimbang (*imbalanced data*).

---

## Thanks
