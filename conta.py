class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("Saldo de R${} do pobre titular {}".format(self.__saldo, self.__titular))
    def deposito(self, valor):
        self.__saldo += valor
    def saque(self, saque):
        self.__saldo -= saque
        print("Seu saldo restante é {}".format(self.__saldo))

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.desposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
