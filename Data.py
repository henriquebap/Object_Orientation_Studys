class Calendario:

    def __init__(self, d, m, a,):
        self.dia = d
        self.mes = m
        self.ano = a

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))