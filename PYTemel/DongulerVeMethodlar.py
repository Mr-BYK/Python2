# If_Else
benimString="Yusuf Kara"
if "Kara" in benimString:
    print("Ifade var")
else:
    print("Ifade yok")

if "ara" in benimString:
    print("Ifade var")
else:
    print("Ifade yok")


# For
yeniListe=[1,2,3,4,5,6]
for rakam in yeniListe:
    if rakam % 2 == 0:
        print(rakam,"sayı çifttir")
    else:
        print(rakam,"sayı tektir")

adım="yusuf kara"
for harf in adım:
    print(harf)

benimTuple2=[1,2,3,4,5,6]
for eleman in benimTuple2:
    print(eleman-10)


koordinat=[(10.2,15.2),(32.4,16.2),(40.2,20.2)]
print(type(koordinat[0]))

for koor in koordinat:
    print(koor)

for(x,y) in koordinat:
    print(y)

garipListe=[(1,2,3),(4,5,6),(7,8,9)]
for(x,y,z) in garipListe:
    print(z)

benimSozluk={"muz":150,"portakal":250,"elma":400}
for (anahtar,deger) in benimSozluk.items():
    print(deger)

# Continue / Break / Pass
benimYeniListem=[5,10,15,20,25,30,35,40,45,50]
for numara in benimYeniListem:
    if numara == 15:
        break
    print(numara)

for numara in benimYeniListem:
    if numara == 15:
        continue
    print(numara)

for numara in benimYeniListem:
    if numara == 15:
        pass

#  While
yeniDegisken=0
while yeniDegisken < 15:
    print(f"yeniDegisken'in güncel değeri:"+str(yeniDegisken))
    yeniDegisken=yeniDegisken+1


# Range
indexx=0
for numaraa in list(range(5,15)):
    print(f"güncel numara: {numaraa} güncel index: {indexx}")
    indexx=indexx+1

# Enumerate
index=0
for (indexx,numaraa) in enumerate(list(range(5,15))):
    print(numaraa)


yemekListesi=["muz","ananas","elma"]
kaloriListesi=[100,200,300]
gunListesi=["pazartesi","salı","çarşamba"]

ziplenmisListe=list(zip(yemekListesi,kaloriListesi,gunListesi))
for eleman in ziplenmisListe:
    print(type(eleman))
