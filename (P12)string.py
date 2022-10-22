data = "ini adalah data string"
print(data)
print(type(data))

#1. cara membuat string 

'''
    1. dengan menggunakan single quote '....'
    2. degan menggunakan double quote "...."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print("'hallo apakabar ?'")
print('"hallo apakabar ?"')
print("besok hari jum'at")

#2. menggunakan tanda \

#membuat tanda ' menjadi string 
print('besok hari jum\'at')
print('g\'day isn\'it')

#backlash
print("c:\\user\\raihan")

#tab 
print("raihan\t amalia")

#backspace 
print("raihan\banisa")

#new line
print("anisa\nraihan") #Lf -> line feed #digunakan oleh os unix, linux 
print("anisa\rraihan") #cr -> cariage return #digunakan oleh bahasa pemograman terdahulu
print("anisa\n\rraihan") #crlf -> cariage return line feed #digunakan oleh windows

#string literal atau raw
print(r'c:\folder\rian')

#multi line literal string
print("""
nama : rian
kelas : TI20c
""")

#multi line literal string dan RAW
print(r"""
nama : rian
kelas : TI20c
website : rian.raihan\com
""")