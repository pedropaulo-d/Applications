from time import sleep
#Declaração de Valores
cal = 'CALCULADORA'
print('-='*20)
print(f'{cal:^40}')
print('-='*20)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
#Calculadora
while True:
    print('[ 1 ] SOMAR.')
    print('[ 2 ] SUBTRAIR.')
    print('[ 3 ] MULTIPLICAR.')
    print('[ 4 ] DIVIDIR.')
    print('[ 5 ] NOVOS VALORES.')
    print('[ 0 ] ENCERRAR CALCULADORA.')
    op = int(input('Qual opção você deseja? '))
    print('-='*20)
    if op == 1:
        print(f'A soma dos valores {n1} e {n2} é igual a: {n1 + n2}')
    elif op == 2:
        print(f'A subtração do valor {n1} por {n2} é igual a: {n1 - n2}')
    elif op == 3:
        print(f'O produto entre os valores {n1} e {n2} é igual a: {n1 * n2}')
    elif op == 4:
        print(f'A divisão do valor {n1} por {n2} é igual a: {n1 / n2}')
    elif op == 5:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op < 0 or op > 5:
        print('Opção inválida! Tente novamente.')
        op = int(input('Qual opção você deseja? '))
    elif op == 0:
        break
for c in range(0, 8):
    print('.')
sleep(1.0)
print('-='*10, 'VOLTE SEMPRE!', '-='*10)
