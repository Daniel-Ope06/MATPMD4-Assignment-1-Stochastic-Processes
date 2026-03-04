import numpy as np

# ========================
# Question 2a: Calculate x
# ========================

# Row C is [0.16, 0.16, 0.22, x, 0.26]
# Stochastic matrix property: sum of probabilities in a row must equal 1.
x = 1.0 - (0.16 + 0.16 + 0.22 + 0.26)
x = round(x, 2)  # Round to avoid floating point errors

print(f"\nCalculated x: {x}")

# Define the Transition Matrix P
# Rows: A, B, C, D, E
P = np.array([
    [0.21, 0.07, 0.15, 0.11, 0.46],
    [0.00, 1.00, 0.00, 0.00, 0.00],
    [0.16, 0.16, 0.22,    x, 0.26],
    [0.00, 0.00, 0.00, 1.00, 0.00],
    [0.21, 0.27, 0.18, 0.24, 0.10]
])

print("\nTransition Matrix P:\n", P)


# =============================================
# Question 2b: Distribution after 3 generations
# =============================================

# Initial distribution: A(13%), B(24%), C(32%), D(28%), E(3%)
pi_0 = np.array([0.13, 0.24, 0.32, 0.28, 0.03])

# Generation 1
# Using @ for matrix multiplication
pi_1 = pi_0 @ P
print(f"\nGen 1 Distribution: {np.round(pi_1, 4)}")

# Generation 2
pi_2 = pi_1 @ P
print(f"\nGen 2 Distribution: {np.round(pi_2, 4)}")

# Generation 3
pi_3 = pi_2 @ P
print(f"\nGen 3 Distribution: {np.round(pi_3, 4)}")

# Shifting from transient states (A, C, E) to absorbing states (B, D).
# B and D are absorbing because they have 1.0 on the diagonal.
