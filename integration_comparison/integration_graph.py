import matplotlib.pyplot as plt
import numpy as np

# Definition of a function and limits of integration
def f(x):
    return x ** 3 + x ** 2


a = 0  # Lower limit
b = 2  # Upper limit

# Range of values for x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Creating a graph
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Filling the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Adding integration limits and graph title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration graph f(x) = x^3 + x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()
