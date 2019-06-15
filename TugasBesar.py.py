import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#Membuat data
#data tersebut dimport melalui excel
data = pd.read_excel('DataNTB.xlsx')
Kabupaten=data.Kabupaten
Pria=data.Laki_Laki
Perempuan=data.Perempuan
Total=data.Total

#Membuat plot menggunakan Bar
dataPlot1 = plt.bar(data.Kabupaten,data.Laki_Laki)
dataPlot2 = plt.bar(data.Kabupaten,data.Perempuan)
dataPlot3 = plt.bar(data.Kabupaten,data.Total)

# Mengatur tampilan plot 
plt.setp(dataPlot1,color ='r', width=0.45)
plt.setp(dataPlot2,color ='b', width=0.3)
plt.setp(dataPlot3,color ='y', width=0.15)

#Membuat Tittle, label , dan Legend serta opsi tambahan

judul = 'Grafik Penduduk NTB\n'
tahun = 'Tahun 2010'
plt.title(judul + tahun)
plt.xticks(rotation=15)
plt.legend(['Laki_Laki','Perempuan','Total'])
plt.xlabel('Kecamatan')
plt.ylabel('Penduduk')

#Menampilkan plot

plt.show()
