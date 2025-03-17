#Criei meu dicionario
produto = {
    #chave    valor, é separado por uma virgula
    'Nome':'Feijão',
    #chave    valor
    'Quantidade':10
}
#alterando valor
produto['Quantidade'] = 100
#alterando nome
produto['Nome'] = 'Ray santos'

#criei uma varia pra receber o valor contido na chaver
nome = produto['Nome']
quantidade = produto['Quantidade']

#printando os valores
print("Nome: ",nome)
print("Quantidade: ",quantidade)


produto = {
    #chave    valor, é separado por uma virgula
    'Nome':['Feijão','Arroz','Farinha'],
    #chave    valor
    'Quantidade': [10,10,100],
}

#lo zip vai unir dois elementos
for ra, boo in zip(produto['Nome'],produto['Quantidade']):
    print("Produto: ",ra,"Quantidade: ",boo)


produto = {
    #chave    valor, é separado por uma virgula
    'Nome':['Feijão','Arroz','Farinha'],
    #chave    valor
    'Quantidade': [10,10,100],
    'preco':[19,17,18]
}

print("--------------------------------------------")
#Adicionei mais uma chave com oa valores e imprimi usando o for juntamente com o  zip que printa todos as chaves e valores
for a,b,c in zip(produto['Nome'],produto['Quantidade'],produto['preco']):
    print("produto: ",a,"Quantidade: ",b,"Preço: ",c)
print("--------------------------------------------")


#CONJUNTO

#lista
numeros = [1,2,3,3]

#SET vai tirar os números repetidos
conjunto = set(numeros)

#print conjunto
print(conjunto)
print("--------------------------------------------")
