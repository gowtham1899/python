import numpy as np

# ----- Vectors -----
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Dot product (vectors)
dot_v = np.dot(v1, v2)
print("Dot product of vectors:", dot_v)

# Cross product (vectors)
cross_v = np.cross(v1, v2)
print("Cross product of vectors:", cross_v)

# ----- Matrices -----
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product (matrices)
dot_m = A @ B
print("\nDot product of matrices (A @ B):\n", dot_m)

# Transpose of a matrix
A_T = A.T
print("\nTranspose of matrix A:\n", A_T)

# Inverse of a matrix
try:
    A_inv = np.linalg.inv(A)
    print("\nInverse of matrix A:\n", A_inv)
except np.linalg.LinAlgError:
    print("\nMatrix A is singular and cannot be inverted.")

# Determinant of a matrix
det_A = np.linalg.det(A)
print("\nDeterminant of matrix A:", det_A)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues of matrix A:", eigenvalues)
print("Eigenvectors of matrix A:\n", eigenvectors)
