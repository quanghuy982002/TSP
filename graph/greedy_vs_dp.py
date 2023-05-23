import matplotlib.pyplot as plt

num_cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
dynamic_Programing = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001993894577026367, 0.003989219665527344, 0.007978439331054688, 0.02895045280456543, 0.05048823356628418, 0.13318848609924316]

greedy = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

plt.plot(num_cities, dynamic_Programing)
plt.plot(num_cities, greedy)
plt.xlabel('Number of Cities')
plt.ylabel('Execution Time (seconds)')
plt.title('TSP Execution Time')
plt.show()
