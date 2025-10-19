# 🎬 Netflix Analytics Dashboard

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0.0-green.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Pandas-2.1.4-orange.svg" alt="Pandas">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</div>

<p align="center">
  <strong>Dashboard analisis komprehensif untuk mengeksplorasi data konten Netflix</strong>
</p>

<p align="center">
  Dashboard interaktif yang menganalisis 8,000+ konten Netflix dengan visualisasi data yang menarik dan insights mendalam tentang strategi konten platform streaming terbesar di dunia.
</p>

---

## 📊 Demo

> **Live Demo**: [Lihat Dashboard](https://akhmadnabilg.pythonanywhere.com/)

### Screenshots

**Dashboard Overview**
<img width="1916" height="685" alt="image" src="https://github.com/user-attachments/assets/f0ced8a8-b3e6-4788-901c-0411d1592e0a" />


**Data Cleaning Process**
<img width="1909" height="927" alt="image" src="https://github.com/user-attachments/assets/e8914893-718a-4822-8fc0-148f74089f9e" />


**Interactive Visualizations**
<img width="1916" height="941" alt="image" src="https://github.com/user-attachments/assets/e7085b63-97b8-470d-9153-d977a5717133" />


**Insights & Analytics**
<img width="1917" height="958" alt="image" src="https://github.com/user-attachments/assets/7da22730-89e0-4549-b94e-7f3a4ce2e598" />


---

## ✨ Fitur Utama

### 📈 **9+ Visualisasi Interaktif**

-   **Pie Chart**: Perbandingan Movies vs TV Shows
-   **Histogram**: Distribusi tahun rilis konten
-   **Line Chart**: Pertumbuhan konten tahunan (2008-2021)
-   **Scatter Plot**: Korelasi tahun rilis dan durasi
-   **Bar Charts**: Rating distribution, top genres, top countries
-   **Multi-Country Analysis**: Top directors & actors per negara

### 🧹 **Data Cleaning Documentation**

-   Penjelasan step-by-step proses pembersihan data
-   Interactive accordion untuk setiap langkah
-   Visualisasi before/after cleaning
-   Missing values handling strategy

### 💡 **10 Key Insights**

-   Content strategy analysis (Movies vs TV Shows)
-   Growth patterns (2015-2020 expansion)
-   Target audience demographics (TV-MA & TV-14 dominance)
-   Global expansion strategy (USA, India, UK)
-   Genre diversity & international content
-   Talent distribution across regions
-   Original content competitive advantage
-   Future strategy predictions

### 🎨 **Modern UI/UX**

-   Netflix-inspired design dengan tema merah & hitam
-   Fully responsive untuk mobile, tablet, dan desktop
-   Smooth scrolling & animations
-   Dark theme yang nyaman di mata
-   Independent table scrolling dengan indicators

---

## 🚀 Instalasi & Setup

### Prerequisites

-   Python 3.8 atau lebih tinggi
-   pip (Python package manager)

### Langkah Instalasi

1. **Clone Repository**

```bash
git clone https://github.com/your-username/netflix-analytics-dashboard.git
cd netflix-analytics-dashboard
```

2. **Buat Virtual Environment** (Opsional tapi direkomendasikan)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Download Dataset**

-   Download dataset dari [Kaggle - Netflix Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
-   Letakkan file `netflix_titles.csv` di root directory project

5. **Jalankan Aplikasi**

```bash
python app.py
```

6. **Buka Browser**

```
http://localhost:5000
```

---

## 📁 Struktur Project

```
netflix_dashboard/
│
├── app.py                      # Flask application & data processing
├── netflix_titles.csv          # Dataset Netflix (download from Kaggle)
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── .gitignore                  # Git ignore rules
│
├── templates/
│   └── index.html              # Main dashboard template
│
├── static/
│   ├── style.css               # Custom styling (1600+ lines)
│   └── images/                 # Generated visualizations
│       ├── pie_chart.png
│       ├── histogram.png
│       ├── line_chart.png
│       ├── scatter_plot.png
│       ├── rating_dist.png
│       ├── top_genres.png
│       ├── top_countries.png
│       ├── top_directors.png
│       └── top_actors.png
│
└── venv/                       # Virtual environment (not in git)
```

---

## 🛠️ Tech Stack

### Backend

-   **Python 3.8+**: Core programming language
-   **Flask 3.0.0**: Web framework untuk routing & templating
-   **Pandas 2.1.4**: Data manipulation & analysis
-   **NumPy 1.26.2**: Numerical computations

### Data Visualization

-   **Matplotlib 3.8.2**: Chart generation
-   **Seaborn 0.13.0**: Statistical data visualization

### Frontend

-   **HTML5**: Semantic markup
-   **CSS3**: Modern styling dengan custom properties
-   **JavaScript (Vanilla)**: Interactivity & animations
-   **Google Fonts (Poppins)**: Typography

---

## 📊 Dataset

**Source**: [Netflix Shows Dataset by Shivam Bansal](https://www.kaggle.com/datasets/shivamb/netflix-shows)

**Dataset Details**:

-   **8,807 rows** (setelah cleaning: ~8,790 rows)
-   **12 columns**: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description
-   **Timeframe**: Konten ditambahkan hingga 2021
-   **Coverage**: 190+ negara

**Data Cleaning Steps**:

1. ✅ Missing values identification
2. ✅ Categorical imputation (director, cast, country)
3. ✅ Row deletion untuk kolom kritis (date_added, rating, duration)
4. ✅ Data type conversion (datetime parsing)
5. ✅ Data validation & quality checks

---

## 🎯 Key Insights dari Analisis

### 📌 Content Strategy

-   **70% Movies** vs **30% TV Shows** - fokus pada konten sinematik
-   **Massive growth 2015-2020** - peak di 2019-2020
-   **Modern content** - mayoritas dirilis dalam 10-15 tahun terakhir

### 📌 Target Audience

-   **TV-MA & TV-14** dominan - target dewasa & remaja mature
-   Durasi film optimal: **90-120 menit**
-   Bukan family-friendly platform seperti Disney+

### 📌 Global Expansion

-   **USA #1** producer (dominan)
-   **India #2** - rising market
-   **UK #3** - stable contributor
-   190+ negara dengan konten lokal

### 📌 Content Diversity

-   **International Movies** - genre #1
-   **Drama & Comedy** - genre universal
-   Talent lokal untuk setiap regional market

---

## 🤝 Contributing

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📝 To-Do / Future Improvements

-   [ ] Deploy ke Heroku/Vercel/Railway
-   [ ] Tambahkan filter interaktif (tahun, negara, genre)
-   [ ] Export data ke CSV/Excel
-   [ ] Dark/Light theme toggle
-   [ ] Real-time data update dari API
-   [ ] User authentication untuk saved preferences
-   [ ] Comparison dengan platform lain (Disney+, Prime Video)
-   [ ] Machine Learning predictions (content recommendation)

---

## 👥 Authors

**Akhmad Nabil Gibran**

-   GitHub: [@akhmadgibran](https://github.com/akhmadgibran)
-   Twitter: [@nabilplayground](https://twitter.com/nabilplayground)

**Veri Abror Hadi**

-   Instagram: [@veri_abr](https://instagram.com/veri_abr)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

-   **Dataset**: [Shivam Bansal](https://www.kaggle.com/shivamb) via Kaggle
-   **Netflix**: Inspiration untuk design & color scheme
-   **Flask Community**: Documentation & tutorials
-   **Python Data Science Community**: Pandas, Matplotlib, Seaborn

---

## 📧 Contact

Punya pertanyaan atau saran? Jangan ragu untuk:

-   Open an [issue](https://github.com/your-username/netflix-analytics-dashboard/issues)
-   Hubungi kami di social media

---

<div align="center">
  <p>Made with ❤️ and ☕ by Akhmad Nabil Gibran & Veri Abror Hadi</p>
  <p>⭐ Star repo ini jika bermanfaat!</p>
</div>
