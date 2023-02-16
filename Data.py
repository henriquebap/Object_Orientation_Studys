class Calendario:

    def __init__(self, d, m, a,):
        self.dia = d
        self.mes = m
        self.ano = a

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))

class Retangulo:

    def __init__(self, x, y):
                self.__x = x
                self.__y = y
                self.__area = x * y

    def obter_area(self):
                return self.__area