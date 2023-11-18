import csv
import pandas as pd
from tabulate import tabulate
import os
import sys
from getpass import getpass


# fungsi registrasi member
def register_anggota():
    os.system("cls")
    username = input("masukkan username anda : ")
    password = getpass("masukkan password anda : ", stream=None)

    data_regis = []
    with open("data_csv/data_login.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    username_already = False

    for regis in data_regis:
        if username == regis["username"]:
            print("Username sudah ada mohon ganti dengan yang lain !")
            username_already = True
            enter = input("klik enter untuk melanjutkan...")
            print(enter, menu_login())

    if username_already == False:
        new_data = {"username": username, "password": password}
        with open("data_csv/data_login.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=new_data.keys())
            writer.writerow(new_data)

        print("Data berhasil ditambahkan!")
        enter = input("klik enter untuk melanjutkan...")
        print(enter, menu_login())


# login admin
def login_admin():
    os.system("cls")
    username = input("masukkan username anda : ")
    password = input("masukkan password anda : ")

    data_regis = []
    with open("data_csv/admin_login.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    data_login = []
    for i in data_regis:
        if username == i["username"] and password == i["password"]:
            data_login.append(i)
            print("login berhasil")
            menu_fungsi_admin()

    if len(data_login) == 0:
        print("akun tidak ditemukan")


# login member
def login_anggota():
    os.system("cls")
    username = input("masukkan username anda : ")
    password = input("masukkan password anda : ")

    data_regis = []
    with open("data_csv/data_login.csv", "r") as file:
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


# menu login
def menu_login():
    os.system("cls")
    namafile = "data_txt/login_padi.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    opsi = int(input("masukkan pilihan : "))

    if opsi == 1:
        register_anggota()
    elif opsi == 2:
        login_anggota()
    elif opsi == 3:
        login_admin()
    else:
        print("Masukkan Pilihan yang tepat")


# menu fungsi informasi untuk admin
def main():
    os.system("cls")
    nama_berkas = "data_csv/list1_padi.csv"

    data_padi_df = baca_dari_csv(nama_berkas)

    tampilkan_daftar_padi(data_padi_df)

    print("Menu:")
    print("1. Tambah Jenis Padi dan Harga Bibit")
    print("2. Edit Harga Padi")
    print("3. Hapus Jenis Padi")
    print("4. Informasi Pupuk")
    print("5. Informasi pestisida")
    print("6. Kembali")

    while True:
        pilihan = input("Pilih menu (1/2/3/4/5/6/7): ")

        if pilihan == "1":
            jenis_padi = input("Masukkan jenis padi: ")
            harga_bibit = float(input("Masukkan harga bibit: "))
            potensi_hasil = float(input("Masukkan potensi hasil: "))
            musim = input("Masukkan musim: ")
            umur = input("Masukkan umur: ")
            data_padi_df = tambah_harga_padi(
                data_padi_df, jenis_padi, harga_bibit, potensi_hasil, musim, umur
            )
            simpan_ke_csv(data_padi_df, nama_berkas)
            print("Data telah disimpan.")
            input("klik enter untuk melanjutkan...")
            main()
        elif pilihan == "2":
            jenis_padi = input("Masukkan jenis padi yang ingin diedit: ")
            harga_bibit = float(input("Masukkan harga bibit baru: "))
            potensi_hasil = float(input("Masukkan potensi hasil baru: "))
            musim = input("Masukkan musim baru: ")
            umur = input("Masukkan umur baru: ")
            data_padi_df = edit_harga_padi(
                data_padi_df, jenis_padi, harga_bibit, potensi_hasil, musim, umur
            )
            simpan_ke_csv(data_padi_df, nama_berkas)
            print("Data telah diedit")
            input("Klik enter untuk melanjutkan...")
            main()
        elif pilihan == "3":
            jenis_padi = input("Masukkan jenis padi yang ingin dihapus: ")
            data_padi_df = hapus_harga_padi(data_padi_df, jenis_padi)
            simpan_ke_csv(data_padi_df, nama_berkas)
            print("Data telah dihapus")
            input("Klik enter unutk melanjutkan...")
            main()
        elif pilihan == "4":
            main_pupuk()
            tampilkan_daftar_pupuk()
            tambah_harga_pupuk()
            edit_harga_pupuk()
            hapus_harga_pupuk()
            baca_dari_csv_pupuk()
            simpan_ke_csv_pupuk()
        elif pilihan == "5":
            main_pestisida()
            tampilkan_daftar_pestisida()
            tambah_harga_pestisida()
            edit_harga_pestisida()
            hapus_harga_pestisida()
            baca_dari_csv_pestisida()
            simpan_ke_csv_pestisida()
        elif pilihan == "6":
            menu_fungsi_admin()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# menu fungsi pada admin
def menu_fungsi_admin():
    os.system("cls")
    namafile = "data_txt/menu_admin.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    while True:
        memilih = input("Pilih (1/2/3/4) : ")

        if memilih == "1":
            main()
            tampilkan_daftar_padi()
            tambah_harga_padi()
            edit_harga_padi()
            hapus_harga_padi()
            baca_dari_csv()
            simpan_ke_csv()
        elif memilih == "2":
            tampilkan_tabel_admin("data_csv/hasil_kalkulasi.csv")
        elif memilih == "3":
            tampilkan_tabel_member()
        elif memilih == "4":
            question = input("apakah anda yakin untuk keluar aplikasi ? (y/n)")
            if question == "y":
                print("Terimakasih sudah menggunakan aplikasi kami.")
                sys.exit()
            elif question == "n":
                print("Melanjutkan aplikasi.")
            else:
                print("Masukkan pilihan yang tepat.")
        else:
            print("pilihan tidak ditemukan.")


# menu informasi untuk member
def main_tambah():
    os.system("cls")
    nama_berkas = "data_csv/list1_padi.csv"
    data_padi_df = baca_dari_csv(nama_berkas)

    tampilkan_daftar_padi(data_padi_df)
    print("1. Informasi Pupuk")
    print("2. Informasi Pestisida")
    print("3. Kembali")

    while True:
        memilih = input("masukkan pilihan : ")
        if memilih == "1":
            main_pupuk_tambah()
        elif memilih == "2":
            main_pestisida_tambah()
        if memilih == "3":
            menu_fungsi_member()
        else:
            print("Masukkan pilihan yang tepat")


# menu fungsi pada member
def menu_fungsi_member():
    os.system("cls")
    namafile = "data_txt/menu_member.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    while True:
        memilih = input("Pilih menu (1/2/3): ")

        if memilih == "1":
            main_tambah()
        elif memilih == "2":
            tampilkan_tabel("data_csv/hasil_kalkulasi.csv")
        elif memilih == "3":
            question = input("Apakah anda yakin untuk keluar aplikasi? (y/n): ")
            if question.lower() == "y":
                print("Terimakasih sudah menggunakan aplikasi kami.")
                sys.exit()
            elif question.lower() == "n":
                print("Melanjutkan aplikasi.")
            else:
                print("Masukkan pilihan yang tepat.")
        else:
            print("Masukkan pilihan yang tersedia. Mohon masukkan opsi yang tepat.")


# ========================PADI======================
# membaca data yang ada di csv
def baca_dari_csv(nama_berkas):
    os.system("cls")
    try:
        df = pd.read_csv(nama_berkas)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(
            columns=["Jenis Padi", "Harga Bibit", "Potensi Hasil", "Musim", "Umur"]
        )
    return df


# menampilkan tabel
def tampilkan_daftar_padi(df):
    os.system("cls")
    df["Potensi Hasil"] = df["Potensi Hasil"].apply(
        lambda x: f"{x} (kg)" if "kg" not in str(x) else x
    )
    print("Daftar Harga Padi:")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


# fungsi menambahkan data dari tabel
def tambah_harga_padi(df, jenis_padi, harga_bibit, potensi_hasil, musim, umur):
    os.system("cls")
    new_data = {
        "Jenis Padi": jenis_padi,
        "Harga Bibit": harga_bibit,
        "Potensi Hasil": potensi_hasil,
        "Musim": musim,
        "Umur": umur,
    }
    df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
    return df


# fungsi edit data pada tabel
def edit_harga_padi(df, jenis_padi, harga_bibit, potensi_hasil, musim, umur):
    os.system("cls")
    if jenis_padi in df["Jenis Padi"].values:
        df.loc[
            df["Jenis Padi"] == jenis_padi,
            ["Harga Bibit", "Potensi Hasil", "Musim", "Umur"],
        ] = [harga_bibit, potensi_hasil, musim, umur]
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
    return df


# fungsi hapus data pada tabel
def hapus_harga_padi(df, jenis_padi):
    os.system("cls")
    if jenis_padi in df["Jenis Padi"].values:
        df = df[df["Jenis Padi"] != jenis_padi]
        df.reset_index(drop=True, inplace=True)
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
    return df


# fungsi simpan data ke dalam csv
def simpan_ke_csv(df, nama_berkas):
    os.system("cls")
    df.to_csv(nama_berkas, index=False)


# PUPUK
########################################################################################################
def baca_dari_csv_pupuk(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Jenis Padi", "Pupuk", "Harga Pupuk"])
    return df


# menampilkan tabel
def tampilkan_daftar_pupuk(df):
    os.system("cls")
    print("Daftar Harga Pupuk:")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


# fungsi menambahkan data dari tabel
def tambah_harga_pupuk(df, padi, pupuk, harga_pupuk):
    os.system("cls")
    new_data = {
        "Jenis Padi": padi,
        "Pupuk": pupuk,
        "Harga Pupuk": harga_pupuk,
    }
    df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
    return df


# fungsi edit data pada tabel
def edit_harga_pupuk(df, padi, pupuk, harga_pupuk):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df.loc[
            df["Jenis Padi"] == padi,
            ["Pupuk", "Harga Pupuk"],
        ] = [pupuk, harga_pupuk]
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga padi.")
    return df


# fungsi hapus data pada tabel
def hapus_harga_pupuk(df, padi):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df = df[df["Jenis Padi"] != padi]
        df.reset_index(drop=True, inplace=True)
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga padi.")
    return df


# fungsi simpan data ke dalam csv
def simpan_ke_csv_pupuk(df, nama_file):
    os.system("cls")
    df.to_csv(nama_file, index=False)


# menu fungsi informasi untuk admin
def main_pupuk():
    os.system("cls")
    nama_file = "data_csv/pupuk_padi.csv"

    data_pupuk_df = baca_dari_csv_pupuk(nama_file)

    tampilkan_daftar_pupuk(data_pupuk_df)

    print("Menu:")
    print("1. Tambah Jenis Padi dan Harga Bibit")
    print("2. Edit Harga Padi")
    print("3. Hapus Jenis Padi")
    print("4. Kembali")

    while True:
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            padi = input("Masukkan jenis padi: ")
            pupuk = input("Masukkan pupuk: ")
            harga_pupuk = float(input("Masukkan harga pupuk : "))
            data_pupuk_df = tambah_harga_pupuk(data_pupuk_df, padi, pupuk, harga_pupuk)
            simpan_ke_csv_pupuk(data_pupuk_df, nama_file)
            print("Data telah disimpan.")
            input("Klik enter untuk melanjutkan")
            main_pupuk()
        elif pilihan == "2":
            padi = input("Masukkan jenis padi yang ingin diedit: ")
            pupuk = input("Masukkan pupuk baru: ")
            harga_pupuk = float(input("Masukkan harga baru: "))
            data_pupuk_df = edit_harga_pupuk(data_pupuk_df, padi, pupuk, harga_pupuk)
            simpan_ke_csv_pupuk(data_pupuk_df, nama_file)
            print("Data telah diedit")
            input("Klik enter untuk melanjutkan")
            main_pupuk()
        elif pilihan == "3":
            padi = input("Masukkan jenis padi yang ingin dihapus: ")
            data_pupuk_df = hapus_harga_pupuk(data_pupuk_df, padi)
            simpan_ke_csv_pupuk(data_pupuk_df, nama_file)
            print("Data telah terhapus")
            input("Klik enter untuk melanjutkan")
            main_pupuk()
        elif pilihan == "4":
            main()
            tampilkan_daftar_padi()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# fungsi informasi untuk member
def main_pupuk_tambah():
    os.system("cls")
    nama_file = "data_csv/pupuk_padi.csv"

    data_pupuk_df = baca_dari_csv_pupuk(nama_file)

    tampilkan_daftar_pupuk(data_pupuk_df)

    print("Menu:")
    print("1. Kembali")
    while True:
        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            main_tambah()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# PESTISIDA
##############################################################################################################
def baca_dari_csv_pestisida(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Jenis Padi", "Pestisida", "Harga Pestisida"])
    return df


# menampilkan tabel pestisida
def tampilkan_daftar_pestisida(df):
    os.system("cls")
    print("Daftar Harga Pestisida : ")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


# fungsi menambahkan data dari tabel
def tambah_harga_pestisida(df, padi, pestisida, harga_pestisida):
    os.system("cls")
    new_data = {
        "Jenis Padi": padi,
        "Pestisida": pestisida,
        "Harga Pestisida": harga_pestisida,
    }
    df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
    return df


# fungsi edit data pada tabel
def edit_harga_pestisida(df, padi, pestisida, harga_pestisida):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df.loc[
            df["Jenis Padi"] == padi,
            ["Pestisida", "Harga Pestisida"],
        ] = [pestisida, harga_pestisida]
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga padi.")
    return df


# fungsi hapus data pada tabel
def hapus_harga_pestisida(df, padi):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df = df[df["Jenis Padi"] != padi]
        df.reset_index(drop=True, inplace=True)
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga padi.")
    return df


# fungsi simpan data ke dalam csv
def simpan_ke_csv_pestisida(df, nama_file):
    os.system("cls")
    df.to_csv(nama_file, index=False)


# menu fungsi informasi untuk admin
def main_pestisida():
    os.system("cls")
    nama_file = "data_csv/pestisida_padi.csv"

    data_pestisida_df = baca_dari_csv_pestisida(nama_file)

    tampilkan_daftar_pestisida(data_pestisida_df)

    print("Menu:")
    print("1. Tambah Jenis Padi dan Harga Bibit")
    print("2. Edit Harga Padi")
    print("3. Hapus Jenis Padi")
    print("4. Kembali")
    while True:
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            padi = input("Masukkan jenis padi: ")
            pestisida = input("Masukkan pestisida : ")
            harga_pestisida = float(input("Masukkan harga pestisida : "))
            data_pestisida_df = tambah_harga_pestisida(
                data_pestisida_df, padi, pestisida, harga_pestisida
            )
            simpan_ke_csv_pestisida(data_pestisida_df, nama_file)
            print("Data telah disimpan.")
            input("klik enter untuk melanjutkan")
            main_pestisida()
        elif pilihan == "2":
            padi = input("Masukkan jenis padi yang ingin diedit : ")
            pestisida = input("Masukkan pestisida baru: ")
            harga_pestisida = float(input("Masukkan harga baru : "))
            data_pestisida_df = edit_harga_pestisida(
                data_pestisida_df, padi, pestisida, harga_pestisida
            )
            simpan_ke_csv_pestisida(data_pestisida_df, nama_file)
            print("data telah diedit")
            input("Klik enter untuk melanjutkan")
            main_pestisida()
        elif pilihan == "3":
            padi = input("Masukkan jenis padi yang ingin dihapus : ")
            data_pestisida_df = hapus_harga_pupuk(data_pestisida_df, padi)
            simpan_ke_csv_pestisida(data_pestisida_df, nama_file)
            print("data telah dihapus")
            input("Klik enter untuk melanjutkan...")
            main_pestisida()
        elif pilihan == "4":
            main()
            tampilkan_daftar_padi()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# fungsi informasi untuk member
def main_pestisida_tambah():
    os.system("cls")
    nama_file = "data_csv/pestisida_padi.csv"

    data_pestisida_df = baca_dari_csv_pestisida(nama_file)

    tampilkan_daftar_pestisida(data_pestisida_df)

    print("Menu:")
    print("1. Kembali")
    while True:
        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            main_tambah()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# ... (Kode lainnya seperti yang sudah Anda bagikan sebelumnya) ...


def simpan_hasil_kalkulasi(
    jenis_padi,
    jumlah_bibit,
    jumlah_pupuk,
    jumlah_pestisida,
    biaya_sdm,
    total_harga,
    harga_jual,
    keuntungan,
    nama_file,
):
    os.system("cls")
    header_exist = os.path.exists(nama_file)

    with open(nama_file, "a", newline="") as file:
        # Menambah header jika file masih kosong
        if not header_exist:
            file.write(
                "Jenis Padi,Jumlah Bibit,Jumlah Pupuk,Jumlah Pestisida,Biaya SDM,Total Harga,Harga Jual,Keuntungan\n"
            )

        # Menulis data ke file CSV
        file.write(
            f"{jenis_padi},{jumlah_bibit},{jumlah_pupuk},{jumlah_pestisida},{biaya_sdm},{total_harga},{harga_jual},{keuntungan}\n"
        )


def kalkulasi_total(
    data_padi_df,
    data_pupuk_df,
    data_pestisida_df,
    jenis_padi,
    jumlah_bibit,
    jumlah_pupuk,
    jumlah_pestisida,
    biaya_sdm,
    nama_file="data_csv/hasil_kalkulasi.csv",
):
    os.system("cls")
    if jenis_padi in data_padi_df["Jenis Padi"].values:
        harga_bibit = data_padi_df[data_padi_df["Jenis Padi"] == jenis_padi][
            "Harga Bibit"
        ].values[0]

        if jenis_padi in data_pupuk_df["Jenis Padi"].values:
            harga_pupuk = data_pupuk_df[data_pupuk_df["Jenis Padi"] == jenis_padi][
                "Harga Pupuk"
            ].values[0]
        else:
            harga_pupuk = 0

        if jenis_padi in data_pestisida_df["Jenis Padi"].values:
            harga_pestisida = data_pestisida_df[
                data_pestisida_df["Jenis Padi"] == jenis_padi
            ]["Harga Pestisida"].values[0]
        else:
            harga_pestisida = 0

        total_bibit = harga_bibit * jumlah_bibit
        total_pupuk = harga_pupuk * jumlah_pupuk
        total_pestisida = harga_pestisida * jumlah_pestisida
        total_biaya_sdm = biaya_sdm

        total_harga = total_bibit + total_pupuk + total_pestisida + total_biaya_sdm

        return total_harga
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
        return None


def main_kalkulasi():
    os.system("cls")
    data_padi_df = pd.read_csv("data_csv/list1_padi.csv")
    data_pupuk_df = pd.read_csv("data_csv/pupuk_padi.csv")
    data_pestisida_df = pd.read_csv("data_csv/pestisida_padi.csv")

    jenis_padi = input("Masukkan jenis padi: ")
    jumlah_bibit = int(input("Masukkan jumlah bibit: "))
    jumlah_pupuk = int(input("Masukkan jumlah pupuk: "))
    jumlah_pestisida = int(input("Masukkan jumlah pestisida: "))
    biaya_sdm = float(input("Masukkan biaya SDM: "))

    total_harga = kalkulasi_total(
        data_padi_df,
        data_pupuk_df,
        data_pestisida_df,
        jenis_padi,
        jumlah_bibit,
        jumlah_pupuk,
        jumlah_pestisida,
        biaya_sdm,
    )

    if total_harga is not None:
        print(f"Total Harga: {total_harga}")
        harga_jual = float(input("Masukkan harga jual: "))

        keuntungan = harga_jual - total_harga
        print(f"Keuntungan: {keuntungan}")

        simpan_hasil_kalkulasi(
            jenis_padi,
            jumlah_bibit,
            jumlah_pupuk,
            jumlah_pestisida,
            biaya_sdm,
            total_harga,
            harga_jual,
            keuntungan,
            "data_csv/hasil_kalkulasi.csv",
        )
    tampilkan_tabel_admin("data_csv/hasil_kalkulasi.csv")


def tampilkan_tabel(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
        if not df.empty:
            print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))
        else:
            print(f"File {nama_file} kosong.")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    print("1. Kembali")
    memilih = input("pilih opsi : ")
    if memilih == "1":
        menu_fungsi_member()
    else:
        tampilkan_tabel(nama_file)


def tampilkan_tabel_admin(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
        if not df.empty:
            print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))
        else:
            print(f"File {nama_file} kosong.")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    print("1. mulai kalkulasi ")
    print("2. Kembali")
    memilih = input("pilih opsi : ")
    if memilih == "1":
        main_kalkulasi()
    elif memilih == "2":
        menu_fungsi_admin()
    else:
        tampilkan_tabel(nama_file)


# ================fungsi hapus member===================
def tampilkan_tabel_member():
    os.system("cls")
    df = pd.read_csv("data_csv/data_login.csv")
    print("Tabel Keseluruhan:")
    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
    menu_tabel_member()


def menu_tabel_member():
    print("1. Kembali")
    memilih = input("pilih opsi : ")
    while True:
        if memilih == "1":
            menu_fungsi_admin()
        else:
            print("Opsi tidak ditemukan")
            input("Tekan Enter Untuk Mengulang...")


menu_login()
