import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)

# Parameters
alpha = 3.53
beta = 0.54
dt = 0.01
N = 2500

plt.figure(figsize=(12, 6))

# Generate 3 different realisations
for walk in range(3):
    x = 0
    path = [x]

    for i in range(N):
        t = i * dt
        dx = (1/alpha) * np.sin(x) * np.cos(t) * dt + \
            (1/beta) * np.random.normal(0, 1) * np.sqrt(dt)
        x = x + dx
        path.append(x)

    plt.plot(path, alpha=0.8, linewidth=1.5, label=f'Realisation {walk + 1}')

plt.title(
    'Three Realisations of the Generalised Random Walk (dt=0.01)',
    fontsize=14
)
plt.xlabel('Step', fontsize=12)
plt.ylabel('Position (x)', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
