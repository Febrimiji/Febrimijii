# operasi logika boolean

# not, or, and

# NOT
print("===NOT===")
a = False
b = not a
print("data a = ", a)
print("..................NOT")
print("print data c=", b)

# OR - Jika salah satu bernilai TRUE maka hasil = TRUE
print("===OR===")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True 
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND - Jika salah satu bernilai FALSE, hasil = FALSE
print("===AND===")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True 
b = True
c = a and b
print(a, "AND", b, "=", c)