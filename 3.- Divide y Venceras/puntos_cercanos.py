import math
import random

def distancia_euclidea(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + ( p1[1]-p2[1])**2)

def fuerza_bruta(puntos_x):
    n = len(puntos_x)
    min_distance =  0x3f3f3f3f  # float("inf")
    for i in range(n):
        for j in range(i+1, n):
            d = distancia_euclidea(puntos_x[i], puntos_x[j])
            min_distance = min(d, min_distance)
    return min_distance

def combinar(franja, d):
    min_distance = d
    for i in range(len(franja)):
        for j in range(i+1, len(franja)):
            if franja[j][1] - franja[i][1]< d:
                distancia = distancia_euclidea(franja[i], franja[j])
                min_distance = min(min_distance, distancia)

    return min_distance


def dyv_puntos_cercanos(puntos_x, puntos_y):
    n = len(puntos_x)
    if n <= 3:
        return fuerza_bruta(puntos_x)
    else:
        mid = n//2
        puntos_x_i = puntos_x[ : mid]
        puntos_x_d = puntos_x[ mid : ]

        puntos_y_i = []
        puntos_y_d = []

        mid_x = puntos_x[mid][0]

        for p in puntos_y:
            if p[0] <= mid_x:
                puntos_y_i.append(p)
            else:
                puntos_y_d.append(p)

        min_i = dyv_puntos_cercanos(puntos_x_i, puntos_y_i)
        min_d = dyv_puntos_cercanos(puntos_x_d, puntos_y_d)

        d = min(min_i, min_d)

        franja = []
        for p in puntos_y:
            if abs(p[0]-mid_x) < d:
                franja.append(p)

        dist_franja = combinar(franja, d)
        return dist_franja


n = 5
puntos =[(random.randint(-n*10, n*10), random.randint(-n*10, n*10)) for _ in range(n)]

puntos_x = puntos.copy()
puntos_x.sort(key= lambda p: p[0])
puntos_y = puntos.copy()
puntos_y.sort(key= lambda p: p[1])

distancia_minima = dyv_puntos_cercanos(puntos_x, puntos_y)
print(str(distancia_minima))