grafo = {}

def adicionar_no(grafo, no):
    if no not in grafo:
        grafo[no] = []

    else:
        print(f"O no {no} já existe!")

def adicionar_aresta(grafo, no1, no2):
    if no1 not in grafo:
        adicionar_no(grafo, no1)

    if no2 not in grafo:
        adicionar_no(grafo, no2)

    #Adicionar conexões
    grafo[no1].append(no2)
    grafo[no2].append(no1)

def listar_grafo(grafo):
    print("Estrutura do grafo: ")
    for no in grafo:
        print(f"{no} -> {grafo[no]}")


#Testar o grafo
cidade = input("Digite a cidade: ")
adicionar_no(grafo, cidade)

cidade = input("Digite a cidade: ")
adicionar_no(grafo, cidade)

cidade = input("Digite a cidade: ")
adicionar_no(grafo, cidade)

cidade = input("Digite a cidade: ")
adicionar_no(grafo, cidade)

#Adicionar as arestas
cidade_origem = input("Digite a cidade de origem: ")
cidade_destino = input("Digite a cidade de destino: ")
adicionar_aresta(grafo, cidade_origem, cidade_destino)

cidade_origem = input("Digite a cidade de origem: ")
cidade_destino = input("Digite a cidade de destino: ")
adicionar_aresta(grafo, cidade_origem, cidade_destino)

cidade_origem = input("Digite a cidade de origem: ")
cidade_destino = input("Digite a cidade de destino: ")
adicionar_aresta(grafo, cidade_origem, cidade_destino)

cidade_origem = input("Digite a cidade de origem: ")
cidade_destino = input("Digite a cidade de destino: ")
adicionar_aresta(grafo, cidade_origem, cidade_destino)

#listar
listar_grafo(grafo)