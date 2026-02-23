# Sistem Manajemen Data Produk Online Shop

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Library](https://img.shields.io/badge/Library-Tabulate-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

**Capstone Project - Module 1**
**Program:** Data Science & Machine Learning
**Millitia Christy Eirene Roselie**

---

## Project Overview

Sistem Manajemen Data Produk Online Shop adalah aplikasi berbasis terminal yang dirancang untuk membantu pengelolaan data produk secara efisien. Aplikasi ini mengimplementasikan operasi **CRUD** _(Create, Read, Update, Delete)_ lengkap dengan fitur laporan statistik produk, sehingga memudahkan pengelola toko dalam memantau dan mengelola inventaris produk.

---

## Fitur Utama

### 1. Tambah Produk _(Create)_
- Menambahkan produk baru dengan data lengkap: ID, Nama, Harga, Stok, dan Kategori
- Validasi ID produk agar tidak terjadi duplikasi
- Konfirmasi sebelum data disimpan

### 2. Lihat Produk _(Read)_
- Menampilkan seluruh daftar produk dalam format tabel yang rapi
- Pencarian produk berdasarkan ID produk

### 3. Update Produk _(Update)_
- Memperbarui data produk yang sudah ada berdasarkan ID
- Mendukung perubahan pada kolom: `nama`, `harga`, `stok`, dan `kategori`
- Menampilkan preview perubahan nilai lama dan nilai baru sebelum dikonfirmasi, serta menampilkan data setelah update berhasil

### 4. Hapus Produk _(Delete)_
- Menghapus produk tertentu berdasarkan ID
- Menghapus seluruh produk sekaligus
- Konfirmasi sebelum penghapusan dilakukan

### 5. Laporan Stok
- Menampilkan ringkasan statistik harga produk:
    - Total jumlah produk
    - Rata-rata harga
    - Harga tertinggi & terendah beserta nama produknya
- Menampilkan jumlah produk per kategori

---

## Data Produk Awal

Sistem dilengkapi dengan **10 produk awal** dari dua kategori utama:

| ID      | Nama Produk        | Harga (Rp) | Stok | Kategori   |
| ------- |:------------------:|:----------:|:----:|:----------:|
| PRD001  | Backpack           | 450,000    | 10   | Aksesoris  |
| PRD002  | Sepatu Sneakers    | 750,000    | 20   | Fashion    |
| PRD003  | Hoodie             | 500,000    | 15   | Fashion    |
| PRD004  | Jam Tangan Digital | 350,000    | 8    | Aksesoris  |
| PRD005  | Topi Baseball      | 150,000    | 5    | Fashion    |
| PRD006  | Kacamata           | 100,000    | 6    | Aksesoris  |
| PRD007  | Syal               | 90,000     | 5    | Aksesoris  |
| PRD008  | Dompet             | 80,000     | 6    | Aksesoris  |
| PRD009  | Kaos Polos         | 120,000    | 25   | Fashion    |
| PRD010  | Celana Jogger      | 200,000    | 12   | Fashion    |

---

## Struktur Program

```
Capstone_Module_1.py
│
├── produk_list              # Data produk (list of dict)
│
├── tampilkan_tabel()        # Fungsi untuk menampilkan data dalam format tabel
│
├── tambah_produk()          # CREATE  - Tambah produk baru
├── cari_id()                # READ    - Helper fungsi pencarian berdasarkan ID
├── lihat_produk()           # READ    - Lihat semua / cari produk
├── update_produk()          # UPDATE  - Perbarui data produk
├── hapus_produk()           # DELETE  - Hapus satu atau semua produk
├── laporan_produk()         # REPORT  - Statistik dan laporan stok
│
└── Main Loop                # Menu utama program
```

---

## Cara Menjalankan Program

1. **Pastikan Python sudah terinstall** di komputer Anda (Python 3.x)

2. **Install library yang dibutuhkan:**
    ```bash
    pip install tabulate
    ```

3. **Jalankan program:**
    ```bash
    python Capstone_Module_1.py
    ```

4. **Navigasi Menu Utama:**
    ```
    ===== MENU UTAMA =====
    1. Tambah Produk
    2. Lihat Produk
    3. Update Produk
    4. Hapus Produk
    5. Laporan Stok
    6. Exit
    ```

---

## Tools dan Teknologi

- **Bahasa Pemrograman:** Python 3.x
- **Library:** `tabulate` — untuk menampilkan data dalam format tabel yang rapi
- **Tipe Penyimpanan:** In-memory (List of Dictionaries)
- **Editor:** Visual Studio Code / IDE apapun

---

## Catatan Penting

> Data produk bersifat sementara dan **tidak tersimpan secara permanen**. Setiap kali program ditutup dan dibuka kembali, data akan kembali ke kondisi awal.

> Untuk pengembangan lebih lanjut, disarankan mengintegrasikan program ini dengan **database** seperti SQLite atau CSV sebagai media penyimpanan permanen.

