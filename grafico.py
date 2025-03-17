#abreviação dos comandos
#pandas = pd
#matplotlib.pyplot = plt
import pandas as pd
import matplotlib.pyplot as plt

#Carregando os dados
dados_produtos = pd.read_csv('produtos.csv',delimiter=',')

#Criando o gráfico de PRECO por ANO para cada PRODUTO
plt.figure(figsize=(10, 6))

#Plotando os dados para cada produto
for produto in dados_produtos['produto'].unique():
    dados_produto = dados_produtos[dados_produtos['produto'] == produto]
    plt.plot(dados_produto['ano'], dados_produto['preco'], label=produto, marker='o')

#Adicionando titulo e rótulos
plt.title('Preço dos Produtos ao longo dos Anos')
plt.xlabel('ano')
plt.ylabel('preco')
plt.legend(title='produto')

#Exibindo o gráfico
plt.grid(True)
plt.show()



#Mateus Freire Carvalho