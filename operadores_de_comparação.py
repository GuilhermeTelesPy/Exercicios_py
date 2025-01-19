#OS operadores de comparação são operadores que podem dizer como dois valores Python se relacionam e resultam em um booleano
#No sentido mais simplem, voce pode usar esses operadores em numeros 
#EXEMPLO
print(2 < 3)# verifica se 2 é menor que 3
print(2 == 3)# verifica se 2 é igual 3 
print(2 <= 3)# verifica se 2 é igual ou menor que 3 
print(3 <= 3)# verifica se 3 é igual ou menor que 3 
x = 2
y = 3
print(x < y)# verifica se x é menor que y

#Outras comparações 

print ("carl" < "Chris")# Verifica se carl é menor do que Chris, de acordo com o alfabeto sim Carl é menor do que Chris
#print(3 < "Chris")# Recebemos um erro, normalmente o python nao pode dizer como os dois objetos com diferentes se relacionam

#Diferentes tipos numericos como floats e int, sao exceções
print(3 < 4.1)

#Outras exceção surge quando voltamos ao exemplo que come
#mi = array ([21.852, 20.975, 21.75 24.747, 21.441])) 
#bmi > 23 array ([False, False, False, True, False), dtype=bool)

#Numpy descobre que voce deseja comparar todos os elementos em bmi com 23 e retornar os booleanos correspondentes 

#Comparadores 
# < Menor 
# <= Menor Igual
# > Maior 
# >= Maior Igual
# == Igual 
# != Difente

