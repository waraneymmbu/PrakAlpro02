def hitung_keuangan(gaji_per_jam, jam_per_minggu):
    minggu_kerja = 5 
    total_pendapatan = gaji_per_jam * jam_per_minggu * minggu_kerja
    pajak = 0.14 * total_pendapatan
    pendapatan_bersih = total_pendapatan - pajak
    
    baju_aksesoris = 0.10 * pendapatan_bersih
    alat_tulis = 0.01 * pendapatan_bersih
    sisa_setelah_belanja = pendapatan_bersih - (baju_aksesoris + alat_tulis)
    sedekah = 0.25 * sisa_setelah_belanja
    
    untuk_anak_yatim = 0.30 * sedekah
    untuk_kaum_dhuafa = 0.70 * sedekah
    
    return total_pendapatan, pendapatan_bersih, baju_aksesoris, alat_tulis, sedekah, untuk_anak_yatim, untuk_kaum_dhuafa

# Input
gaji_per_jam = float(input("Masukkan gaji per jam: "))
jam_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))

# Hitung keuangan
hasil = hitung_keuangan(gaji_per_jam, jam_per_minggu)

# Output
print(f"Pendapatan sebelum pajak: Rp {hasil[0]:,.2f}")
print(f"Pendapatan setelah pajak: Rp {hasil[1]:,.2f}")
print(f"Uang untuk baju dan aksesoris: Rp {hasil[2]:,.2f}")
print(f"Uang untuk alat tulis: Rp {hasil[3]:,.2f}")
print(f"Total sedekah: Rp {hasil[4]:,.2f}")
print(f"Jumlah untuk anak yatim: Rp {hasil[5]:,.2f}")
print(f"Jumlah untuk kaum dhuafa: Rp {hasil[6]:,.2f}")
