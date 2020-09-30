import numpy as np
import matplotlib.pyplot as plt


numpyDizisi1=np.linspace(0,20,10)
numpyDizisi2=np.linspace(0,20,10)
# Figürün boyutunu ayarlıyoruz
yeniFigur=plt.figure(figsize=(3,3))
# Figürün görüntü kalitesini arttırıyoruz
yeniFigur=plt.figure(dpi=150)

yeniEksen=yeniFigur.add_axes([0.1,0.1,0.9,0.9])
yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 2 ,label="Numpy Dizisi ** 2")
yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 3 ,label="Numpy Dizisi ** 3")
# Lokasyon veriyoruz label isimlerine
yeniEksen.legend(loc=2)
# Dpi değerini burdanda verip png olarak kayıt edebiliriz
yeniFigur.savefig("benimfigur.png",dpi=250)


# VERİ GÖRSELLEŞİTME İLERİ SEVİYE
yeniNumpy=np.linspace(0,10,8)
yeniNumpyDizisi=yeniNumpy ** 3
(benimFigur,benimEksen)=plt.subplots()
# Saydamlık katabilriiz Color kısmına renk kodları ile farklı renkler verebiliriz
benimEksen.plot(numpyDizisi1,numpyDizisi2,color="red",alpha=0.3)
benimEksen.plot(numpyDizisi2,numpyDizisi1,color="blue")

(yeniFigur,yeniEksen)=plt.subplots()
# Çizgi kalınlığını arttırıyoruz
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 2, color="blue", linewidth=1.0)
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 3, color="orange", linewidth=1.0 )
# Çizgi şeklini değiştiriyor
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 4, color="green", linestyle="-.")
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 5, color="green", linestyle=":")
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 6, color="green", linestyle="--")
# Marker vererek çizgilerin içlerini doldurabilriz.
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 7, color="black", linestyle="--",marker="o",markersize=8,markerfacecolor="red")
yeniEksen.plot(numpyDizisi1,numpyDizisi1 + 8, color="black", linestyle="--",marker="+",markersize=4)


# FARKLI GRAFİK ÇEŞİTLERİ
# SCATTER
plt.scatter(numpyDizisi1,numpyDizisi2)

# HISTOGRAM
yeniDizi=np.random.randint(0,100,50)
print(yeniDizi)
plt.hist(yeniDizi)

# BOXPLOT
# Standart sapma için kullanılır
plt.boxplot(yeniDizi)

plt.show()
