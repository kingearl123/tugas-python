# Program Toko Online Sederhana

# Langkah 1: Menyimpan daftar barang dan harga dalam dictionary
items = {
    "Kaos": 50000,
    "Jaket": 150000,
    "Topi": 30000
}

# Langkah 2: Menampilkan daftar barang dan harga
print("Daftar Barang:")
for item, price in items.items():
    print(f"{item}: Rp{price:,}")

# Langkah 3: Meminta pengguna memilih barang
# Menggunakan dictionary untuk menyimpan pembelian
purchases = {}

while True:
    chosen_item = input("\nPilih barang (Kaos, Jaket, Topi) atau ketik 'selesai' untuk mengakhiri: ").lower()
    if chosen_item == 'selesai':  # Periksa apakah input adalah "selesai"
        break  # Menghentikan loop jika pengguna mengetik 'selesai'

    # Cari barang di dictionary secara case-insensitive
    matching_item = next((key for key in items if key.lower() == chosen_item.lower()), None)
    if not matching_item:
        print("Barang tidak tersedia. Silakan pilih barang yang tersedia.")
        continue  # Kembali ke awal loop jika barang tidak ditemukan

    # Langkah 4: Meminta pengguna memasukkan jumlah barang
    quantity_input = input(f"Masukkan jumlah {matching_item} yang ingin dibeli: ")
    if not quantity_input.isdigit():
        print("Jumlah harus berupa angka positif. Silakan coba lagi.")
        continue
    quantity = int(quantity_input)
    if quantity <= 0:
        print("Jumlah harus lebih dari nol. Silakan coba lagi.")
        continue

    # Menambahkan atau memperbarui pembelian di dictionary
    if matching_item in purchases:
        purchases[matching_item] += quantity
    else:
        purchases[matching_item] = quantity

# Langkah 5: Menghitung total harga barang yang dibeli
total_price = 0
for item, quantity in purchases.items():
    item_price = items[item]
    total_price += item_price * quantity

# Langkah 6: Mengecek dan memberikan diskon jika memenuhi syarat
if total_price > 200000:
    discount = 0.1 * total_price
    total_to_pay = total_price - discount
    print(f"\nDiskon 10% diterapkan! Diskon: Rp{discount:,}")
else:
    total_to_pay = total_price
    print("\nTidak ada diskon yang diterapkan.")

# Langkah 7: Menampilkan total harga dan total yang harus dibayar
print(f"\nTotal harga sebelum diskon: Rp{total_price:,}")
print(f"Total yang harus dibayar: Rp{total_to_pay:,}")

# Menampilkan detail pembelian
print("\nDetail pembelian:")
for item, quantity in purchases.items():
    print(f"{item} x{quantity}: Rp{items[item] * quantity:,}")

# Langkah 8: Menutup program dengan ucapan terima kasih
print("\nTerima kasih telah berbelanja!")
