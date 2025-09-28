# Nama         : Muhammad Farel Awaluddin
# NIM          : 2509116055
# Mini Project : 2

# nama donatur awal
donasi = [
     ["Muhammad Farel Awaluddin", 20000]
]

nominal = (20000, 50000, 100000, 300000)

# role pengguna
users = {
    "karyawan" : {"role" : "Karyawan", "password" : "karyawanlogin"},
    "manager"  : {"role" : "Manager", "password" : "managerloginaja"}
}

def menu():
    while True:
        print("\n=======================================================")
        print("Haloo! Anda sedang berada di sistem pencatatatan donasi")
        print("Anda akan diarahkan pada bagian menu")
        print("=======================================================")
        print("1. Menu Login")
        print("2. Menu Keluar")

        try:
            Pilihan = input("Masukkan Angka pilihan anda yaa(1/2): ")

            if Pilihan == "1":
                login()
            elif Pilihan == "2":
                print("Anda akan keluar, terimakasih telah menggunakan layanan kami")
                break
            else:
                print("Angka yang anda masukkan tidak valid, tolong masukkan angka yang ada pada pilihan yang tersedia ")

        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c ya!")
        except EOFError:
            print("Jangan tekan ctrl+z ya!")

def login():
    kesempatan = 5
    while kesempatan > 0:
        print("\n===============================================================================")
        print("Anda Memilih Menu Login, Selamat datang di menu login sistem pencatatan donasi!")
        print("Anda akan diarahkan untuk memilih login berdasarkan role anda")
        print("===============================================================================")

        try:
            username = input("Masukkan Username anda (karyawan/manager): ")
            password = input("Masukkan Password anda: ") 
        
            if username in users and users[username]["password"] == password:
                role = users[username]["role"]
                if role == "Karyawan":
                    Bagian_Karyawan()
                    return
                elif role == "Manager":
                    Bagian_Manager()
                    return
                
            else:
                kesempatan -= 1
                print("Username atau password salah, silahkan masukkan yang benar")

        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c ya!")
        except EOFError:
            print("Jangan tekan ctrl+z ya!")

    if kesempatan == 0:
        print("Maaf kesempatan anda habis, anda akan kembali ke menu utama")

def Bagian_Karyawan():
    while True:
        print("\n==========================================================")
        print("Selamat Datang karyawan, anda akan diarahkan ke fitur anda")
        print("SIlahkan Lihat Menu Dibawah!!!!!!!!!")
        print("==========================================================")
        print("SIlahkan pilih menu yang ingin anda akses")
        print("1. Lihat Donasi")
        print("2. Tambah Donasi")
        print("3. Kembali ke menu utama")
            
        try:
            Menu_Donasi = input("Masukkan angka dari pilihan yang tersedia(1/2/3): ")
            if Menu_Donasi == "1":
                Lihat_donasi()       
            elif Menu_Donasi == "2":
                Tambah_donasi()
            elif Menu_Donasi == "3":
                print("Kembali ke menu utama")
                return
            else:
                print("Anda memasukkan menu yang tidak tersedia")

        except KeyboardInterrupt:
                    print("Jangan tekan ctrl+c ya!")
        except EOFError:
                    print("Jangan tekan ctrl+z ya!")
    
def Bagian_Manager():
    while True:
        print("\n==========================================================")
        print("Selamat Datang Pak Manager, anda akan diarahkan ke fitur anda")
        print("SIlahkan Lihat Menu Dibawah!!!!!!!!!")
        print("==========================================================")
        print("SIlahkan pilih menu yang ingin anda akses")
        print("1. Lihat Donasi")
        print("2. Tambah Donasi")
        print("3. Update Donasi")
        print("4. Hapus Donasi")
        print("5. Kembali ke menu utama")

        try:
            Menu_Donasi2 = input("Masukkan angka dari pilihan yang tersedia(1/2/3/4/5): ")
            if Menu_Donasi2 == "1":
                Lihat_donasi()       
            elif Menu_Donasi2 == "2":
                Tambah_donasi()
            elif Menu_Donasi2 == "3":
                Update_donasi()
            elif Menu_Donasi2 == "4":
                Hapus_donasi()
            elif Menu_Donasi2 == "5":
                print("Kembali ke menu utama")
                return
            else:
                print("Anda memasukkan menu yang tidak tersedia")
        
        except KeyboardInterrupt:
                    print("Jangan tekan ctrl+c ya!")
        except EOFError:
                    print("Jangan tekan ctrl+z ya!")

# bagian read
def Lihat_donasi():
    print("\n=============")
    print("daftar donasi")
    print("=============")

    print("\nBerikut nama donatur dan jumlah donasinya")
    print("============================================")
    for lihat in donasi:
        print("Nama:", lihat[0], "| Donasi:", lihat[1])
    print("============================================")

# bagian create
def Tambah_donasi():
    while True:

        try:
            print("\n===================================")
            print("Selamat datang di menu tambah donasi")
            print("===================================")

            print("\nSilahkan masukkan nominal dan nama ")
            print("Nominal yang tersedia :", nominal)
            jumlah = int(input("Masukkan Nominal yang tersedia: "))
            Nama_donatur = input("Masukkan Nama Anda: ")

            if jumlah in nominal:
                donasi.append([Nama_donatur, jumlah])
                print("Donasi Berhasil ditambahkan")
                Lihat_donasi()
                break
            else:
                print("Input yang anda masukkan tidak valid")
        
        except ValueError:
            print("tolong masukkan angka")
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c ya!")
        except EOFError:
            print("Jangan tekan ctrl+z ya!")
    
# bagian update
def Update_donasi():
    print("\n===================================")
    print("Selamat datang di menu update donasi")
    print("===================================")
    print("Silahkan pilih data yang ingin diubah")
    Lihat_donasi()
    
    try:
        nomor = int(input("Masukkan urutan yang ingin diubah (misalnya:1): ")) - 1

        Update = input("Masukkan data yang ingin diubah (Nama(1), Donasi(2) ):")
        if Update == "1":
            nama_donatur = input("Ganti nama donatur: ")
            donasi[nomor][0] = nama_donatur
            print("Nama Berhasil Diubah")
        elif Update == "2":
            Jumlah_donasi = int(input("Ganti Jumlah donasi sesuai nominal: "))
            donasi[nomor][1] = Jumlah_donasi
            print("Jumlah donasi berhasil diubah")
        else:
            print("Pilihan anda tidak valid")
    except KeyboardInterrupt:
            print("Jangan tekan ctrl+c ya!")
    except EOFError:
            print("Jangan tekan ctrl+z ya!")

# bagian delete
def Hapus_donasi():
    print("\n===================================")
    print("Selamat datang di menu hapus donasi")
    print("===================================")
    print("Silahkan pilih data yang ingin dihapus")
    Lihat_donasi()

    try:
         nomor1 = int(input("Masukkan urutan yang ingin dihapus (misalnya:1): ")) - 1
         terhapus = donasi[nomor1][0]
         donasi.pop(nomor1)
         print(f"Donasi {terhapus} dihapus")

    except ValueError:
            print("tolong masukkan angka")
    except KeyboardInterrupt:
            print("Jangan tekan ctrl+c ya!")
    except EOFError:
            print("Jangan tekan ctrl+z ya!")
    
menu()

