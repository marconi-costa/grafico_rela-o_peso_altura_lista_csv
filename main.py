import pandas as pd
import matplotlib.pyplot as plt

dados =pd.read_csv('C:/Users/marconi.adm/PycharmProjects/graphics_program/lista_nomes.csv')

dados.head()
altura = dados['altura']
peso = dados['peso']

plt.scatter(altura, peso)
plt.show()
