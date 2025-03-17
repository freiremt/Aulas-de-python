
cont = 1
qtdPares = 0
qtdImpar = 0

while cont < 6:

   numero = int(input("Entre com o valor : "))
   
   

   if numero%2==0:

       qtdPares += 1

   else:

       qtdImpar += 1

   cont+= 1
   
print("Quantidade de pare: ",qtdPares)
print("Quantidade de pare: ",qtdImpar)