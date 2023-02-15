a=0
b=1
ttldskn = 0
ttlhrg = 0
brg = input("Masukan Barang Anda (Pisahkan Dengan Koma)\n>> ").split(",")
count = len(brg)
while count > a:
    hrg = int(input(f"\nMasukan Harga Barang {brg[a]}\n>> "))
    if hrg >= 25000000:
        print (f"Diskon 25%")
        dskn = hrg * 0.25
        hrgakh = hrg - dskn
        print (f"\nHarga Sebelum Diskon \t: Rp. {int(hrg)}\nDapat Diskon (25%) \t: Rp. {int(dskn)}\nHarga Setelah Diskon \t: Rp. {int(hrgakh)}")
        ttlhrg += hrgakh
        ttldskn += dskn
        a += 1
        b += 1
    elif hrg >= 10000000:
        print (f"Diskon 10%")
        dskn = hrg * 0.1
        hrgakh = hrg - dskn
        print (f"\nHarga Sebelum Diskon \t: Rp. {int(hrg)}\nDapat Diskon (10%) \t: Rp. {int(dskn)}\nHarga Setelah Diskon \t: Rp. {int(hrgakh)}")
        ttlhrg += hrgakh
        ttldskn += dskn
        a += 1
        b += 1 
    else:
        hrgakh = hrg
        dskn = 0
        print (f"\nHarga Sebelum Diskon \t: Rp. {int(hrg)}\nDapat Diskon (0%) \t: Rp. {int(dskn)}\nHarga Setelah Diskon \t: Rp. {int(hrgakh)}")
        ttlhrg += hrgakh
        a += 1
        b += 1
print (f"\nHarga Total\t\t: Rp. {ttlhrg}\nTotal Diskon\t\t: Rp. {ttldskn}\n")

