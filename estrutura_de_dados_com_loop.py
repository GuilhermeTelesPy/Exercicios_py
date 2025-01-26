# estrutura de dados com laços


#DICIONARIO

mundo = {
    "afeganistão": 30.55,
    "albania": 2.77,
    "algerlia":39.21
}
#nomes das chave e população corresponde como valores

for key, value in mundo.items(): # metodo items isso gerara uma chave e um valor em cada interação, a primeira variavel (key) sempre sera a chave e a segunda variavel o valor (value)
    print(f"{key} -- {value}")

import numpy as np

np_altura = np.array([1.73, 1.68, 1.71, 1.89, 1.79]) # Array altura 
np_peso = np.array([65.4, 59.2, 63.6, 88.4, 68.7]) # Array peso 
imc = np_peso / np_altura ** 2 # calculando o imc
for val in imc: # for que divide os valores por linha, sendo o val = valores, e o imc cada item 
    print(val)
meas = np.array([np_altura, np_peso])
for val in meas: #imprimindo cada elemento do array separadamente 
    print(val)
for val in np.nditer(meas): # usando a função ndite para imprimir cada elemento dos arrays peso e altura separadamente
    print(val)

# se voce quiser iterar sobre o valor-chave use o metodos items, pares e um dicionario, use o metodo item() no dicionario para definir a sequencia no loop 
#se interar sobre todos os elementos em matriz numpy use a ffunção nditer para especificar a sequencia 

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for chave, valor in europe.items():
    print("the capital of " + str(chave) + " is " + str(valor))
    print("the capital of " + str(chave) + " is " + str(valor))