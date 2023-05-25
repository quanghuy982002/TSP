import matplotlib.pyplot as plt

num_cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
dynamic_Programing = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001993894577026367, 0.003989219665527344, 0.007978439331054688, 0.02895045280456543, 0.05048823356628418, 0.13318848609924316]
back_Tracking = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.000997304916381836, 0.006981372833251953, 0.05841851234436035, 0.5458176136016846, 5.442460775375366, 61.3442964553833, 794.7322404384613]
greedy = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
bruteForce = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0055294036865234375, 0.03797030448913574, 0.3848307132720947, 4.23048210144043, 50.50507187843323, 660.2890708446503]

plt.plot(num_cities, dynamic_Programing, label='Dynamic Programming')
plt.plot(num_cities, back_Tracking, label='Backtracking')
plt.plot(num_cities, greedy, label='Greedy')
plt.plot(num_cities, bruteForce, label='Brute Force')

plt.xlabel('Số lượng các thành phố')
plt.ylabel('Thời gian (giây)')
plt.title('Thời gian thực thi theo số lượng thành phố')

plt.legend()
plt.grid(True)
plt.show()
