from pan import brics #importando a variavel brics de outro codigo
import numpy as np
print(brics)

#Selecionar paises com areas maiores que 8 milhores km 
# 3 passos 
    # obter a coluna da area do brics
    # Realizar a compação nesta coluna e armazenamos os resultados
    # Usar o resultados para selecionar os paises
print(brics["area"])
#outros metodos usando o loc e iloc 
#print(brics.loc[:, "area"])
#print(brics.iloc[:, 2])
print(brics["area"] > 8)

is_huge = brics[brics["area"] > 8] #obtendo o Dataframe de territorios maiore que 8m km 
print(is_huge)
print(brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)])

