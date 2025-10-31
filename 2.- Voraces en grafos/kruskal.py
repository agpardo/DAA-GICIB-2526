def sort_candidates(g):
    candidatos = []
    for adjs in g:
        for (origen, destino, peso) in adjs:
            candidatos.append((peso, origen, destino))
    candidatos.sort()
    return candidatos

def update_components(componentes, nuevo_id, viejo_id):
    for i in range(len(componentes)):
        if componentes[i] == viejo_id:
            componentes[i] = nuevo_id

def kruskal(g):
    aristas = sort_candidates(g)
    # [0, 0, 0, 0, 0, 0, 0, 0]
    componentes_conexas = list(range(len(g)))
    numero_componentes = len(componentes_conexas)
    valor = 0
    indice = 0
    while indice < len(aristas) and numero_componentes > 1:
        peso, origen, destino = aristas[indice]
        if componentes_conexas[origen] != componentes_conexas[destino]:
            valor += peso
            update_components(componentes_conexas, componentes_conexas[origen], componentes_conexas[destino])
            numero_componentes -= 1
        indice += 1

    return valor


g = [
    [],
    [(1,3,1), (1,4,2), (1,7,6)],
    [(2,5,2), (2,6,4), (2,7,7)],
    [(3,1,1), (3,4,3), (3,7,5)],
    [(4,1,2), (4,3,3), (4,5,1), (4,6,9)],
    [(5,2,2), (5,4,1), (5,7,8)],
    [(6,2,4), (6,4,9)],
    [(7,1,6), (7,2,7), (7,3,5), (7,5,8)]
]

sol = kruskal(g)
print(sol)