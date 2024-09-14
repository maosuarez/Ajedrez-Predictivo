import networkx as nx
import matplotlib.pyplot as plt

class Prediccion:
    def __init__(self) -> None:
        self.G = nx.Graph()
        self.lista_nodos = []

    def imprimir(self):
        print("nodos",self.G.nodes())
        print("aristas" ,self.G.edges())

    def agregar_nodos(self, lista):
        self.G.add_nodes_from(lista)
        self.lista_nodos += lista

    def delete_nodo(self, nodo):
        self.G.remove_node(nodo)

    def limpiar_grafo(self):
        self.G.clear
    
    def agregar_aristas(self,salida,lista):
        for llegada in lista:
            if (salida,llegada) not in  self.G.edges() and (llegada,salida) not in self.G.edges():
                self.G.add_edge(salida,llegada,weight=1)
    
    def Camino_corto():
        pass

    def mostrar(self):
        nx.draw(self.G, with_labels=True)
        plt.margins(0.2)
        plt.show()

    def short_path(self,inicio, fin):
        path = nx.dijkstra_path(self.G, source=inicio, target=fin)
        return path



