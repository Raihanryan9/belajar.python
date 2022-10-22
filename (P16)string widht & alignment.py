#data

data_nama = "rian raihan"
data_umur = 22
data_tinggi = 165.4
data_nomor_sepatu = 32

#string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"data string"+5*"=")
print(data_string)

#string multiline (dengan menggunkan enter, newline,|n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"data string"+5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"data string"+5*"=")
print(data_string)

#mengatur lebar
data_string = f"""
nama    = {data_nama:>10}
umur    = {data_umur:>10}
tinggi  = {data_tinggi:>10}
sepatu  = {data_nomor_sepatu:>10}
"""
print("\n"+5*"="+"data string"+5*"=")
print(data_string)
