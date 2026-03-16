Código = int(input("Digite o código de 100 a 105 "))
Quant = int(input("Digite a quantidade "))

if Código == 100:
 preço = 1.26
elif Código == 101:
 preço = 1.36
elif Código == 102:
 preço = 1.50
elif Código == 103:
 preço = 1.20
elif Código == 104:
 preço = 1.30
elif Código == 105:
 preço = 1.56
 
total = preço * Quant
print("0 valor a se pagar", total)