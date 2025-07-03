import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Sample Matrix
# -----------------------------
A = np.array([[4, 0], [3, -5]])
print("==== Matrix A ====")
print(A)

# -----------------------------
# 2. Eigenvalues and Eigenvectors
# -----------------------------
eig_vals, eig_vecs = np.linalg.eig(A)

print("\n==== Eigenvalues and Eigenvectors ====")
print("Eigenvalues:")
print(eig_vals)
print("\nEigenvectors (columns):")
print(eig_vecs)

# -----------------------------
# 3. SVD (Singular Value Decomposition)
# -----------------------------
U, S, VT = np.linalg.svd(A)

print("\n==== Singular Value Decomposition (SVD) ====")
print("U matrix:")
print(U)
print("\nSingular values (as array):")
print(S)
print("\nV^T matrix:")
print(VT)

# -----------------------------
# 4. Visualizing Eigenvectors
# -----------------------------
origin = [0], [0]

plt.figure(figsize=(6, 6))
plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)

# Plot eigenvectors
for i in range(len(eig_vals)):
    vec = eig_vecs[:, i]
    plt.quiver(*origin, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, label=f"λ={eig_vals[i]:.2f}")

plt.title("Eigenvectors of A")
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.show()
