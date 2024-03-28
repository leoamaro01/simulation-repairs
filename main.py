from simulation_repairs import *
from variables import weibull_distribution, exponential_distribution
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler

# Check if directory exists and create it if not
if not os.path.exists('temp'):
    os.makedirs('temp')

cant = [10, 20, 50, 100]
ratios = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]  # Define your ratios here
runs = 20
matrix = []
table = []
scaler = StandardScaler()

for count ,num in enumerate(cant):
    y =[]
    for ratio in ratios:
        s = int(num / ratio)
        mean = 0
        times = []
        for i in range(runs):
            total_time = simulate(n=num, s=s, get_explosion_time=weibull_distribution, get_repair_time=exponential_distribution, max_time=0)
            mean += total_time
            times.append(total_time)

        # Calculate mean
        mean /= runs
        # Calculate variance
        variability = np.var(times)
        # Calculate standard deviation
        std_dev = np.std(times)
        # Calculate confidence interval
        confidence_interval = stats.norm.interval(0.95, loc=mean, scale=std_dev/np.sqrt(runs))
        table.append([num, s, mean, variability, std_dev,confidence_interval])
        y.append(mean)
    matrix.append(y)

    # Log normalization
    y_log = np.log1p(y)  # Applies log(x + 1) for each element in y

    # Z-score normalization
    y_zscore = scaler.fit_transform(np.array(y).reshape(-1, 1)).flatten()

    # Plotting
    plt.figure()
    plt.plot(ratios, y)
    plt.xlabel('Ratio')
    plt.ylabel('Time')
    plt.title(f'N={num}')
    plt.savefig(f'temp/plot_{num}.png')

    if num == cant[0]:
        plt.figure()
        plt.plot(ratios[1:], y[1:])
        plt.xlabel('Ratio')
        plt.ylabel('Time')
        plt.title(f'N={num}, Ratio > 0.25')
        plt.savefig(f'temp/plot_{num}_no_25.png')

        plt.figure()
        plt.plot(ratios[2:], y[2:])
        plt.xlabel('Ratio')
        plt.ylabel('Time')
        plt.title(f'N={num}, Ratio > 0.5')
        plt.savefig(f'temp/plot_{num}_no_50.png')

    plt.figure()
    plt.plot(ratios, y_log)
    plt.xlabel('Ratio')
    plt.ylabel('Normalized Time')
    plt.title(f'N={num}, Log Normalized')
    plt.savefig(f'temp/plot_log_{num}.png')

    plt.figure()
    plt.plot(ratios, y_zscore)
    plt.xlabel('Ratio')
    plt.ylabel('Normalized Time')
    plt.title(f'N={num}, ZScore Normalized')
    plt.savefig(f'temp/plot_zscore_{num}.png')



table = pd.DataFrame(table,columns=['N', 'S', 'Average Time','Variance','Standard Deviation','Confidence Interval'])
print(table.head)
with pd.ExcelWriter('results.xlsx') as writer:
    table.to_excel(writer, sheet_name='Table', index=False)

plt.show()