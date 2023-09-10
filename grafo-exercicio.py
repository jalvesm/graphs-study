import os

class GrafoDirecionado:
    
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.lista_adjacencia[origem].append(destino)

    def mostrar_grafo(self):
        for vertice, vizinhos in self.lista_adjacencia.items():
            print(f"{vertice} -> {', '.join(vizinhos)}")

    def forward_star(self, vertice):
        if vertice in self.lista_adjacencia:
            return self.lista_adjacencia[vertice]

    def reverse_star(self, vertice):
        reverse_star = []
        for v, vizinhos in self.lista_adjacencia.items():
            if vertice in vizinhos:
                reverse_star.append(v)
        return reverse_star

    def grau_entrada(self, vertice):
        if vertice in self.lista_adjacencia:
            grau = 0
            for v in self.lista_adjacencia:
                if vertice in self.lista_adjacencia[v]:
                    grau += 1
            return grau

    def grau_saida(self, vertice):
        if vertice in self.lista_adjacencia:
            return len(self.lista_adjacencia[vertice])


def validar_nome_arquivo(nome_arquivo):
    if not nome_arquivo:
        print("O nome do arquivo não pode estar vazio.")
        return False
    if not os.path.isfile(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return False
    return True


def ler_grafo_de_arquivo(nome_arquivo):
    grafo = GrafoDirecionado()
    
    with open(nome_arquivo, 'r') as arquivo:
        primeira_linha = True
        for linha in arquivo:
            if primeira_linha:
                primeira_linha = False
                continue
            origem, destino = linha.strip().split()
            origem = int(origem)
            destino = int(destino)
            grafo.adicionar_aresta(origem, destino)
    return grafo

def mostra_grau_de_saida(vertice_num): 
    print(f"I) Grau de saída de {vertice_num}: {meu_grafo.grau_saida(vertice_num)}")

def mostra_grau_de_entrada(vertice_num): 
    print(f"II) Grau de entrada de {vertice_num}: {meu_grafo.grau_entrada(vertice_num)}")
    
def mostra_Sucessores(vertice_num):
    print(f"III) Conjunto de sucessores de {vertice_num}:\t{meu_grafo.forward_star(vertice_num)}")
    
def mostra_Predecessores(vertice_num):
    print(f"IV) Conjunto de predecessores de {vertice_num}:\t{meu_grafo.reverse_star(vertice_num)}")
        
if __name__ == "__main__":
    while True:
        nome_arquivo = input("Digite o nome do arquivo: ")
        if validar_nome_arquivo(nome_arquivo):
            meu_grafo = ler_grafo_de_arquivo(nome_arquivo)                
            while True:
                entrada = input("Número do vértice: ")
                try:
                    vertice = int(entrada)
                    break
                except ValueError:
                    print("Por favor, digite um número inteiro válido.")
            
            print("\n--- OUTPUT ---")
            mostra_grau_de_saida(vertice)
            mostra_grau_de_entrada(vertice)
            mostra_Sucessores(vertice)
            mostra_Predecessores(vertice)
            
            break