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
        main()
        tampilkan_daftar_padi()
        tambah_harga_padi()
        edit_harga_padi()
        hapus_harga_padi()
        baca_dari_csv()
        simpan_ke_csv()

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
            main_tambah()

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

        print("\nMenu:")
        print("1. Tambah Jenis Padi dan Harga Bibit")
        print("2. Simpan Data")
        print("3. Edit Harga Padi")
        print("4. Hapus Jenis Padi")
        print("5. Keluar")
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
            menu_login()
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
    while True:
        tampilkan_daftar_padi(harga_padi_df)

        print("1. Keluar")
        ayam = input("pilih 1 untuk keluar : ")

        if ayam == "1":
            menu_login()


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


print(menu_login())
