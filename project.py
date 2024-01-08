import os
import datetime as dt

# deklarasi variable
pesanUlang = True
rekap_pesanan = []
rekap_bayar = []
totalMakan = 0
totalMinum = 0
totalPaket = 0
tanggalSekarang = dt.date.today()
tahun = tanggalSekarang.year

# daftar menu
makanan = {
    "1.Bakso" : 15000,
    "2.Mie ayam" : 10000,
    "3.Spageti" : 18000,
    "4.Chicken" : 10000,
    "5.Nasi goreng" : 12000,
    "6.Mie goreng" : 10000,
    "7.Kebab" : 10000,
    "8.Burger" : 20000,
    "9.Kwetiau" : 10000,
    "10.Hot dog": 18000
}

minuman = {
    "1.Es teh manis"   : 5000,
    "2.Chocolate"  : 8000,
    "3.Green tea" : 7000,
    "4.Mineral" : 3000,
    "5.Kopi     " : 5000,
    "6.Orange jus" : 7000,
    "7.Boba ice" : 10000,
    "8.Es kelapa" : 6000
}

paket = {
    "1.bakso + es teh manis" : 18000,
    "2.mie ayam + es teh manis" : 12000,
    "3.Burger + boba ice" : 25000,
    "4.kwetiau + orange jus" : 15000
}

# function start
def header():
    '''function header'''
    print(45*"\033[0;34m=")
    print("** welcome to 3fm restourant **".upper().center(45))
    print(f"saudara/i {namaPembeli}".upper().center(45))
    print(45*"\033[;034m=")
    print(tanggalSekarang.strftime("\033[0;39mTanggal : %d-%m-%Y"))

def opsi_boking():
    '''opsi boking'''
    print("\ndata booking".upper())
    nama = input("Nama : ")
    bulan = int(input("Bulan: "))
    tanggal = int(input("Tanggal: "))
    tgl = dt.date(tahun,bulan,tanggal)
    jumlahOrang = int(input("Jumlah orang : "))
    jam = input("jam [siang/sore/malam] : ")
    print(45*"=")
    print("data booking ".upper().center(45))
    print(45*"=")
    print("Nama         : ", nama)
    print("Jumlah orang : ", jumlahOrang, "orang")
    print("Tanggal      : ", tgl.strftime("%d-%m-%Y"))
    print("jam          : ", jam)
    print(45*"=")
     
def opsi_pesan():
    '''opsi pesan'''
    paket_atau_satuan = input("\nPaket atau satuan: ")
    if paket_atau_satuan == "satuan" or paket_atau_satuan == "Satuan":       
        jenisPesanan = input("\nsilahkan mau pesan makan/minum : ".upper())
        print(f"\n{'Menu':<20}  {'Harga':<16}\n")

        if jenisPesanan == "makan" or jenisPesanan == "Makan":
            for menu,harga in makanan.items() :
                print(f"{menu:<20} Rp.{harga:<18}")
        elif jenisPesanan == "minum" or jenisPesanan == "Minum":
            for menu,harga in minuman.items() :
                print(f"{menu}\t\tRp.{harga}")
        else :
            print("NOTE : Periksa inputan anda")
        return jenisPesanan
    else:
        for menu,harga in paket.items():
            print(f"{menu:<30} Rp.{harga:<18}")
        
def pesanMakan():    
    '''pesanan == makan'''
    if noPesanan == 1 :
        rekap_pesanan.append(f"Bakso x{jumlahPesan}")
        totalMakan = 15000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 2 :
        rekap_pesanan.append(f"Mie ayam x{jumlahPesan}")
        totalMakan= 10000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 3 :
        rekap_pesanan.append(f"Spageti x{jumlahPesan}")
        totalMakan = 18000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 4 :
        rekap_pesanan.append(f"Chiken x{jumlahPesan}")
        totalMakan = 10000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 5 :
        rekap_pesanan.append(f"Nasi goreng x{jumlahPesan}")
        totalMakan = 12000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 6 :
        rekap_pesanan.append(f"Mie goreng x{jumlahPesan}")
        totalMakan = 10000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 7 :
        rekap_pesanan.append(f"Kebab x{jumlahPesan}")
        totalMakan = 7000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 8 :
        rekap_pesanan.append(f"Burger x{jumlahPesan}")
        totalMakan = 20000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 9 :
        rekap_pesanan.append(f"Kwetiau x{jumlahPesan}")
        totalMakan = 10000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    elif noPesanan == 10 :
        rekap_pesanan.append(f"Hot dog x{jumlahPesan}")
        totalMakan = 18000 * jumlahPesan
        rekap_bayar.append(totalMakan)
    else:
        print("Periksa inputan anda")
    return noPesanan,jumlahPesan

