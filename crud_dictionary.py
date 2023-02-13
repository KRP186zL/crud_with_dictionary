import os
import datetime
import random
import string
import time

template_mahasiswa = {
    "nama":"",
    "nim":"",
    "kelas":"",
    "prodi":"",
    "lahir":datetime.datetime(1111,1,1)
}
data_mahasiswa = {}
while True:
    os.system("clear")
    print(f"{'SELAMAT DATANG':^30}")
    print("""MENU
1. Tambah Mahasiswa
2. Lihat Mahasiswa
3. Update Mahasiswa
4. Delete Mahasiswa
5. Exit Program""")

    menu = int(input("Masukkan Pilihan Anda [1/2/3/4/5]: "))
    if menu == 1:
        while True:
            os.system("clear")
            print("TAMBAHKAN MAHASISWA\n")
            mahasiswa = dict.fromkeys(template_mahasiswa.keys())
            mahasiswa["nama"] = input("Masukkan Nama\t\t: ").title()
            mahasiswa["nim"] = input("Masukkan Nim\t\t: ")
            mahasiswa["kelas"] = input("Masukkan Kelas\t\t: ").title()
            mahasiswa["prodi"] = input("Masukkan Prodi\t\t: ").title()
            print("\nTanggal Lahir")
            tahun = int(input("Masukkan Tahun(yyyy)\t: "))
            bulan = int(input("Masukkan Bulan(1-12)\t: "))
            tanggal = int(input("Masukkan Tanggal(1-31)\t: "))
            mahasiswa["lahir"] = datetime.datetime(tahun,bulan,tanggal)

            KEY = "".join((random.choice(string.ascii_uppercase) for i in range (5)))
            data_mahasiswa.update({KEY:mahasiswa})
            
            print("\n\nData Berhasil di tambahkan !\n")
            time.sleep(1.5)
            inputan = input("Tambah Lagi? [y/n]: ")
            if inputan == "y".lower():
                os.system("clear")
                continue
            elif inputan =="n".lower():
                os.system("clear")
                break
            else : 
                print("\n\npunya otak ga sih lo goblok ? \ndikasih pilihan menu yang ada malah pilih yang ga ada".upper())
                time.sleep(2)
                print("\n\nprogram dihentikan secara paksa karena anda tolol !".upper())
                exit()
            

    elif menu == 2 : 
        os.system("clear")
        while True:
            print("LIHAT MAHASISWA\n")
            print(f"{'KEY':^6} {'NAMA':^21} {'NIM':^18} {'KELAS':<6} {'PRODI':^16} {'Tanggal Lahir':^15}")
            print(f"{'-'*86}")
            
            for mahasiswa in data_mahasiswa:
                key = mahasiswa
                
                nama = data_mahasiswa[key]["nama"]
                nim = data_mahasiswa[key]["nim"]
                kelas = data_mahasiswa[key]["kelas"]
                prodi = data_mahasiswa[key]["prodi"]
                lahir = data_mahasiswa[key]["lahir"].strftime("%x")

                print(f"{key:<8} {nama:<23} {nim:<13} {kelas:^6} {prodi:^18} {lahir:^13}")
            ganti_menu = input("\n\nKeluar [y]: ")
            if ganti_menu == "y".lower():
                os.system("clear")
                break
            else:
                os.system("clear")
                continue

    elif menu == 3 :
        os.system("clear")
        update_data = data_mahasiswa.copy()
        while True:
            print("UPDATE MAHASISWA\n")
            masukkan_key_update = input("Masukkan Key Mahasiswa yang ingin di update datanya(lihat menu 2). Exit(keluar): ").upper()
            if masukkan_key_update in update_data:
                print(f'''\nData yang ingin anda update adalah:
Nama\t\t: {update_data[masukkan_key_update]["nama"]}
Nim\t\t: {update_data[masukkan_key_update]["nim"]}
Kelas\t\t: {update_data[masukkan_key_update]["kelas"]}
Prodi\t\t: {update_data[masukkan_key_update]["prodi"]}
Tanggal Lahir\t: {update_data[masukkan_key_update]["lahir"].strftime("%x")}''')

                print("\n\nSilahkan masukkan data baru.")
                #data baru
                update_data['nama'] = input("Masukkan Nama\t: ").title()
                update_data['nim'] = input("Masukkan Nim\t: ").title()
                update_data['kelas'] = input("Masukkan Kelas\t: ").title()
                update_data['prodi'] = input("Masukkan Prodi\t: ").title()
                print("Tanggal Lahir")
                tahun = int(input("Masukkan Tahun Lahir baru\t: "))
                bulan = int(input("Masukkan Bulan Lahir baru\t: "))
                tanggal = int(input("Masukkan Tanggal Lahir baru\t: "))
                update_data['lahir'] = datetime.datetime(tahun,bulan,tanggal)
                data_mahasiswa.update({masukkan_key_update:update_data})
                print("\n\nData berhasil di update !")
                time.sleep(1.5)
                break

            elif masukkan_key_update == "exit".upper():
                break

            else:
                print("\n\nKeys yang anda masukkan tidak ditemukan\nMohon masukkan kembali dengan benar !")
                time.sleep(1.5)
                os.system("clear")
                continue
            
    elif menu == 4 :
        os.system("clear")
        hapus_data = data_mahasiswa.copy()
        while True:
            os.system("clear")
            print("HAPUS MAHASISWA\n")
            masukkan_key_delete = input("Masukkan Key Mahasiswa yang ingin di hapus datanya(lihat menu 2). Exit(keluar): ").upper()
            if masukkan_key_delete in hapus_data:
                print(f'''\nData yang ingin anda hapus adalah:
Nama\t\t: {hapus_data[masukkan_key_delete]["nama"]}
Nim\t\t: {hapus_data[masukkan_key_delete]["nim"]}
Kelas\t\t: {hapus_data[masukkan_key_delete]["kelas"]}
Prodi\t\t: {hapus_data[masukkan_key_delete]["prodi"]}
Tanggal Lahir\t: {hapus_data[masukkan_key_delete]["lahir"].strftime("%x")}''')
                hapus = input("Ketik [delete] untuk menghapus data: ").lower()
                if hapus == "delete" or hapus == "hapus":
                    del data_mahasiswa[masukkan_key_delete]
                    print("\n\nData berhasil dihapus!")
                    time.sleep(1.5)
                    break
                    
                else:
                    print("Data tidak jadi dihapus!")
                    time.sleep(1.5)
                    
            elif masukkan_key_delete == "exit".upper():
                break

            else:
                print("\n\nKeys yang anda masukkan tidak ditemukan\nMohon masukkan kembali dengan benar !")
                time.sleep(1.5)
                os.system("clear")
                continue
        
    elif menu == 5 :
        print("\n\nProgram dihentikan !".upper())
        exit()
    
    else :
        print("\nMenu yang anda pilih tidak tersedia! \nSilahkan pilih kembali")
        time.sleep(1.5)
        os.system("clear")
        continue
