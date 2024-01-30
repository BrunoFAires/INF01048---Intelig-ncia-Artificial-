from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo



def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    result = set()
    pos_empty = estado.find('_')

    # esquerda
    if(pos_empty % 3 != 0):
        result.add(('esquerda', estado[0:pos_empty - 1] + '_' + estado[pos_empty - 1] + estado[pos_empty + 1:])) 

    # abaixo
    if(pos_empty + 3 < len(estado)):
        result.add(('abaixo', estado[0:pos_empty] + estado[pos_empty + 3] + estado[pos_empty + 1:pos_empty+3] + '_' + estado[pos_empty+4:])) 
    
    # acima
    if(pos_empty - 3 > 0):
        result.add(('acima', estado[0:pos_empty - 3] + '_' + estado[pos_empty - 2:pos_empty] + estado[pos_empty-3] + estado[pos_empty + 1:])) 
    

    # direita
    if(pos_empty not in [2, 5, 8]):
        result.add(('direita', estado[:pos_empty] + estado[pos_empty + 1] + '_' + estado[(pos_empty + 2):])) 

    return result


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    graph = set()

    children = sucessor(nodo.estado)
    for child in children:
        graph.add(Nodo(child[1], nodo, child[0], nodo.custo + 1))

    return graph

def reconstruir_caminho(node:Nodo):
    caminho = []
    while node:
        caminho.append(node.acao)
        node = node.pai
    return caminho

def hammingDistance(F:list[Nodo]) -> int:
    finalState = '12345678_'
    distance = None
    i = 0
    position = 0
    for f in F:
        actualDistance = sum(c1 != c2 for c1, c2 in zip(f.estado, finalState)) + f.custo
        if (distance == None or actualDistance < distance):
            distance = actualDistance
            position = i
        i += 1
    return position

def astar_hamming(estado:str)->list[str]:
    finalState = '12345678_'
    X = [] ##Conjunto de Explorados
    F: list[Nodo] = []
    F.append(Nodo(estado, None, None, 1))
    while F:
        currentNode = F.pop(hammingDistance(F))
        if(currentNode.estado == finalState):
            return reconstruir_caminho(currentNode)
        if(currentNode not in X):
            X.append(currentNode)
            a = expande(currentNode)
            childrens = list(a)
            for child in childrens:
                if(child not in X):
                    F.append(child)
    return None


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
