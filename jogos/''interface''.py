from time import sleep
from forca import forca
from adivinhacao import adivinhacao
from funções import ponto
print('*'*33)
print('ESCOLHA O SEU JOGO!')
print('*'*33)
while True:
    print('*'*33)
    print('[ 1 ] ADIVINHAÇÃO')
    print('[ 2 ] FORCA')
    print('[ 0 ] ENCERRAR PROGRAMA')
    print('*'*33)
    escolha = int(input('Opção: '))
    if escolha == 1:
        print('INCIANDO O JOGO DE ADIVINHAÇÃO!')
        ponto()
        sleep(1.0)
        adivinhacao()
    elif escolha == 2:
        print('INICIANDO O JOGO DA FORCA!')
        ponto()
        sleep(1.0)
        forca()
    elif escolha < 0 or escolha > 2:
        print('ERRO! ESCOLHA UMA OPÇÃO VÁLIDA!')
        escolha = int(input('Opção: '))
    elif escolha == 0:
        break
print('*'*33)
print('FIM DO PROGRAMA!')
