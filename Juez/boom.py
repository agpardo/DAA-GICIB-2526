import heapq


def dijkstra(g, start):
    distances = [float('infinity')] * len(g)
    distances[start] = 0

    pq = [(0, start)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if distances[current_vertex] <= current_distance:
            for neighbor, weight in g[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
    return distances


def solve(g, types, nTypes):
    solution = [float('infinity')] * nTypes
    for v in range(len(g)):
        distances = dijkstra(g, v)
        for u in range(len(distances)):
            if u != v and types[v] == types[u]:
                solution[types[v]] = min(solution[types[v]], distances[u])
    return solution


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    g = []
    types = list(map(int, input().strip().split()))
    typesSet = set()
    for i in range(n):
        g.append([])
        typesSet.add(types[i])
    for i in range(m):
        u, v, c = map(int, input().strip().split())
        g[u].append((v, c))
        g[v].append((u, c))
    sol = solve(g, types, len(typesSet))
    for s in sol:
        print(str(s), end=" ")
