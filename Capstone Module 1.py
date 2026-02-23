# ========================================
# SISTEM MANAJEMEN DATA PRODUK ONLINE SHOP
# ========================================

produk_list = [
    {"id": "PRD001", "nama": "Backpack", "harga": 450000, "stok": 10, "kategori": "Aksesoris"},
    {"id": "PRD002", "nama": "Sepatu sneakers", "harga": 750000, "stok": 20, "kategori": "Fashion"},
    {"id": "PRD003", "nama": "Hoodie", "harga": 500000, "stok": 15, "kategori": "Fashion"},
    {"id": "PRD004", "nama": "Jam tangan digital", "harga": 350000, "stok": 8, "kategori": "Aksesoris"},
    {"id": "PRD005", "nama": "Topi baseball", "harga": 150000, "stok": 5, "kategori": "Fashion"},
    {"id": "PRD006", "nama": "Kacamata", "harga": 100000, "stok": 6, "kategori": "Aksesoris"},
    {"id": "PRD007", "nama": "Syal", "harga": 90000, "stok": 5, "kategori": "Aksesoris"},
    {"id": "PRD008", "nama": "Dompet", "harga": 80000, "stok": 6 , "kategori": "Aksesoris"},
    {"id": "PRD009", "nama": "Kaos Polos", "harga": 120000, "stok": 25, "kategori": "Fashion"},
    {"id": "PRD010", "nama": "Celana Jogger", "harga": 200000, "stok": 12, "kategori": "Fashion"},
]

from tabulate import tabulate

# ==============================
# FUNGSI UNTUK MENAMPILKAN DATA
# ==============================

def tampilkan_tabel(data):
    if not data:
        print("Belum ada data.")
        return

    headers = ["ID", "Nama", "Harga", "Stok", "Kategori"]
    rows = []

    for produk in data:
        rows.append([
            produk["id"],
            produk["nama"],
            f"{produk['harga']:,.0f}",
            produk["stok"],
            produk["kategori"]
        ])

    print(tabulate(rows, headers=headers, tablefmt="grid"))


# ==============================
# CREATE
# ==============================

def tambah_produk():
    while True:
        print("\n=== MENU TAMBAH PRODUK ===")
        print("1. Tambah Produk Baru")
        print("2. Kembali ke Menu Utama")

        pilih = input("Pilih menu: ")

        if pilih == "1":

            id_produk = input("Masukkan ID produk: ")

            if cari_id(id_produk):
                print("ID sudah terdaftar.")
                continue

            nama = input("Masukkan nama produk: ")

            try:
                harga = float(input("Masukkan harga: "))
                stok = int(input("Masukkan stok: "))
            except:
                print("Harga dan stok harus berupa angka.")
                continue

            kategori = input("Masukkan kategori: ")

            print("\nData yang akan disimpan:")
            tampilkan_tabel([{
                "id": id_produk,
                "nama": nama,
                "harga": harga,
                "stok": stok,
                "kategori": kategori
            }])

            while True:
                konfirmasi = input("Simpan data? (y/n): ").lower()
                if konfirmasi == "y":
                    produk_list.append({
                        "id": id_produk,
                        "nama": nama,
                        "harga": harga,
                        "stok": stok,
                        "kategori": kategori
                    })
                    print("Produk berhasil ditambahkan.")
                    break
                elif konfirmasi == "n":
                    print("Data tidak jadi disimpan.")
                    break
                else:
                    print("Input tidak valid. Masukkan y atau n.")

        elif pilih == "2":
            break
        else:
            print("Menu tidak tersedia.")


# ==============================
# READ
# ==============================

def cari_id(id_produk):
    for produk in produk_list:
        if produk["id"] == id_produk:
            return produk
    return None


