#merubah case dari string

#merubah semua ke uper case

salam = "hai"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

#merubah semua ke lower case
apakabar = "KABAR BAIK"
print("KABAR BAIK = " + apakabar)
apakabar = apakabar.lower()
print("lower = " + apakabar)

#pengecekan dengan isX methode

#contoh pengecekan islower
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
#contoh pengecekan isupper
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))
#contoh pengecekan alpha (mengecek semua huruf)
salam = "sist"
apakah_alpha = salam.isalpha()
print(salam + " is alpha = " + str(apakah_alpha))
#contoh pengecekan isalnum (huruf dan angka)
salam = "sist23"
apakah_alnum = salam.isalnum()
print(salam + " is alnum = " + str(apakah_alnum))
#contoh pengecekan decimal (angka saja)
salam = "sist"
apakah_decimal = salam.isdecimal()
print(salam + " is decimal = " + str(apakah_decimal))
#contoh pengecekan isspace (spasi, tab, newline)
salam = "sist"
apakah_space = salam.isspace()
print(salam + " is space = " + str(apakah_space))
#contoh pengecekan title (semua kata dimulai dengan huruf besar)
judul = "Rian Raihan"
cek_judul = judul.istitle()
print(judul + " is judul = " + str(cek_judul))

#pengecekan startswith dan endswith
cek_start = "Rian raihan".startswith("Rian")
print("start = " + str(cek_start))

cek_end = "Rian raihan".endswith("raihan")
print("end = " + str(cek_end))

#penggabungan komponen join () dan split ()
pisah = ['rian','raihan','amalia']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "rianraihanamalia"
print(gabungan.split("raihan"))

#alokasi karakter ljust, ljust, center
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,"-")
print("'"+tengah+"'")

tengah = "tengah".strip("-")
print("'"+tengah+"'")