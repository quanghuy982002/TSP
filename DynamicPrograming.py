def tsp(matrix):
    n = len(matrix)
    memo = {}  # Bảng ghi nhớ để lưu trữ các kết quả tính toán trung gian

    def calculate_minimum_cost(current_node, remaining_nodes):
        if (current_node, remaining_nodes) in memo:
            return memo[current_node, remaining_nodes]

        if not remaining_nodes:
            return matrix[current_node][0]  # Trường hợp cơ sở: Không còn nút nào, trở về nút 0

        costs = []
        for next_node in remaining_nodes:
            updated_remaining_nodes = tuple(node for node in remaining_nodes if node != next_node)
            if (next_node, updated_remaining_nodes) not in memo:
                result = matrix[current_node][next_node] + calculate_minimum_cost(next_node, updated_remaining_nodes)
                memo[next_node, updated_remaining_nodes] = result
            costs.append(memo[next_node, updated_remaining_nodes])

        memo[current_node, remaining_nodes] = min(costs)  # Lưu trữ kết quả tối ưu vào bảng ghi nhớ
        return memo[current_node, remaining_nodes]

    optimal_cost = calculate_minimum_cost(0, tuple(range(1, n)))

    path = [0]
    remaining_nodes = tuple(range(1, n))
    while remaining_nodes:
        next_node = min(remaining_nodes, key=lambda node: matrix[path[-1]][node] + memo[node, tuple(n for n in remaining_nodes if n != node)])
        path.append(next_node)
        remaining_nodes = tuple(node for node in remaining_nodes if node != next_node)

    path.append(0)  # Kết thúc tại nút 0

    return optimal_cost, path



matrix = [
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
optimal_cost, optimal_path = tsp(matrix)

print("Optimal Cost:", optimal_cost)
print("Optimal Path:", optimal_path)



