# Numpy Array / Numpy Dizisi
import numpy as np
benimListem=[10,20,30]
print(type(benimListem))

# Array
np.array(benimListem)
print(np.array(benimListem))

matrixListem=[[10,20,30],[20,30,40],[30,40,50]]
print(matrixListem[1][0])
print(np.array(matrixListem))

# Numpy Methods
# Arange
print(list(range(0,10)))

print(np.arange(0,10))
print(np.arange(0,10,2))

# Zeros
print(np.zeros(5))
print(np.zeros((5,5)))

# Ones
print(np.ones(5))
print(np.ones((5,5)))

# Linspace
print(np.linspace(0,10,5))
print(np.linspace(0,10,20))

# Eye
print(np.eye(3))
print(np.eye(10))

# Random
# Rastgale bazı değeler bize  veriyor
print(np.random.randn(8))
print(np.random.randn(4,4))

print(np.random.randint(1,10))
print(np.random.randint(1,10,5))

# Numpy Series Methods /Numpy Dizi Methodları
benimRandomDizim=np.random.randint(0,100,30)
print(benimRandomDizim)

print(benimRandomDizim.reshape(6,5))
print(benimRandomDizim.max())
print(benimRandomDizim.min())
print(benimRandomDizim.argmin())
print(benimRandomDizim.argmax())