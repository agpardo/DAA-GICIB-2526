def obtener_mejor(candidatos, datos):
    mejor_ratio = -1
    mejor_seleccion = 0

    for c in candidatos:
        ratio = datos["beneficio"][c] / datos["coste"][c]
        if ratio > mejor_ratio:
            mejor_ratio = ratio
            mejor_seleccion = c
    return mejor_seleccion

def knapsack(datos):
    candidatos = set()
    n = len(datos["coste"])
    for i in range(n):
        candidatos.add(i)

    solucion = [0]*n
    limite_aux = datos["limite"]

    while candidatos and limite_aux >0:
        seleccionado = obtener_mejor(candidatos,datos)
        candidatos.remove(seleccionado)

        if limite_aux >= datos["coste"][seleccionado]:
            limite_aux -= datos["coste"][seleccionado]
            solucion[seleccionado] = 1.0
        else:
            ratio = limite_aux / datos["coste"][seleccionado]
            limite_aux = 0
            solucion[seleccionado] = ratio

    return solucion

datos = {
    "coste" : [10, 20, 30, 40, 50],
    "beneficio" : [20, 30, 66, 40, 60],
    "limite" : 100
}

sol = knapsack(datos)
print(sol)
