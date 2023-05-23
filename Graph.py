import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import sys

# Ma trận khoảng cách
dist_matrix = np.array([
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0],
])

# Tạo đồ thị
G = nx.Graph()

# Thêm các thành phố vào đồ thị
for i in range(1, dist_matrix.shape[0] + 1):  # Thay đổi range từ 1 đến dist_matrix.shape[0] + 1
    G.add_node(i)

# Thêm các cạnh đường đi vào đồ thị
for i in range(1, dist_matrix.shape[0] + 1):  # Thay đổi range từ 1 đến dist_matrix.shape[0] + 1
    for j in range(i + 1, dist_matrix.shape[1] + 1):  # Thay đổi range từ i + 1 đến dist_matrix.shape[1] + 1
        G.add_edge(i, j, weight=dist_matrix[i - 1, j - 1])  # Trừ 1 ở đây để lấy giá trị từ ma trận khoảng cách

# Vẽ đồ thị
pos = nx.spring_layout(G)  # Xác định vị trí của các nút
labels = nx.get_edge_attributes(G, 'weight')  # Nhãn trọng số cho các cạnh

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.axis('off')
plt.show()
