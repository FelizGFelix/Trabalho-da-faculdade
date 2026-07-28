import sqlite3
import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def cadastro():
    limpar()
    class Cliente():
        def __init__(self):
            self.nome = ""
            self.cpf = 0
            self.credito = 0
            self.endereco = ""
            self.cep = 0
            self.cidade = ""
            self.estado = ""
            self.cargo = ""

        def cadastro_iniciar(self):
            print("Bem-vindo ao sistema de cadastro de funcionários da Hells Market")
            print("Para iniciar preenchencha o campo de informações básicas:")

            self.nome = input("Digite o seu nome: ")
            self.cpf = int(input("Digite o seu CPF: "))
            self.credito = float(input("Digite o seu limite de crédito: "))
            self.endereco = input("Digite o seu endereço: ")
            self.cep = int(input("Digite o seu CEP: "))
            self.cidade = input("Digite a cidade em que vive: ")
            self.estado = input("Digite o estado em que vive: ")
            self.cargo = input("Digite o seu cargo na empresa: ")

            ficha_funcionario = {
                "Nome" : self.nome,
                "CPF" : self.cpf,
                "Crédito" : self.credito,
                "Endereço" : self.endereco,
                "CEP" : self.cep,
                "Cidade" : self.cidade,
                "Estado" : self.estado,
                "Cargo" : self.cargo
            }

            limpar()

            print("Cadastro Finalizado!")

            return ficha_funcionario

    funcionario = Cliente()
    funcinario_cadastrado = funcionario.cadastro_iniciar()

    banco = sqlite3.connect("hell_market_funcionarios.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS hells_market ('Código' INTEGER, 'Nome' TEXT, 'CPF' INTEGER UNIQUE, 'Crédito' REAL, 'Endereço' TEXT, 'CEP' INTEGER UNIQUE, 'Cidade' TEXT, 'Estado' TEXT, 'Cargo' TEXT, PRIMARY KEY('Código'))")
    cursor.execute("INSERT INTO hells_market (Nome, CPF, Crédito, Endereço, CEP, Cidade, Estado, Cargo) VALUES (:Nome, :CPF, :Crédito, :Endereço, :CEP, :Cidade, :Estado, :Cargo)", funcinario_cadastrado)
    banco.commit()
    banco.close()

def mostrar_funcionarios():
    limpar()

    banco = sqlite3.connect("hell_market_funcionarios.db")
    banco.row_factory = sqlite3.Row
    cursor = banco.cursor()
    cursor.execute("SELECT * from hells_market")
    dict_list = [dict(row) for row in cursor.fetchall()]

    for i in dict_list:
        print("---------------------------------")
        print("Nome: ", i["Nome"])
        print("CPF: ", i["CPF"])
        print("Crédito: ", i["Crédito"])
        print("Endereço: ", i["Endereço"])
        print("CEP: ", i["CEP"])
        print("Cidade: ", i["Cidade"])
        print("Estado: ", i["Estado"])
        print("Cargo: ", i["Cargo"])

    print("-------------------------------------")
    input("Digite qualquer valor para retornar: ")


def main():
    resposta = 0

    while True:
        resposta = int(input("1 - Cadastrar Funcionário \n2 - Mostrar funcionários\n"))

        if resposta == 1:
            cadastro()

        if resposta == 2:
            mostrar_funcionarios()



if __name__ == "__main__":
    main()
