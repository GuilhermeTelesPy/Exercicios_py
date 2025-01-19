pop = [30.55, 2.77, 39.21] # população dos paises 
paises = ["afeganistao", "albania", "argelia"] #paises
ind_alb = paises.index("albania") # descobrir a popoulação da albania 
print(ind_alb)# imprimi o (metodo)index da albania que esta na posição 1 
print(pop[ind_alb]) #imprimi a polução da albania 


# feita a construção de 2 indices para conectar os elementos, porem nao a abordagem nao é intuitiva, tem uma forma melhor de conectar os elementos diretamente sem usar indice

#DICIONARIOS
# para criar dicionarios é preciso usar chave{}

pop = [30.55, 2.77, 39.21] # população dos paises 
paises = ["afeganistao", "albania", "argelia"] #paises

mundo = {"afeganistao":30.55, "albania":2.77, "argelia":39.21} #as chaves sao os nomes dos paises, e o valores a população
print(mundo["afeganistao"])

# Chave exclusivas em um dicionario devem ser os chamados de objetos imutaveis, o conteudo de objetos imutaveis nao podem ser alterados apos sua criação

mundo["sealand"] = 0.000027 # adicionado a população de sealand ao dicionario mundo 
print(mundo)
print("sealand" in mundo)

mundo["sealand"] = 0.000028 # atualizada o valor de sealand ao dicionario mundo 
print(mundo)
print("sealand" in mundo)

del(mundo["sealand"]) #feita a exclusao de sealand no dicionario mundo

print(mundo)

#listas vs dicionarios, sao bem semelhantes, sendo possivel, selecionar, atualizar e remover elementos com colchete[], mas exite uma diferenças, a lista é uma sequencia de valores
# que são indexados por um intervalo de numeros, os dicionarios é indexado por chaves exclusivar, que podem ser de qualquer tipo imutavel
# quando usar?, se você tem um coleção de valores, onde a ordem é importante e deseja selecionar facilmente o subconjunto inteiro de dados, devem usar um lista 
# se você precisa de algum tipo de tabela de pesquisa onde procura os dados, deve ser rapido e onde você pode especificar chaves exclusivas, o dicionario é a opção

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe["france"]["capital"])

# Create sub-dictionary data
data = {"capital": "rome", "population": 59.83}

# Add data to europe under key 'italy'
europe["italy"] = data

# Print europe
print(europe)