def lihat_produk():
    while True:
        print("\n=== MENU LIHAT PRODUK ===")
        print("1. Lihat Semua Produk")
        print("2. Cari Produk berdasarkan ID")
        print("3. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_tabel(produk_list)

        elif pilih == "2":
            id_produk = input("Masukkan ID: ")
            produk = cari_id(id_produk)

            if produk:
                tampilkan_tabel([produk])
            else:
                print("Produk tidak ditemukan.")

        elif pilih == "3":
            break
        else:
            print("Menu tidak tersedia.")


# ==============================
# UPDATE
# ==============================

def update_produk():
    while True:
        print("\n=== MENU UPDATE PRODUK ===")
        print("1. Update Produk")
        print("2. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            id_produk = input("Masukkan ID produk: ")
            produk = cari_id(id_produk)

            if not produk:
                print("Produk tidak ditemukan.")
                continue

            print("Data saat ini:")
            tampilkan_tabel([produk])

            while True:
                konfirmasi = input("Yakin ingin update? (y/n): ").lower()
                if konfirmasi == "y":
                    break
                elif konfirmasi == "n":
                    print("Update dibatalkan.")
                    break
                else:
                    print("Input tidak valid. Masukkan y atau n.")

            if konfirmasi != "y":
                continue

            kolom = input("Bagian yang ingin diubah (nama/harga/stok/kategori): ")

            if kolom not in produk or kolom == "id":
                print("Bagian tersebut tidak bisa diubah.")
                continue

            nilai_lama = produk[kolom]
            nilai_baru = input("Masukkan nilai baru: ")

            try:
                if kolom == "harga":
                    nilai_baru = float(nilai_baru)
                elif kolom == "stok":
                    nilai_baru = int(nilai_baru)
            except:
                print("Input tidak valid.")
                continue

            print(f"\nPerubahan yang akan dilakukan pada kolom '{kolom}':")
            print(f"  Nilai lama : {nilai_lama}")
            print(f"  Nilai baru : {nilai_baru}")

            while True:
                konfirmasi2 = input("\nApakah Data akan diUpdate? (y/n): ").lower()
                if konfirmasi2 == "y":
                    produk[kolom] = nilai_baru
                    print("Produk berhasil diperbarui.")
                    print("\nData setelah diperbarui:")
                    tampilkan_tabel([produk])
                    break
                elif konfirmasi2 == "n":
                    print("Data tidak jadi diupdate.")
                    break
                else:
                    print("Input tidak valid. Masukkan y atau n.")

        elif pilih == "2":
            break
        else:
            print("Menu tidak tersedia.")


# ==============================
# DELETE
# ==============================

def hapus_produk():
    while True:
        print("\n=== MENU HAPUS PRODUK ===")
        print("1. Hapus Produk")
        print("2. Hapus Semua Produk")
        print("3. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            id_produk = input("Masukkan ID produk: ")
            produk = cari_id(id_produk)

            if not produk:
                print("Produk tidak ditemukan.")
                continue

            print("Data yang akan dihapus:")
            tampilkan_tabel([produk])

            while True:
                konfirmasi = input("Yakin ingin hapus? (y/n): ").lower()
                if konfirmasi == "y":
                    produk_list.remove(produk)
                    print("Produk berhasil dihapus.")
                    break
                elif konfirmasi == "n":
                    print("Penghapusan dibatalkan.")
                    break
                else:
                    print("Input tidak valid. Masukkan y atau n.")

        elif pilih == "2":
            if not produk_list:
                print("Tidak ada produk untuk dihapus.")
                continue

            print("Semua produk yang akan dihapus:")
            tampilkan_tabel(produk_list)

            while True:
                konfirmasi = input("Yakin ingin hapus SEMUA produk? (y/n): ").lower()
                if konfirmasi == "y":
                    produk_list.clear()
                    print("Semua produk berhasil dihapus.")
                    break
                elif konfirmasi == "n":
                    print("Penghapusan dibatalkan.")
                    break
                else:
                    print("Input tidak valid. Masukkan y atau n.")

        elif pilih == "3":
            break
        else:
            print("Menu tidak tersedia.")

# ==============================
# LAPORAN STOK
# ==============================

def laporan_produk():
    while True:
        print("\n=== MENU LAPORAN ===")
        print("1. Lihat Laporan")
        print("2. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            if not produk_list:
                print("Belum ada data produk.")
                continue

            # Mengumpulkan semua harga dari setiap produk
            semua_harga = [produk["harga"] for produk in produk_list]

            # Menghitung statistik harga
            total_produk   = len(produk_list)
            rata_rata_harga = sum(semua_harga) / len(semua_harga)
            harga_tertinggi = max(semua_harga)
            harga_terendah  = min(semua_harga)

            # Mencari produk termahal dan termurah
            produk_termahal = max(produk_list, key=lambda produk: produk["harga"])
            produk_termurah = min(produk_list, key=lambda produk: produk["harga"])

            # Hitung jumlah produk per kategori
            kategori_data = {}
            for produk in produk_list:
                kategori = produk["kategori"]
                if kategori not in kategori_data:
                    kategori_data[kategori] = 0
                kategori_data[kategori] += 1

            # Tampilan ringkasan statistik
            baris_statistik = [
                ["Total Produk",    f"{total_produk} produk"],
                ["Rata-rata Harga", f"Rp {rata_rata_harga:,.0f}"],
                ["Harga Tertinggi", f"Rp {harga_tertinggi:,.0f}  →  {produk_termahal['nama']}"],
                ["Harga Terendah",  f"Rp {harga_terendah:,.0f}  →  {produk_termurah['nama']}"],
            ]

            print("\n========== LAPORAN PRODUK ==========")
            print(tabulate(baris_statistik, headers=["Keterangan", "Nilai"], tablefmt="grid"))

            # Tampilan ringkasan per kategori
            baris_kategori = []
            for kategori, jumlah in kategori_data.items():
                baris_kategori.append([kategori, f"{jumlah} produk"])

            print("\n--- Jumlah Produk per Kategori ---")
            print(tabulate(baris_kategori, headers=["Kategori", "Jumlah"], tablefmt="grid"))

        elif pilih == "2":
            break
        else:
            print("Menu tidak tersedia.")

# ==============================
# MENU UTAMA
# ==============================

while True:
    print("\n===== MENU UTAMA =====")
    print("1. Tambah Produk")
    print("2. Lihat Produk")
    print("3. Update Produk")
    print("4. Hapus Produk")
    print("5. Laporan Stok")
    print("6. Exit")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_produk()
    elif pilih == "2":
        lihat_produk()
    elif pilih == "3":
        update_produk()
    elif pilih == "4":
        hapus_produk()
    elif pilih == "5":        
        laporan_produk()
    elif pilih == "6":      
        print("Program selesai.")
        break
    else:
        print("Menu tidak tersedia.")