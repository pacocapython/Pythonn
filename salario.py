vh = float(input("Digite o quanto você ganha por hora: "))
nh = float(input("Digite quantas horas você trabalha por mês: "))

total = vh * nh
IR = total * 0.11
INSS = total * 0.8
SIND = total * 0.5
total1 = IR + INSS + SIND
total2 = total1 - total

print(f'O salário bruto é {total}') 
print(f'Você pagou {IR} ao imposto de renda')
print(f'Você pagou {INSS} ao inss')
print(f'Você pagou {SIND} ao sindicato')
print(f'O salário liquido é equivalente a {total2}')
