import numpy as np
altura = [1.80, 1.70, 1.60, 1.65, 1.92]
peso = [81.0, 65.5, 55.0, 60.0, 100.0 ]

np_altura = np.array(altura)
np_peso = np.array(peso)
print(np_altura)
print(np_peso)

imc = np_peso / np_altura ** 2
print(imc)


n= np.array([True, 1, 2])
print(n)