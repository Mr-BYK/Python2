import numpy as np
import pandas as pd
# Series
benimSozlugum={"Atıl":50,"Zeynep":40,"Mehmet":30}
print(pd.Series(benimSozlugum))
print("-"*60)
benimYaslarım=[50,40,30]
benimIsimlerim=["Atıl","Zeynep","Mehmet"]
print(pd.Series(benimYaslarım))
print("-"*60)
print(pd.Series(benimYaslarım,benimIsimlerim))
print("-"*60)
print(pd.Series(data=benimYaslarım, index=benimIsimlerim))
print("-"*60)
numpyDizisi=np.array([50,40,30])
print(numpyDizisi)
print(pd.Series(numpyDizisi))
print("-"*60)
print(pd.Series(numpyDizisi,benimIsimlerim))

# Series Attribute
yeniSeri=pd.Series(["Yusuf","Ayse","Osman"],[1,2,3])
print(yeniSeri)
print("-"*60)

yarismaSonucu1=pd.Series([10,5,1],["Yusuf","Ayse","Osman"])
print(yarismaSonucu1)
print("-"*60)

yarismaSonucu2=pd.Series([20,10,8],["Yusuf","Ayse","Osman"])
print(yarismaSonucu2)
print("-"*60)

sonSonuc=yarismaSonucu1+yarismaSonucu2
print(sonSonuc)
print("-"*60)

farkliSeries1=pd.Series([20,30,40,50],["a","b","c","d"])
farkliSeries2=pd.Series([10,5,3,1],["a","c","f","g"])
print(farkliSeries1+farkliSeries2)