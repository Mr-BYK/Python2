# Numpy Indexs
import numpy as np
benimDizim=np.arange(0,15)
print(benimDizim)
print(benimDizim[5])

# Numpy Slicing
print(benimDizim[3:8])

benimDizim[3:8] = -5
print(benimDizim)

baskaDizi=np.arange(0,24)
print(baskaDizi)

slicingDizi=baskaDizi[4:9]
print(slicingDizi)
slicingDizi[:]=700
print(slicingDizi)
print(baskaDizi)

# Geçerli dizideki değerleri etkilememesi için
ornekDizi=np.arange(0,24)
print(ornekDizi)
ornekDiziKopyasi=ornekDizi.copy()
print(ornekDiziKopyasi)
print(ornekDizi)

ornekDiziKopyasiSlicing=ornekDiziKopyasi[3:6]
ornekDiziKopyasiSlicing [:]=800
print(ornekDiziKopyasiSlicing)
print(ornekDiziKopyasi)
print(ornekDizi)

# Matrix Indexs
benimListem=[[10,20,30],[20,30,40],[40,50,60]]
benimMatrixDizim=np.array(benimListem)
print(benimMatrixDizim)

# Matrix Slicing
print(benimMatrixDizim[0])
print(benimMatrixDizim[1,2])
print(benimMatrixDizim[1][2])
print(benimMatrixDizim[1:,2])
print(benimMatrixDizim[0:,2])
print(benimMatrixDizim[2:,2:])

yeniListe=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
yeniMatrix=np.array(yeniListe)
print(yeniMatrix)
print( "-" *50)
print(yeniMatrix[[4,2,0]])

