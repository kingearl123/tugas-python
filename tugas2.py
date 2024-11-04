# Data film dengan kategori umur
film_semua_umur = (1, "Mahabrata", "Semua Umur")
film_remaja = (2, "Upin", "13+")
film_dewasa = (3, "Naruto", "18+")

# Menampilkan daftar film yang tersedia
print("Daftar Film:")
print(f"ID: {film_semua_umur[0]}, Title: \"{film_semua_umur[1]}\", Kategori: {film_semua_umur[2]}")
print(f"ID: {film_remaja[0]}, Title: \"{film_remaja[1]}\", Kategori: {film_remaja[2]}")
print(f"ID: {film_dewasa[0]}, Title: \"{film_dewasa[1]}\", Kategori: {film_dewasa[2]}")

# Mengambil input dari pengguna
username = input("Masukkan Nama Anda: ")
user_age = int(input("Masukkan usia Anda: "))
user_code = int(input("Masukkan kode film yang ingin diakses: "))

# Menentukan akses berdasarkan usia dan kode film dengan and, or, not
if user_code == film_semua_umur[0] and (user_age >= 0 or not user_age < 0):
    akses_status = "Akses Diberikan"
    selected_film = film_semua_umur[1]
elif user_code == film_remaja[0] and user_age >= 13:
    akses_status = "Akses Diberikan"
    selected_film = film_remaja[1]
elif user_code == film_dewasa[0] and user_age >= 18:
    akses_status = "Akses Diberikan"
    selected_film = film_dewasa[1]
else:
    akses_status = "Akses Ditolak atau Kode Film Tidak Valid"
    selected_film = None


# Menampilkan hasil akses
if selected_film:
    print(f'{username}, Anda mengakses film "{selected_film}" - {akses_status}')
else:
    print("Film tidak ditemukan atau akses ditolak.")
