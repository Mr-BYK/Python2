#Functions
# Düzenli kod yazmaya , sorunları daha kolay çözmeye ve girdi çıktı(input-return) işlemlerine yarar

benimAdim="Yusuf Kara"
benimAdimBuyukHarfli=benimAdim.upper()
print(benimAdimBuyukHarfli)
print(benimAdim)

def ilkFonksiyonum():
    print("ilkFonskisonum")
ilkFonksiyonum()

# INPUT-RETURN
# INPUT

def merhabadünya(yazdirilacakisim):
    print("merhaba")
    print(yazdirilacakisim)

def merhaba(isim="yusuf"):
    print("merhaba")
    print(isim)

def toplama(numara1,numara2):
    sonuc=numara1+numara2
    print(sonuc)
toplama(10,20)
toplama(-220,350)

yenidegisken=toplama(10,20)
type(yenidegisken)

# RETURN
def dondurmeliToplama(num1,num2):
    return  num1+num2

yeniSonuc=dondurmeliToplama(10,20)
type(yeniSonuc)

def kontrolFonsliyon(s):
    if s == "yusuf":
        print("verdiğiniz string yusuf")
    else:
        print("verdiğiniz string baska bir sey")

kontrolFonsliyon("yusuf")

kontrolFonsliyon("kara")

# Args & Kwargs
# * işareti istediğin kadar değer girmemizi sağlıyor

def yeniToplamaa(*args):
    return sum(args)

yeniToplamaa(10,20,30,40,50,60)

def benimFonksiyonum(*args):
    print(args)
    return args
print(type(benimFonksiyonum(20,30,40)))

def ornekFonksiyon(**kwargs):
    print(kwargs)
    return kwargs

print(type(ornekFonksiyon(muz=100,elma=200,portakal=300)))


def keyWordKontrol(**kwargs):
    if "yusuf" in kwargs:
        print(" yusuf var")
    else:
        print("yusuf yok")

keyWordKontrol(ahmet=70,yusuf=40,yasin=60)

# Önemli Fonskiyonlar
def bolmeIslemi(numara):
    return numara/2
print(bolmeIslemi(20))

benimListem=[1,2,3,4,5,6,7,8,9,10]
yeniListe=[]
for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))
print(yeniListe)

# map Fonksiyonu
print(list(map(bolmeIslemi,benimListem)))
def kontrolFonksiyonu(string):
    return "u" in string

print(kontrolFonksiyonu("yusuf"))
print(kontrolFonksiyonu("leyla"))

# Map
stringListesi=["yusuf","leyla","melih","yasin","sülo","tilki"]
sonucListesi=list(map(kontrolFonksiyonu,stringListesi))
print(sonucListesi)

# Filter
print(list(filter(kontrolFonksiyonu,stringListesi))) # sadece true değerleri gösterir

# Lambda
carpma=lambda  numara: numara*3
carpma(10)

ornekListesi=[10,20,30]
print(list(map(lambda  numara: numara * 4 ,ornekListesi)))
