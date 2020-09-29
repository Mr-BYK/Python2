# Error Handling
def toplama(numara1,numara2):
    return numara1+numara2
x=int(input("İlk numaranızı girin:"))
y=int(input("İkinci numaranızı girin:"))
print(toplama(x,y))

# Try & Except & Else & Finally

while True:
    try:
        benimInt=int(input("Numaranızı giriniz:"))
    except:
        print("Lütfen gerçekten numara giriniz.")
        continue
    else:
        print("Teşekkürler")
        break
    finally:
        print("Finally çağrıldı")


