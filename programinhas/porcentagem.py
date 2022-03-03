from time import sleep
print('-='*20)
print('DESCONTO E AUMENTO EM PORCENTAGEM!')
print('-='*20)
n2 = float(input('Valor total que você tem: '))
n3 = float(input('Valor percentual: '))
print('-='*20)
while True:
    print('[ 1 ] DESCONTAR')
    print('[ 2 ] AUMENTAR')
    print('[ 3 ] DIGITAR NOVOS VALORES')
    print('[ 0 ] FECHAR PROGRAMA')
    n1 = int(input('Qual opção você deseja? '))
    print('-='*20)
    if n1 == 1:
        descont = n2 * ((100 - n3) / 100)
        print(f'Descontando {n3:.0f}% de {n2:.0f}, fica igual a: {descont:.0f}!')
    if n1 == 2:
        aument = n2 * ((100 + n3) / 100)
        print(f'Aumentando {n3:.0f}% de {n2:.0f}, fica igual a: {aument:.0f}!')
    if n1 == 3:
        n2 = float(input('Valor total que você tem: '))
        n3 = float(input('Valor percentual: '))
    if n1 == 0:
        break
sleep(2)
print('FIM DO PROGRAMA!')
print('VOLTE SEMPRE!')
