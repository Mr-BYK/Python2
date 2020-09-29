    # Instance & Attribute

# Instance:Bir sınıf üretiğimizde o sınıfın örneği,nesnesi instance olur
# Attribute: O sınıfın kendi özeliikleri attribute denir.
# Sınıfı neden üretiriz? Bu sınıftan bir çok farklı örnek yapabiliriz,üretebiliriz.
class SuperKahraman():

    def __init__(self,isimInput,yasIsnput,meslekInput):
        print("init çağrıldı")
        self.isim=isimInput
        self.yas=yasIsnput
        self.meslek=meslekInput

    # Methods
    def ornekMethod(self):
        print(f"Ben bir süperkahramanım ve mesleğim: {self.meslek}")

superman=SuperKahraman("Superman","30","Soytarılık")
print(superman.isim)
superman.isim="Yusuf KARA"

    # Methods
superman.ornekMethod()

    # Inheritance
class Hayvan():

    def __init__(self):
        print("Hayvan sınıfı init çağrıldı")

    def method1(self):
        print("Hayvan sınıfı method1 çağrıldı")

    def method2(self):
        print("Hayvan sınıfı method2 çağrıldı")

benimHayvanim=Hayvan()
benimHayvanim.method1()
benimHayvanim.method2()

class Kedi(Hayvan):

    def __init__(self):
        Hayvan.__init__(self)
        print("Kedi sınıfı init çağrıldı")

    def türü(self):
        print("Tekir")
# Override
    def method1(self):
        print("Kedi sınıfındaki method1 çağrıldı")

benimKedi=Kedi()
benimKedi.method1()
benimKedi.method2()
benimKedi.türü()

digerHayvan=Hayvan()

digerHayvan.method1()

digerKedi=Kedi()
digerKedi.method1()


    #Polymorphism
class Elma():
    def __init__(self,isim):
        self.isim=isim
    def bilgiVer(self):
        return self.isim + " 100 kaloridir"

class Muz():
    def __init__(self,isim):
        self.isim=isim

    def bilgiVer(self):
        return self.isim + " 150 Kaloridir"

elma=Elma("Elma")
elma.bilgiVer()
muz=Muz("Muz")
muz.bilgiVer()

meyveListesi=[elma,muz]
for meyve in meyveListesi:
    print(meyve.bilgiVer())

# Special Methods
class Meyve():
    def __init__(self,isim,kalori):
        self.isim=isim
        self.kalori=kalori


    def __str__(self):
        return  f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"

    def __len__(self):
        return self.kalori

muz=Meyve("Muz",150)
print(muz.kalori)
print(muz)
print(len(muz))

# Methodları tanımladıktan sonra istenilen str yazdırdı
print(muz)
len(muz)
elma=Meyve("Elma",200)
len(elma)
print(elma)

# Daha fazlası için py Spracial Methods ara


