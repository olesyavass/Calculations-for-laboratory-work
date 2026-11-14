import numpy as np
print("БОЛЬШАЯ ПРУЖИНА")
delta_l = 0.1
l0 = 30
l = np.array([34, 38.6, 42.5, 46.5])
l_rav = l-l0
delta_l_rav = np.sqrt(2*delta_l**2)
print("Удлинения:", ", ".join(f"{i:.2f}+-{delta_l_rav:.2f}" for i in l_rav))
M = np.array([0.1, 0.2, 0.3, 0.4])
delta_M = 0.001
g = 10
k = M*g/(l_rav/100)
M_mean = np.mean(M)
l_rav_mean = np.mean(l_rav) / 100
delta_k_kosv = np.sqrt((g / l_rav_mean)**2 * delta_M**2 + (M_mean * g / l_rav_mean**2)**2 * (delta_l_rav / 100)**2)
def dk(k):
    N = len(k)
    k_mean = np.mean(k)
    sigma_k = np.sqrt(np.sum((k-k_mean)**2)/(N*(N-1)))
    delta_k_sl = sigma_k*3.18
    delta_k = np.sqrt(delta_k_kosv**2 + delta_k_sl**2)
    return delta_k, sigma_k, delta_k_sl
delta_k, sigma_k, delta_k_sl = dk(k)
print(f"Косвенная погрешность жесткости:{delta_k_kosv:.2f}")
print(f"Среднеквадратичная погрешность среднего арифметического:{sigma_k:.2f}")
print(f"Случайная погрешность жесткости:{delta_k_sl:.2f}")
print(f"Полная абсолютная погрешность жесткости:{delta_k:.1f}")
print(f"Доверительный интервал жесткости: [{np.mean(k) - delta_k:.1f}; {np.mean(k) + delta_k:.1f}]")
print("МАЛАЯ ПРУЖИНА")
delta_l = 0.1
l0 = 23
l = np.array([28, 32.5, 37.7, 42.4])
l_rav = l-l0
delta_l_rav = np.sqrt(2*delta_l**2)
print("Удлинения:", ", ".join(f"{i:.2f}+-{delta_l_rav:.2f}" for i in l_rav))
M = np.array([0.1, 0.2, 0.3, 0.4])
delta_M = 0.001
g = 10
k = M*g/(l_rav/100)
M_mean = np.mean(M)
l_rav_mean = np.mean(l_rav) / 100
delta_k_kosv = np.sqrt((g / l_rav_mean)**2 * delta_M**2 + (M_mean * g / l_rav_mean**2)**2 * (delta_l_rav / 100)**2)
def dk(k):
    N = len(k)
    k_mean = np.mean(k)
    sigma_k = np.sqrt(np.sum((k-k_mean)**2)/(N*(N-1)))
    delta_k_sl = sigma_k*3.18
    delta_k = np.sqrt(delta_k_kosv**2 + delta_k_sl**2)
    return delta_k, sigma_k, delta_k_sl
delta_k, sigma_k, delta_k_sl = dk(k)
print(f"Косвенная погрешность жесткости:{delta_k_kosv:.2f}")
print(f"Среднеквадратичная погрешность среднего арифметического:{sigma_k:.2f}")
print(f"Случайная погрешность жесткости:{delta_k_sl:.2f}")
print(f"Полная абсолютная погрешность жесткости:{delta_k:.1f}")
print(f"Доверительный интервал жесткости: [{np.mean(k) - delta_k:.1f}; {np.mean(k) + delta_k:.1f}]")
