import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template
import os
from collections import Counter

# Menggunakan 'Agg' backend untuk Matplotlib (penting untuk server)
matplotlib.use('Agg')

# Inisialisasi Aplikasi Flask
app = Flask(__name__)


# --- FUNGSI-FUNGSI UNTUK MEMBUAT VISUALISASI ---

# (Fungsi-fungsi lama: generate_pie_chart, generate_histogram, dll. tetap ada di sini)
def generate_pie_chart(df):
    plt.figure(figsize=(8, 8))
    type_counts = df['type'].value_counts()
    plt.pie(type_counts, labels=type_counts.index, colors=['#e50914', "#2200ff"], textprops={'color': "w"}, autopct='%1.1f%%', startangle=90)
    plt.title('Perbandingan Jumlah Film vs Acara TV', fontsize=16)
    plt.legend()
    plt.ylabel('')
    plt.savefig('static/images/pie_chart.png', bbox_inches='tight')
    plt.close()

def generate_histogram(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['release_year'], bins=30, color='royalblue')
    plt.title('Distribusi Konten Berdasarkan Tahun Rilis', fontsize=16)
    plt.xlabel('Tahun Rilis', fontsize=12)
    plt.ylabel('Jumlah Konten', fontsize=12)
    plt.savefig('static/images/histogram.png', bbox_inches='tight')
    plt.close()

def generate_line_chart(df):
    df['year_added'] = df['date_added'].dt.year.astype(int)
    content_added_per_year = df['year_added'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    content_added_per_year.plot(kind='line', marker='o', color='forestgreen')
    plt.title('Jumlah Konten yang Ditambahkan ke Netflix per Tahun', fontsize=16)
    plt.xlabel('Tahun', fontsize=12)
    plt.ylabel('Jumlah Konten Ditambahkan', fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig('static/images/line_chart.png', bbox_inches='tight')
    plt.close()

def generate_scatter_plot(df):
    movies_df = df[df['type'] == 'Movie'].copy()
    movies_df['duration_min'] = pd.to_numeric(movies_df['duration'].str.replace(' min', ''), errors='coerce')
    movies_df.dropna(subset=['duration_min'], inplace=True)
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=movies_df, x='release_year', y='duration_min', alpha=0.6, color='darkred')
    plt.title('Hubungan Antara Tahun Rilis dan Durasi Film', fontsize=16)
    plt.xlabel('Tahun Rilis', fontsize=12)
    plt.ylabel('Durasi (menit)', fontsize=12)
    plt.savefig('static/images/scatter_plot.png', bbox_inches='tight')
    plt.close()

# --- FUNGSI-FUNGSI BARU ---

def generate_rating_distribution(df):
    """Membuat Bar Chart: Distribusi Rating Konten."""
    plt.figure(figsize=(14, 7))
    sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index, palette='plasma')
    plt.title('Distribusi Rating Konten di Netflix', fontsize=16)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Jumlah', fontsize=12)
    plt.xticks(rotation=45)
    plt.savefig('static/images/rating_distribution.png', bbox_inches='tight')
    plt.close()

def generate_top_genres(df):
    """Membuat Bar Chart: 15 Genre Paling Populer."""
    genres = df['listed_in'].str.split(', ').explode()
    top_15_genres = pd.Series(Counter(genres)).nlargest(15)
    plt.figure(figsize=(12, 8))
    sns.barplot(y=top_15_genres.index, x=top_15_genres.values, orient='h', palette='rocket')
    plt.title('15 Genre Paling Populer di Netflix', fontsize=16)
    plt.xlabel('Jumlah Judul', fontsize=12)
    plt.ylabel('Genre', fontsize=12)
    plt.savefig('static/images/top_genres.png', bbox_inches='tight')
    plt.close()

def generate_top_countries(df):
    """Membuat Bar Chart: 10 Negara Produksi Terbanyak."""
    plt.figure(figsize=(12, 8))
    top_10_countries = df['country'].value_counts().nlargest(10)
    sns.barplot(y=top_10_countries.index, x=top_10_countries.values, orient='h', palette='viridis')
    plt.title('10 Negara dengan Produksi Konten Terbanyak', fontsize=16)
    plt.xlabel('Jumlah Konten', fontsize=12)
    plt.ylabel('Negara', fontsize=12)
    plt.savefig('static/images/top_countries.png', bbox_inches='tight')
    plt.close()
    return top_10_countries # Return untuk digunakan di fungsi lain

