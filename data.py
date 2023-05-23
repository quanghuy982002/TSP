import random

def generate_distance_matrix(num_cities, min_distance, max_distance):
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = random.uniform(min_distance, max_distance)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

num_cities = 30
min_distance = 1
max_distance = 100

distance_matrix = generate_distance_matrix(num_cities, min_distance, max_distance)

for row in distance_matrix:
    print(row)
