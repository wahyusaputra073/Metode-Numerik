print("\n==========================================")
print("  METODE BAGI DUA")
print("  Nama  : Wahyu Harry Saputra Sembiring")
print("  NIM   : 2009106049")
print("  Kelas : Informatika A 2020")
print("==========================================\n")

import numpy as np
import matplotlib.pyplot as plt

pers = input("Masukkan persamaan fungsi x : ")
a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
e =  1e-5

def f(x):
    return eval(pers)

if f(a)*f(b)>0:
    print("Persamaan tidak memiliki akar")

else:
    print("n        a              c                  b              f(a)            f(c)                   f(b)")
    for i in range(10):
        c = (a + b) / 2
        print(i+1, "\t", format(a, ".5f"), "\t", format(c, ".5f"), "\t", format(b, ".5f"), "\t", format(f(a), ".5f"), "\t", format(f(c)), "\t       ", format(f(b), ".5f"))
        if abs(f(c))<e:
            break
        elif f(a)*f(c)<0:
            b=c
        else:
            a=c

    print("\nAkar persamaan adalah = ", a, " dan ", b)
    x = np.linspace(2.5, 2.6, 100)
    # plt.plot(x, f(x))
    # plt.grid()