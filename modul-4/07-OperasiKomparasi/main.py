# Operasi komparasi

# setiap kali selalu bertipe boolean (TRUE/FALSE)

# >, <, <=, =>, !=, is, dan is not

# deklarasi variabel
a = 4
b = 2

# lebih besar dari (>)
print("=== lebih besar dari (>)")
hasil = a > 2  # TRUE
print(a, ">", 2, "=", hasil)
hasil = a < 2 #FALSE
print(a, "<", 2, "=", hasil)
hasil = b > 2 #TRUE
print(b, ">", 2, "=", hasil)
hasil = b < 2  #FALSE
print(b, "<", 2, "=", hasil)

# lebih dari sama dengan (=)
print("===Lebih Dari Sama Dengan (<=)")
hasil = a <= 2 #FALSE
print(a, "<=", 2, "=", hasil)
hasil = b <= 3 #TRUE
print(b, "<=", 3, "=", hasil)
hasil = b >= 2 #FALSE
print(b, ">=", 2, "=", hasil)

# tidak sama dengan (!=)
print("===tidak sama dengan(!=)")
hasil = a != 2 #TRUE
print(a, "!=", 2, "=", hasil)
hasil = b != 2 #FALSE
print(b, "!=", 2, "=", hasil)


# is sebagai komparasi objek
x = 5
y = 5

hasil = x is y
print("nilai x : ", x, "id: ", hex(id(x)))
print("nilai y : ", y, "id: ", hex(id(y)))
print(x, y, "=", hasil)

# is not sebagai komparasi objek
x = 5
y = 5

hasil = x is not y
print("nilai y : ", y, "id: ", hex(id(y)))
print("nilai x : ", x, "id: ", hex(id(x)))
print(y, x, "=", hasil)