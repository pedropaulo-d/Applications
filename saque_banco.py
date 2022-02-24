print('-='*30)
print('{:^30}'.format(' BANCO PP'))
print('-='*30)
valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
ced50 = 50
totalced = 0
while True:
    if total >= ced50:
        total -= ced50
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${ced50}')
        if ced50 == 50:
            ced50 = 20
        elif ced50 == 20:
            ced50 = 10
        elif ced50 == 10:
            ced50 = 1
        totalced = 0
        if total == 0:
            break
print('{:-^30}'.format(' VOLTE SEMPRE! '))
