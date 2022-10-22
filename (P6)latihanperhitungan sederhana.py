#PROGRAM KONVERSI TEMPERATUR

#PROGRAM KONVERSI TEMPERATUR CELCIUS KE SATUAN LAIN
print("\nPROGRAM KONVERSI TEMPERATUR\n")
print("===CELCIUS===")

celcius = float(input("masukan suhu dalam celcius : "))
print("suhu adalah",celcius, "celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur",reamur,"reamur")

#fahrenheit
fahrenheit = ((9/5)*celcius) + 32
print("suhu dalam fahrenheit",fahrenheit,"fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin",kelvin,"kelvin")

print("\n===REAMUR===\n")
reamur = float(input("masukan suhu dalam reamur : "))
print("suhu adalah",reamur, "reamur")

#celcius
celcius = (5/4) * reamur
print("suhu dalam celcius",celcius,"celcius")

#fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit",fahrenheit,"fahrenheit")

#kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin",kelvin,"kelvin")

print("\n===FAHRENHEIT===\n")
fahrenheit = float(input("masukan suhu dalam fahrenheit : "))
print("suhu adalah",fahrenheit, "fahrenheit")

#celcius 
celcius = ((5/9) * fahrenheit) - 32
print("suhu dalam celcius",celcius,"celcius")

#reamur
reamur =((4/9) * fahrenheit) - 32
print("suhu dalam reamur",reamur,"reamur")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin",kelvin,"kelvin")

print("\n===KELVIN===\n")
kelvin = float(input("masukan suhu dalam kelvin : "))
print("suhu adalah",kelvin,"kelvin")

#celcius 
celcius = kelvin - 273
print("suhu dalam celcius",celcius,"celcius")

#reamur
reamur = ((4/5) * kelvin) - 237
print("suhu dalam reamur",reamur,"reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit",fahrenheit,"fahrenheit")