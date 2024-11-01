import numpy as np
# q(x) va f(x) funksiyalarini aniqlash
def q(x):
    return np.pi**2
def f(x):
    return 2 * np.pi**2 * np.sin(np.pi * x)
def solve_tridiagonal(a, b, c, d):
    n = len(d)
    c_prime = np.zeros(n-1)
    d_prime = np.zeros(n)
    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]
    for i in range(1, n-1):
        temp = b[i] - a[i-1] * c_prime[i-1]
        c_prime[i] = c[i] / temp
        d_prime[i] = (d[i] - a[i-1] * d_prime[i-1]) / temp
    d_prime[n-1] = (d[n-1] - a[n-2] * d_prime[n-2]) / (b[n-1] - a[n-2] * c_prime[n-2])
    x = np.zeros(n)
    x[-1] = d_prime[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i+1]
    return x
def rayleigh_ritz(n):
    #  Interval va x nuqtalarini aniqlash
    x = np.linspace(0, 1, n+2)
    h = np.diff(x)  # har bir bo'lakning uzunligi
    # Tridiagonal matritsaning koeffitsiyentlari
    a = np.zeros(n-1)
    b = np.zeros(n)
    c = np.zeros(n-1)
    d = np.zeros(n)
    #  Integrallarni hisoblash (Q1, Q2, Q3, Q4, Q5, Q6)
    for i in range(1, n+1):
        hi = h[i-1]
        if i < n:
            a[i-1] = -10 + np.pi**2 / 60
        if i > 1:
            c[i-2] = -10 + np.pi**2 / 60
        b[i-1] = 20 + np.pi**2 / 15
        d[i-1] = 40 * np.sin(np.pi * x[i]) * (1 - np.cos(np.pi * 0.1))
    c_vector = solve_tridiagonal(a, b, c, d)
    return c_vector
n = int(input("n ni kiriting: "))
c = rayleigh_ritz(n)
for i in range(1, n+1):
    print(f"c{i} = {c[i-1]:.10f}")
