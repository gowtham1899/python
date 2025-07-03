import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# -----------------------------
# 1. Discrete Distribution: Binomial
# -----------------------------
print("==== Binomial Distribution ====")
n, p = 10, 0.5  # 10 trials, 50% success rate
x_val = 3
binom_prob = binom.pmf(x_val, n, p)
print(f"P(X = {x_val}) for Binomial(n=10, p=0.5): {binom_prob}")

# Generate samples
binom_samples = binom.rvs(n, p, size=10)
print("Sample binomial values:", binom_samples)

# -----------------------------
# 2. Continuous Distribution: Normal
# -----------------------------
print("\n==== Normal Distribution ====")
mu, sigma = 0, 1  # standard normal

# PDF and CDF
pdf_val = norm.pdf(0, mu, sigma)
cdf_val = norm.cdf(1, mu, sigma)
print(f"PDF at x=0: {pdf_val}")
print(f"CDF at x=1: {cdf_val}")

# Plot Normal Distribution
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, mu, sigma), label='Normal PDF')
plt.title('Normal Distribution PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()

# -----------------------------
# 3. Bayes' Theorem - Manual Calculation
# -----------------------------
print("\n==== Bayes' Theorem ====")
# Given:
# P(Disease) = 1%
# P(Positive | Disease) = 99%
# P(Positive | No Disease) = 5%

P_D = 0.01
P_not_D = 1 - P_D
P_Pos_given_D = 0.99
P_Pos_given_not_D = 0.05

# Total probability of testing positive
P_Pos = (P_Pos_given_D * P_D) + (P_Pos_given_not_D * P_not_D)

# Apply Bayes' Theorem
P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos

print(f"P(Disease | Positive Test): {P_D_given_Pos:.4f}")
