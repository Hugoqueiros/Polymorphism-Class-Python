from Veiculo import *

class Aviao():

    def __init__(self, origem = '', destino = '', lotacao_pa = 0, lotacao_pi = 0):
        self.origem = origem
        self.destino = destino
        self.lotacao_pa = lotacao_pa
        self.lotacao_pi = lotacao_pi


    
    def getOrigem(self):
        return self.origem

    def setOrigem(self):
        self.origem = str(input("Origem: "))

    def getDestino(self):
        return self.destino

    def setDestino(self):
        self.destino = str(input("Destino: "))

    def getLotacao_pa(self):
        return self.lotacao_pa

    def setLotacao_pa(self):
        self.lotacao_pa = int(input("Passageiros a Bordo: "))

    def getLotacao_pi(self):
        return self.lotacao_pi

    def setLotacao_pi(self):
        self.lotacao_pi = int(input("Pilotos a Bordo: "))

    def informacoes_aviao(self):
        return "\n____Informações do Aviao____ " + "\nOrigem- " + self.origem +"\nDestino- " + self.destino + "\nLotação Passageiros- " + str(self.lotacao_pa) + "\nLotação Pilotos- " + str(self.lotacao_pi)
