'''
Labels and title Matplotlib

Buat Label untuk Plot
Dengan Pyplot, Anda dapat menggunakan fungsi xlabel()
and ylabel() untuk menyetel label untuk sumbu x dan y.

'''
'Tambahkan label ke sumbu x dan y:'
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

'''
Buat Judul untuk Plot
Dengan Pyplot, Anda dapat menggunakan title() fungsi untuk menetapkan judul plot.
'''
'Tambahkan judul plot dan label untuk sumbu x dan y:'
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()


''''
Atur Properti Font untuk Judul dan Label
Anda dapat menggunakan fontdict parameter di xlabel(), ylabel(), 
dan title() untuk mengatur properti font untuk judul dan label.
'''
'Atur properti font untuk judul dan label:'

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x,y)
plt.show()

''''
Posisikan Judul
Anda dapat menggunakan locparameter in title() untuk memposisikan judul.

Nilai hukumnya adalah: 'left', 'right', dan 'center'. Nilai default adalah 'center'.
'''

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()