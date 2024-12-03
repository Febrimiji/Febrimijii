# string adalah kumpulan dari karakter

data = "ini adalah string"
print(data)
print("panjang karakter :", len (data ))
print("tipe data :", type (data ))

# 1. cara membuat string

"""
   1. dengan menggunakan single quotes '...'
   2. dengan menggunakan double quotes "..."
"""

data = 'menggunakan single quotes'
print(data)

data = "menggunakan double quotes"
print(data)

print("ini adalah hari jum'at")
print("nama saya adalah ma'ul")

# 2. kekuatan tanda \

# membuat ' menjadi string
print('mari sholat jum\'at')
print('saya ma\'ul')

# double backslash
print('C:\\user\\adam')

# tab (\t)
print("MU\bJuara")

# backspace(\b)
print("MU\bJuara")

# newline (enter)
print("baris satu.\nbaris dua.") # LF -> line feed # macOS
print("baris satu.\n\baris dua.") # CRLF -> windows

# raw string
print(r'C:\user\adam')

