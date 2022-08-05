from Pessoa import *

class Piloto (Pessoa):

    def __init__(self, nome = '', nacionalidade = '', idade = 0, carta_piloto =''):
        super().__init__(nome, nacionalidade, idade)
        self.carta_piloto = carta_piloto

    def getCarta(self):
        return self.carta_piloto
    
    def setcarta(self):
        self.carta_piloto = str(input("Carta de Piloto: "))


    def mostra_pilotos (self):
        print("\n____Informações Piloto____\n")
        super().print()
        print("Carta de Piloto- " + self.carta_piloto)