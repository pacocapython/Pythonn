a = int(input("digite um número inteiro: "))
b = int(input("digite outro número inteiro: "))
c = int(input("digite mais um número inteiro: "))

if a < b and a < c:
    print(f'Dentre os três números, {a} é o menor número')
elif b < a and b < c:
    print(f'Dentre os três números, {b} é o menor número')
elif c < a and c < b:
    print(f'Dentre os três números, {c} é o menor número')