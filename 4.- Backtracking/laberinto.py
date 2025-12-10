import copy

def is_sol(lab, r, c):
    return r == len(lab)-1 and c == len(lab[0])-1

def es_mejor(lab, best):
    filas = len(lab)-1
    columnas = len(lab[0])-1
    return lab[filas][columnas] < best[filas][columnas]

def es_factible(lab, new_r, new_c):
    return 0<= new_r < len(lab) and 0<= new_c < len(lab[0]) and lab[new_r][new_c] == 0

def print_lab(lab):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            print("|", end="")
            if lab[i][j] == -1:
                print(" *", end="\t")
            elif lab[i][j] == 0:
                print("  ", end="\t")
            else:
                print(f"{lab[i][j]:2}", end="\t")
        print("|")
        print("-"*4*len(lab))


def laberinto_bt(lab, best, r, c, k):
    if is_sol(lab, r, c):
        if es_mejor(lab, best):
            best = copy.deepcopy(lab)
    else:
        direcciones = [(0,1), (1,0), (0, -1), (-1,0)]
        for direccion in direcciones:
            new_fila = r + direccion[0]
            new_columna = c + direccion[1]
            if es_factible(lab, new_fila, new_columna):
                lab[new_fila][new_columna] = k
                best = laberinto_bt(lab, best, new_fila, new_columna, k+1)
                lab[new_fila][new_columna] = 0
    return best


lab = [
    [0, 0, -1, 0, 0, 0, 0, -1, 0, 0],
    [-1, 0, -1, 0, 0, -1, -1, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, -1, 0, -1, 0],
    [0, -1, 0, 0, -1, -1, -1, 0, 0, 0],
    [0, 0, -1, -1, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, -1, 0, 0],
    [-1, 0, 0, -1, -1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, 0, 0, 0, 0, -1, -1],
    [-1, 0, 0, 0, 0, -1, 0, -1, -1, 0],
    [0, 0, -1, 0, -1, -1, 0, 0, 0, 0]
]

k = 1
lab[0][0] = k
best = copy.deepcopy(lab)
best[len(best)-1][len(best[0])-1] = 0x3f3f3f3f
best = laberinto_bt(lab, best, 0, 0, k+1)
print_lab(best)



