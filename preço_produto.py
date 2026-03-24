p1 = float(input("Digite o preço do produto: "))
p2 = float(input("Digite o preço do produto: "))
p3 = float(input("Digite o preço do produto: "))

if p1 < p2 and p1 < p3:
 print("Você deve comprar o produto 1, com o preço de R$", p1)
elif p2 < p1 and p2 < p3:
 print("Você deve comprar o produto 1, com o preço de R$", p2)
elif p3 < p1 and p3 < p2:
 print("Você deve comprar o produto 1, com o preço de R$", p3)
