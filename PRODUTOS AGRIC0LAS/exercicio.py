import pandas as pd

produtosAgricolas = pd.read_csv("produtosAgricolas.csv")
print(produtosAgricolas)

indice = produtosAgricolas["produtividade"].idxmax()

produto_maior_produtividade = produtosAgricolas.loc[indice, "tipo_de_cultivo"]
produtividade = produtosAgricolas.loc[indice, "produtividade"]

print("Produto com a maior produtividade: ",produto_maior_produtividade, "com",produtividade , "unidades")

produto_menor_custo_medio = produtosAgricolas.loc[indice, "tipo_de_cultivo"]
custo_medio = produtosAgricolas.loc[indice, "custo_medio"]

print("Produto com o menor custo médio: ",produto_menor_custo_medio, "com", custo_medio , "reais")

produto_menor_uso_de_agua = produtosAgricolas.loc[indice, "tipo_de_cultivo"]
uso_de_agua = produtosAgricolas.loc[indice, "uso_de_agua"]

print("Produto com menor Uso de Água: ",produto_menor_uso_de_agua, "com", uso_de_agua , "Litros")

#mean = media
#len = indentificacao
#pandas = analise de dados