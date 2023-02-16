class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def extrato(self):
        print("Saldo de R${} do pobre titular {}".format(self.saldo, self.titular))
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, saque):
        self.saldo -= saque
        print("Seu saldo restante é {}".format(self.saldo))

