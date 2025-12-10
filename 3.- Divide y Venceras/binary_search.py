
def busqueda_binaria(lista, buscado, inf, sup):
    if inf > sup:
        return -1
    else:
        mitad = (inf + sup) // 2
        if lista[mitad] == buscado:
            return mitad
        elif lista[mitad]> buscado:
            return busqueda_binaria(lista, buscado, inf, mitad-1)
        else:
            return busqueda_binaria(lista, buscado, mitad+1, sup)


v = [1, 3, 4, 5, 6, 7, 9]
number = -200
pos = busqueda_binaria(v, number, 0, len(v)-1)
print(pos)