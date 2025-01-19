#OPERADORES BOOLEANOS

#and = e 
#or = ou
#not = não

#o operador and funciona como exatamente como voce esperaria, Leva dois booleanos e retorna True somente se ambos os booleanos forem True
print(True and True)
print(False and False)
print(True and False)
x = 12 
print(x > 5 and x < 15)

#o operador OR funciona de forma semelhante, mas a diferença é que apenas pelo menos um dos booleanos que ele usa deve ser True
print(True or True)
print(False or True) # os false sao avaliados com True 
print(False or False)# somente false e false resulta em false
y = 5
print(y < 7 or y > 13)

#Not ele simplesmete nego o valor booleano em que voce o usa 
print(not True)
print(not False)
#o operador not normalmente é util se voce estiver combinando diferentes booleanos 

#Comparação com  matrizes 
# np.logical_and()
# np.logical_or()
# np.logical_not()

#np.logical_and(bmi > 21, bmi < 22)
#

x = 8
y = 9
print(not(not(x < 3) and not(y > 14 or y > 10)))