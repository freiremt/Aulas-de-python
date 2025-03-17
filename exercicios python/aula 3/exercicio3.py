valorA = int(input("Solicite um número: "))  
valorB = int(input("Solicite um número: "))
soma = valorA + valorB
if soma>20:
    print("A soma é Maior que 20: ",soma)
    soma = soma + 8
    print("Novo valor: ",soma)
else:
    print("A soma é Menor que 20: ",soma)
    soma = soma - 5
    print("Novo valor: ",soma)

    
    #Mateus Freire Carvalho