import numpy as np

# np.random.seed(3)

alpha = 3.53
beta = 0.54
N = 2500
num_walks = 1000
dt_values = [0.05, 0.1, 0.2, 0.4]

print(
    f"Mean final position after {N} steps (averaged over {num_walks} walks):")
print("-" * 64)

for dt in dt_values:
    # Initialize a vector 'x' to track the positions of all 1000 walks.
    # x_0 = 0 for all paths.
    x = np.zeros(num_walks)

    for i in range(N):
        t = i * dt

        # Drift: a(x,t)*dt
        # Passing the vector 'x' into np.sin() calculates the spatial drift
        # for all 1000 walks simultaneously (element-wise).
        drift = (1/alpha) * np.sin(x) * np.cos(t) * dt

        # Noise: b(x,t)*dW
        # size=num_walks forces NumPy to draw 1000 independent samples.
        # Every single walk receives its own independent random noise.
        noise = (1/beta) * np.random.normal(0, 1, size=num_walks) * np.sqrt(dt)

        # This vector addition updates the positions of all 1000 walks at once,
        # mathematically identical to running 1000 separate loops, but faster.
        x = x + drift + noise

    mean_position = np.mean(x)
    print(f"dt = {dt} | Mean Final Position = {mean_position:.4f}")
