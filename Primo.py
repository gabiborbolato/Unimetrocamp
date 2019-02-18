NumberTest = int(input('Digite um numero a ser testado\n'))
div = 2
Test = 0
if(NumberTest == 1):
    print('nao eh primo')
while(NumberTest > div):
    Test = NumberTest % div
    if (Test == 0):
        print('nao eh primo')
        break
    else:
        div = div + 1

if(Test!=0 or NumberTest == 2):
    print('primo')






