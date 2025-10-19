# 🚀 Panduan Upload ke GitHub

## 📋 Repository Information

**Nama Repository (Pilih salah satu)**:

-   `netflix-analytics-dashboard` ⭐ (Recommended)
-   `netflix-data-insights`
-   `netflix-content-analytics`

**Repository Description** (Copy paste ke GitHub):

```
🎬 Interactive dashboard analyzing 8,000+ Netflix content with beautiful visualizations and deep insights. Built with Python, Flask, Pandas & Matplotlib. Features data cleaning docs, 9+ charts, and strategic business analysis.
```

**Topics/Tags** (Tambahkan di GitHub):

```
netflix, data-analysis, data-visualization, python, flask, pandas, matplotlib, seaborn, dashboard, analytics, data-science, web-app, netflix-dataset, data-cleaning, insights
```

---

## 🔧 Setup Git & Push ke GitHub

### Step 1: Initialize Git (jika belum)

```bash
cd /c/0_main_storage/python-projects/netflix_dashboard
git init
```

### Step 2: Add All Files

```bash
git add .
```

### Step 3: Commit Pertama

```bash
git commit -m "🎉 Initial commit: Netflix Analytics Dashboard with 9+ visualizations and insights"
```

### Step 4: Buat Repository di GitHub

1. Buka https://github.com/new
2. **Repository name**: `netflix-analytics-dashboard`
3. **Description**: (copy dari atas)
4. **Visibility**: Public
5. **JANGAN** centang "Initialize with README" (karena kita sudah punya)
6. Klik **Create repository**

### Step 5: Connect ke GitHub

```bash
# Ganti 'your-username' dengan username GitHub kamu
git remote add origin https://github.com/your-username/netflix-analytics-dashboard.git

# Atau pakai SSH (jika sudah setup SSH key)
git remote add origin git@github.com:your-username/netflix-analytics-dashboard.git
```

### Step 6: Push ke GitHub

```bash
git branch -M main
git push -u origin main
```

---

## ✅ Checklist Sebelum Push

-   [x] `.gitignore` sudah dibuat ✅
-   [x] `README.md` sudah dibuat ✅
-   [x] `requirements.txt` sudah dibuat ✅
-   [x] `LICENSE` sudah dibuat ✅
-   [ ] File `netflix_titles.csv` ada di root folder
-   [ ] Visualisasi sudah di-generate (run `python app.py` sekali)
-   [ ] Tidak ada file sensitif (API keys, passwords, dll)
-   [ ] Code sudah ditest dan berjalan dengan baik

---

## 📸 Optional: Tambahkan Screenshots

Untuk membuat README lebih menarik, ambil screenshots dan simpan di folder `screenshots/`:

```bash
mkdir screenshots
```

Lalu upload screenshots:

-   `screenshots/hero-section.png`
-   `screenshots/data-cleaning.png`
-   `screenshots/visualizations.png`
-   `screenshots/insights.png`

Update path di README.md dari:

```markdown
![Dashboard Preview](static/images/screenshot-hero.png)
```

Menjadi:

```markdown
![Dashboard Preview](screenshots/hero-section.png)
```

---

## 🎨 GitHub Repository Settings

### About Section (Edit di GitHub):

-   **Website**: (Kosongkan dulu atau isi dengan deployed URL nanti)
-   **Topics**: netflix, data-analysis, python, flask, pandas, matplotlib, dashboard, analytics
-   **Description**: Copy dari atas

### Features to Enable:

-   ✅ Issues
-   ✅ Projects (optional)
-   ✅ Wiki (optional)
-   ✅ Discussions (optional untuk community)

### Branch Protection (Optional tapi recommended):

-   Protect `main` branch
-   Require pull request reviews
-   Require status checks to pass

---

## 🔄 Update Workflow (Setelah Push Pertama)

Ketika ada perubahan:

```bash
# 1. Check status
git status

# 2. Add changes
git add .

# 3. Commit dengan message yang jelas
git commit -m "✨ Add new feature: filter by year"
# atau
git commit -m "🐛 Fix navbar toggle on mobile"
# atau
git commit -m "📝 Update README with deployment instructions"

# 4. Push
git push
```

### Emoji Commit Convention:

-   🎉 `:tada:` - Initial commit
-   ✨ `:sparkles:` - New feature
-   🐛 `:bug:` - Bug fix
-   📝 `:memo:` - Documentation
-   🎨 `:art:` - UI/UX improvements
-   ♻️ `:recycle:` - Code refactoring
-   🔥 `:fire:` - Remove code/files
-   🚀 `:rocket:` - Performance improvements

---

## 🌐 Deployment (Coming Soon)

### Option 1: Render.com (Free)

1. Connect GitHub repo
2. Select "Web Service"
3. Build command: `pip install -r requirements.txt`
4. Start command: `python app.py`

### Option 2: Railway.app (Free)

1. Connect GitHub repo
2. Auto-detects Flask app
3. Deploy!

### Option 3: PythonAnywhere (Free tier available)

1. Upload code
2. Setup virtual environment
3. Configure WSGI

---

## 📞 Troubleshooting

### Push Rejected?

```bash
# Pull changes first
git pull origin main --rebase

# Then push
git push
```

### Wrong Remote URL?

```bash
# Remove old remote
git remote remove origin

# Add correct remote
git remote add origin https://github.com/correct-username/repo-name.git
```

### Large Files?

```bash
# Remove from git history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/large-file" \
  --prune-empty --tag-name-filter cat -- --all
```

---

## 🎯 Next Steps After Push

1. ⭐ Star your own repo (untuk visibility)
2. 📝 Create first issue untuk todo list
3. 🔖 Create releases/tags untuk versioning
4. 🤝 Invite collaborators (Veri Abror Hadi)
5. 📊 Enable GitHub Pages (optional - untuk static docs)
6. 🚀 Deploy to production
7. 📣 Share di social media!

---

Good luck! 🚀
