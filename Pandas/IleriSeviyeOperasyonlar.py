import numpy as np
import pandas as pd
maasSozlugu={
    "Departman":["Yazılım","Satış","Pazarlama","Finans",],
        "Çalışan Ismi":["Ahmet","Yusuf","Mehmet","Burak",],
        "Maas":[1000,1500,2000,3000]
}
maasDataFrame=pd.DataFrame(maasSozlugu)
print(maasDataFrame)

print("-"*50)
# Departman isimlerini gösteriyor
print(maasDataFrame["Departman"].unique())
# Kaç tane departman olduğunu gösterir
print(maasDataFrame["Departman"].nunique())
# Değer sayılarını gösterir
print(maasDataFrame["Departman"].value_counts())
# Bir departmana işlem yapmak için
def brunette(maas):
    return maas * 0.66
print(maasDataFrame["Maas"].apply(brunette))
# Boş değerleri gösterir
print(maasDataFrame.isnull())

yeniVeri={
    "Karakter Sınıfı":["South Park","South Park","Simpson","Simpson","Simpson"],
    "Karakter Ismi":["Cartman","Kenny","Homer","Bart","Bart"],
    "Karakter Yas":[9,10,50,20,10]
}
karakterDf=pd.DataFrame(yeniVeri)
print(karakterDf)
print(karakterDf.pivot_table(values="Karakter Yas",index=["Karakter Sınıfı","Karakter Ismi"]))

# Önemli Notlar

# read_csv = Okumak içindir         karakterDf.read_excel("KarakterDf.xlxs")
# to_csv = Yazmak içindir           karakterDf.to_excel("yeniKarakterDf.xlxs")
