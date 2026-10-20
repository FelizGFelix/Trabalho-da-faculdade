import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


pilha_dados = []

def inserir():
    limpar()
    dado = input("Digite o valor a ser adicionado na pilha: ")

    pilha_dados.append(dado)

    print("Dado inserido com sucesso!")


def retirar():
    limpar()

    pilha_dados.pop()

    print("Operação realizada com sucesso!")

def visualizar():
    limpar()
    for i in pilha_dados:
        print(i)

    print("--------------------")

    input("Digite qualquer valor para retornar: ")
    limpar()


def main():
    resposta = 0

    while True:
        resposta = int(input("1 - inserir dados\n2 - retirar dados\n3 - visualizar dados\n->"))


        if resposta == 1:
            inserir()

        elif resposta == 2:
            retirar()

        elif resposta == 3:
            visualizar()

if __name__ == "__main__":
    main()