# Program untuk menemukan elemen terbesar dan terkecil dalam sebuah list

# Langkah 1: Membuat list kosong untuk menyimpan angka
numbers = []

# Langkah 2: Meminta pengguna memasukkan 5 angka
print("Masukkan 5 angka:")
for i in range(5):
    while True:  # Loop untuk validasi input
        num = input(f"Angka ke-{i + 1}: ")
        if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):  # Validasi angka termasuk negatif
            numbers.append(int(num))  # Menambahkan angka ke list
            break
        else:
            print("Masukkan angka yang valid.")

# Langkah 3: Menemukan elemen terbesar dan terkecil dalam list
max_number = max(numbers)  # Fungsi max untuk menemukan angka terbesar
min_number = min(numbers)  # Fungsi min untuk menemukan angka terkecil

# Langkah 4: Menampilkan hasil
print("\nAngka yang Anda masukkan:", numbers)
print(f"Elemen terbesar dalam list: {max_number}")
print(f"Elemen terkecil dalam list: {min_number}")
