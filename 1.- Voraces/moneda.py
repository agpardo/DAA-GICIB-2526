
def cambio(monedas, cantidad):
    sol = [0]*len(monedas)
    gasto_aux = cantidad
    indice = 0
    while gasto_aux > 0 and indice < len(monedas):
        if monedas[indice] <= cantidad:
            sol[indice] = gasto_aux // monedas[indice]
            gasto_aux = gasto_aux % monedas[indice]

        indice += 1

    return sol


monedas = [50, 20, 10, 5, 2, 1]

print("Dime el dinero que necesitas:")
dinero = int(input())
sol = cambio(monedas, dinero)

print("El cambio para " + str(dinero) + " es: ")
for indice in range(len(sol)):
    if sol[indice] > 0:
        print(str(sol[indice]) + " monedas de " + str(monedas[indice]))
