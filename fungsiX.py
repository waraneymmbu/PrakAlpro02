def fungsi(x):
    if x == 0:
        return "Tidak terdefinisi (pembagian oleh nol)"
    return (2 * x**3 + 2 * x + 15) / x

x = int(input("Masukkan nilai x (bilangan bulat): "))

hasil = fungsi(x)

print(f"Hasil dari f({x}) adalah: {hasil}")
