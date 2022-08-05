from Aviao import *

class Veiculo:

    def __init__(self, capacidade, matricula):
        self.capacidade = capacidade
        self.matricula = matricula
        self.aviao = Aviao()

    def getCapacidade(self):
        return self.capacidade

    def setCapacidade(self):
        self.capacidade = int(input("Capacidade: "))

    def getMatricula(self):
        return self.matricula

    def setMatricula(self):
        self.matricula = str(input("\nMatricula: "))

    def setAviao(self, aviao):
        self.aviao = aviao

    def getAviao(self,aviao):
        print(self.aviao.informacoes_aviao())
        print("Matrícula- " + self.matricula)
        print("Capacidade- " + str(self.capacidade))
