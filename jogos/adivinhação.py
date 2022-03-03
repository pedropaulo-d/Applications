from random import randint

def adivinhacao():
    mensagem_inicial()

    pontos = 1000
    total_de_tentativas = 0
    rodada = 1
    numero_secreto = randint(1, 100)

    dif = pergunta1_usuario()

    if dif == 1:
        total_de_tentativas = 20
    elif dif == 2:
        total_de_tentativas = 10
    elif dif == 3:
        total_de_tentativas = 5
    while total_de_tentativas > 0:
        print('*'*33)
        print(f'PONTUAÇÃO ATUAL: {pontos}')
        print(f'Tentativa {rodada}, você ainda tem {total_de_tentativas} tentativas')
        chute = int(input("Digite um número entre 1 e 100: "))
        if chute < 1 or chute > 100:
            print('ERRO! Digite um número entre 1 e 100.')
            continue
        print(f"Você digitou: {chute}")
        total_de_tentativas -= 1
        rodada += 1
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns! Você ACERTOU!")
            print('*'*33)
            break
        else:
            if maior:
                print('Você ERROU! Seu chute foi MAIOR que o número secreto!')
            elif menor:
                print('Você ERROU! Seu chute foi MENOR que o número secreto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    mensagem_final(numero_secreto, pontos)

def mensagem_inicial():
    print('*' * 33)
    print("Bem vindo ao jogo de Adivinhação!")
    print('*' * 33)

def pergunta1_usuario():
    print('Qual o nível de dificuldade?')
    print('[ 1 ] FÁCIL, [ 2 ] MÉDIO, [ 3 ] DIFÍCIL')
    dif = int(input('Defina o nível: '))
    return dif

def mensagem_final(numero_secreto, pontos):
    print('*' * 33)
    print("Fim do jogo!")
    print(f'O número secreto era: {numero_secreto}!')
    print(f'Sua pontuação final foi: {pontos}.')

if __name__ == '__main__':
    adivinhacao()
