import numpy as np

def crank_nicolson(l, T, alpha, m, N, f):
    """
    Sabohat
    Crank-Nicolson usuli yordamida parabolik tenglamani yechish.
    Parametrlar:
        l (float): Segmentning uzunligi.
        T (float): Maksimal vaqt.
        alpha (float): Doimiy qiymat.
        m (int): X yo'nalishidagi bo'linmalar soni.
        N (int): Vaqt yo'nalishidagi bo'linmalar soni.
        f (function): Dastlabki shart funksiyasi f(x).
        
    Natija:
        Har bir x va t nuqtasidagi yaqinlashtirilgan yechimlar.
    """
    h = l / m
    k = T / N
    λ = (alpha ** 2) * (k / h ** 2)
    w = np.zeros((m + 1, N + 1))
    for i in range(1, m):
        w[i, 0] = f(i * h)  
    l1 = 1 + λ
    u1 = -λ / (2 * l1)
    l_arr = np.zeros(m)
    u_arr = np.zeros(m)
    l_arr[1] = l1
    u_arr[1] = u1
    for i in range(2, m):
        l_arr[i] = 1 + λ + λ * u_arr[i - 1] / 2
        u_arr[i] = -λ / (2 * l_arr[i])
    for j in range(1, N + 1):
        t = j * k
        z = np.zeros(m + 1)
        z[1] = ((1 - λ) * w[1, j - 1] + λ * w[2, j - 1] / 2) / l_arr[1]
        for i in range(2, m):
            z[i] = ((1 - λ) * w[i, j - 1] + λ / 2 * (w[i + 1, j - 1] + w[i - 1, j - 1] + z[i - 1])) / l_arr[i]
        w[m - 1, j] = z[m - 1]
        for i in range(m - 2, 0, -1):
            w[i, j] = z[i] - u_arr[i] * w[i + 1, j]
    results = []
    for j in range(N + 1):
        t = j * k
        time_results = [(i * h, w[i, j]) for i in range(1, m)]
        results.append((t, time_results))
    return results
def f(x):
    return np.sin(np.pi * x)  

l =7.0      # Segment uzunligi
T = 0.5      # Maksimal vaqt
alpha = 1.0  # Doimiy qiymat
m = 10       # X bo'yicha bo'linmalar soni
N = 100      # Vaqt bo'yicha bo'linmalar soni
solution = crank_nicolson(l, T, alpha, m, N, f)
for t, values in solution:
    print(f"t = {t:.4f}")
    for x, w in values:
        print(f"x = {x:.4f}, w = {w:.6f}")
    print()