def generate_top_actors(df):
    """Membuat Catplot: Top 3 Aktor di 10 Negara Teratas."""
    df_actor_viz = df[(df['cast'] != 'Unknown') & (df['country'] != 'Unknown')].copy()
    
    def split_and_clean(text):
        return [item.strip() for item in text.split(',')]

    df_actor_viz['country_list'] = df_actor_viz['country'].apply(split_and_clean)
    df_actor_viz['cast_list'] = df_actor_viz['cast'].apply(split_and_clean)
    
    df_exploded = df_actor_viz.explode('country_list').explode('cast_list')
    df_exploded.rename(columns={'country_list': 'country_single', 'cast_list': 'actor'}, inplace=True)
    
    actor_counts = df_exploded.groupby(['country_single', 'actor']).size().reset_index(name='count')
    
    top_countries = df_exploded['country_single'].value_counts().nlargest(10).index
    filtered_counts = actor_counts[actor_counts['country_single'].isin(top_countries)]
    
    top_actors_per_country = filtered_counts.groupby('country_single').apply(lambda x: x.nlargest(3, 'count')).reset_index(drop=True)

    g = sns.catplot(
        data=top_actors_per_country, x='count', y='actor', col='country_single',
        kind='bar', col_wrap=2, sharex=False, sharey=False, height=4, aspect=1.5, palette='viridis'
    )
    g.fig.suptitle('Top 3 Aktor di Negara Produksi Teratas', y=1.03, fontsize=16, fontweight='bold')
    g.set_titles("Negara: {col_name}", weight='bold')
    g.set_axis_labels("Jumlah Kemunculan", "Nama Aktor")
    plt.savefig('static/images/top_actors.png', bbox_inches='tight')
    plt.close()

def generate_top_directors(df, top_countries_list):
    """Membuat Subplots: Top 3 Sutradara di 3 Negara Teratas."""
    top_3_countries = top_countries_list.index[:3] # Ambil 3 negara teratas dari list
    
    fig, axes = plt.subplots(1, 3, figsize=(20, 7))
    fig.suptitle('Top 3 Sutradara Paling Produktif di Masing-Masing Negara', fontsize=18, y=1.02)

    for i, country in enumerate(top_3_countries):
        country_df = df[df['country'].str.contains(country)]
        directors = country_df['director'].str.split(', ').explode()
        directors = directors[directors != 'Unknown']
        
        if not directors.empty:
            top_3_directors = directors.value_counts().nlargest(3)
            sns.barplot(ax=axes[i], x=top_3_directors.values, y=top_3_directors.index, palette='plasma')
            axes[i].set_title(country, fontsize=14)
            axes[i].set_xlabel('Jumlah Konten')
            axes[i].set_ylabel('')
            for j, count in enumerate(top_3_directors.values):
                axes[i].text(count, j, f' {count}', va='center', fontsize=11, ha='left')
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('static/images/top_directors.png', bbox_inches='tight')
    plt.close()


# --- ROUTE UTAMA APLIKASI ---
@app.route('/')
def dashboard():
    if not os.path.exists('static/images'):
        os.makedirs('static/images')

    # 1. Muat dan proses data
    df_raw = pd.read_csv('netflix_titles.csv')
    table_head_html = df_raw.head().to_html(classes='dataframe', index=False, border=0)
    missing_before = df_raw.isnull().sum()
    missing_before_html = missing_before[missing_before > 0].to_frame(name='Jumlah Hilang').to_html(classes='dataframe', border=0)
    
    df_cleaned = df_raw.copy()
    df_cleaned['director'] = df_cleaned['director'].fillna('Unknown')
    df_cleaned['cast'] = df_cleaned['cast'].fillna('Unknown')
    country_mode = df_cleaned['country'].mode()[0]
    df_cleaned['country'] = df_cleaned['country'].fillna(country_mode)
    df_cleaned.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)
    df_cleaned['date_added'] = pd.to_datetime(df_cleaned['date_added'].str.strip(), errors='coerce')
    df_cleaned.dropna(subset=['date_added'], inplace=True)
    
    missing_after = df_cleaned.isnull().sum()
    missing_after_html = missing_after.to_frame(name='Jumlah Hilang').to_html(classes='dataframe', border=0)
    
    # 2. Buat semua grafik dari data yang sudah bersih
    generate_pie_chart(df_cleaned)
    generate_histogram(df_cleaned)
    generate_line_chart(df_cleaned)
    generate_scatter_plot(df_cleaned)
    
    # Panggil fungsi-fungsi baru
    generate_rating_distribution(df_cleaned)
    generate_top_genres(df_cleaned)
    top_10_countries_series = generate_top_countries(df_cleaned) # Simpan hasilnya
    generate_top_directors(df_cleaned, top_10_countries_series) # Kirim sebagai argumen
    generate_top_actors(df_cleaned)

    # 3. Siapkan nama file gambar untuk dikirim ke template
    image_files = {
        'pie_chart': 'images/pie_chart.png',
        'histogram': 'images/histogram.png',
        'line_chart': 'images/line_chart.png',
        'scatter_plot': 'images/scatter_plot.png',
        'rating_dist': 'images/rating_distribution.png',
        'top_genres': 'images/top_genres.png',
        'top_countries': 'images/top_countries.png',
        'top_directors': 'images/top_directors.png',
        'top_actors': 'images/top_actors.png',
    }
    
    return render_template('index.html', 
                           images=image_files,
                           table_head=table_head_html,
                           missing_before=missing_before_html,
                           missing_after=missing_after_html)

if __name__ == '__main__':
    app.run(debug=True, port=5001)