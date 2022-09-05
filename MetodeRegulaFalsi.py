print("\n==========================================")
print("  METODE REGULA-FALSI")
print("  Nama  : Wahyu Harry Saputra Sembiring")
print("  NIM   : 2009106049")
print("  Kelas : Informatika A 2020")
print("==========================================\n")

def f(x):
    return 2.71828183-5*x**2
a = int(input("Masukkan selang pertama : "))
b = int(input("Masukkan selang kedua : "))
n = int(input("Masukkan jumlah iterasi : "))
if f(a) * f(b) > 0:
    print("Kesalahan Regula-Falsi")
else:
    k=1
    while(k<=n):
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a) * f(c) < 0:
            b=c
        else:
            a=c
        print("Akar = ", c, "pada iterasi = ", k)
        k = k+1

# x**3-x-2