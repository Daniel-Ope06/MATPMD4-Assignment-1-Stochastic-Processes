import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# np.random.seed(3)

alpha = 3.53
beta = 0.54
dt = 0.01
N = 2500
num_walks = 5000

# Initialize a vector 'x' to track the positions of all walks.
x = np.zeros(num_walks)

for i in range(N):
    t = i * dt
    drift = (1/alpha) * np.sin(x) * np.cos(t) * dt
    noise = (1/beta) * np.random.normal(0, 1, size=num_walks) * np.sqrt(dt)
    x = x + drift + noise

# Plotting the histogram
plt.figure(figsize=(10, 6))
# Using density=True to normalize the histogram,
# making it easier to compare to a standard curve
plt.hist(
    x, bins=50, density=True, alpha=0.7,
    color='lightblue', edgecolor='black'
)
plt.title(f'Histogram of Final Positions for {num_walks} Walks (dt={dt})')
plt.xlabel('Final Position (x)')
plt.ylabel('Density')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Run D'Agostino's K-squared test for normality
stat, p_value = stats.normaltest(x)
print(f"Normality Test Statistic: {stat:.4f}")
print(f"p-value: {p_value:.4f}")
