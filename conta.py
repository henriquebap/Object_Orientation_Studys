class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite