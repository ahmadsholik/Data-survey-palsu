import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

# Inisialisasi Faker untuk nama Indonesia
fake = Faker('id_ID')

# Jumlah data yang ingin dibuat
n_rows = 150

# Konfigurasi opsi pilihan
kelas_options = ['X', 'XI', 'XII']
gender_options = ['Laki-laki', 'Perempuan']
jam_options = ['Kurang dari 1 jam', '1–3 jam', '3–5 jam', 'Lebih dari 5 jam']
media_options = ['Instagram', 'TikTok', 'Facebook', 'YouTube', 'Twitter', 'Snapchat']
tujuan_options = ['Hiburan', 'Komunikasi', 'Belajar', 'Berita']
pengaruh_options = ['Tidak mengganggu', 'Sedikit mengganggu', 'Sangat mengganggu']
bantu_options = ['Ya', 'Tidak']
frekuensi_options = ['Setiap hari', 'Beberapa kali seminggu', 'Jarang', 'Tidak pernah']
saran_options = [
    'Batasi waktu penggunaan',
    'Gunakan HP seperlunya',
    'Matikan notifikasi saat belajar',
    'Tidak ada',
    'Buat jadwal penggunaan'
]

# Generate data acak
data = {
    'Timestamp': [fake.date_time_between(
        start_date=datetime(2025, 1, 1), 
        end_date=datetime(2025, 12, 31)
    ).strftime('%Y-%m-%d %H:%M:%S') for _ in range(n_rows)],
    
    'Nama': [fake.name() for _ in range(n_rows)],
    'Kelas': np.random.choice(kelas_options, n_rows),
    'Jenis Kelamin': np.random.choice(gender_options, n_rows),
    'Berapa jam rata-rata Anda menggunakan media sosial setiap hari?': 
        np.random.choice(jam_options, n_rows),
    'Media sosial apa yang paling sering Anda gunakan?': 
        np.random.choice(media_options, n_rows),
    'Apa tujuan utama Anda menggunakan media sosial?': 
        np.random.choice(tujuan_options, n_rows),
    'Apakah penggunaan media sosial memengaruhi waktu belajar Anda?': 
        np.random.choice(pengaruh_options, n_rows, p=[0.3, 0.5, 0.2]),
    'Apakah Anda merasa media sosial membantu meningkatkan prestasi akademik Anda?': 
        np.random.choice(bantu_options, n_rows, p=[0.4, 0.6]),
    'Seberapa sering Anda menggunakan media sosial untuk kegiatan belajar?': 
        np.random.choice(frekuensi_options, n_rows),
    'Berapa nilai rata-rata rapor Anda semester lalu?': 
        np.round(np.clip(np.random.normal(85, 5, n_rows), 70, 100), 1),  # Perbaikan di sini
    'Apakah Anda memiliki saran untuk meminimalkan dampak negatif media sosial terhadap prestasi belajar?': 
        np.random.choice(saran_options, n_rows)
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Membatasi nilai rapor antara 70-100
df['Berapa nilai rata-rata rapor Anda semester lalu?'] = df['Berapa nilai rata-rata rapor Anda semester lalu?'].clip(70, 100)

# Menyimpan ke file Excel
df.to_excel('Survei_Pengaruh_Media_Sosial_Generated.xlsx', index=False, engine='openpyxl')

print("File Excel berhasil dibuat dengan 150 data!")
