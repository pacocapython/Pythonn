peso = float(input("Digite o peso de peixes: "))

limite = 50
multa_quilo = 4

if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_por_quilo
else:
    excesso = 0
    multa = 0

print("Peso de peixes", {peso}, "kg")
print("Excesso", {excesso}, "kg")
print("Multa a pagar R$", multa)