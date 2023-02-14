#Declarando as nomeclaturas em dicionario dentro de uma tupla.
siglas = ({'BAIRRONOVO': 'BRD.PVO.BNO.COA',
          'CANDEIAS': 'BRD.CDEY.PLH.COA',
          'DOMPEDRO': 'BRD.PVO.DPD.COA',
          'ELDORADO': 'BRD.PVO.ELD.COA',
          'GLOBOFIBER': 'BRD.PVO.GFB.COA',
          'ITAPUA': 'BRD.ITDO.CNT.COA',
          'NOVOHORIZONTE': 'BRD.PVO.NOH.COA',
          'TRANSAMAZONICA': 'BRD.PVO.TRN.COA',
          'VILAVERDE': 'BRD.PVO.VLV.COA',
          'VILAVERDEII': 'BRD.PVO.VLV.COC',
          'SAOFRANCISCO': 'BRD.PVO.SAF.COA',
          'NOVAMUTUM': 'BRD.PVO.NVM.COA',
          'DOMPEDROII': 'BRD.PVO.DPD.COB',
          'ULISSES': 'BRD.PVO.UGM.COA',
          'VILAVERDEIII': 'BRD.PVO.VLV.COD',
          'JARDIMAMERICA': 'BRD.PVO.JAME.COA',
          'JACIPARANA': 'BRD.PVO.JAPA.COA',
          'SANTOANTONIO': 'BRD.PVO.STAN.COA',
          'HUMAITA': 'BRD.HUT.NHV.COA'})

#Função para a formatação da nomeclatura.
def nomeclatura(modo, olt, mac, slot, pon, siglas):
    if modo == 2 or olt == 'CANDEIAS':
        formatacao = (f'{siglas[olt]}.' + f'{slot}.' + f'{pon}.' + f'{mac}')
    else:
        formatacao = (f'{siglas[olt]}.'+f'{slot}.'+f'{pon}.'+f'{mac}'+'@brd')
    return formatacao

#Função para a formatação das informações que serão printadas.
def display_infos(modo, mac, olt, slot, pon, sinal, vlan, user, senha):
    print(f'*LEMBRE DE HABILITAR O ACESSO REMOTO!*\n'
          f'- MAC/SERIAL: {mac}\n'
          f'- OLT: {olt}\n'
          f'- SLOT: {slot}\n'
          f'- PON: {pon}\n'
          f'- Sinal: -{sinal}\n'
          f'- VLAN: {vlan}')

    if modo == 3:
        print(f'- Usuário: {user}\n'
                f'- Senha: {senha}\n')

    if modo == 1 or modo == 2:
            print(f'- Nomeclatura: {nomeclatura(modo, olt, mac, slot, pon, siglas)}')

    print('-=' * 30)

#Tela onde tudo é exibido no final.
def printout_info():

    while True:
        modo = int(input('[ 1 ] - IPOE\n'
                         '[ 2 ] - IPOE1G\n'
                         '[ 3 ] - PPPOE\n'
                         '----> '))
        olt = str(input('OLT: ')).upper().strip().replace(" ", "")
        mac = input('MAC/SERIAL: ')
        slot = int(input('SLOT: '))
        pon = int(input('PON: '))
        sinal = float(input('SINAL: -'))
        print('-='*30)
        vlan = 0
        user = ''
        senha = ''

        if modo == 1:
            vlan = 2020

        elif modo == 2:
            vlan = 2022

        elif modo == 3:
            vlan = 2000
            user = str(input('Usário: '))
            senha = int(input('Senha: '))
            print('-=' * 30)

        if modo == 3:
            if olt == 'ITAPUA' or olt == 'ECOVILLEIII':
                vlan = 2001

        display_infos(modo, mac, olt, slot, pon, sinal, vlan, user, senha)

        continua = str(input('Continuar? ')).upper().strip()[0]
        print('-='*30)
        if continua == 'N':
            break

    print('FIM DO PROGRAMA!')

if(__name__ == '__main__'):
    printout_info()
