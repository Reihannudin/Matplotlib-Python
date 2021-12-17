'Matplotlib Pyplot'
'''
plot
Sebagian besar utilitas Matplotlib terletak di bawah pyplot submodule, 
dan biasanya diimpor dengan pltalias:
'''
import matplotlib.pyplot as plt

'Sekarang paket Pyplot dapat disebut sebagai plt.'

'Gambar garis dalam diagram dari posisi (0,0) ke posisi (6,250):'
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()