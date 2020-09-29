import numpy as np
import pandas as pd
data=np.random.random((4,3))
print(data)
dataFrame=pd.DataFrame(data)
print(dataFrame)
yeniDataFrame=pd.DataFrame(data,index=["Hatce","Yusuf","Benjamin","İntizar"],columns=["Yaş","Maaş","Çalışma Saati"])
print(yeniDataFrame)
print("-"*50)
print(yeniDataFrame["Yaş"])
print("-"*50)
print(yeniDataFrame["Çalışma Saati"])
print("-"*50)
print(yeniDataFrame.loc["Hatce"])
print(yeniDataFrame.loc["Yusuf"])
print("-"*50)
print(yeniDataFrame.iloc[1])

# DataFrame Index

yeniDataFrame["Emeklilik Yaşı"]=yeniDataFrame["Yaş"]+yeniDataFrame["Yaş"]
print(yeniDataFrame)
print(yeniDataFrame.drop("Emeklilik Yaşı",axis=1))
print(yeniDataFrame)

# Tamamen silmek için
yeniDataFrame.drop("Emeklilik Yaşı",axis=1,inplace=True)
print(yeniDataFrame)
print("-"*50)
print(yeniDataFrame.loc["Hatce","Maaş"])
print("-"*50)
print(yeniDataFrame<0)
# Pozitif rowları getirme
print(yeniDataFrame[yeniDataFrame["Yaş"]>0])

#  Index Değiştirme
print(yeniDataFrame.reset_index())
yeniIndexListesi=["Hatice","Yasuo","Bünyamin","Azer"]
yeniDataFrame["Yeni Index"]=yeniIndexListesi
print(yeniDataFrame)
print(yeniDataFrame.set_index("Yeni Index"))
# Kalıcı index değiştirmek için inplace kullanırız
yeniDataFrame.set_index("Yeni Index",inplace=True)
print(yeniDataFrame)
print("-"*50)
# Multiındex
ilkIndeksler=["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
icIndeksler=["Homer","Bart","Marge","Cartman","Kenny","Kyle"]
birlesmisIndeksler=list(zip(ilkIndeksler,icIndeksler))
birlesmisIndeksler=pd.MultiIndex.from_tuples(birlesmisIndeksler)
print(birlesmisIndeksler)
print("-"*50)
benimFilmListem=[[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
filmListemNumpyDizisi=np.array(benimFilmListem)
filmDataFrame=pd.DataFrame(filmListemNumpyDizisi,index=birlesmisIndeksler,columns=["Yaş","Meslek"])
print(filmDataFrame)
print(filmDataFrame.loc["Simpson"])
print(filmDataFrame.loc["South Park"])
print("-"*50)
print(filmDataFrame.loc["South Park"].loc["Kenny"])

filmDataFrame.index.names=["Film Adı","İsim"]
print(filmDataFrame)
