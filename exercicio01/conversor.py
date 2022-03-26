class Conversor:
    def __init__(self, medida, escolha):
        self.__medida = medida
        self.__escolha = escolha

    def medida(self):
        return self.__medida

    def uni_medida(self):
        if self.__escolha == 1:
            self.__unidade = 'milha(s)'
        elif self.__escolha == 2:
            self.__unidade = 'polegada(s)'
        elif self.__escolha == 3:
            self.__unidade = 'pé(s)'
        elif self.__escolha == 4:
            self.__unidade = 'centímetro(s)'
        elif self.__escolha == 5:
            self.__unidade = 'metro(s)'
        elif self.__escolha == 6:
            self.__unidade = 'quilometro(s)'
        return self.__unidade

    def milha(self):
        # converter milha para milha
        if self.__escolha == 1:
            self.__milha = self.__medida
            return self.__milha
        # converter polegada para milha
        elif self.__escolha == 2:
            self.__milha = self.__medida / 63360
            return self.__milha
        # converter pe para milha
        elif self.__escolha == 3:
            self.__milha = self.__medida * 0.000189394
            return self.__milha
        # converter centimetro para milha
        elif self.__escolha == 4:
            self.__milha = self.__medida / 160000
            return self.__milha
        # converter metro para milha
        elif self.__escolha == 5:
            self.__milha = self.__medida / 1600
            return self.__milha
        # converter quilometro para milha
        elif self.__escolha == 6:
            self.__milha = self.__medida / 1.6
            return self.__milha

    def polegada(self):
        # converter milha para polegada
        if self.__escolha == 1:
            self.__polegada = self.__medida * 63360
            return self.__polegada
        # converter polegada para polegada
        elif self.__escolha == 2:
            self.__polegada = self.__medida
            return self.__polegada
        # converter pe para polegada
        elif self.__escolha == 3:
            self.__polegada = self.__medida * 12
            return self.__polegada
        # converter centimetro para polegada
        elif self.__escolha == 4:
            self.__polegada = self.__medida / 2.54
            return self.__polegada
        # converter metro para polegada
        elif self.__escolha == 5:
            self.__polegada = self.__medida / 0.0254
            return self.__polegada
        # converter quilometro para polegada
        elif self.__escolha == 6:
            self.__polegada = self.__medida * 39370.08
            return self.__polegada

    def pe(self):
        # converter milha para pe
        if self.__escolha == 1:
            self.__pe = self.__medida * 5280
            return self.__pe
        # converter polegada para pe
        elif self.__escolha == 2:
            self.__pe = self.__medida / 12
            return self.__pe
        # converter pe para pe
        elif self.__escolha == 3:
            self.__pe = self.__medida
            return self.__pe
        # converter centimetro para pe
        elif self.__escolha == 4:
            self.__pe = self.__medida / 30.48
            return self.__pe
        # converter metro para pe
        elif self.__escolha == 5:
            self.__pe = self.__medida / 0.3048
            return self.__pe
        # converter quilometro para pe
        elif self.__escolha == 6:
            self.__pe = self.__medida * 3280.84
            return self.__pe

    def centimetro(self):
        # converter milha para centimetro
        if self.__escolha == 1:
            self.__centimetro = self.__medida * 160000
            return self.__centimetro
        # converter polegada para centimetro
        elif self.__escolha == 2:
            self.__centimetro = self.__medida * 2.54
            return self.__centimetro
        # converter pe para centimetro
        elif self.__escolha == 3:
            self.__centimetro = self.__medida * 30.48
            return self.__centimetro
        # converter centimetro para centimetro
        elif self.__escolha == 4:
            self.__centimetro = self.__medida
            return self.__centimetro
        # converter metro para centimetro
        elif self.__escolha == 5:
            self.__centimetro = self.__medida * 100
            return self.__centimetro
        # converter quilometro para centimetro
        elif self.__escolha == 6:
            self.__centimetro = self.__medida * 100000
            return self.__centimetro

    def metro(self):
        # converter milha para metro
        if self.__escolha == 1:
            self.__metro = self.__medida * 1600
            return self.__metro
        # converter polegada para metro
        elif self.__escolha == 2:
            self.__metro = self.__medida * 0.0254
            return self.__metro
        # converter pe para metro
        elif self.__escolha == 3:
            self.__metro = self.__medida * 0.3048
            return self.__metro
        # converter centimetro para metro
        elif self.__escolha == 4:
            self.__metro = self.__medida / 100
            return self.__metro
        # converter metro para metro
        elif self.__escolha == 5:
            self.__metro = self.__medida
            return self.__metro
        # converter quilometro para metro
        elif self.__escolha == 6:
            self.__metro = self.__medida * 1000
            return self.__metro

    def quilometro(self):
        # converter milha para quilometro
        if self.__escolha == 1:
            self.__quilometro = self.__medida * 1.6
            return self.__quilometro
        # converter polegada para quilometro
        elif self.__escolha == 2:
            self.__quilometro = self.__medida * 0.0000254
            return self.__quilometro
        # converter pe para quilometro
        elif self.__escolha == 3:
            self.__quilometro = self.__medida * 0.0003048
            return self.__quilometro
        # converter centimetro para quilometro
        elif self.__escolha == 4:
            self.__quilometro = self.__medida / 100000
            return self.__quilometro
        # converter metro para quilometro
        elif self.__escolha == 5:
            self.__quilometro = self.__medida / 1000
            return self.__quilometro
        # converter quilometro para quilometro
        elif self.__escolha == 6:
            self.__quilometro = self.__medida
            return self.__quilometro