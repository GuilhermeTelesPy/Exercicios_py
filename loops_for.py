import matplotlib as mt 

# Loop For receita
#For var in seq:
    #expression
#para cada var, uma variavel, em seq, uma sequencia, execute as expressoes

fam = [1.73, 1.68, 1.71, 1.89]
print(fam)
for altura in fam: # altura é um nome arbitario, eu poderia chamar de a outra coisa, quando voce executa esses script o python encontra o loop for e avalia o elemento seq fam nesse caso
    print(altura)

for index, altura in enumerate(fam):
    print("index", index, ":", altura)

for c in "family":
    print(c.capitalize())


    # house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for com in house:
    print(f"the {com[0]} is {com[1]} sqm")