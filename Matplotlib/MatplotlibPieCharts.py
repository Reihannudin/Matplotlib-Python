'''
Matplotlib Pie Charts

Membuat Diagram Lingkaran
Dengan Pyplot, Anda dapat menggunakan pie() fungsi untuk menggambar 
diagram lingkaran:
'''
'Diagram lingkaran sederhana:'
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

'''
Seperti yang Anda lihat, diagram lingkaran menggambar satu bagian (disebut irisan) 
untuk setiap nilai dalam larik (dalam hal ini [35, 25, 25, 15]).

Secara default, plot irisan pertama dimulai dari sumbu x dan bergerak berlawanan 
arah jarum jam :
'''

'''
Catatan: Ukuran setiap irisan ditentukan dengan membandingkan nilai dengan semua 
nilai lainnya, dengan menggunakan rumus ini:

Nilai dibagi dengan jumlah semua nilai: x/sum(x)
'''

'''
Labels
Tambahkan label ke diagram lingkaran dengan labelparameter.

The label parameter harus array dengan satu label untuk setiap wedge:
'''

'Diagram lingkaran sederhana:'
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

'''
Start Angle
Seperti yang disebutkan, sudut awal default adalah pada sumbu x, 
tetapi Anda dapat mengubah sudut awal dengan menentukan startangle parameter.

The startangle parameter didefinisikan dengan sudut dalam derajat, sudut default adalah 0:
'''

'Mulai irisan pertama pada 90 derajat:'
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 


'''
Explode
Mungkin Anda ingin salah satu wedges menonjol? The explode parameter memungkinkan Anda untuk melakukan itu.

The explode parameter, jika ditentukan, dan tidak None, harus array dengan satu nilai untuk setiap wedge.

Setiap nilai menunjukkan seberapa jauh dari pusat setiap irisan ditampilkan:
'''

'Tarik irisan "Apel" 0,2 dari tengah pai:'
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

'''
Shadow
Tambahkan bayangan ke diagram lingkaran dengan mengatur shadowsparameter ke True:
'''
'Tambahkan bayangan:'
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

'''
warna
Anda dapat mengatur warna setiap irisan dengan colorsparameter.

The colorsparameter, bila ditentukan, harus array dengan satu nilai untuk setiap wedge:
'''
'Tentukan warna baru untuk setiap irisan:'

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

'''
Anda dapat menggunakan nilai warna Heksadesimal , 
salah satu dari 140 nama warna yang didukung , atau salah satu pintasan berikut:

'r'- Merah
'g'- Hijau
'b'- Biru
'c'- Cyan
'm'- Magenta
'y'- Kuning
'k'- Hitam
'w'- Putih
'''

'''
Legenda
Untuk menambahkan daftar penjelasan untuk setiap irisan, gunakan legend() fungsi:
'''
'Tambahkan legenda:'
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

'''
Legenda Dengan Header
Untuk menambahkan header ke legenda, tambahkan titleparameter ke legend fungsi.
'''
'Tambahkan legenda dengan tajuk:'
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()