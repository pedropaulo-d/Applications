class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrair(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}.')

    def depositar(self, valor):
        self.__saldo += valor

    def __podesacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if self.__podesacar(valor):
            self.__saldo -= valor

    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}


class Data:

    def __init__(self, dia, mes, ano):
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    @property
    def data(self):
        return (f'{self.dia}/{self.mes}/{self.ano}')
