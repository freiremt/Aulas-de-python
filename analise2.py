import pandas as pd
dadosProdutos = pd.read_csv("produtos.csv")

indice = dadosProdutos["preco"].idxmax()
#Obtendo o Produto com a maior preço
produto_maior_preco = dadosProdutos.loc[indice, "produto"]
preco = dadosProdutos.loc[indice, "produto"]

print("Produto com a maior quantidade: ",produto_maior_preco, "com",preco , "unidades")





#Mateus Freire Carvalho