import pandas as pd

dadosProdutos = pd.read_csv("produtos.csv")
print(dadosProdutos.columns)

dadosProdutos['preco'].max()
print("Média do Preço dos Produtos ", dadosProdutos['preco'].mean())


#Mateus Freire Carvalho