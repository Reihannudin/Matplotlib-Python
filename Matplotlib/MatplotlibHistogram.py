''''
Histogram
Histogram adalah grafik yang menunjukkan distribusi frekuensi .

Ini adalah grafik yang menunjukkan jumlah pengamatan dalam 
setiap interval yang diberikan.

Contoh: Katakanlah Anda meminta tinggi 250 orang, Anda mungkin 
akan mendapatkan histogram seperti ini:
'''

'''
Anda dapat membaca dari histogram bahwa ada kira-kira:

2 orang dari 140 hingga 145cm
5 orang dari 145 hingga 150cm
15 orang dari 151 hingga 156cm
31 orang dari 157 hingga 162cm
46 orang dari 163 hingga 168cm
53 orang dari 168 hingga 173cm
45 orang dari 173 hingga 178cm
28 orang dari 179 hingga 184cm
21 orang dari 185 hingga 190cm
4 orang dari 190 hingga 195cm
'''

'''
Buat Histogram
Di Matplotlib, kami menggunakan hist() fungsi untuk membuat histogram.

The hist()fungsi akan menggunakan array nomor untuk membuat histogram, 
array dikirim ke fungsi sebagai argumen.

Untuk mempermudah, kami menggunakan NumPy untuk menghasilkan array dengan 
250 nilai secara acak, di mana nilai akan terkonsentrasi di sekitar 170, 
dan standar deviasinya adalah 10. Pelajari lebih lanjut tentang Distribusi 
Data Normal di Tutorial Pembelajaran Mesin kami .
'''

'Distribusi Data Normal oleh NumPy:'
import numpy as np

x = np.random.normal(170, 10, 250)

print(x)

'The hist() Fungsi akan membaca array dan menghasilkan histogram:'

'Histogram sederhana:'
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

