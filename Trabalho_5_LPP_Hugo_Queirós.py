from Veiculo import *
from Aviao import *
from Pessoa import *
from Passageiro import *
from Piloto import *

i = 0
opcao= 0
aviao_inserido = False

print("____GESTÃO DO AEROPORTO____")

while aviao_inserido == False :

    #é criado um transporte e um tipo de trasnporte onde são declarados os atributos
    transporte = Veiculo (0,'')
    aviao = Aviao('', '', 0, 0)
    transporte.setMatricula()
    aviao.setOrigem()
    aviao.setDestino()
    transporte.setCapacidade()
    aviao.setLotacao_pi()
    aviao.setLotacao_pa()
    transporte.setAviao(aviao)

    pilotos= []
    passageiros = []

    #verificações para o avião ser adicionado e passar ao menu
    if aviao.getLotacao_pa() + aviao.getLotacao_pi() <= transporte.getCapacidade() and transporte.getMatricula != ''  and aviao.getOrigem() != '' and aviao.getOrigem() != '' and aviao.getDestino() != '' and  transporte.getCapacidade() != '' and aviao.getLotacao_pi() != '' and aviao.getLotacao_pa() != '':
        aviao_inserido = True
        while opcao != 6:
            print()
            print ('''[ 1 ] Inserir Passageiros 
[ 2 ] Inserir Pilotos
[ 3 ] Lista de Passageiros
[ 4 ] Lista de Pilotos
[ 5 ] Informações do Avião
[ 6 ] Sair ''')
            opcao= int(input("\nEscolha uma das opções: "))

            if opcao == 1 :
                for i in range (0, aviao.getLotacao_pa()):
                    print("\n____Adicionar Passageiros____")
                    pa = Passageiro('', '', 1, '')
                    pa.setNome()
                    pa.setNacionalidade()
                    pa.setIdade()
                    pa.setPassaporte()
                    passageiros.append(pa)
                    #após inserção de todos os atributos é adicionado à lista criada para os passageiros

            if opcao == 2 :
                for i in range (0, aviao.getLotacao_pi()):
                    print("\n____Adicionar Piloto____")
                    pi = Piloto('', '', 1, '')
                    pi.setNome()
                    pi.setNacionalidade()
                    pi.setIdade()
                    pi.setcarta()
                    pilotos.append(pi)
                    #após inserção de todos os atributos é adicionado à lista criada para os passageiros

            if opcao == 3:
                for i in range (0, len(passageiros)):
                    #ciclo for que percorre a lista e printa todos os passageiros
                    passageiros[i].mostra_passageiro()

            if opcao == 4:
                for i in range (0, len(pilotos)):
                    #ciclo for que percorre a lista e printa todos os passageiros
                    pilotos[i].mostra_pilotos()

            if opcao == 5:
                #mostra as informações do avião
                print(transporte.getAviao(aviao))
    
    else :
        print("\nDados Inseridos Inválidos. Tente Novamente.\n")