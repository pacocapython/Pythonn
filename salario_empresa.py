sf = float(input("Digite o salário fixo: R$ "))
v = float(input("Digite o valor total das vendas: R$ "))

limite = 1500.00
taxa1 = 0.03
taxa2 = 0.05

if v <= limite:
    comissao = v * taxa1
else:
    comissao_base = limite * taxa1
    valor_excedente = v - limite
    comissao_excedente = valor_excedente * taxa2
    comissao = comissao_base + comissao_excedente

st = sf + comissao

print(f'O salário total do vendedor é: {st}')
