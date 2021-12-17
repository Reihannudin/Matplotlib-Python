'''
Gaya garis

Anda dapat menggunakan argumen kata kunci linestyle, atau lebih pendek ls,
 untuk mengubah gaya garis yang diplot:
'''
'Gunakan garis putus putus:'
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

'Gunakan garis putus-putus:'
plt.plot(ypoints, ls = 'dashed')
plt.show()

'''
Sintaks lebih pendek
Gaya garis dapat ditulis dalam sintaks yang lebih pendek:

linestyledapat ditulis sebagai ls.

dotteddapat ditulis sebagai :.

dasheddapat ditulis sebagai --.
'''
'Sintaks yang lebih pendek:'

plt.plot(ypoints, ls = ':')
plt.show()

'''
Gaya Garis
Anda dapat memilih salah satu dari gaya ini:

Style	                 Or
'solid' (default)    	 '-'	
'dotted'	             ':'	
'dashed'	             '--'	
'dashdot'	             '-.'	
'None'     	           '' or ' '	
'''

'''
Warna garis
Anda dapat menggunakan argumen kata kunci color 
atau yang lebih pendek c untuk mengatur warna garis:
'''
'atur warna garus menjadi merah'
plt.plot(ypoints, color= 'r')
plt.show()

'Anda juga dapat menggunakan nilai warna heksadesimal :'

'Plot dengan garis hijau yang indah:'
plt.plot(ypoints, c = '#4CAF50')
plt.show()

'Atau salah satu dari 140 nama warna yang didukung .'

'Plot dengan warna bernama "hotpink":'
plt.plot(ypoints, c = 'hotpink')
plt.show()


'''
Lebar Garis
Anda dapat menggunakan argumen kata kunci linewidth 
atau yang lebih pendek lwuntuk mengubah lebar garis.

Nilainya adalah angka mengambang, dalam poin:
'''
'Plot dengan garis lebar 20.5pt:'
plt.plot(ypoints, linewidth = '20.5')
plt.show()

'''
Beberapa Baris

Anda dapat memplot baris sebanyak yang Anda suka hanya 
dengan menambahkan lebih banyak plt.plot() fungsi:
'''
'Gambar dua garis dengan menentukan plt.plot() fungsi untuk setiap garis:'
y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)

plt.show()

'''
Anda juga dapat memplot banyak garis dengan menambahkan titik untuk sumbu x dan y 
untuk setiap garis dalam plt.plot()fungsi yang sama .

(Pada contoh di atas kami hanya menentukan titik pada sumbu y, 
artinya titik pada sumbu x mendapatkan nilai default (0, 1, 2, 3).)

Nilai x- dan y- berpasangan:
'''

'Gambar dua garis dengan menentukan nilai titik x dan y untuk kedua garis:'
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()