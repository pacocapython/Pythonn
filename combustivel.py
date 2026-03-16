l = float(input("Digite a quantidade de litros: "))
t = str(input("Digite o tipo de combustível (1-álcool / 2-gasolina): "))

if t == "1":
    p = 2.19
if l <= 20:
    d = 0.03
else:
    d = 0.05

if t == "2":
    p = 2.99
if l <= 20:
    d = 0.04
else:
    d = 0.06

t = l * p
vd = t * d
vf = t - vd

print('Valor a pagar', {vf})