import csv
import pandas as pd
from tabulate import tabulate

user = {"admin": "123"}


def register_anggota():
    username = input("masukkan username anda : ")
    password = input("masukkan password anda : ")
    if username == "admin":
        print("username tidak dapat ditambahkan")
        return

    data_regis = []
    with open("try.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    username_already = False

    for regis in data_regis:
        if username == regis["username"]:
            print("Username sudah ada mohon ganti dengan yang lain !")
            username_already = True
            break
    if username_already == False:
        new_data = {"username": username, "password": password}
        with open("try.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=new_data.keys())
            writer.writerow(new_data)

        print("Data berhasil ditambahkan!")


def login_anggota():
    username = input("masukkan username anda : ")
    password = input("masukkan password anda : ")

    if username == "admin" and password == "123":
        print("Halo admin ! ")
        menu_fungsi_admin()

    data_regis = []
    with open("try.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    data_login = []
    for i in data_regis:
        if username == i["username"] and password == i["password"]:
            data_login.append(i)
            print("login berhasil")
            menu_fungsi_member()

        if len(data_login) == 0:
            print("akun tidak ditemukan")


def tampilkan_daftar_padi(df):
    print("Daftar Harga Padi:")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


def tambah_harga_padi(df, jenis_padi, harga_bibit):
    new_data = {"Jenis Padi": jenis_padi, "Harga Bibit": harga_bibit}
    df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
    return df


def edit_harga_padi(df, jenis_padi, harga_bibit):
    if jenis_padi in df["Jenis Padi"].values:
        df.loc[df["Jenis Padi"] == jenis_padi, "Harga Bibit"] = harga_bibit
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
    return df


def hapus_harga_padi(df, jenis_padi):
    if jenis_padi in df["Jenis Padi"].values:
        df = df[df["Jenis Padi"] != jenis_padi]
        df.reset_index(drop=True, inplace=True)
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
    return df


def main():
    nama_berkas = "list_padi.csv"

    harga_padi_df = baca_dari_csv(nama_berkas)

    while True:
        tampilkan_daftar_padi(harga_padi_df)

        print("Menu:")
        print("1. Tambah Jenis Padi dan Harga Bibit")
        print("2. Simpan Data")
        print("3. Edit Harga Padi")
        print("4. Hapus Jenis Padi")
        print("5. Kembali")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            jenis_padi = input("Masukkan jenis padi: ")
            harga_bibit = float(input("Masukkan harga bibit: "))
            harga_padi_df = tambah_harga_padi(harga_padi_df, jenis_padi, harga_bibit)
        elif pilihan == "2":
            simpan_ke_csv(harga_padi_df, nama_berkas)
            print("Data telah disimpan.")
        elif pilihan == "3":
            jenis_padi = input("Masukkan jenis padi yang ingin diedit: ")
            harga_bibit = float(input("Masukkan harga bibit baru: "))
            harga_padi_df = edit_harga_padi(harga_padi_df, jenis_padi, harga_bibit)
        elif pilihan == "4":
            jenis_padi = input("Masukkan jenis padi yang ingin dihapus: ")
            harga_padi_df = hapus_harga_padi(harga_padi_df, jenis_padi)
        elif pilihan == "5":
            menu_fungsi_admin()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def simpan_ke_csv(df, nama_berkas):
    df.to_csv(nama_berkas, index=False)


def baca_dari_csv(nama_berkas):
    try:
        df = pd.read_csv(nama_berkas)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Jenis Padi", "Harga Bibit"])
    return df


def main_tambah():
    nama_berkas = "list_padi.csv"
    harga_padi_df = baca_dari_csv(nama_berkas)
    tampilkan_daftar_padi(harga_padi_df)
    print("1. Kembali")
    memilih = input("masukkan pilihan : ")
    if memilih == 1:
        menu_fungsi_member()


def baca_dari_csv(nama_berkas):
    try:
        df = pd.read_csv(nama_berkas)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Jenis Padi", "Harga Bibit"])
    return df


def menu_login():
    print("1. registrasi")
    print("2. login")
    opsi = int(input("masukkan pilihan : "))

    if opsi == 1:
        register_anggota()
    if opsi == 2:
        login_anggota()


def menu_fungsi_admin():
    print("1.Informasi Padi")
    print("2. Kalkulasi Data")
    memilih = input("Pilih (1/2) : ")

    if memilih == "1":
        main()
        tampilkan_daftar_padi()
        tambah_harga_padi()
        edit_harga_padi()
        hapus_harga_padi()
        baca_dari_csv()
        simpan_ke_csv()
    elif memilih == "2":
        print("fitur belum tersedia.")
    else:
        print("piliha tidak ditemukan.")


def menu_fungsi_member():
    print("1. Informasi Padi")
    print("2. Hasil Kalkulasi Data")
    memilih = input("Pilih (1/2) : ")

    if memilih == "1":
        main_tambah()
    elif memilih == "2":
        print("fungsi belum tersedia")
    else:
        print("masukkan pilihan yang tersedia")


menu_login()
