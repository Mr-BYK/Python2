import numpy as np
import pandas as pd

# Eksik Veriler
sozlukVerisi={"Istanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"Izmır":[35,33,32]}
havaDurumuDataFrame=pd.DataFrame(sozlukVerisi)
print(havaDurumuDataFrame)

print(havaDurumuDataFrame.dropna())
print(havaDurumuDataFrame.dropna(axis=1))

yeniVeriDataFrame={"Istanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"Izmır":[35,33,32],"Antalya":[35,np.nan,np.nan]}
yeniVeriDataFrame=pd.DataFrame(yeniVeriDataFrame)
print(yeniVeriDataFrame)

print(yeniVeriDataFrame.dropna(axis=1,thresh=2))

# Ya da NaN değerlerin yerine istedğimiz sayıyı yazdırabiliriz 20 değerini yazdırıyorum
print(yeniVeriDataFrame.fillna(20))

# groupby * Veri Analizi
maasSozlugu={
    "Departman":["Yazılım","Satış","Pazarlama","Finans","İnsan Kaynakları","Hukuk"],
        "Çalışan Ismi":["Ahmet","Yusuf","Mehmet","Burak","Zeynep","Fatma"],
        "Maas":[1000,1500,2000,3000,4000,5000]
}
maasDataFrame=pd.DataFrame(maasSozlugu)
print(maasDataFrame)

grupObjesi=maasDataFrame.groupby("Departman")
print(grupObjesi.count())
print(grupObjesi.mean())
print(grupObjesi.max())
print(grupObjesi.min())
print(grupObjesi.describe())



# concat
print("concat"+"-"*50)
sozluk1={"Isim":["Ahmet","Mehmet","Zeynep","Atıl"],
         "Spor":["Koşu","Yüzme","Koşu","Basketbol"],
         "Kalori":[100,200,300,400]
}
dataFrame1=pd.DataFrame(sozluk1,index=[0,1,2,3])
print(dataFrame1)


sozluk2={"Isim":["Osman","Levent","Yusuf","Yasin"],
         "Spor":["Koşu","Yüzme","Koşu","Basketbol"],
         "Kalori":[450,250,350,500]
}
dataFrame2=pd.DataFrame(sozluk2,index=[4,5,6,7])


sozluk3={"Isim":["Melih","Emre","Kerem","Burak"],
         "Spor":["Koşu","Yüzme","Koşu","Basketbol"],
         "Kalori":[500,250,300,150]
}
dataFrame3=pd.DataFrame(sozluk3,index=[8,9,10,11])

yeniDataFrame=pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=0)
print(yeniDataFrame)

# Merge  #Birleştirme

mergeSozluk1=sozluk1={"Isim":["Ahmet","Mehmet","Zeynep","Atıl"],
         "Spor":["Koşu","Yüzme","Koşu","Basketbol"]
            }
mergeDataFrame1=pd.DataFrame(mergeSozluk1)
print(mergeDataFrame1)

mergeSozluk2={"Isim":["Ahmet","Mehmet","Zeynep","Atıl"],
              "Kalori":[100,200,300,400]
              }
mergeDataFrame2=pd.DataFrame(mergeSozluk2)
print(mergeDataFrame2)
# on = Hangi parametre üzerinden işlem yapacağımızı gösterir
yeniMergeDataFrame=pd.merge(mergeDataFrame1,mergeDataFrame2,on="Isim")
print(yeniMergeDataFrame)
