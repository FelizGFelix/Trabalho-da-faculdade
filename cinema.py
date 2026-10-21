import os
import networkx as nx

grafo = nx.Graph()

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def retorno():
    print("--------------------")
    input("Digite qualquer valor para retornar: ")
    limpar()

class CinemaCon():
    def __init__(self):
        self.cinema = ""
        self.cidade = ""
        self.loc = ""
        self.preco = 0
        self.ponto = ""
        self.referencia = ""

    def adicionar_no(self):
        limpar()
        self.cinema = input("Digite o nome do cinema: ").upper()
        self.cidade = input("Digite a cidade em que esse cinema fica: ").upper()
        self.loc = input("Digite a localização: ").upper()
        preco_int = float(input("Digite o preço do ingreço: "))

        self.preco = (preco_int * 50) / 100

        self.ponto = input("Digite o ponto de ônibus que leva para lá: ").upper()

        conexao = {
            "Nome do Cinema" : self.cinema,
            "Localização" : self.loc,
            "Preço (inteiro)" : preco_int,
            "Preço (meia entrada)" : self.preco,
            "Ônibus" : self.ponto
        }

        grafo.add_node(self.cinema, **conexao)

        limpar()

        #print(grafo.nodes())
        #print(grafo.nodes(data=True))

        return conexao, grafo

cinema = CinemaCon()

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - ADICIONAR CINEMA\n2 - LISTAR GRAFOS\n3 - CONEXÕES\n->"))

        if resposta == 1:
            cinema.adicionar_no()

if __name__ == "__main__":
    main()