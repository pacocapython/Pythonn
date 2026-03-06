preço = float(input("Digite o preço unitário do produto: "))
unit = int(input("Digite a quantidade de produtos comprados: "))
valor = float(input("Digite o valor dado pelo produto: "))

total = preço * unit

if valor == total:
    print (f'Obrigado, o dinheiro está certo, volte sempre')
elif valor > total:
     troco = valor - total
     print(f'Aqui está o troco do produto', troco)
elif total > valor:
    troco2 = total - valor
    print (f'Dinheiro insuficiente, faltam {troco2} reais')