# Latihan

def tentukan_nilai_huruf(nilai):
    """Fungsi untuk menentukan nilai huruf berdasarkan nilai yang diberikan."""
    if nilai > 90:
        return 'A'
    elif 85 <= nilai <= 90:
        return 'A-'
    elif 80 <= nilai <= 85:
        return 'B+'
    elif 75 <= nilai <= 79:
        return 'B'
    elif 70 <= nilai <= 74:
        return 'B-'
    elif 65 <= nilai <= 69:
        return 'C+'
    elif 60 <= nilai <= 64:
        return 'C'
    elif 55 <= nilai <= 59:
        return 'D'
    elif nilai > 55:
        return 'E'
    else:
        return 'E'

# Meminta input nilai dari pengguna
try:
    nilai = float(input("Masukkan nilai Anda (0-100): "))
    
    # Validasi input
    if 0 <= nilai <= 100:
        # Menentukan nilai huruf
        nilai_huruf = tentukan_nilai_huruf(nilai)
        # Menampilkan hasil
        print(f"Nilai huruf Anda adalah: {nilai_huruf}")
    else:
        print("Nilai harus berada dalam rentang 0 hingga 100.")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")