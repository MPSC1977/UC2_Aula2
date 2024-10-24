import os

os.system('cls')

import numpy as np

dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])

q1 = np.quantile(dados, 0.25) #É POSSÍVEL FAZER COM O MÉTODO PERCENTIL np.percentil(dados, 25)
q2 = np.quantile(dados, 0.50) #É POSSÍVEL FAZER COM O MÉTODO PERCENTIL np.percentil(dados, 50)
q3 = np.quantile(dados, 0.75) #É POSSÍVEL FAZER COM O MÉTODO PERCENTIL np.percentil(dados, 75)

print(f'Q1 25%: {q1}')
print(f'\nQ2 50%: {q2}')
print(f'\nQ3 75%: {q3}')

