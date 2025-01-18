import matplotlib.pyplot as plt # importação da biblioteca 
ano = [1950, 1970, 1990, 2010] #população ao passar duas decadas
pop = [2.519, 3.692, 5.263, 6.972] #aumento da população ao passar dos anos 
# plt.plot(ano, pop) # primeiro argumento corresponde ao eixo horizontal e o segundo ao eixo vertical
plt.scatter(ano, pop) # alterada a função para disperção, ela desenha todos os pontos de dados individuais, nao conecta os pontos
plt.show() #funcão que mostra o grafico 

