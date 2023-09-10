import os

class GrafoDirecionado:
    
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice na lista de adjacência caso ele não exista. 
        
        Args:
            vertice (int): vértice que será lido do arquivo.
        """
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino):
        """Adiciona um vértice origem à lista de adjacência e anexa seu respectivo destino, indicando a direção da relação desse par de vértices.

        Args:
            origem (int): Vértice no qual sai a aresta.
            destino (int): Vértice no qual a aresta entra.
        """
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.lista_adjacencia[origem].append(destino)

    def forward_star(self, vertice):
        """Recebe o vértice do usuário e verifica a existência desse vértice na lista de adjacência. Se esse vértice estiver presente na lista, é retornada lista com todos os vizinhos sucessores relacionados a esse vértice.

        Args:
            vertice (int): Valor inteiro informado pelo usuário.

        Returns:
            lista: Retorna dado do tipo lista contendo os sucessores do vértice inputado.
        """
        if vertice in self.lista_adjacencia:
            return self.lista_adjacencia[vertice]

    def reverse_star(self, vertice):
        """Verifica se existe uma aresta que sai do vértice de interesse (parâmetro) e vai para o vértice da iteração. Anexa o valor do vértice v na lista de predecessores. 

        Args:
            vertice (int): Vértice de interesse informado pelo usuário.

        Returns:
            list: Lista com os predecessores do vértice inputado pelo usuário.
        """
        reverse_star = []
        for v, vizinhos in self.lista_adjacencia.items():
            if vertice in vizinhos:
                reverse_star.append(v)
        
        return reverse_star

    def grau_entrada(self, vertice):
        """Recebe o vértice e calcula o número de elementos com arestas direcionadas a ele.
        
        Args:
            vertice (int): Vértice informado pelo usuário;

        Returns:
            int: Número de elementos contidos 
        """
        if vertice in self.lista_adjacencia:
            grau = 0
            for v in self.lista_adjacencia:
                if vertice in self.lista_adjacencia[v]:
                    grau += 1
            return grau

    def grau_saida(self, vertice):
        """Calcula o número de elementos da lista de adjacência de um vértice.

        Args:
            vertice (int): Vértice informado pelo usuário;

        Returns:
            int: quantidade de elementos contidos na lista de adjacência do vértice.
        """
        if vertice in self.lista_adjacencia:
            return len(self.lista_adjacencia[vertice])


def validar_nome_arquivo(nome_arquivo):
    """Valida nome do arquivo retornando 'False' para dois casos: 
    1º caso: usuário não informa nenhum valor no campo input.
    2º caso: usuário informa um nome que não corresponde aos arquivos contidos no diretório.

    Args:
        nome_arquivo (string): Nome do arquivo informado pelo usuário;

    Returns:
        bool: retorna True caso o nome seja válido. Retorna False caso o nome entre nos dois casos descritos acima.
    """
    if not nome_arquivo:
        print("O nome do arquivo não pode estar vazio.")
        return False
    if not os.path.isfile(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return False
    return True

def ler_grafo_de_arquivo(nome_arquivo):
    """O método abre o arquivo, pula a leitura da primeira linha e parte para as próximas linhas do arquivo lido.

    Args:
        nome_arquivo (string): Nome do arquivo informado pelo usuário;

    Returns:
        grafo: grafo conforme lido pelo arquivo (exceto primeira linha);
    """
    grafo = GrafoDirecionado()
    
    with open(nome_arquivo, 'r') as arquivo:
        primeira_linha = True
        for linha in arquivo:
            if primeira_linha:
                primeira_linha = False
                continue
            limpar_dados(linha, grafo)
    return grafo

def limpar_dados(linha_do_arquivo, grafo):
    """Limpa espaços vazios da última linha lida. Os dados remanescentes são separados em duas variáveis, são elas: os vértices de origem e destino da aresta. Converte os valores para o tipo inteiro. Adiciona essas variáveis ao grafo após conversão.

    Args:
        linha_do_arquivo (string): linha completa lida pelo arquivo, incluindo espaços vazios.
        grafo: representação do grafo no estado atual.
    """
    origem, destino = linha_do_arquivo.strip().split()
    origem = int(origem)
    destino = int(destino)
    grafo.adicionar_aresta(origem, destino)

def imprimir_grau_de_saida(vertice_num): 
    """Imprime grau de saída do vértice informado pelo usuário.

    Args:
        vertice_num (int): Vértice do input.
    """
    print(f"I) Grau de saída de {vertice_num}: {meu_grafo.grau_saida(vertice_num)}")

def imprimir_grau_de_entrada(vertice_num): 
    """Imprime no console o grau de entrada do vértice informado pelo usuário.

    Args:
        vertice_num (int): Vértice obtido pelo input.
    """
    print(f"II) Grau de entrada de {vertice_num}: {meu_grafo.grau_entrada(vertice_num)}")
    
def imprimir_Sucessores(vertice_num):
    """Imprime no console os sucessores do vértice informado pelo usuário.

    Args:
        vertice_num (int): Vértice obtido pelo input.
    """
    print(f"III) Conjunto de sucessores de {vertice_num}:\t{meu_grafo.forward_star(vertice_num)}")
    
def imprimir_Predecessores(vertice_num):
    """Imprime no console os predecessores do vértice informado pelo usuário.

    Args:
        vertice_num (int): Vértice obtido pelo input.
    """
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
            imprimir_grau_de_saida(vertice)
            imprimir_grau_de_entrada(vertice)
            imprimir_Sucessores(vertice)
            imprimir_Predecessores(vertice)       
            
            break