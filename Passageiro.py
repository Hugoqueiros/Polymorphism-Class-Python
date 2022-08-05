from Pessoa import *

class Passageiro(Pessoa):

    def __init__(self, nome, nacionalidade, idade, passaporte):
        super().__init__(nome, nacionalidade, idade)
        self.passaporte = passaporte

    def getPassaporte(self):
        return self.passaporte
    
    def setPassaporte(self):
        self.passaporte = str(input("Passaporte: "))


    def mostra_passageiro(self):
        print("\n____Informações Passageiro____\n")
        super().print()
        print("Passaporte- " + self.passaporte)