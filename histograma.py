import matplotlib.pyplot as plt
#help(plt.hist) # abre a documentação, x deve ser uma lista de valores para os quais voce deseja construir um histograma, e os bins informa o python em bins os dados devem ser divididos
valores = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6] # lista com 12 valores 
plt.hist(valores, bins=3) # valores = x, 
plt.show()
