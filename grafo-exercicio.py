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

if __name__ == "__main__":
    nome_arquivo = input("Nome do arquivo: ")
    meu_grafo = ler_grafo_de_arquivo(nome_arquivo)

    while True:
        entrada = input("Número do vértice: ")
        try:
            vertice = int(entrada)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    
    print(f"Forward Star de {vertice}: {meu_grafo.forward_star(vertice)}")
    print(f"Reverse Star de {vertice}: {meu_grafo.reverse_star(vertice)}")
    print(f"Grau de Entrada de {vertice}: {meu_grafo.grau_entrada(vertice)}")
    print(f"Grau de Saída de {vertice}: {meu_grafo.grau_saida(vertice)}")