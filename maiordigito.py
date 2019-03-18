
numero = int(input('Digite um numero para verificar o maior digito:\n'))

max = 0
verif = True

while verif:
    div = numero % 10
    if div > max:
        max = div

    if numero < 1:
        verif = False

    numero = numero//10

print(max)












