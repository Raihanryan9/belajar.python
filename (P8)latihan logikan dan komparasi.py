#membuat gabungan area rentang dari angka

#+++++3----10++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

#+++++3-----
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3=",isKurangDari)

#------10++++
isLebihDari = (inputUser > 10)
print("lebih dari 10=",isLebihDari)

#++++3-----10++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ", isCorrect)

#----3++++10---
#kasus irisan
print("\n",10*"=","\n")

inputUser = float(input("masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))

#-----3+++++++
#lebih dari 3
isLebihDari = inputUser > 3
print("lebih dari 3 = ",isLebihDari)

#+++++10-----
isKurangDari = inputUser < 10
print("kurang dari 10 = ",isKurangDari)

#----3++++10---
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan : ", isCorrect)

#tugas
print("\n",10*"=","\n")

inputUser = float(input("masukan angka yang bernilai\nlebih dari 0\ndan\nkurang dari 5\nlebih dari 8\natau\nkurang dari 11\n : "))
isLebihDari = inputUser > 0
print("lebih dari 0 = ",isLebihDari)

isKurangDari = inputUser < 5
print("kurang dari 5 = ",isKurangDari)

islebih = inputUser > 8
print("lebih dari 8 = ",islebih)

iskurang = inputUser < 11
print("kurang dari 11 = ",iskurang)

ishasil = isLebihDari and isKurangDari
isCorrect = islebih or iskurang
print("angka yang dimasukan = ",isCorrect)

print("\n",10*"=","\n")

inputUser = float(input("masukan angka yang bernilai\nkurang dari 0\ndan\nlebih dari 5\nkurang dari 8\natau\nlebih dari 11\n : "))
isKurangDari = inputUser < 0
print("kurang dari 0 = ",isKurangDari)

isLebihDari = inputUser > 5
print("lebih dari 5 = ",isLebihDari)

iskurang = inputUser < 8
print("kurang dari 8 = ",iskurang)

islebih = inputUser > 11
print("lebih dari 11 = ",islebih)

ishasil = isKurangDari and isLebihDari
isCorrect = iskurang or islebih
print("angka yang dimasukan = ",isCorrect)