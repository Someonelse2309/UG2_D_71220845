hp = str(input("Masukan Nomor Telepon Anda\n>> "))
if len(hp)==12:
    spl = [hp[i:i+4] for i in range(0, len(hp), 4)]
    op1 = spl[0]
    if op1 == ("0816"):
        print ("Nomor Yang Anda Gunakan Adalah Indosat")
    elif op1 == ("0814"):
        print ("Nomor Yang Anda Gunakan Adalah Telkomsel")
    else:
        print ("Maaf Nomor Yang Anda Gunakan Tidak Diketahui Operatornya")
    gg = int(spl[2])
    if gg%2 == 1:
        print ("Nomor Yang Digunakan Adalah Ganjil")
    else:
        print ("Nomor Yang Digunakan Adalah Genap")
else:
    print ("Maaf Nomro Anda Kurang/Lebih")