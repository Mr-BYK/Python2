# List
benimListem = [10,20,30,40]
print(type(benimListem))
benimListem[0] = 100
print(benimListem)
benimListem.remove(40)
print(benimListem)
benimListem.pop() # son değeri çıkartır
print(benimListem)
benimListem
benimListem.count(20)  #sayma

karisikListe = [1,2,3.5,"byk",9]
sonucum = karisikListe[3]
print(karisikListe[3])

karmasikListe = [[1,2,3,["a","b"],50],40,20,["z",5.5],[3,["a"]]]
bDegiskenimiz = karmasikListe[0][3][1]
print(bDegiskenimiz)

# Dict
benimYemekKaloriSozlugum = {"elma" : 100, "karpuz" : 200, "muz" : 300}
print(benimYemekKaloriSozlugum["muz"])

benimYemekKaloriSozlugum["elma"] = 200
print(benimYemekKaloriSozlugum)

yeniDictionary = {"anahtar1" : 100, "anahtar2" : [10,20,30,40,4.5,"atıl"],"anahtar3" : {"anahtar9" : 4}}
print(yeniDictionary.keys())
print(yeniDictionary.values())

print(yeniDictionary["anahtar2"][-1])
print(yeniDictionary["anahtar3"]["anahtar9"])

# Set
benimListem = [1,2,3,1,2,3]
print(type(benimListem))
benimListeSetim=set(benimListem)
print(type(benimListeSetim))

benimSet = {"a","b","c","a"}
print(type(benimSet))

bosListe = []
print(type(bosListe))
bosListe.append(1)
print(bosListe)


bosSozluk={}
print(type(bosSozluk))
bosSozluk["anahtarkelime"]=10
print(bosSozluk)

benimBosSetim=set()
print(type(benimBosSetim))
benimBosSetim.add(10)
print(benimBosSetim)
benimBosSetim.add(10)
benimBosSetim.add(10)
benimBosSetim.add(20)
benimBosSetim.add(20)
print(benimBosSetim)

# Tuple
benimListem = [1,2,"a",4.5]
print(benimListem[0])
benimListem[0]=100
print(benimListem)

benimTuple = (1,2,"a",4.5)
print(benimTuple)
print(benimTuple.count(2)) #sayma
print(benimTuple.index(2)) #kacıncı index

# Boolean
benimBoolean = True
print(type(benimBoolean))
print(10>5)
print(5>10)

#NOT
print(not 5 == 5) # 5 5'e eşit değil
print(not 5 == 4) # 5 4'e eşit değil




