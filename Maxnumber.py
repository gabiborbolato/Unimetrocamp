lista = []
quantDeNumb = 0

while quantDeNumb < 10:
    num = int(input('Digite um numero\n'))
    lista.append(num)
    quantDeNumb = quantDeNumb + 1

print(lista)
max = 0
for i in range (0, len(lista)):
    if max < lista[i]:
        max = lista[i]

print(max)

    
