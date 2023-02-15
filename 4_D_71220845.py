ulg = 1
smuanama = ['']
smuamember = ['']
while ulg == 1:
    print ("======= Selamat Datang =======")
    print ("Masukan Pilihan Anda\n 1. Menambah Data\n 2. Melihat Data\n 3. Keluar")
    pil1 = int(input(">> "))
    if pil1 == 1:
        nama = str(input("\nMasukan Nama Pengguna\n>> "))
        member = str(input("Masukan Pilihan Member\n>> "))
        smuanama.append(nama)
        smuamember.append(member)
        ulg = 1
        print ("\n")
    elif pil1 == 2:
        a = 1
        b = 1
        print ("Nama - Membership")
        jmlh = len(smuanama)
        while a < jmlh:
            print (f"{a}. {smuanama[b]} - {smuamember[b]}")
            a += 1
            b += 1
        ulg = 1
        print ("\n")
    elif pil1 == 3:
        print ("Terima Kasih")
        ulg = 0
    else:
        print ("Maaf Input Anda Invalid\n")
        ulg = 1