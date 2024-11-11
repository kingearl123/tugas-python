# Definisi data film
film_semua_umur = {"id": 1, "judul": "Mahabrata", "kategori": "Semua Umur"}
film_remaja = {"id": 2, "judul": "Upin", "kategori": "13+"}
film_dewasa = {"id": 3, "judul": "Naruto", "kategori": "18+"}

# Menampilkan daftar film yang tersedia
print("Daftar Film:")
print(f"KODE: {film_semua_umur['id']}, Title: \"{film_semua_umur['judul']}\", Kategori: {film_semua_umur['kategori']}")
print(f"KODE: {film_remaja['id']}, Title: \"{film_remaja['judul']}\", Kategori: {film_remaja['kategori']}")
print(f"KODE: {film_dewasa['id']}, Title: \"{film_dewasa['judul']}\", Kategori: {film_dewasa['kategori']}")

# Mengambil input dari pengguna
username = input("Masukkan Nama Anda: ")
user_age = int(input("Masukkan usia Anda: "))
user_code = int(input("Masukkan kode film yang ingin diakses: "))

# Menentukan akses berdasarkan usia dan kode film menggunakan and, or, not
if user_code == film_semua_umur["id"] and (user_age >= 0 or not user_age < 0):
    akses_status = f'Akses Diberikan ke film "{film_semua_umur["judul"]}"'
elif user_code == film_remaja["id"] and user_age >= 13:
    akses_status = f'Akses Diberikan ke film "{film_remaja["judul"]}"'
elif user_code == film_dewasa["id"] and user_age >= 18:
    akses_status = f'Akses Diberikan ke film "{film_dewasa["judul"]}"'
else:
    akses_status = "Akses Ditolak atau Kode Film Tidak Valid"

# Menampilkan hasil akses
print(f"{username}, {akses_status}")
