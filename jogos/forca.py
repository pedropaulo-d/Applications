from random import randint

#CÓDIGO PRINCIPAL DO JOGO
def forca():

    mensagem_inicial()
    palavra_secret = gerar_palavra()
    palavras_restantes = inicial_letras(palavra_secret)
    enforcou = False
    acertou = False
    erros = 0
    palavra_inicial(palavras_restantes)

    while not enforcou and not acertou:
        resp = str(input('Qual letra? ')).strip().upper()
        if resp in palavra_secret:
            chute_correto(resp, palavra_secret, palavras_restantes)
        else:
            erros += 1
            perde_forca(erros)
        if erros > 7:
            enforcou = True
        if "_" not in palavras_restantes:
            acertou = True
        print(f'{palavras_restantes}')
        print(f'Ainda resta {palavras_restantes.count("_")} letras.')
    print('*' * 33)
    print('FIM DO JOGO!')
    mensagem_ganhador(acertou, palavra_secret)
    mensagem_perdedor(enforcou, palavra_secret)

#FUNÇÕES DO JOGO
def mensagem_inicial():
    print('*'*33)
    print('BEM VINDO AO JOGO DA FORCA!')
    print('*'*33)

def gerar_palavra():
    palavras_random = []
    arquivo = open('palavras.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        palavras_random.append(linha)
    arquivo.close()
    num_random = randint(0, len(palavras_random) - 1)
    palavra_secret = palavras_random[num_random].upper()
    return palavra_secret

def inicial_letras(palavra):
    return ['_' for letras in palavra]

def chute_correto(resp, palavra_secret, palavras_restantes):
    cont = 0
    for letra in palavra_secret:
        if resp == letra:
            palavras_restantes[cont] = letra
        cont += 1

def palavra_inicial(palavras_restantes):
    print('PALAVRA SECRETA:')
    print()
    print(palavras_restantes)
    print()
    print('É UMA FRUTA!')
    print('*' * 33)

#Mensagens Especiais
def mensagem_perdedor(enforcou, palavra_secret):
    if enforcou == True:
        print('VOCÊ FOI ENFORCADO!!')
        print(f'A PALAVRA SECRETA ERA: {palavra_secret}!')
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def mensagem_ganhador(acertou, palavra_secret):
    if acertou == True:
        print(f'A PALAVRA SECRETA ERA: {palavra_secret}!')
        print('PARABÉNS, VOCÊ GANHOU O JOGO!!')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def perde_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    print('Puts, palavra errada!')
    print()

if __name__ == '__main__':
    forca()
