def obtener_mejor(candidatos, datos):

    mejor_beneficio = -1
    mejor_seleccion = 0

    for c in candidatos:
        if datos["beneficio"][c] > mejor_beneficio:
            mejor_beneficio = datos["beneficio"][c]
            mejor_seleccion = c

    return mejor_seleccion


def scheduling(datos, max_dias):
    n = len(datos["beneficio"])
    candidatos = set()

    for i in range(n):
        candidatos.add(i)

    sol = [-1]*(max_dias+1)

    while candidatos:
        seleccionado = obtener_mejor(candidatos, datos)
        candidatos.remove(seleccionado)
        fecha = datos["limite"][seleccionado]
        encontrado = False
        while not encontrado and fecha>0:
            if sol[fecha] == -1:
                sol[fecha] = seleccionado
                encontrado = True
            fecha -= 1
    return sol


datos = {
    "beneficio": [50, 10, 15, 30],
    "limite": [2, 1, 2, 1]
}

sol = scheduling(datos, max(datos["limite"]))
print(sol)