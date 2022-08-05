class Pessoa:

    def __init__(self, nome, nacionalidade, idade):
        #atributo protegido
        self._nome = nome
        #atributo público
        self.nacionalidade = nacionalidade
        #atributo privado
        self.__idade = idade

    def getNome(self):
        return self.nome

    def setNome(self):
        self.nome = str(input("Nome: "))

    def getNacionalidade(self):
        return self.nacionalidade

    def setNacionalidade(self):
        self.nacionalidade = str(input("Nacionalidade: "))

    def getIdade(self):
        return self.idade

    def setIdade(self):
        self.idade = int(input("Idade: "))
    
    def mostra_pessoa(self):
        print("Nome- " + self.nome + "\nNacionalidade- " + self.nacionalidade +"\nIdade- " + str(self.idade))

    def print(self):
        print("Nome- " + self.nome + "\nNacionalidade- " + self.nacionalidade +"\nIdade- " + str(self.idade))    