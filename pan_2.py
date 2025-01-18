#Maneira diferente de escrever dados em DataFrame(Colunas)

# Selcionar colunas []

from pan import brics #importando a variavel de outro codigo 
print(brics[["paises"]])#Selecionando apenes a coluna paises do objetom, se quise selecionar apenas a coluna pais, e manter os dados em DataFrame, precisa usar colchetes duplos
print(type(brics[["paises"]]))
print(brics[1:4])# Fatiando o codigo coluna 1 a 3, o ultimo objeto sempre 1a+

#loc é uma tecnica para selecionar parte de seus dados com base em rotulos 
#iloc é baseado na posição

print(brics.loc[["RU"]])# para obter o dataframe temos que colocar colchetes duplos assim acessando a linha inteira
print(brics.loc[["RU", "IN", "CN"]])
print(brics.loc[["RU", "IN", "CN"], ["paises", "capital"]])#Selecinado apenas colunas especificas
print(brics.loc[:, ["paises", "capital"]])#Seleciando todas as colunas especificas
print(brics.loc[["RU"]])#acessando o indice RU
print(brics.iloc[[1]])#acessando o indice 1 ao inves de RU pelo iloc
print(brics.iloc[[1,2,3]])#acessando indice baseado na posição
print(brics.iloc[[1,2,3], [0, 1]])#acessando indice baseado na posição
print(brics.iloc[:, [0,1]])#Seleciando todas as colunas especificas com iloc baseado na posição