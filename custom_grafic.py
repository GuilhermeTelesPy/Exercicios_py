import matplotlib.pyplot as plt 
anos = [1950, 1951, 1952, 2100]
pop =  [2.538, 2.57, 2.62, 1]

# mais dados
anos = [1800, 1850, 1900] + anos
pop = [1.0, 1.262, 1.650] + pop


plt.plot(anos, pop)
plt.xlabel("anos") #linha horizontal do grafico
plt.ylabel("pop") #linha vertical do grafico
plt.title("Projeções da população mundial") #titulo do grafico
plt.yticks([0, 2, 4, 6, 8, 10], # Coloca o grafico em perspectiva começando do numero 2
           ["0","2B", "4B", "6B", "8B", "10B"]) # lista com os nomes de exibição dos ticks
plt.show # mostra o grafico