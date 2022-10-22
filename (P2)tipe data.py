#tipe data

#tipe data integer 
data_integer = 12
print("data : ", data_integer)
print("-bertipe : ", type(data_integer))

#tipe data float yaitu tipe data yang memiliki koma
data_float = 1.2
print("data : ", data_float)
print("-bertipe : ", type(data_float))

#tipe data string yaitu tipe data kumpulan karakter
data_string = "raihan"
print("data : ", data_string)
print("-bertipe : ", type(data_string))

#tipe data boolean/biner (true & false)
data_bool = True
print("data : ", data_bool)
print("-bertipe : ", type(data_bool))
data_bool = False
print("data : ", data_bool)
print("-bertipe : ", type(data_bool))

##TIPE Data khusus

#bilangan kompleks
data_complex = complex(2.3)
print("data : ", data_complex)
print("-bertipe : ", type(data_complex))

#tipe data dari bahas c
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("-bertipe : ", type(data_c_double))
