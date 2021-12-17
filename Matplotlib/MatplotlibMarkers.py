'''
Markers

Anda dapat menggunakan argumen kata kunci marker untuk 
menekankan setiap poin dengan penanda tertentu:
'''

'Tandai setiap titik dengan lingkaran:'
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, marker = 'o')
plt.show()

'Tandai setiap titik dengan bintang:'
plt.plot(ypoints, marker = '*')
plt.show()


'''
Referensi Penanda
Anda dapat memilih salah satu dari penanda ini:

Marker	Description
'o'	    Circle	
'*'	    Star	
'.'	    Point	
','	    Pixel	
'x'	    X	
'X'	    X (filled)	
'+'	    Plus	
'P'	    Plus (filled)	
's'	    Square	
'D'	    Diamond	
'd'	    Diamond (thin)	
'p'	    Pentagon	
'H'	    Hexagon	
'h'	    Hexagon	
'v'	    Triangle Down	
'^'	    Triangle Up	
'<'	    Triangle Left	
'>'	    Triangle Right	
'1'	    Tri Down	
'2'	    Tri Up	
'3'	    Tri Left	
'4'	    Tri Right	
'|'	    Vline	
'_'	    Hline	
'''

'''
Format String fmt
Anda juga dapat menggunakan parameter notasi string 
pintasan untuk menentukan penanda.

Parameter ini juga disebut fmt, dan ditulis dengan sintaks ini:
marker|line|color
'''

'Tandai setiap titik dengan lingkaran:'
plt.plot(ypoints, 'o:r')
plt.show()

'''
Nilai penanda bisa apa saja dari Referensi Penanda di atas.

Nilai garis dapat berupa salah satu dari berikut ini:
'''

'Referensi Garis'
'''
Line Syntax      Description
    '-'	          Solid line	
    ':'	          Dotted line	
    '--'	      Dashed line	
    '-.'	      Dashed/dotted line
'''
'''
Catatan: Jika Anda meninggalkan nilai baris di parameter fmt, 
tidak ada baris yang akan diplot.
'''

'Nilai warna pendek dapat berupa salah satu dari berikut ini:'
'''
Referensi Warna
Color Syntax	Description
    'r'	            Red	
    'g'	            Green	
    'b'	            Blue	
    'c'	            Cyan	
    'm'	            Magenta	
    'y'	            Yellow	
    'k'	            Black	
    'w'	            White
'''
'''
Ukuran penanda

Anda dapat menggunakan argumen kata kunci markersizeatau versi 
yang lebih pendek, msuntuk mengatur ukuran penanda:
'''

'Atur ukuran spidol menjadi 20:'

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

'''
Warna Penanda

Anda dapat menggunakan argumen kata kunci markeredgecolor atau 
yang lebih pendek mecuntuk mengatur warna tepi penanda:
'''
'Atur warna EDGE menjadi merah:'
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

'''
Anda dapat menggunakan argumen kata kunci markerfacecolor atau 
yang lebih pendek mfc untuk mengatur warna di dalam tepi penanda:
'''
'Atur warna WAJAH menjadi merah:'
plt.plot(ypoints, marker = 'o', ms = 20, mfc= 'r')
plt.show()

'Gunakan baik yang mec dan mfc argumen untuk warna seluruh penanda:'

'Atur warna tepi dan wajah menjadi merah:'
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

'Anda juga dapat menggunakan nilai warna heksadesimal :'
'Tandai setiap titik dengan warna hijau yang indah:'
plt.plot(ypoints, marker = 'o', ms = 20 , mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

'Atau salah satu dari 140 nama warna yang didukung .'
'Tandai setiap titik dengan warna bernama "hotpink":'
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()