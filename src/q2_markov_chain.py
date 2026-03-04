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


# ===========================
# Question 2c: Canonical Form
# ===========================

# Current State Order: A(0), B(1), C(2), D(3), E(4)
# Absorbing States: B(1), D(3)
# Transient States: A(0), C(2), E(4)

# The new order to group Absorbing first, then Transient.
# New Order: B, D, A, C, E
canonical_order = [1, 3, 0, 2, 4]

# Move Row B to top & Row D to second to top
P_rows_sorted = P[canonical_order, :]

# Move Col B to left, Col D to second to left
P_canonical = P_rows_sorted[:, canonical_order]

print("\nCanonical Matrix P_canonical:\n", P_canonical)

# Structure of Canonical Form:
# | I  0 |  (Absorbing rows)
# | R  Q |  (Transient rows)

# 2 absorbing states and 3 transient states.
num_absorbing = 2
num_transient = 3

# Q: Transient to Transient (Bottom-Right block)
# Take rows from index 2 to end, and columns from index 2 to end
Q = P_canonical[num_absorbing:, num_absorbing:]

print("\nMatrix Q (Transient -> Transient):\n", Q)

# R: Transient to Absorbing (Bottom-Left block)
# Take rows from index 2 to end, and columns from index 0 to 2
R = P_canonical[num_absorbing:, :num_absorbing]

print("\nMatrix R (Transient -> Absorbing):\n", R)


# ===============================
# Question 2d: Fundamental Matrix
# ===============================

# Formula: N = (I - Q)^(-1)
# I: Identity matrix
# Q: Transition probability between transient states
# N: Fundamental matrix

I = np.eye(3)  # noqa: E741
N = np.linalg.inv(I - Q)

print("\nFundamental Matrix N:\n", np.round(N, 4))


# =====================================
# Question 2e: Mean Steps to Absorption
# =====================================

# Formula: M = N @ 1 (column vector of ones)
ones = np.ones((3, 1))
M = N @ ones

print("\nMean Steps to Absorption M:\n", np.round(M, 4))


# =====================================
# Question 2f: Absorption Probabilities
# =====================================

# Formula: B = N @ R
B = N @ R

print("\nAbsorption Probabilities B:\n", np.round(B, 4))
