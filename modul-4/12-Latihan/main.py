# input dari pengguna
tinggi = float(input("masukkan tinggi badan : "))
berat = float(input("masukkan berat badan : "))

tinggi = tinggi / 100
bmi = berat / (tinggi ** 2 )

print(f"skor BMI adalah : {bmi:.1f}")