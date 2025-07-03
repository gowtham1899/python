import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ------------------------------------
# 1. Single-variable Derivative
# ------------------------------------
x = sp.symbols('x')
f = x**2 + 3*x + 2

# Derivative
f_prime = sp.diff(f, x)
print("Function:     f(x) =", f)
print("Derivative:   f'(x) =", f_prime)

# Evaluate derivative at a point
x0 = 2
slope = f_prime.subs(x, x0)
y0 = f.subs(x, x0)
print(f"Slope at x={x0}: f'({x0}) = {slope}")

# ------------------------------------
# Plot: f(x) and Tangent Line
# ------------------------------------
f_lambdified = sp.lambdify(x, f, 'numpy')
x_vals = np.linspace(-5, 5, 400)
y_vals = f_lambdified(x_vals)

# Tangent line: y = slope * (x - x0) + y0
tangent_line = slope * (x_vals - x0) + y0

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="f(x)")
plt.plot(x_vals, tangent_line, '--', label=f"Tangent at x={x0}")
plt.scatter([x0], [y0], color='red', label=f"Point ({x0}, {y0})")
plt.title("Derivative and Tangent Line")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

# ------------------------------------
# 2. Multivariable Gradient
# ------------------------------------
x, y = sp.symbols('x y')
g = x**2 + y**2 + x*y

# Gradient vector (∇g)
grad_g = [sp.diff(g, var) for var in (x, y)]
print("\nMultivariable Function: g(x, y) =", g)
print("Gradient ∇g =", grad_g)

# Evaluate gradient at (1, 2)
point = (1, 2)
grad_at_point = [partial.subs({x: point[0], y: point[1]}) for partial in grad_g]
print(f"Gradient at point {point}: {grad_at_point}")

# ------------------------------------
# Plot: 3D Surface with Gradient Vector
# ------------------------------------
# Lambdify function
g_lambdified = sp.lambdify((x, y), g, 'numpy')

# Grid
x_vals = np.linspace(-3, 3, 30)
y_vals = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x_vals, y_vals)
Z = g_lambdified(X, Y)

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
ax.quiver(point[0], point[1], g_lambdified(*point),
          grad_at_point[0], grad_at_point[1], 0,
          color='r', length=1.5, normalize=True, label="Gradient Vector")

ax.set_title("3D Surface Plot with Gradient Vector")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("g(x, y)")
plt.legend()
plt.show()
