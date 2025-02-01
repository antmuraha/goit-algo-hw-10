import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definition of a function
def f(x):
    return x**3 + x**2


# Limits of integration
a, b = 0, 2

# Exact integral using quad
quad_integral, quad_error = quad(f, a, b)

# Range of N values
N_values = np.logspace(1, 4, num=50, dtype=int)  # 10 to 10,000
monte_carlo_results = []
differences = []

for N in N_values:
    x_random = np.random.uniform(a, b, N)
    y_random = f(x_random)
    monte_carlo_integral = (b - a) * np.mean(y_random)

    monte_carlo_results.append(monte_carlo_integral)
    differences.append(abs(monte_carlo_integral - quad_integral))

# Plotting results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(N_values, monte_carlo_results, label='Monte Carlo Integral', marker='o', linestyle='--')
plt.axhline(y=quad_integral, color='r', linestyle='-', label='Quad Integral')
plt.xscale('log')
plt.xlabel('Number of Points (N)')
plt.ylabel('Integral Value')
plt.legend()
plt.title('Monte Carlo vs Quad Integration')

plt.subplot(1, 2, 2)
plt.plot(N_values, differences, label='Difference',
         marker='s', linestyle='-', color='m')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of Points (N)')
plt.ylabel('Difference')
plt.legend()
plt.title('Difference between Methods')

plt.tight_layout()
plt.show()
