from pan import brics
import pandas as pd 

for val in brics:
    print(val) # ele pega os valores das colunas

# no pandas, voce deve mencionar explicitamente que deseja itera(repetir)

#voce faz isso chamando o metodo iterrows no pais brics, especificando assim outro
# o metodo iterrows analisa o DataFrame e em cada iteração, gera dois dados: o rotulo da linha e, em seguida, os dados reais na linha com um serie de pandas
for lab, row in brics.iterrows(): #armazenamos o roturo da linha em (lab) e os dados com (row):
    print(lab)
   # print(row)

#for lab, row in brics.iterrows():
  #  print(f"{lab} : {row["capital"]}") #imprimindo somente a lista de capitais

#for lab, row in brics.iterrows():
 #   brics.loc[lab, "name_length"] + len(row["paises"])
  #  print(brics)