def pesanMinum():
    '''pesan == minum'''
    if noPesanan == 1 :
        rekap_pesanan.append(f"Ice tea x{jumlahPesan}")
        totalMinum = 5000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    elif noPesanan == 2 :
        rekap_pesanan.append(f"Chocolat x{jumlahPesan}")
        totalMinum = 8000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    elif noPesanan == 3 :
        rekap_pesanan.append(f"Green tea x{jumlahPesan}")
        totalMinum = 7000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    elif noPesanan == 4 :
        rekap_pesanan.append(f"Mineral x{jumlahPesan}")
        totalMinum = 3000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    elif noPesanan == 5 :
        rekap_pesanan.append(f"Kopi x{jumlahPesan}")
        totalMinum = 5000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    elif noPesanan == 6 :
        rekap_pesanan.append(f"Orange jus x{jumlahPesan}")
        totalMinum = 7000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    elif noPesanan == 7 :
        rekap_pesanan.append(f"Boba ice x{jumlahPesan}")
        totalMinum = 10000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    elif noPesanan == 8 :
        rekap_pesanan.append(f"Es kelapa x{jumlahPesan}")
        totalMinum = 6000 * jumlahPesan
        rekap_bayar.append(totalMinum)
    else:
        print("Periksa inputan anda")
        
def pesan_paket():
    '''pesan == paket'''
    if noPesanan == 1:
        rekap_pesanan.append(f"Bakso & es teh manis x{jumlahPesan}")
        totalPaket = 18000 * jumlahPesan
        rekap_bayar.append(totalPaket)
    elif noPesanan == 2:
        rekap_pesanan.append(f"Mie ayam & es teh manis x{jumlahPesan}")
        totalPaket = 12000 * jumlahPesan
        rekap_bayar.append(totalPaket)
    elif noPesanan == 3:
        rekap_pesanan.append(f"Burger & boba ice x{jumlahPesan}")
        totalPaket = 25000 * jumlahPesan
        rekap_bayar.append(totalPaket)
    elif noPesanan == 4:
        rekap_pesanan.append(f"Kwetiau & orange jus x{jumlahPesan}")
        totalPaket = 15000 * jumlahPesan
        rekap_bayar.append(totalPaket)
    else:
        print("Periksa inputan anda")
        
def pembayaran():
    '''fungsi untuk pembayaran'''
    print("-"*45)
    pembayaran = print("Pilihan Pembayarn\n1.virtual Account\n2.Cash\n3.Transfer")
    pembayaran = int(input("\nSilahkan Pilih No Pembayaran = "))
    if pembayaran == 1 :
        bank = input("BRI/BCA  : ")
        if bank == "BRI" or bank == "bri" :
            print("Briva : 0125695355")
            print("-"*45)
        elif bank == "BCA" or bank == "bca" :
            print("Bca virtual account : 098564678")
            print("-"*45)
        else:
            print("Periksa inputan anda")
    elif pembayaran == 2 :
        print(r"''Silahkan Lakukan Pembayaran dikasir''".upper())
        print("-"*45)
    elif pembayaran == 3 :
        bank = input("BRI/BCA  : ")
        if bank == "BRI" or bank == "bri" :
            print("BRI : 0357928693(maghfur hasani)")
            print("-"*45)
        elif bank == "BCA" or bank == "bca" :
            print("BCA : 07645727256(maghfur hasani)")
            print("-"*45)
    else:
        print("Periksa inputan anda")


# main program
namaPembeli = input("nama: ".upper())
os.system('cls')

print(45*"-")
print("| resto kami menyedikan 2 opsi pemesanan |".upper().center(45))
print(45*"-")
print("1.Booking\n2.Pesan\n".upper())
opsi = input("Booking Atau Pesan? => ")
header()

if opsi == "booking" or opsi =="Booking" or opsi == "boking" or opsi == "Boking":
    opsi_boking()
elif opsi == "pesan" or opsi == "Pesan":
    while True:
        jenisPesanan= opsi_pesan()
        noPesanan = int(input("\nSilahkan input no menu : "))
        jumlahPesan = int(input("Berapa banyak : "))
        
        if jenisPesanan == "makan" or jenisPesanan == "Makan":
            pesanMakan()
        elif jenisPesanan == "minum" or jenisPesanan == "Minum":
            pesanMinum()
        else:
            pesan_paket()
            
        pesananTambahan = input("ada lagi (y/t) ? : ")
        if pesananTambahan == "y" or pesananTambahan == "Y":
            continue
        elif pesananTambahan == "t" or pesananTambahan == "T":
            break
        else:
            print("NOTE: Periksa inputan anda")
            print("-"*45)
            continue
        
    # hasil  orderan
    total_bayar = sum(rekap_bayar)
    format_pesanan = ", ".join(rekap_pesanan)
        
    print(45*"\033[0;34m_")
    print("rekap pesanan".center(45).upper())
    print(f"=> saudara\i {namaPembeli} <= ".center(45).upper()) 
    print("-"*45)
    print(f"\033[0;39mpesanan       = {format_pesanan}")
    print(f"Total pesanan = {total_bayar:,}")
    
    while True:
        uang = int(input(f"uang          = "))
        kembalian = uang - total_bayar
        if kembalian < 0 :
            kesalahanInput = print("\n\"Pastikan nominal anda tidak kurang dari jumlah yang harus dibayar\"")
            continue
        else:
            break
    
    print(f"kembalian     = {kembalian:,}")
    
    # pembayaran
    while True:
        pembayaran()
        konfirmasi = input("Konfirmasi pembayaran [y/t]: ")
        if konfirmasi == "y" or konfirmasi == "Y" :
            print('virtual account: 02163981')
            print('Nama: maghfurhasani')
            break
        else :
            True 
else :
    print("NOTE : Periksa inputan anda")
        
# footer
print(45*"\033[0;34m_")
print("terimakasih atas kunjungannya".upper().center(45))
print("selamat menikmati".upper().center(45))
print(45*"-")
