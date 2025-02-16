def hitung_berat_badan(tinggi, bmi_diharapkan):
    berat_badan = bmi_diharapkan * (tinggi ** 2)
    return berat_badan

tinggi = float(input("Masukkan tinggi badan (m): "))
bmi_diharapkan = float(input("Masukkan BMI yang diharapkan: "))

berat_badan = hitung_berat_badan(tinggi, bmi_diharapkan)

print(f"Berat badan yang diperlukan untuk BMI {bmi_diharapkan} dengan tinggi {tinggi} m adalah {berat_badan:.2f} kg")
