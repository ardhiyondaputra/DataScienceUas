# 📘 Judul Proyek
Klasifikasi Gender Berdasarkan Nama Menggunakan TF-IDF dan Perbandingan Model Machine Learning serta Deep Learning

## 👤 Informasi
- **Nama:** Ardhiyonda Wahyu Putra Viardhana  
- **Repo:**   
- **Video:** 

---

# 1. 🎯 Ringkasan Proyek
Proyek ini bertujuan untuk melakukan klasifikasi gender (Male/Female) berdasarkan nama seseorang menggunakan pendekatan Data Science dan Machine Learning. Dataset berupa teks nama diolah menggunakan teknik TF-IDF untuk ekstraksi fitur, kemudian dibandingkan performanya menggunakan tiga model utama:

- Baseline Model: Logistic Regression

- Advanced Model: Random Forest Classifier

- Deep Learning Model: Multilayer Perceptron (MLP)

Evaluasi dilakukan menggunakan metrik klasifikasi seperti accuracy, precision, recall, dan F1-score untuk memastikan performa model yang seimbang pada kedua kelas.
---

# 2. 📄 Problem & Goals
**Problem Statements:** 
- Data gender sering kali tidak tersedia secara eksplisit dalam sistem informasi.

- Nama sebagai data teks memiliki struktur sederhana namun tetap mengandung pola linguistik.

- Diperlukan pendekatan yang tepat untuk merepresentasikan teks nama agar dapat diproses oleh model Machine Learning.

- Perlu dibandingkan efektivitas model klasik dan deep learning pada data teks sederhana.

**Goals:** 
- Membangun sistem klasifikasi gender berbasis nama dengan performa yang dapat dipertanggungjawabkan.

- Membandingkan performa model baseline, machine learning, dan deep learning.

- Menentukan model terbaik berdasarkan hasil evaluasi empiris.

- Menyediakan pipeline yang reproducible dan terdokumentasi dengan baik.

---
## 📁 Struktur Folder
```
project/
│
├── data/
│   └── name_gender_dataset.csv
│
├── notebooks/
│   └── 234311032_Ardhiyonda.ipynb
│
├── src/
│   └── Data Import & MakeDir.py
│   └── Data Loading & Cleaning.py
│   └── Data Splitting.py
│   └── Data Transformation.py
│   └── EDA Visualization.py
│   └── Evaluation & Comparison
│   └── Feature Engineering.py
│   └── Model Training.py
│   
├── models/
│   ├── baseline_logistic_regression.pkl
│   ├── label_encoder.pkl
│   ├── deep_learning_model.keras
│   ├── random_forest_model.keras
│   └── tfidf_vectorizer.pkl
│
├── images/
│   └── Accuracy per Epoch.png
│   └── Confusion Matrix - Deep Learning (MLP).png
│   └── Loss per Epoch.png
│   
├── Laporan Proyek Machine Learning.md
├── Checklist Submit.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── README.md
```
---

# 3. 📊 Dataset
- **Sumber:** UCI Machine Learning Repository
- **Jumlah Data:** 147.241 baris 
- **Tipe:** Text (Nama) dan Label Kategorikal (Gender)

### Fitur Utama
| Fitur | Deskripsi |
|------|-----------|
| Name | Nama individu (teks) |
| Gender | Label target (0 = Male, 1 = Female) |

---

# 4. 🔧 Data Preparation
- **Cleaning:** Pengecekan dan penghapusan data duplikat serta memastikan tidak ada missing value pada kolom nama dan gender.
- **Label Handling:** Label gender tetap dalam bentuk kategorikal ("M" dan "F") tanpa encoding eksplisit, karena model scikit-learn mampu menangani label kategorikal secara langsung.
- **Transformasi Teks:** Data nama diproses menggunakan TF-IDF Vectorizer untuk mengubah teks menjadi representasi numerik.
- **Splitting Data:**  
  Dataset dibagi menggunakan stratified train-test split untuk menjaga proporsi kelas:
  - Train: 80%
  - Test: 20%
  - random_state = 42
- **Handling Imbalance:** Distribusi kelas gender tidak seimbang, sehingga digunakan `class_weight='balanced'` pada Random Forest untuk mengurangi bias terhadap kelas mayoritas.

---

# 5. 🤖 Modeling
- **Model 1 – Baseline:** Logistic Regression (`max_iter=1000`)
- **Model 2 – Advanced ML:** Random Forest Classifier dengan optimasi hyperparameter dan class weighting.
- **Model 3 – Deep Learning:** Multilayer Perceptron (MLP) dengan arsitektur:
  - Dense(128, ReLU)
  - Dropout(0.3)
  - Dense(64, ReLU)
  - Dropout(0.3)
  - Dense(1, Sigmoid)

---

# 6. 🧪 Evaluation
**Metrik:** 
- Accuracy
- Precision
- Recall
- F1-Score

### Hasil Singkat
| Model | Score | Catatan |
|-------|--------|---------|
| Baseline (LogReg) | Accuracy: 0.78 F1-score: 0.78 | Model paling stabil dan konsisten. Performa seimbang pada kedua kelas meskipun sederhana. |
| Advanced (Random Forest) | Accuracy: 0.68 F1-score: 0.68 | Cenderung bias ke salah satu kelas meskipun sudah menggunakan class_weight='balanced'. Tidak optimal untuk data teks TF-IDF berdimensi tinggi. |
| Deep Learning (MLP) | Accuracy: 0.77 F1-score: 0.77 | Mampu mendekati performa baseline, namun membutuhkan tuning dan resource lebih besar. |

---

# 7. 🏁 Kesimpulan
- **Model terbaik:** Logistic Regression
- **Alasan:** Memberikan akurasi dan F1-score tertinggi dengan kompleksitas rendah.
- **Insight:** TF-IDF sangat efektif untuk data teks sederhana seperti nama. Model kompleks tidak selalu memberikan hasil lebih baik.

---

# 8. 🔮 Future Work
- [ ] Eksplorasi n-gram pada TF-IDF
- [ ] Feature engineering lebih lanjut (Domain knowledge kimia)
- [ ] Tuning model (GridSearch/Bayesian Optimization)
- [ ] Coba arsitektur DL lain (Graph Neural Networks)
- [ ] Deployment (API/Web App)

---

# 9. 🔁 Reproducibility
Gunakan environment:
**Python 3.10+**

**Main Libraries:**
- pandas
- numpy
- scikit-learn
- tensorflow
- matplotlib
- seaborn

Instalasi:
```bash
pip install -r requirements.txt
