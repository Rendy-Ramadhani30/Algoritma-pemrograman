# Program Total Belanja dan Diskon

print("===== INPUT BARANG =====")
jumlah_a = int(input("Jumlah Permen A       : "))
harga_a = float(input("Harga Satuan Permen A : Rp "))
jumlah_b = int(input("Jumlah Minuman B       : "))
harga_b = float(input("Harga Satuan Minuman B : Rp "))

total_a = jumlah_a * harga_a
total_b = jumlah_b * harga_b
total_belanja = total_a + total_b

if total_belanja >= 100000:
    diskon = total_belanja * 0.10
else:
    diskon = 0

total_bayar = total_belanja - diskon

print("\n===== HASIL PERHITUNGAN =====")
print(f"{'Nama Barang':<12}{'Jumlah':>8}{'Harga':>14}{'Total':>14}")
print(f"{'Permen A':<12}{jumlah_a:>8}{harga_a:>14,.0f}{total_a:>14,.0f}")
print(f"{'Minuman B':<12}{jumlah_b:>8}{harga_b:>14,.0f}{total_b:>14,.0f}")
print("-" * 48)
print(f"Total Belanja : Rp {total_belanja:,.0f}")
print(f"Diskon        : Rp {diskon:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")

bayar = float(input("\nMasukkan jumlah pembayaran: Rp "))

if bayar < total_bayar:
    print(f"Uang kurang   : Rp {total_bayar - bayar:,.0f}")
else:
    kembalian = bayar - total_bayar
    print(f"Pembayaran    : Rp {bayar:,.0f}")
    print(f"Kembalian     : Rp {kembalian:,.0f}")
    