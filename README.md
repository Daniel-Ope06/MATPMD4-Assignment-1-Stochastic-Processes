# 📈 MATPMD4 Assignment 1: Stochastic Processes

This repository contains the Python simulations and mathematical analyses for the MATPMD4 (Stochastic Processes) module of the MSc program.

The project explores fundamental stochastic concepts through numerical simulation, statistical testing, and algorithm implementation from scratch.

## 🎯 Key Topics Covered

| Topic | Description | Methods / Algorithms |
| --- | --- | --- |
| **Markov Chains** | Analysis of state transitions and limiting distributions. | Matrix operations, steady-state probability calculations. |
| **Generalised Random Walks** | Simulating diffusion-dominated continuous-time stochastic differential equations. | Euler-Maruyama method, Monte Carlo estimation, D'Agostino's K-squared test. |
| **High-Dimensional Optimisation** | Finding the maximum of a complex, multi-modal 4D function. | Metropolis-Hastings Algorithm (MCMC), random walks with probabilistic acceptance. |

## 📂 Repository Structure

To maintain a clean Git history without the noise of Jupyter notebook JSON metadata, the core development is tracked using standard `.py` files tailored for VS Code's interactive window. These are compiled into the final Jupyter Notebook format required for the university submission.

* `MATPMD4_Assignment1_3539054.ipynb`: The final, executable Jupyter Notebook containing all formatted markdown explanations, LaTeX equations, and code cells.
* `MATPMD4_Assignment1_3539054.pdf`: The static, executed PDF version of the notebook submitted for grading.
* `src/` : The `.py` files used for interactive development and version control.

## 🛠️ Technologies Used

* **Python 3**
* **NumPy:** For vectorized numerical simulations and matrix operations.
* **Matplotlib:** For plotting random walk realisations, histograms, and MCMC convergence chains.
* **SciPy:** For formal statistical normality testing.

## 🚀 How to Run

* Clone the repository.

* Ensure the required libraries are installed:

```bash
pip install numpy matplotlib scipy
```

* Open `MATPMD4_Assignment1_3539054.ipynb` in your preferred environment and execute the cells sequentially. The code includes fixed random seeds to ensure reproducible simulation outputs and plots.
