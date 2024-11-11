# Definisi data film tanpa dictionary atau array
film_1_id = 1
film_1_judul = "Mahabrata"
film_1_kategori = "Semua Umur"

film_2_id = 2
film_2_judul = "Upin"
film_2_kategori = "13+"

film_3_id = 3
film_3_judul = "Naruto"
film_3_kategori = "18+"

# Menampilkan daftar film yang tersedia
print("Daftar Film:")
print(f"KODE: {film_1_id}, Title: \"{film_1_judul}\", Kategori: {film_1_kategori}")
print(f"KODE: {film_2_id}, Title: \"{film_2_judul}\", Kategori: {film_2_kategori}")
print(f"KODE: {film_3_id}, Title: \"{film_3_judul}\", Kategori: {film_3_kategori}")

# Mengambil input dari pengguna
username = input("Masukkan Nama Anda: ")
user_age = int(input("Masukkan usia Anda: "))
user_code = int(input("Masukkan kode film yang ingin diakses: "))

# Menentukan akses berdasarkan usia dan kode film menggunakan and, or, not
if user_code == film_1_id and (user_age >= 0 or not user_age < 0):
    akses_status = f'Akses Diberikan ke film "{film_1_judul}"'
elif user_code == film_2_id and user_age >= 13:
    akses_status = f'Akses Diberikan ke film "{film_2_judul}"'
elif user_code == film_3_id and user_age >= 18:
    akses_status = f'Akses Diberikan ke film "{film_3_judul}"'
else:
    akses_status = "Akses Ditolak atau Kode Film Tidak Valid"

# Menampilkan hasil akses
print(f"{username}, {akses_status}")
