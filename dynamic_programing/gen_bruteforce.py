import time
from sys import maxsize
from itertools import permutations

def tsp(graph, s):
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
    min_cost = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        k = s
        path = [s]
        for j in i:
            current_cost += graph[k][j]
            k = j
            path.append(j)
        current_cost += graph[k][s]
        path.append(s)
        min_cost = min(min_cost, current_cost)
    return min_cost

graph = [
    [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
    [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
    [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
    [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
    [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
    [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
    [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
    [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
    [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
    [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
    [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
    [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
    [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
]

num_cities_list = []
execution_time_list = []

for num_cities in range(1, len(graph) + 1):
    start_time = time.time()
    subgraph = graph[:num_cities][:num_cities]
    s = 0  # Starting city
    min_cost = tsp(subgraph, s)
    end_time = time.time()
    execution_time = end_time - start_time

    num_cities_list.append(num_cities)
    execution_time_list.append(execution_time)

    print("Number of cities:", num_cities)
    print("Execution time:", execution_time)
    print("------------------------------")

print("Number of cities:", num_cities_list)
print("Execution time:", execution_time_list)
