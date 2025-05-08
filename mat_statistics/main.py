from scipy.integrate import quad
import numpy as np

np.random.seed(42)
n = 1000
u1 = np.random.uniform(size=n)
x = np.zeros(n)

for i in range(n):
    if u1[i] < 2/7:
        # F1(x) = x^(1/1000)
        u2 = np.random.uniform()
        x[i] = u2 ** 1000
    else:
        # F2(x) = x^(1/100)
        u2 = np.random.uniform()
        x[i] = u2 ** 100

sample_mean = np.mean(x)

def integral1(x):
    return x * (1/1000) * x ** (1/1000 - 1)

result1 = quad(integral1, 0, 1)
E_X1 = result1[0]

def integral2(x):
    return x * (1/100) * x ** (1/100 - 1)

result2 = quad(integral2, 0, 1)
E_X2 = result2[0]

theoretical_mean = (2/7) * E_X1 + (5/7) * E_X2

print(f"Выборочное среднее: {sample_mean:.6f}")
print(f"Теоретическое среднее: {theoretical_mean:.6f}")