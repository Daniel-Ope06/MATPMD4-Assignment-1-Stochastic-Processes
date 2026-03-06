import numpy as np
import matplotlib.pyplot as plt


def f(w, x, y, z):
    himmel1 = -((w**2 + x - 11)**2 + (w + x**2 - 7)**2) / 100
    himmel2 = -((y**2 + z - 11)**2 + (y + z**2 - 7)**2) / 100
    peak1 = 4.0 * np.exp(
        -0.2 * ((w-2.5)**2 + (x-1.8)**2 + (y+1.2)**2 + (z-0.7)**2))
    peak2 = 3.8 * np.exp(
        -0.18 * ((w+1.8)**2 + (x-2.2)**2 + (y-2.5)**2 + (z+1.5)**2))
    peak3 = 3.5 * np.exp(
        -0.22 * ((w-0.5)**2 + (x+2.8)**2 + (y-1.8)**2 + (z+2.3)**2))
    peak4 = 3.3 * np.exp(
        -0.25 * ((w+2.2)**2 + (x+0.8)**2 + (y+2.5)**2 + (z-2.1)**2))
    interaction = 0.2 * np.sin(w + x) * np.cos(y - z)

    return himmel1 + himmel2 + peak1 + peak2 + peak3 + peak4 + interaction


def metropolis_hastings(f, x_init, sigma, n_steps):
    x_current = x_init
    f_current = f(*x_current)
    f_history = [f_current]
    x_history = [x_current.copy()]

    for i in range(n_steps):
        x_proposal = x_current + np.random.normal(0, sigma, size=4)
        f_proposal = f(*x_proposal)

        # Accept if better
        if f_proposal > f_current:
            x_current = x_proposal
            f_current = f_proposal

        # If worse, accept with a probability
        # proportional to how much worse it is
        else:
            acceptance_probability = f_proposal / f_current
            if np.random.uniform(0, 1) < acceptance_probability:
                x_current = x_proposal
                f_current = f_proposal

        f_history.append(f_current)
        x_history.append(x_current.copy())

    return f_history, x_history


def analyze_run(f_history, x_history):
    # Find Best Value and Position
    best_index = np.argmax(f_history)
    best_f = f_history[best_index]
    best_x = x_history[best_index]

    # Calculate Acceptance Ratio
    # If history[i] != history[i-1], the move was accepted.
    f_history_arr = np.array(f_history)
    accepted_moves = np.sum(f_history_arr[1:] != f_history_arr[:-1])
    acceptance_ratio = accepted_moves / (len(f_history) - 1)

    return best_f, best_x, acceptance_ratio


sigma = 0.5
n_steps = 5000
seeds = [0, 3, 4, 6, 12]

plt.figure(figsize=(12, 6))

for i, seed in enumerate(seeds):
    np.random.seed(seed)
    x_init = np.random.uniform(-3.5, 3.5, size=4)

    f_history, x_history = metropolis_hastings(f, x_init, sigma, n_steps)

    best_f, best_x, acc_ratio = analyze_run(f_history, x_history)

    plt.plot(f_history, alpha=0.8, linewidth=1.5, label=f'Run {i+1}')

    final_pos = x_history[-1]
    print(f"--- Run {i+1} ---")
    print(f"Max Found: {best_f:.4f}")
    print(
        f"Final Position: w={final_pos[0]:.2f}, x={final_pos[1]:.2f}, y={final_pos[2]:.2f}, z={final_pos[3]:.2f}")
    print(
        f"Best Position:  w={best_x[0]:.2f}, x={best_x[1]:.2f}, y={best_x[2]:.2f}, z={best_x[3]:.2f}")
    print(f"Acceptance Ratio: {acc_ratio:.2%}\n")

plt.title(
    'Metropolis-Hastings Optimisation (5 Runs, $\\sigma=0.5$)',
    fontsize=14
)
plt.xlabel('Step', fontsize=12)
plt.ylabel('Function Value f(w,x,y,z)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
