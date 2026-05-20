#____ atividade móveis ____
import pandas as pd
import os
import numpy as np


os.system('cls')

df_custos_moveis = pd.read_csv('planilha_moveis.csv')
print(df_custos_moveis)

df_custos_moveis['Total arrecadado'] = (
    df_custos_moveis ['Preco']+
    df_custos_moveis ['Vendidos']
)

print(df_custos_moveis.head())
print()
print(df_custos_moveis[['Produto','Total arrecadado']])


#--------------------------------------------------

array_custo_moveis = np.array(df_custos_moveis['Total arrecadado'])


# print('\nMédidas de tendência central')
# print(100*"_")

# media = np.mean(array_custo_moveis)
# print(f'\nMédia dos custos: {media:.2f}')

# mediana = np.median(array_custo_moveis)
# print(f'\nMediana dos custos: {mediana:.2f}')

# q1 =np.quantile(df_custos_moveis, 0.25) # 25%
# q2 =np.quantile(df_custos_moveis, 0.50) # 50%
# q3 =np.quantile(df_custos_moveis, 0.75) # 75%

q1 = np.quantile(df_custos_moveis['Total arrecadado'], 0.25)
q2 = np.quantile(df_custos_moveis['Total arrecadado'], 0.50)
q3 = np.quantile(df_custos_moveis['Total arrecadado'], 0.75)


print('\nMédidas de posição')
print(100*"_")
print(f'Faixa de menores preços: {q1: .2f}')
print(f'Faixa central de preços dos produtos: {q2}')
print(f'Faixa de maior margem financeira: {q3: .2f}')