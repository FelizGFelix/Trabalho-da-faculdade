import networkx as nx

grafo = nx.Graph()

#com adicionar um nó
grafo.add_node("Curitiba")
grafo.add_node("Campo Largo")
grafo.add_node("Pinhais")

#criar arestas
grafo.add_edge("Curitiba", "Campo Largo")

print(grafo)
print(grafo.nodes)
print(grafo.edges)