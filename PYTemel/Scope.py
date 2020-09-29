# local,Enclosing,Global,Built-In

benimAdim="Yusuf"
# Global

def benimFonksiyonum():
    benimAdim="Hatce"
    # Enclosing
    def icFonksiyon():
        benimAdim="Bekir"
         # Local
        print(benimAdim)
    icFonksiyon()

    # benimFonksiyonum()
benimFonksiyonum()
print(benimAdim)

y = 10
def yeniFonksiyon(y):
    print(y)
    y=5
    print(y)
    return y
yeniFonksiyon(3)

y = 10
def ornekFonksiyon():
    global y
    y = 12
    print(y)
ornekFonksiyon()
