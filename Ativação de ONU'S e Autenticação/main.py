#Declarando as nomeclaturas em dicionario dentro de uma tupla.
siglas = ({'BAIRRONOVO': 'BRD.PVO.BNO.COA.',
          'CANDEIAS': 'BRD.CDEY.PLH.COA',
          'DOMPEDRO': 'BRD.PVO.DPD.COA',
          'ECOVILLEII': 'BRD.PVO.ECV.COB',
          'ECOVILLEIII': 'BRD.PVO.ECV.COC',
          'ELDORADO': 'BRD.PVO.ELD.COA',
          'GLOBOFIBER': 'BRD.PVO.GFB.COA',
          'ITAPUA': 'BRD.ITDO.CNT.COA',
          'NOVOHORIZONTE': 'BRD.PVO.NOH.COA',
          'TRANSAMAZONICA': 'BRD.PVO.TRN.COA',
          'VILAVERDE': 'BRD.PVO.VLV.COA',
          'VILAVERDEII': 'BRD.PVO.VLV.COC',
          'SAOFRANCISCO': 'BRD.PVO.SAF.COA',
          'NOVAMUTUM': 'BRD.PVO.NVM.COA',
          'GUAJARAMIRIM': 'BRD.GUM.CNT.COA',
          'NOVAMAMORE': 'BRD.NVME.CNV.COA',
          'DOMPEDROII': 'BRD.PVO.DPD.COB',
          'ULISSES': 'BRD.PVO.UGM.COA',
          'VILAVERDEIII': 'BRD.PVO.VLV.COD',
          'JARDIMAMERICA': 'BRD.PVO.JAME.COA',
          'JACIPARANA': 'BRD.PVO.JAPA.COA',
          'SANTOANTONIO': 'BRD.PVO.STAN.COA',
          'HUMAITA': 'BRD.HUT.NHV.COA'})

#Função para a formatação da nomeclatura.
def nomeclatura(modo, olt, mac, slot, pon, siglas):
    if modo == 'IPOE1G' or olt == 'CANDEIAS':
        formatacao = (f'{siglas[olt]}.' + f'{slot}.' + f'{pon}.' + f'{mac}')
    else:
        formatacao = (f'{siglas[olt]}.'+f'{slot}.'+f'{pon}.'+f'{mac}'+'@brd')
    return formatacao

#Função para a formatação das informações que serão printadas.
def display_infos(modo, mac, olt, slot, pon, sinal, vlan, usuario, senha):
    print(f'-MAC/SERIAL: {mac}\n'
          f'-OLT: {olt}\n'
          f'-SLOT: {slot}\n'
          f'-PON: {pon}\n'
          f'-Sinal: -{sinal}\n'
          f'-VLAN: {vlan}')

    if modo == 'PPPOE':
        print(f'-Usuário: {usuario}\n'
                f'-Senha: {senha}\n')

    if modo == 'IPOE' or modo == 'IPOE1G':
            print(f'-Nomeclatura: {nomeclatura(modo, olt, mac, slot, pon, siglas)}')

    print('-=' * 30)

#Tela onde tudo é exibido no final.
def printout_info():

    while True:
        print('-='*-30)
        modo = str(input('IPOE, IPOE1G OU PPPOE? ')).upper().strip().replace(" ", "")
        olt = str(input('OLT: ')).upper().strip().replace(" ", "")
        mac = input('MAC/SERIAL: ')
        slot = int(input('SLOT: '))
        pon = int(input('PON: '))
        sinal = float(input('SINAL: -'))
        print('-='*30)
        vlan = 0
        usuario = ''
        senha = ''

        if modo == 'IPOE':
            vlan = 2020

        elif modo == 'IPOE1G':
            vlan = 2022

        elif modo == 'PPPOE':
            vlan = 2000
            usuario = str(input('Usário: '))
            senha = int(input('Senha: '))
            print('-=' * 30)

        if modo == 'PPPOE':
            if olt == 'ITAPUA' or olt == 'ECOVILLEIII':
                vlan = 2001

        display_infos(modo, mac, olt, slot, pon, sinal, vlan, usuario, senha)

        continua = str(input('Continuar? ')).upper().strip()[0]
        if continua == 'N':
            break

    print('FIM DO PROGRAMA!')

if(__name__ == '__main__'):
    printout_info()
