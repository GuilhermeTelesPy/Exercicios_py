# o loop while é um pouco semelhante a um instrução if: ele executa o codigo interno se a construção do for True 
#No entanto, ao contrario da instrução if, o loop while continuara, executando o codigo enquando a condição for verdadeira

# While Condição:
    #Expression

#Exempo suponha que voce esteja calculando numericamente um modelo com base de seus dados, isso envolve dar os mesmos passos repetidamente,ate que o erro entre seus dados esteja abaixo em algum limite 
#digamos que com um erro de cinquenta e que nosso algoritmo sofisticado divide o erro por quatro em cada execução, continua ate que erro esteja acima de 1 

error = 50.0

while error > 1:
    error = error / 4
    print(error)

#ele volta 3 vezes no codigo ate que a condição seja menor que 1 

x = 1
while x < 4 :

    print(x)

    x = x + 1

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")

    offset = offset - 1
    print(offset)