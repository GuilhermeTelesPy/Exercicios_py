#como resolver

#calcular a chance analicamente usando equações  
#simular os processo milhares de vezes, e veja em qua fração das simulações voce chega a 60 passos 
    #esta é uma forma de estatisticas de hackers

#a primeira coisa que precisamos sao geradores aleatorios, para que possamos simular o dado

import numpy as np

print(np.random.seed(123)) #como esse numero aleatorio foi criado?, os computadores normalmente geram os chamados numeros pseudo-aleatorios, formula matematica, a partir de um semente aleatoria
print(np.random.rand())# se definir a semente para 123 e chamar o rand mais duas vezes obtermos os mesmos numeros aleatorios, sao pseudo aleatorio, é aleatorio mas consistente

#coin toos

np.random.seed(123)
moeda = np.random.randint(0, 2) # para que ele gere aleatoriamente o ou 1, passamos dois argumentos o primeiro dever ser 0 e segundo 2, porque 2 nao sera incluido
print(moeda)

if moeda == 0:
    print("Cara")
else:
    print("Coroa")

print(np.random.randint(1,2,3,4,5,6,7))

# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice > 3 and dice < 5:
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice,step)