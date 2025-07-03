import math
import matplotlib.pyplot as plt

# -----------------------------
# Sample Data
# -----------------------------
data = [10, 12, 15, 14, 18, 21, 24, 24, 30, 35]
data_sorted = sorted(data)
n = len(data_sorted)

print("==== Descriptive Statistics (Pure Python) ====")
print("Data:", data)

# -----------------------------
# 1. Mean
# -----------------------------
mean_val = sum(data) / n
print(f"Mean: {mean_val}")

# -----------------------------
# 2. Median
# -----------------------------
if n % 2 == 1:
    median_val = data_sorted[n // 2]
else:
    median_val = (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
print(f"Median: {median_val}")

# -----------------------------
# 3. Standard Deviation (Population)
# -----------------------------
squared_diffs = [(x - mean_val) ** 2 for x in data]
variance = sum(squared_diffs) / n
std_dev = math.sqrt(variance)
print(f"Standard Deviation: {std_dev}")

# -----------------------------
# 4. Interquartile Range (IQR)
# -----------------------------
def percentile(sorted_list, percent):
    k = (len(sorted_list) - 1) * percent / 100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_list[int(k)]
    d0 = sorted_list[f] * (c - k)
    d1 = sorted_list[c] * (k - f)
    return d0 + d1

q1 = percentile(data_sorted, 25)
q3 = percentile(data_sorted, 75)
iqr = q3 - q1
print(f"IQR (Q3 - Q1): {iqr}")

# -----------------------------
# 5. Optional: Histogram Plot
# -----------------------------
plt.hist(data, bins=8, color='lightblue', edgecolor='black')
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1.5, label='Mean')
plt.axvline(median_val, color='green', linestyle='dashed', linewidth=1.5, label='Median')
plt.title("Histogram of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()
