import pandas as pd
import os
import numpy as np

os.system('cls')

df_custos = pd.read_csv('planilha_de_custos.csv')
print(df_custos.head())

print('\nDados Obtidos')
print(100 * '=')
print(df_custos.head())

# Criando uma nova coluna
df_custos['Custo Total (R$)'] = (
    df_custos['Preco de Compra (R$)'] + 
    (df_custos['Preco de Compra (R$)']*df_custos['Imposto (%)'] / 100)+
    df_custos['Frete (R$)']+
    df_custos['Taxa Operacional (R$)']
)

print(df_custos.head())
print()
print(df_custos[['Produto', 'Custo Total (R$)']].head(10))



#--------------------------------------------------

array_custo_total = np.array(df_custos['Custo Total (R$)'])
# print(array_custo_total)
print('\nMédidas de tendência central')
print(100*"_")

media = np.mean(array_custo_total)
print(f'\nMédia dos custos: {media:.2f}')

mediana = np.median(array_custo_total)
print(f'\nMediana dos custos: {mediana:.2f}')

#----------------------------------------------------

#quartis

q1 =np.quantile(array_custo_total, 0.25) # 25%
q2 =np.quantile(array_custo_total, 0.50) # 50%
q3 =np.quantile(array_custo_total, 0.75) # 75%


print('\nMédidas de posição')
print(100*"_")
print(f'Q1: {q1: .2f}')
print(f'Q2: {q2}')
print(f'Q3: {q3: .2f}')