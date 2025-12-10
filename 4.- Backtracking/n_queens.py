
def es_solucion(sol, k):
    return len(sol) == k

def es_factible(sol, row, col):
    factible = True

    i = 1
    while factible and i <= row:
        feasible_col = (sol[row - i] != col)
        feasible_diag_45 = (sol[row - i] != col - i) # Fila superior a la izquierda
        feasible_diag_135 = (sol[row - i] != col + i) # Fila superior a la derecha
        factible = feasible_col and feasible_diag_45 and feasible_diag_135
        i += 1

    return factible

# row es el k de las transparencias
def n_reinas(n, sol, row, sol_encontrada):
    if es_solucion(sol, row):
        return True, sol
    else:
        col = 0
        while not sol_encontrada and col <n:
            if es_factible(sol, row, col):
                sol[row] = col
                sol_encontrada, sol = n_reinas(n, sol, row+1, sol_encontrada)
                # Backtracking
                if not sol_encontrada:
                    sol[row] = -1
            col += 1

    return sol_encontrada, sol

n = 4
sol = [-1] * n
encontrado, sol = n_reinas(n, sol, 0, False)
if encontrado:
    print(sol)