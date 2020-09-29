import numpy as np
import matplotlib.pyplot as plt
yasListesi = [10,20,30,40,50,60,65,70,75,80]
kiloListesi = [20,60,80,85,86,87,70,90,95,90]
numpyYasListesi = np.array(yasListesi)
numpyKilolistesi = np.array(kiloListesi)
plt.plot(numpyYasListesi,numpyKilolistesi,"r")
plt.xlabel("YAS")
plt.ylabel("KILO")
plt.title("Kilonun Yaşa göre Değişimi")
# plt.show()

# Customize # Özelleştirme
numpyDizisi1=np.linspace(0,10,20)
print(numpyDizisi1)
numpyDizisi2=numpyDizisi1**3
print(numpyDizisi2)
plt.plot(numpyDizisi1,numpyDizisi2,"g+-")

plt.subplot(1,2,1)
plt.plot(numpyDizisi1,numpyDizisi2,"r*-")
plt.plot(1,2,2) # 1 sıra olacak 2 kolon olacak , şu an 2. grafiği çiziyoruz
plt.plot(numpyDizisi2,numpyDizisi1,"g--")


# Figure
benimfigure=plt.figure()
figureAxes=benimfigure.add_axes([0.1,0.1,0.8,0.8])
figureAxes.plot(numpyDizisi1,numpyDizisi2,"g")
figureAxes.set_xlabel("X ekseni Veri İsmi")
figureAxes.set_ylabel("Y ekseni veri İsmi")
figureAxes.set_title("Grafik Başlığı")
# plt.show()
"""
# Sublots
# Yeni Figure
figure2=plt.figure()
eksen1=figure2.add_axes([0.1,0.1,0.9,0.9])
eksen2=figure2.add_axes([0.3,0.3,0.3,0.3])

eksen1.plot(numpyDizisi1,numpyDizisi2,"g")
eksen1.set_title("Ana Grafik Başlığı")
eksen1.set_xlabel("X Ekseni")
eksen1.set_ylabel("Y Ekseni")

eksen2.plot(numpyDizisi1,numpyDizisi2,"b")
eksen2.set_xlabel("X Ekseni")
eksen2.set_ylabel("Y Ekseni")
eksen2.set_title("Küçük Grafik Başlığı")

benimEksen=plt.figure()
# benimEksen=benimEksen.plot(numpyDizisi1,numpyDizisi2,"b")
(benimFigure,benimEksen)=plt.subplots(nrows=1,ncols=2)


plt.show()


"""

