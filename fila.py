import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

fila_dados = []

def inserir():
    limpar()
    dado = input("Digite o dado a ser interido: ")

    fila_dados.append(dado)

    print("Operação realizada com sucesso!")

def retirada():
    limpar()

    del fila_dados[0]

    print("Operação realizada com sucesso!")

def visualizar():
    limpar()

    for i in fila_dados:
        print(i)

    print("---------------")

    input("Digite qualquer valor para retornar: ")

def main():
    resposta = 0

    while True:
        resposta = int(input("1 - inserir\n2 - retirar\n3 - visualizar\n->"))

        if resposta == 1:
            inserir()

        elif resposta == 2:
            retirada()

        elif resposta == 3:
            visualizar()

if __name__ == "__main__":
    main()