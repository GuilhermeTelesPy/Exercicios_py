#voce joga o dado cem vezes,depedendo do resultado voce sobe ou desce degraus, isso é chamado de passeio aleatorio, e voce sabe com simular isso
#Mas você ainda precisa responder à pergunta principal: qual é a chance de chegar a 60 degraus de altura?


import numpy as np 
np.random.seed(123) 
tails = [0] 
for x in range(10): 
    coin = np.random.randint(0, 2) 
    tails.append(tails [x] + coin)


#calcular a distribuição

np.random.seed = [123]
final_tails = []
for x in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2) 
        tails.append(tails [x] + coin)