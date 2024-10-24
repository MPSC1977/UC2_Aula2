import os

os.system('cls')

import numpy as np

precos_casas = [150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000]

media = np.mean(precos_casas)
mediana = np.median(precos_casas)


print('Média: ', media)
print('\nMediana: ', mediana)

print('A mediana é a medida que melhor representa o valor típico diante dos dados apresentados')