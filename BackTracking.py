def tsp(graph):
    n = len(graph)
    visited = [False] * n
    path = []
    min_cost = float('inf')

    def backtrack(curr_vertex, cost, count):
        nonlocal min_cost
        if count == n and graph[curr_vertex][0] > 0:
            min_cost = min(min_cost, cost + graph[curr_vertex][0])
            print("Path:", path + [0], "Cost:", cost + graph[curr_vertex][0])
            return

        for next_vertex in range(n):
            if not visited[next_vertex] and graph[curr_vertex][next_vertex] > 0:
                visited[next_vertex] = True
                path.append(next_vertex)
                print("Backtrack:", path)
                backtrack(next_vertex, cost + graph[curr_vertex][next_vertex], count + 1)
                visited[next_vertex] = False
                path.pop()

    visited[0] = True  # Xuất phát từ đỉnh 0
    path.append(0)  # Thêm đỉnh 0 vào đường đi
    print("Backtrack:", path)
    backtrack(0, 0, 1)  # Gọi hàm backtrack với đỉnh 0 là đỉnh xuất phát, cost ban đầu là 0, và count ban đầu là 1

    return min_cost


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost = tsp(graph)
print("Minimum cost:", min_cost)
