# Hata Yönetimi ve Hesap Nakinesi
def hesapla(a,b,islem):
    if islem not in "+ - * / ":
        return "lütfen dört işlemlerden birisini seçiniz. + - * /"
    if islem == "+":
        return  (str(a))+" + "+str(b)+ "  =  "+str((a+b))
    if islem == "-":
        return  (str(a))+" - "+str(b)+ "  =  "+str((a-b))
    if islem == "*":
        return  (str(a))+" * "+str(b)+ "  =  "+str((a*b))
    if islem == "/":
        return  (str(a))+" / "+str(b)+ "  =  "+str((a/b))

a = int(input("İlk sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))
islem = input("İşleminizi seçiniz: + - * /")
print(hesapla(a, b, islem))

# işlemi sonsuz döngüye aktar
while True:
    try:
        a = int(input("İlk sayıyı giriniz: "))
        b = int(input("İkinci sayıyı giriniz: "))
        islem = input("İşleminizi seçiniz: + - * /")
        print(hesapla(a, b, islem))
    except:
        print("Geçersiz işlem")


