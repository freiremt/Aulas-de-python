#Criado 2 variaveis
qtdPares = 0
qtdImpar = 0

#Criando laaço for
for i in range(5):

    #recebendo os valores
   numero = int(input("Entre com o valor : "))
   
   #se o resto da divisão for igual a zero ele é par
   if numero%2==0:

    #contando a quantidade de pares
       qtdPares += 1
    #se a primeira condição for falsa ele irá conta a quantidade de impares
   else:
        #contando a quantidade de impares
       qtdImpar += 1

   #Imprimindo os elementos
print("Quantidade de pare: ",qtdPares)
print("Quantidade de pare: ",qtdImpar)