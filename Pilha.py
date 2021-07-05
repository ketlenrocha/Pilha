from No import No
class Pilha:
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        novo_nodo = No(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossível remover valor de pilha vazia."
        self.topo = self.topo.anterior


    def imprimir(self):

        print(f"{self.topo}")
