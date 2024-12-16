# Program untuk menghitung jumlah kata dalam sebuah kalimat

# Meminta pengguna memasukkan sebuah kalimat
sentence = input("Masukkan sebuah kalimat: ")

# Menghitung jumlah kata
# Split digunakan untuk memisahkan kalimat menjadi daftar kata berdasarkan spasi
words = sentence.split()

# Menghitung panjang daftar kata
word_count = len(words)

# Menampilkan jumlah kata kepada pengguna
print(f"Jumlah kata dalam kalimat tersebut adalah: {word_count}")
