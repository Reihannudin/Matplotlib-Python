''''
Tampilkan Banyak Plot

Dengan subplots() fungsi ini Anda dapat 
menggambar banyak plot dalam satu gambar
'''
'Menggambar 2 plot:'
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

'''
Subplot() Fungsi

The subplots()Fungsi mengambil tiga argumen yang menjelaskan tata letak gambar.

Tata letak diatur dalam baris dan kolom, yang diwakili oleh argumen pertama dan kedua .

Argumen ketiga mewakili indeks plot saat ini.
'''
plt.subplot(1, 2, 1)
#gambar tersebut memiliki 1 baris, 2 kolom, dan plot ini adalah plot pertama..

plt.subplot(1, 2, 2)
#gambar tersebut memiliki 1 baris, 2 kolom, dan plot ini adalah plot kedua.

''''
Jadi, jika kita menginginkan gambar dengan 2 baris dan 1 kolom 
(artinya kedua plot akan ditampilkan di atas satu sama lain, bukan berdampingan), 
kita dapat menulis sintaks seperti ini:
'''

'Gambar 2 plot di atas satu sama lain:'
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()

'''
Anda dapat menggambar plot sebanyak yang Anda suka pada satu gambar, 
cukup jelaskan jumlah baris, kolom, dan indeks plot.
'''
'Menggambar 6 plot:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()


''''
Judul
Anda dapat menambahkan judul ke setiap plot dengan title() fungsi:
'''
'2 kavling, dengan judul :'
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()


'''
Judul Super
Anda dapat menambahkan judul ke seluruh gambar dengan suptitle() fungsi:
'''
'Tambahkan judul untuk seluruh gambar:'
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()