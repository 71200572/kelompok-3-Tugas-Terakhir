
print("")
print("==========SISTEM PEMANTAUAN DAN PERINGATAN DINI BANJIR==========")
print("")
print("")

lokasi =str(input("MASUKKAN LOKASI KOTA ANDA: "))
print("")
print("Selamat datang di program sistem pemantauan terjadinya di",lokasi, "!")

while True:
    try:
        suhu = int(input("MASUKKAN SUHU UDARA DI LOKASI ANDA (Celcius): "))
        if (suhu <= 26):
            print(suhu,"C dingin")
            break
        elif (suhu <= 28):
            print(suhu,"C normal")
            break
        elif (suhu <= 30):
            print(suhu,"C panas")
            break
        elif (suhu >= 31):
            print(suhu,"C sangat panas")
            break
        else:
            print("suhu tidak ada.")
    except ValueError:
        print("data harus berupa angka, coba lagi!!")
    
while True:
    try:
        udara = int(input("MASUKKAN KELEMBAPAN UDARA DI LOKASI ANDA: " ))
        if (udara <= 30):
            print(udara,"%","sangat rendah")
            break
        elif (udara <= 44):
            print(udara,"%","rendah")
            break
        elif (udara <= 64):
            print(udara,"%","normal")
            break
        elif (udara <= 74):
            print(udara,"%","tinggi")
            break
        elif (udara >= 75):
            print(udara,"%","sangat tinggi")
            break
        else:
            print("tidak ada dalam daftar")
    except ValueError:
        print("data harus masuk berupa angka, coba lagi!!")
        
while True:
    try:
        angin = int(input("MASUKKAN KECEPATAN ANGIN DI LOKASI ANDA: "))
        if (angin <= 20):
            print(angin,'km/jam rendah')
            break
        elif (angin <= 40):
            print(angin,'km/jam normal')
            break
        elif (angin >= 40):
            print(angin,'km/jam tinggi')
            break
    except ValueError:
        print("data harus berupa angka, coba lagi!!")

while True:
    try:
        air = int(input("MASUKKAN TINGGI AIR SUNGAI DI LOKASI ANDA: "))
        if (air <= 170):
            print(air,"Cm dalam status masih Normal, hijau")
            break
        elif (air <= 200):
            print(air,'Cm dalam status Waspada, kuning')
            break
        elif (air <= 250):
            print(air,"Cm dalam status Siaga, orange")
            break
        elif (air >= 250):
            print(air,'Cm dalam status Bahaya, merah')
            break
    except ValueError:
        print("data harus berupa angka, silahkan coba lagi!!")
        
#kel babakan kecamatan kiaracondong dekat sungai cicadas.
#30 c
#65%
#45 km/jam
#200 cm status waspada, kuning

#print(suhu,udara,angin,air)