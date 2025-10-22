# Exemplo: Rede de cidades conectadas por estradas

grafo = {
    'São Paulo': ['Campinas', 'Rio de Janeiro', 'Curitiba'],
    'Campinas': ['São Paulo', 'Belo Horizonte'],
    'Rio de Janeiro': ['São Paulo', 'Belo Horizonte'],
    'Curitiba': ['São Paulo', 'Florianópolis'],
    'Belo Horizonte': ['Campinas', 'Rio de Janeiro'],
    'Florianópolis': ['Curitiba']
}


for cidade, conexoes in grafo.items():
    print(f"{cidade} --> {conexoes}")

from collections import deque

def bfs_caminho_mais_curto(grafo, inicio, destino):
    visitados = set()
    fila = deque([[inicio]])
    
    while fila:
        caminho = fila.popleft()
        vertice = caminho[-1]
        
        if vertice == destino:
            return caminho
        
        elif vertice not in visitados:
            for vizinho in grafo.get(vertice, []):
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
            
            visitados.add(vertice)
    
    return None

# Teste 1: São Paulo -> Florianópolis
print("Caminho de São Paulo até Florianópolis:")
print(bfs_caminho_mais_curto(grafo, 'São Paulo', 'Florianópolis'))

# Teste 2: Campinas -> Curitiba
print("\nCaminho de Campinas até Curitiba:")
print(bfs_caminho_mais_curto(grafo, 'Campinas', 'Curitiba'))

# Teste 3: Belo Horizonte -> Florianópolis
print("\nCaminho de Belo Horizonte até Florianópolis:")
print(bfs_caminho_mais_curto(grafo, 'Belo Horizonte', 'Florianópolis'))
