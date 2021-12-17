'''
Memplot titik x dan y

The plot() Fungsi digunakan untuk menggambar poin 
(penanda) dalam sebuah diagram.

Secara default, plot() fungsi menarik garis dari titik ke titik.

Fungsi mengambil parameter untuk menentukan titik dalam diagram.

Parameter 1 adalah array yang berisi titik-titik pada sumbu x .

Parameter 2 adalah array yang berisi titik-titik pada sumbu y .

Jika kita perlu memplot garis dari (1, 3) ke (8, 10), 
kita harus melewatkan dua array [1, 8] dan [3, 10] ke fungsi plot.
'''

'Gambarlah garis dalam diagram dari posisi (1, 3) ke posisi (8, 10):'
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

'''
The x-axis adalah sumbu horisontal.

The y-axis adalah sumbu vertikal.
'''

'''
Plotting Tanpa Garis

Untuk memplot penanda saja, Anda dapat menggunakan parameter notasi string pintasan 'o', 
yang berarti 'berdering'.
'''

'Gambar dua titik dalam diagram, satu di posisi (1, 3) dan satu di posisi (8, 10):'
xpoints = np.array([1,8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

'Anda akan mempelajari lebih lanjut tentang penanda di bab berikutnya.'

'''
Beberapa Poin

Anda dapat memplot titik sebanyak yang Anda suka, pastikan Anda memiliki jumlah titik 
yang sama di kedua sumbu.
'''

'Gambarlah garis dalam diagram dari posisi (1, 3) ke (2, 8) lalu ke (6, 1) dan akhirnya ke posisi (8, 10):'
xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints)
plt.show()


'''
Poin X Default

Jika kita tidak menentukan titik pada sumbu x, mereka akan mendapatkan nilai default 0, 1, 2, 3, 
(dst. tergantung pada panjang titik y.

Jadi, jika kita mengambil contoh yang sama seperti di atas, dan mengabaikan titik-x, 
diagramnya akan terlihat seperti ini:
'''

'Merencanakan tanpa titik-x:'
ypoints = np.array([3,8,1,10,5,7])

plt.plot(ypoints)
plt.show()

'Titik -x pada contoh di atas adalah [0, 1, 2, 3, 4, 5].'

xpoints = np.array([0, 1,2,3,4,5])
plt.plot(xpoints, ypoints)
plt.show()
