import numpy as np
import matplotlib.pyplot as plt
from math import e #untuk memanggil bilangan eksponen natural (e)

#mendefinisikan fungsi 
def f(x):
    return e**x-5*x**2

#sesi input nilai awal yang dikonversi ke pecahan
x0 = float(input('x0: '))
x1 = float(input('x1: '))
eps = float(input('epsilon: '))

#metode bagi dua
def bisection(x0,x1,eps):
    step = 1
    print('\n\n*** --Metode Bagi Dua-- ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iterasi-%d,x2 = %0.6f dan f(x2) = %0.6f dan f(x2)' % (step,x2,f(x2)))
        if f(x0) * f(x2)<0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition =  abs(f(x2))>eps
    print('\n Akar Persamaan Tersebut : %0.8f' % x2)

#Menggambar Fungsi 
rr= np.linspace(0,2,100 )#Masukan nilai tebakan awal
plt.plot(rr, f(rr))
plt.show()
plt.savefig('fungsi.png') #untuk menyimpan gambar fungsi

#Pengecekan nilai awal
if  f(x0) * f(x1) >0.0:
    print('Nilai yang Diprediksi tidak mengurung akar')
    print('Silahkan mecoba ulang prediksi nilai baru')
else:
    bisection(x0,x1,eps)