#merubah tipe data dari tipe data lain
#int, flost, str, bool

##INTEGER
print("===INTEGER===")
data_int = 9;
print("data = ", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, "type =",type(data_float))
print("data = ", data_str, "type = ",type(data_str))
print("data = ", data_bool, "type = ",type(data_bool))

##FLOAT
print("===FLOAT===")
data_float = 0;
print("data = ", data_float, ",type =",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_bool, "type =",type(data_bool))

##BOOLEAN
print("===BOOLEAN===")
data_bool = True;
print("data = ", data_bool, ",type =",type(data_bool))

data_int = int(data_bool)#nilai dibulatkan kebawah
data_str = str(data_bool)
data_float = bool(data_bool)#akan false/true jika nilai false/true
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_float, "type =",type(data_float))

##STRING
print("===STRING===")
data_str = "10";
print("data = ", data_str, ",type =",type(data_str))

data_int = int(data_str)#string harus angka
data_float = str(data_str)#string harus angka
data_bool = bool(data_str)#false jika string kosong
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_float, "type =",type(data_float))
print("data = ", data_bool, "type =",type(data_bool))

