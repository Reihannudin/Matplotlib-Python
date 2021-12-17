'Matplotlib Menambahkan Garis Grid'
'''
Tambahkan Garis Grid ke Plot
Dengan Pyplot, Anda dapat menggunakan grid()
fungsi untuk menambahkan garis kisi ke plot.
'''
'Tambahkan garis kisi ke plot'
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

'''
Tentukan Garis Grid Yang Akan Ditampilkan

Anda dapat menggunakan axisparameter dalam grid() fungsi untuk menentukan garis 
kisi mana yang akan ditampilkan.

Nilai hukum adalah: 'x', 'y', dan 'keduanya'. Nilai default adalah 'keduanya'.
'''
'Tampilkan hanya garis kisi untuk sumbu x:'
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

'Tampilkan hanya garis kisi untuk sumbu y:'

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()


''''
Atur Properti Garis untuk Grid

Anda juga dapat mengatur properti garis dari grid, seperti ini: 
grid(color = ' color ', linestyle = ' linestyle ', linewidth = number ).
'''
'Setel properti garis kisi:'
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()