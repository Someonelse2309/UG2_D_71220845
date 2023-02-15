a=0
b=1
ttldskn = 0
ttlhrg = 0
brg = input("Masukan Barang Anda (Pisahkan Dengan Koma)\n>> ").split(",")
count = len(brg)
while count > a:
    hrg = int(input(f"Masukan Harga Barang {brg[a]}\n>> "))
    if hrg > 25000000:
        print (f"Diskon 25%")
        dskn = hrg * 0.25
        hrgakh = hrg - dskn
        print (f"Dapat Diskon Rp. {dskn}\nHarga setelah diskon {hrgakh}\nHarga sebelum diskon {hrg}")
        ttlhrg += hrgakh
        ttldskn += dskn
        a += 1
        b += 1
    elif hrg > 10000000:
        print (f"Diskon 10%")
        dskn = hrg * 0.1
        hrgakh = hrg - dskn
        print (f"Dapat Diskon Rp. {dskn}\nHarga setelah diskon {hrgakh}\nHarga sebelum diskon {hrg}")
        ttlhrg += hrgakh
        ttldskn += dskn
        a += 1
        b += 1 
    else:
        hrgakh = hrg
        dskn = 0
        print (f"Dapat Diskon Rp. {dskn}\nHarga setelah diskon {hrgakh}\nHarga sebelum diskon {hrg}")
        ttlhrg += hrgakh
        a += 1
        b += 1
print (f"Harga Total {ttlhrg}\nTotal Diskon {ttldskn}")

