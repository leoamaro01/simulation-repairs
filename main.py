from simulation_repairs import *
from variables import weibull_distribution, exponential_distribution
import matplotlib.pyplot as plt
import os

# Check if directory exists and create it if not
if not os.path.exists('temp'):
    os.makedirs('temp')

cant = [10, 20, 50, 100]
ratios = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]  # Define your ratios here
matrix = []
for num in cant:
    y =[]
    for ratio in ratios:
        s = int(num / ratio)
        y.append(simulate(n=num, s=s, get_explosion_time=weibull_distribution, get_repair_time=exponential_distribution))
    matrix.append(y)

    # Plotting
    plt.figure()
    plt.plot(ratios, y)
    plt.xlabel('Ratio')
    plt.ylabel('Time')
    plt.title(f'N={num}')
    plt.savefig(f'temp/plot_{num}.png')