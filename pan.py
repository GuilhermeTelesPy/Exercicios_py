import pandas as pd

#Dictionary of dictionaries
#europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
#          'france': { 'capital':'paris', 'population':66.03 },
#          'germany': { 'capital':'berlin', 'population':80.62 },
#          'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
#print(europe["france"]["capital"])

# Create sub-dictionary data
#data = {"capital": "rome", "population": 59.83}

# Add data to europe under key 'italy'
#europe["italy"] = data

# Print europe
#print(europe)

# pandas é uma ferramenta de manipulação de dados de alto nivel, construida no pacote numpy, nos pandas, armazenamos os dados tabulares como a tabela brics aqui como um objeto chamado 
# dataframe 

#DATAFRAME com dicionario 

dict = {
    "paises":["Brasil", "Russia","India", "China", "Africa do sul"],
    "capital":["Brasilia", "Moscou", "Nova Delhi", "Pequim", "Pretoria"],
    "area":[8.516, 17.10, 3.286, 9.597, 1.221],
    "populacao":[200.4, 143.5, 1252, 1357, 52.98]
}

# As chaves são os rotulos das colunas e os valores sao as colunas correspondentesl, em forma de listas
import pandas as pd
brics = pd.DataFrame(dict) #função frame

print(brics)

brics.index = ["BR", "RU", "IN", "CN", "AS"] # Atribuindo o rotulos manualmente 

print(brics)

# CSV, valores separados por virgula
#importar dados CSV para o python usando a função read

# brics = pd.read_csv("Caminho", index_col = 0)


