class debit:
    def __init__(self, username, pin, saldo, norek):
        self.username = username
        self.pin = pin
        self.saldo = saldo 
        self.norek = norek 

# ini buat bikin akunnya (username, pin, saldo, norek)
# norek buat validasi debitnya itu
p1 = debit("robin", "123", 500000, "321")
p2 = debit("batman", "456", 600000, "654")
p3 = debit("gas stove and fridge", "789", 600000, "987")
# array u untuk nyimpen akun2 yg udh ada
u = [p1, p2, p3]

def tarikTunai(saldo):
    print("\n======================================================")
    x = [50000, 100000, 150000]
    # ini terserah sih klo mo nambain smpe 300rb juga silakan
    for i in range(len(x)):
        print(f"    {i+1}. {x[i]}") 
    print(f"    {len(x)+1}. Tulis nominal sendiri")
    print("    Ketik 0 untuk batal")
    print("======================================================")
    i = int(input(f">> Pilih nominal [1-{len(x)+1}]: "))
    if i == 0:
        return
    if i == len(x)+1:
        nom = int(input(">> Masukkan nominal yang diinginkan: "))
        while nom%50000 != 0:
            print("Hanya bisa kelipatan 50000")
            nom = int(input(">> Masukkan nominal yang diinginkan: "))
    else:
        nom = x[i-1]

    saldo -= nom
    if saldo < 0:
        print("Saldo anda tidak cukup")
        saldo += nom
    else:
        print(f"*uang senilai Rp {nom} keluar*")
    return saldo

def transfer(norek, pin, saldo):
    print("\n======================================================")
    print("    1. Transfer ke sesama Bank")
    print("    2. Transfer ke Bank lain (biaya admin Rp 2.500)")
    print("======================================================")
    tujuan = int(input(">> Pilih [1 atau 2]: "))
    norekTujuan = str(input(">> Nomor rekening tujuan: "))
    x = [100000, 200000, 300000]
    print("\n======================================================")
    for i in range(len(x)):
        print(f"    {i+1}. {x[i]}") 
    print(f"    {len(x)+1}. Tulis nominal sendiri")
    print("    Ketik 0 untuk batal")
    print("======================================================")
    i = int(input(f">> Pilih nominal [1-{len(x)+1}]: "))

    if i == 0:
        return
    if i == len(x)+1:
        nom = int(input(">> Masukkan nominal yang diinginkan: "))
    else:
        nom = x[i-1]
    
    if tujuan == 1:
        saldo -= nom
    else:
        nom += 2500
        saldo -= nom

    if saldo < 0:
        print("Saldo anda tidak cukup")
        saldo += nom
    else:
        print(f"Transfer senilai Rp {nom} berhasil")
    return saldo

def gantiPin(pin):
    pinLama = str(input(">> Masukkan PIN lama: "))
    for j in range(3):
        if pinLama == pin:
            pinBaru = str(input(">> Masukkan PIN baru: "))
            konfirmasi = str(input(">> Ketik ulang PIN baru: "))
            if konfirmasi != pinBaru:
                while konfirmasi != pinBaru:
                    konfirmasi = str(input(">> PIN tidak sesuai, ketik ulang PIN baru: "))
                    if konfirmasi == pinBaru:
                        p.pin = pinBaru
                        print("\nPIN telah diganti")
                        break
                    else:
                      continue
                return
            else:
                p.pin = pinBaru
                print("\nPIN telah diganti")
                return
        elif j == 2 and pinLama != pin:
            print("3 kali salah pin, kartu diblokir")
            return -1
        elif pinLama != pin:
            print("Pin salah")
            pinLama = str(input(">> Masukkan PIN lama: "))

def menu(username):
    print("\n======================================================")
    print(f"    Selamat datang, {p.username}")
    print("    1. Cek Saldo")
    print("    2. Tarik Tunai")
    print("    3. Transfer")
    print("    4. Ganti PIN")
    print("    Ketik 0 untuk keluar")
    print("======================================================")
    x = int(input(">> Pilih transaksi [1-4]: "))
    if x == 0:
        return -1
    elif x == 1:
        return p.saldo
    elif x == 2:
        saldo = tarikTunai(p.saldo)
    elif x == 3:
        saldo = transfer(p.norek, p.pin, p.saldo)
    else:
        saldo = gantiPin(p.pin)
    return saldo
    
norek = ''
i = 0

print("======================================================")
print("         Automated Teller Machine [Rp 50.000]        ")
print("======================================================\n")
norek = str(input(">> Masukkan Nomor Rekening: "))
while norek != u[i].norek: 
    if norek == u[i].norek:
        break
    elif i == len(u)-1 and norek != u[i].norek:
        print("\nNomor rekening tidak terdaftar (kartu tidak valid)")
        norek = str(input(">> Masukkan Nomor Rekening: "))
        i = 0
        continue
    i += 1

p = u[i]
pin = str(input(">> Masukkan PIN: "))
for j in range(3):
    if pin == p.pin:
        pin = p.pin
        lanjut = "y"
        while lanjut == "y":
            transaksi = menu(p.username)
            if transaksi == -1:
                break
            elif transaksi != None:
                p.saldo = transaksi
                print(f"Sisa saldo anda Rp {p.saldo}")
            else:
                continue 
            lanjut = str(input(">> Lakukan transaksi lain? [y/n]: "))
        break
    elif j == 2 and pin != p.pin:
        print("3 kali salah PIN, kartu diblokir")
    elif pin != p.pin:
        print("PIN salah")
        pin = str(input(">> Masukkan PIN: "))
print("\n  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("/            Transaksi selesai           \\")
print("\ Terima kasih telah menggunakan ATM ini /")
print("  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
