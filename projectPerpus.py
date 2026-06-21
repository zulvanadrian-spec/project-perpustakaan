import csv

FILE = "buku.csv"


def baca_data():
    data = []

    try:  # ---> untuk mengecek file 'buku.csv', jika ada lanjut baca data
        with open(FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

    except FileNotFoundError:
        print("\nFile Buku Belum ter isi") # ---> jika file  'buku.csv' tidak ada data maka munculkan 'File Belum ter isi'
        print("Silahkan Isi Buku terlebih dahulu") 
        pass

    return data


def simpan_data(data):
    with open(FILE, "w", newline="") as file: # ---> 'open()'= membuka file, "w"= tulis ulang data, 'newline'= mengisi baris kosong
        fieldnames = ["id", "judul", "penulis", "kategori", "stok"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader() # ---> untuk menulis header : id,judul,penulis,kategori,stok
        writer.writerows(data) # ---> untuk menulis semua data


def tampilkan_data(data):
    print("\n===== DATA BUKU =====")
    print()
    print(f"{'ID':<10} {'Judul':<35} {'Penulis':<20} {'Kategori':<12} {'Stok'}") # --> {'..':<10} = untuk menatur posisi rata kiri jarak 10 huruf
    print("-" * 85)

    for buku in data:
        print(
            f"{buku['id']:<10} {buku['judul']:<35} {buku['penulis']:<20} {buku['kategori']:<12} {buku['stok']}"
        )


def tambah_buku(data):
    buku = {
        "id": input("ID Buku   : "),
        "judul": input("Judul     : "),
        "penulis": input("Penulis   : "), 
        "kategori": input("Kategori  : "),
        "stok": input("Stok      : ")
    }

    data.append(buku)
    simpan_data(data)
    print("Data berhasil ditambahkan")


def update_buku(data):
    id_buku = input("Masukkan ID Buku : ")

    for buku in data:
        if buku["id"] == id_buku:
            buku["judul"] = input("Judul Baru    : ")
            buku["penulis"] = input("Penulis Baru  : ")  
            buku["kategori"] = input("Kategori Baru : ")
            buku["stok"] = input("Stok Baru     : ")

            simpan_data(data)
            print("Data berhasil diupdate")
            return

    print("ID tidak ditemukan")


#======= Menghapus Buku dari Koleksi =======

def hapus_buku(data):
    id_buku = input("Masukkan ID Buku : ")

    for buku in data:
        if buku["id"] == id_buku:
            data.remove(buku)
            simpan_data(data)
            print("Data berhasil dihapus")
            return

    print("ID tidak ditemukan")


#====== Mencari Buku =======

def cari_buku(data):
    keyword = input("Masukkan Judul : ").lower()
    ditemukan = False

    for buku in data:
        if keyword in buku["judul"].lower():
            print(f"  {buku['id']} | {buku['judul']} | {buku['penulis']} | {buku['kategori']} | Stok: {buku['stok']}")
            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan")


# ========= Mengurutkan data judul dari a-z =========

def sort_judul(data):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            if data[j]["judul"] > data[j + 1]["judul"]:
                data[j], data[j + 1] = data[j + 1], data[j]

    tampilkan_data(data)


# ========= Mengurutkan data stok mulai dri yg terkecil ===========

def sort_stok(data):
    for i in range(len(data)):
        max_idx = i
        for j in range(i + 1, len(data)):
            if int(data[j]["stok"]) > int(data[max_idx]["stok"]):
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]

    tampilkan_data(data)


while True:
    data = baca_data()

    print("""
===== PERPUSTAKAAN =====

1. Tambah Buku
2. Lihat Buku
3. Update Buku
4. Hapus Buku
5. Cari Buku
6. Sort Judul
7. Sort Stok
0. Keluar
""")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        tambah_buku(data)
    elif pilihan == "2":
        tampilkan_data(data)
    elif pilihan == "3":
        update_buku(data)
    elif pilihan == "4":
        hapus_buku(data)
    elif pilihan == "5":
        cari_buku(data)
    elif pilihan == "6":
        sort_judul(data)
    elif pilihan == "7":
        sort_stok(data)
    elif pilihan == "0":
        print("Program selesai")
        break
    else:
        print("Menu tidak tersedia")