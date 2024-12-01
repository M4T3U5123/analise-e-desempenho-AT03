import matplotlib.pyplot as plt

# Valores de média e mediana dos tempos de execução e RAM utilizada
media_tempo = 5.2
media_ram = 4430
mediana_tempo = 5.0
mediana_ram = 4430

# Dados para os gráficos
categorias = ['Tempo de Execução', 'RAM Utilizada']
media_valores = [media_tempo, media_ram]
mediana_valores = [mediana_tempo, mediana_ram]

# Gráfico de médias
plt.figure(figsize=(8, 6))
plt.bar(categorias, media_valores, color=['blue', 'green'])
plt.title('Médias dos Tempos de Execução e RAM Utilizada')
plt.ylabel('Valores')
plt.show()

# Gráfico de medianas
plt.figure(figsize=(8, 6))
plt.bar(categorias, mediana_valores, color=['orange', 'purple'])
plt.title('Median dos Tempos de Execução e RAM Utilizada')
plt.ylabel('Valores')
plt.show()