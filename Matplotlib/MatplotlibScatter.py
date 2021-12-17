'''
Matplotlib Scatter

Membuat Scatter Plot
Dengan Pyplot, Anda dapat menggunakan scatter() fungsi untuk menggambar plot pencar.

The scatter()plot fungsi satu dot untuk setiap observasi. Dibutuhkan dua larik dengan 
panjang yang sama, satu untuk nilai sumbu x, dan satu untuk nilai pada sumbu y:
'''
'Sebuah plot pencar sederhana:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

'''
Pengamatan pada contoh di atas adalah hasil dari 13 mobil yang lewat.

Sumbu X menunjukkan berapa umur mobil.

Sumbu Y menunjukkan kecepatan mobil saat melintas.

Apakah ada hubungan antara pengamatan?

Tampaknya semakin baru mobil, semakin cepat dikendarai, 
tetapi itu bisa jadi kebetulan, lagipula kami hanya mendaftarkan 13 mobil.

'''

'''
Bandingkan Plot
Dalam contoh di atas, tampaknya ada hubungan antara kecepatan dan usia, 
tetapi bagaimana jika kita juga memplot pengamatan dari hari lain? 
Akankah plot pencar memberi tahu kita sesuatu yang lain?
'''
'Gambarlah dua plot pada gambar yang sama:'
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

'''
Catatan: Kedua plot diplot dengan dua warna berbeda, secara default 
biru dan oranye, Anda akan mempelajari cara mengubah warna nanti di 
bab ini.
'''

'''
Dengan membandingkan kedua plot, saya pikir aman untuk mengatakan 
bahwa keduanya memberi kita kesimpulan yang sama: semakin baru mobil, 
semakin cepat ia melaju.
'''

'''
warna
Anda dapat mengatur warna Anda sendiri untuk setiap plot pencar dengan 
argumen color atau c:
'''
'Atur warna spidol Anda sendiri:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

'''
Warnai Setiap Titik
Anda bahkan dapat mengatur warna tertentu untuk setiap titik dengan 
menggunakan larik warna sebagai nilai untuk cargumen:
'''
'Catatan: Anda tidak dapat menggunakan colorargumen untuk ini, hanya c argumen'

'Atur warna spidol Anda sendiri:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple",
                  "beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()


'''
Peta Warna
Modul Matplotlib memiliki sejumlah peta warna yang tersedia.

Peta warna seperti daftar warna, di mana setiap warna memiliki nilai yang berkisar 
dari 0 hingga 100.

Berikut adalah contoh peta warna:

Peta warna ini disebut 'viridis' dan seperti yang Anda lihat berkisar dari 0,
yang merupakan warna ungu, dan hingga 100, 
yang merupakan warna kuning.
'''

'''
Cara Menggunakan ColorMap
Anda dapat menentukan peta warna dengan argumen kata kunci cmap dengan nilai peta warna, 
dalam hal ini 'viridis' yang merupakan salah satu peta warna bawaan yang tersedia di Matplotlib.

Selain itu, Anda harus membuat larik dengan nilai (dari 0 hingga 100), 
satu nilai untuk setiap titik dalam plot pencar:
'''

'Buat larik warna, dan tentukan peta warna di plot sebar:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

'Anda dapat menyertakan peta warna dalam gambar dengan menyertakan plt.colorbar() pernyataan:'

'Sertakan peta warna yang sebenarnya:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

'''
Tersedia ColorMaps
Anda dapat memilih salah satu dari peta warna bawaan:

Name		          	Reverse	
Accent		          	Accent_r	
Blues		          	Blues_r	
BrBG		          	BrBG_r	
BuGn		          	BuGn_r	
BuPu		          	BuPu_r	
CMRmap		          	CMRmap_r	
Dark2		          	Dark2_r	
GnBu		          	GnBu_r	
Greens		          	Greens_r	
Greys		          	Greys_r	
OrRd		          	OrRd_r	
Oranges		          	Oranges_r	
PRGn		          	PRGn_r	
Paired		          	Paired_r	
Pastel1		          	Pastel1_r	
Pastel2		          	Pastel2_r	
PiYG		          	PiYG_r	
PuBu		          	PuBu_r	
PuBuGn		          	PuBuGn_r	
PuOr		          	PuOr_r	
PuRd		          	PuRd_r	
Purples		          	Purples_r	
RdBu		          	RdBu_r	
RdGy		          	RdGy_r	
RdPu		          	RdPu_r	
RdYlBu		          	RdYlBu_r	
RdYlGn		          	RdYlGn_r	
Reds		          	Reds_r	
Set1		          	Set1_r	
Set2		          	Set2_r	
Set3		          	Set3_r	
Spectral	         	Spectral_r	
Wistia		          	Wistia_r	
YlGn		          	YlGn_r	
YlGnBu		          	YlGnBu_r	
YlOrBr		          	YlOrBr_r	
YlOrRd		          	YlOrRd_r	
afmhot		          	afmhot_r	
autumn		          	autumn_r	
binary		          	binary_r	
bone		          	bone_r	
brg		 	            brg_r	
bwr		 	            bwr_r	
cividis		          	cividis_r	
cool		          	cool_r	
coolwarm	         	coolwarm_r	
copper		          	copper_r	
cubehelix	         	cubehelix_r	
flag		          	flag_r	
gist_earth	         	gist_earth_r	
gist_gray	         	gist_gray_r	
gist_heat	         	gist_heat_r	
gist_ncar	         	gist_ncar_r	
gist_rainbow          	gist_rainbow_r	
gist_stern	          	gist_stern_r	
gist_yarg	          	gist_yarg_r	
gnuplot		          	gnuplot_r	
gnuplot2	          	gnuplot2_r	
gray		          	gray_r	
hot		 	            hot_r	
hsv		 	            hsv_r	
inferno		          	inferno_r	
jet		 	            jet_r	
magma		          	magma_r	
nipy_spectral		 	nipy_spectral_r	
ocean		 	        ocean_r	
pink		 	        pink_r	
plasma		 	        plasma_r	
prism		 	        prism_r	
rainbow		 	        rainbow_r	
seismic		 	        seismic_r	
spring		 	        spring_r	
summer		 	        summer_r	
tab10		 	        tab10_r	
tab20		 	        tab20_r	
tab20b		 	        tab20b_r	
tab20c		 	        tab20c_r	
terrain		 	        terrain_r	
twilight		      	twilight_r	
twilight_shifted		twilight_shifted_r	
viridis		 	        viridis_r	
winter		 	        winter_r	
'''

'''
Ukuran
Anda dapat mengubah ukuran titik dengan sargumen.

Sama seperti warna, pastikan array untuk ukuran memiliki 
panjang yang sama dengan array untuk sumbu x dan y:
'''
'Atur ukuran Anda sendiri untuk spidol:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()


'''
Alfa
Anda dapat menyesuaikan transparansi titik-titik dengan alphaargumen.

Sama seperti warna, pastikan array untuk ukuran memiliki panjang yang 
sama dengan array untuk sumbu x dan y:
'''
'Atur ukuran Anda sendiri untuk spidol:'
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

'''
Gabungkan Ukuran Warna dan Alfa

Anda dapat menggabungkan peta warna dengan ukuran berbeda pada titik-titik. 
Ini paling baik divisualisasikan jika titik-titiknya transparan:
'''

'Buat array acak dengan 100 nilai untuk titik-x, titik-y, warna dan ukuran:'
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()
