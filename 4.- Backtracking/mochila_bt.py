import copy

def es_solucion(sol, datos):
    return (sol['w']+ min(datos['w'])) > datos['W']

def es_factible(sol, datos, i):
    return (sol['w'] + datos['w'][i])<= datos['W']

def add(sol, i, datos):
    sol['x'][i] += 1
    sol['w'] += datos['w'][i]
    sol['v'] += datos['v'][i]

def remove(sol, i, datos):
    sol['x'][i] -= 1
    sol['w'] -= datos['w'][i]
    sol['v'] -= datos['v'][i]

def mochila_bt(datos, sol, mejor, k):
    if es_solucion(sol, datos):
        print("He explorado la solucion: ", end=' ')
        print(sol['x'], end =' ')
        print(" Valor: " + str(sol['v']))
        if sol['v']> mejor['v']:
            mejor = copy.deepcopy(sol)
    else:
        for i in range(k, datos['n']):
            if es_factible(sol, datos, i):
                add(sol, i, datos)
                mejor = mochila_bt(datos, sol, mejor, i)
                remove(sol, i, datos)

    return mejor



datos =  {'n' : 4, 'W':8, 'w': [2,3,4,5], 'v': [3,5,6,10]}
k = 0
sol = { 'x': [0]*datos['n'], 'v':0, 'w':0 }
mejor = { 'x': [0]*datos['n'], 'v':0, 'w':0 }
mejor = mochila_bt(datos, sol, mejor, k)
print(mejor)