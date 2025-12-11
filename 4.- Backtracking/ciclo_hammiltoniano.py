def is_sol(g, sol, k):
    return len(sol) == len(g) + 1 and sol[0] == k

def es_factible(adj, sol, num_nodos):
    return adj not in sol or (adj == sol[0] and len(sol) == num_nodos)

def ciclo_hamiltoniano(g, k, sol):
    if is_sol(g, sol, k):
        print(sol)
    else:
        for adj in g[k]:
            if es_factible(adj, sol, len(g)):
                sol.append(adj)
                ciclo_hamiltoniano(g, adj, sol)
                sol.pop()


g = [
    [1, 2, 3],
    [0, 2, 4, 5],
    [0, 1, 3, 5, 6],
    [0, 2, 6, 7],
    [1, 5],
    [1, 2, 4, 6],
    [2, 3, 5, 7],
    [3, 6]
]

start = 0
sol = [start]
ciclo_hamiltoniano(g, start, sol)