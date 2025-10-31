def scheduling(candidatos, dia_maximo):
    solucion = [-1] * (dia_maximo+1)

    for candidato in candidatos:
        dia = candidato[2]
        encontrado = False
        while dia >=0 and not encontrado:
            if solucion[dia] == -1:
                solucion[dia] = candidato
                encontrado = True
            # else
            dia -= 1
    return solucion


if __name__ == "__main__":
    n = int(input().strip())
    dia_maximo = -1
    candidatos = []

    for _ in range(n):
        nombre, dia, nivel = input().strip().split()
        if int(dia) > dia_maximo:
            dia_maximo = int(dia)

        candidatos.append([int(nivel), nombre, int(dia)])
        #candidatos= [ [50, Manuel, 0], [10, Diego, 0] ,...]

    candidatos.sort(reverse=True)

    solucion = scheduling(candidatos, dia_maximo)

    for indice in range(len(solucion)):
        candidato = solucion[indice]
        if candidato == -1:
            print("DIA: " + str(indice) +": SIN TENTADOR")
        else:
            print("DIA: " + str(indice) + ": " + candidato[1] + ", LE SOBRAN " + str(candidato[2]-indice) + " DIAS")

