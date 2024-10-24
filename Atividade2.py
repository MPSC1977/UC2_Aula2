import os

os.system('cls')

import pandas as pd
import numpy as np

df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')
print(df)

nome_produto = df['Nome do Produto']
total_vendas = df['Total']

media = np.mean(total_vendas)
mediana = np.median(total_vendas)

print(100 * '=')
print('\nTENDÊNCIA CENTRAL')
print(f'\nO preço médio total de vendas é de R${media}')
print(f'\nA mediana total de vendas é de R${mediana}')

q1 = np.quantile(total_vendas, 0.25)
q2 = np.quantile(total_vendas, 0.50)
q3 = np.quantile(total_vendas, 0.75)

print(50 * '=')
print('\nTENDÊNCIA POSICIONAL')
print(f'\n25% dos produtos tem valor total de venda inferior a R${q1}')
print(f'\n50% dos produtos tem valor total de venda inferior a R${q2}')
print(f'\n75% dos produtos tem valor total de venda inferior a R${q3}')

print(80 * '=')
print('\nMAIS VENDIDOS')
mais_vendidos = df[df['Total']>q3].sort_values(by='Total', ascending=False)
print(mais_vendidos)
