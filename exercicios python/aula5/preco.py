valor = float(input("Valor do produto: ",))
quantidade = float(input("Valor da quantidade: ",))

if quantidade < 10:
    desconto = 0
elif quantidade < 20:
    desconto = 0.1
else:
    desconto: 0.2 

valor_sem_desconto = quantidade * valor
valor_com_desconto = valor = (1-desconto)
valor_total = quantidade * valor_com_desconto
valor_desconto = quantidade * valor * desconto
porcentagem_desconto = desconto * 100

print(f"valor total sem desconto: ", valor_sem_desconto)
print(f"valor unitário: R$ {valor: .2f}")
print(f"valor com desconto: R$ {valor: .2f}({porcentagem_desconto: .0f}% de desconto)")
print(f"valor total: R$ {valor_total: .2f}(desconto total: R$ {valor_desconto:.2f})")

#Mat3us Fre1re Carvalh0