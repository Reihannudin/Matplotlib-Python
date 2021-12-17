'''
Membuat Bar

Dengan Pyplot, Anda dapat menggunakan bar() fungsi untuk menggambar grafik batang:
'''
'Gambar 4 batang:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

'''
The bar() Fungsi mengambil argumen yang menjelaskan tata letak bar.

Kategori dan nilainya diwakili oleh argumen pertama dan kedua sebagai array. 
'''
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)
plt.show()

'''
Batang Horisontal

Jika Anda ingin bilah ditampilkan secara horizontal, bukan vertikal, 
gunakan barh() fungsi:
'''
'Gambar 4 batang horizontal:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

'''
Warna Batang
The bar() and barh() mengambil argumen kata kunci color untuk mengatur warna bilah:
'''
'Gambar 4 batang merah:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

'''
Nama Warna
Anda dapat menggunakan salah satu dari 140 nama warna yang didukung .
'''
'Gambar 4 batang "hot pink":'
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

'''
Warna Hex
Atau Anda dapat menggunakan nilai warna Heksadesimal :
'''
'Gambar 4 batang dengan warna hijau yang indah:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()

'''
Lebar Batang
The bar() mengambil argumen kata kunci widthuntuk mengatur lebar dari bar:
'''
'Gambar 4 batang yang sangat tipis:'

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

'Nilai lebar default adalah 0,8'

'Catatan: Untuk bilah horizontal, gunakan height alih-alih width.'

''''
Tinggi Batang
The barh() mengambil argumen kata kunci height untuk mengatur ketinggian bar:
'''

'Gambar 4 batang yang sangat tipis:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()

'Nilai ketinggian default adalah 0,8'