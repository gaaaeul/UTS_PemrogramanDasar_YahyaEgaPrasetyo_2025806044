# UTS Pemrograman Dasar

## Identitas Mahasiswa
Nama : Yahya Ega Prasetyo  
NIM  : 2025806044 
Mata Kuliah : Pemrograman Dasar  
Semester : 2  
Universitas Insan Pembangunan Indonesia

---

# Deskripsi Program

## Soal 1 — Sistem Data Mahasiswa Terintegrasi (C)
Program ini dibuat menggunakan bahasa C untuk mengelola data mahasiswa menggunakan linked list dinamis.

### Fitur:
- Input data mahasiswa
- Menampilkan data mahasiswa
- Mencari data berdasarkan NIM
- Menghapus data mahasiswa
- Menghitung nilai akhir dan huruf mutu
- Menyimpan data ke file CSV

### Konsep yang Digunakan:
- Struct
- Pointer
- Dynamic Memory
- Linked List
- File Handling
### Cara Menjalankan Program : Buka terminal, masuk ke folder
### Compile Program
`bash
gcc mahasiswa.c -o mahasiswa
### Menjalankan Program
.\mahasiswa

---

## Soal 2 — Guess Battle (Python)
Program game tebak angka berbasis multi-level menggunakan Python.

### Fitur:
- Login pemain
- 3 level permainan
- Sistem skor otomatis
- Penyimpanan skor ke file JSON
- Menampilkan Top 5 Score

### Level:
- Level 1 : angka 1–10
- Level 2 : angka 1–50
- Level 3 : angka 1–100

### Library:
- random
- json
- colorama
### Cara Menjalankan Program:
### Masuk ke Folder
Bash
cd guest_battle
### Menjalankan Program
py main.py

---

## Soal 3 — Analisis Teks Otomatis (Python)
Program untuk menganalisis file teks dan menghasilkan laporan statistik otomatis.

### Fitur:
- Menghitung jumlah baris
- Menghitung jumlah kata
- Menghitung huruf vokal dan konsonan
- Menampilkan 5 kata paling sering muncul
- Membuat grafik frekuensi ASCII

### File:
- input.txt
- report.txt
### Cara Menjalankan Program:
### Masuk ke Folder
Bash
cd analyzer
### Menjalankan Program
py main.py

---

## Soal 4 — Konversi Data CSV ke JSON
Program Python untuk membaca file CSV hasil program C dan mengubahnya ke format JSON.

### Fitur:
- Membaca data mahasiswa dari CSV
- Menghitung rata-rata nilai akhir
- Mengubah data ke format JSON

### File:
- data_mahasiswa.csv
- data_mahasiswa.json
### Cara Menjalankan Program:
### Masuk ke Folder Pyhton
Bash
cd pyhton
### Menjalankan Program
py konversi.py

---
# Dokumentasi Output

## Soal 1 — Sistem Data Mahasiswa

### Menu Program
![Menu Program](docs/soal1-menu.png)

### Data Mahasiswa
![Data Mahasiswa](docs/soal1-data.png)

### File CSV
![CSV](docs/soal1-csv.png)

---

## Soal 2 — Guess Battle

### Login Pemain
![Login](docs/soal2-login.png)

### Gameplay
![Gameplay](docs/soal2-gameplay.png)

### Top Score
![Top Score](docs/soal2-topscore.png)

### File JSON
![JSON](docs/soal2-json.png)

---

## Soal 3 — Analisis Teks Otomatis

### Terminal Output
![Terminal](docs/soal3-terminal.png)

### Hasil Report
![Report](docs/soal3-report.png)

### Input Text
![Input](docs/soal3-input.png)

---

## Soal 4 — Konversi CSV ke JSON

### Proses Konversi
![Konversi](docs/soal4-konversi.png)

### Hasil JSON
![JSON](docs/soal4-json.png)

---

# Struktur Folder

```txt
UTS_PemrogramanDasar_Nama_NIM
│
├── .vscode
│   ├── settings.json
│   ├── tasks.json
│   └── launch.json
│
├── C
│   ├── mahasiswa.c
│   ├── mahasiswa.exe
│   └── data_mahasiswa.csv
│
├── Python
│   │
│   ├── guest_battle
│   │   ├── main.py
│   │   ├── game.py
│   │   ├── scoreboard.py
│   │   └── scores.json
│   │
│   ├── analyzer
│   │   ├── main.py
│   │   ├── analyzer.py
│   │   ├── input.txt
│   │   └── report.txt
│   │
│   ├── konversi.py
│   ├── data_mahasiswa.csv
│   └── data_mahasiswa.json
│
├── docs
│   ├── soal1-menu.png
│   ├── soal1-data.png
│   ├── soal1-csv.png
│   ├── soal2-login.png
│   ├── soal2-gameplay.png
│   ├── soal2-topscore.png
│   ├── soal2-json.png
│   ├── soal3-terminal.png
│   ├── soal3-report.png
│   ├── soal3-input.png
│   ├── soal4-konversi.png
│   └── soal4-json.png
│
└── README.md