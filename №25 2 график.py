import os
import numpy as np
import matplotlib.pyplot as plt
def mnk(x, y, delta_y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mean_xx = np.mean(x*x)
    mean_yy = np.mean(y*y)
    mean_xy = np.mean(x*y)
    V = mean_xx - mean_x**2
    U = mean_yy - mean_y**2
    k = (mean_xy - mean_x*mean_y)/V
    b = mean_y - k*mean_x
    sigma_y = np.mean(delta_y)
    sigma_k = sigma_y*np.sqrt(1/V)
    sigma_b = sigma_y*np.sqrt((mean_x**2)/V)
    r = (mean_xy - mean_x*mean_y)/np.sqrt(U*V)
    return k, b, sigma_k, sigma_b, r
def dt(t):
    N = len(t)
    t_mean = np.mean(t)
    delta_t_pr = 0.2
    sigma_t = np.sqrt(np.sum((t-t_mean)**2)/(N*(N-1)))
    delta_t_sl = sigma_t*4.30
    delta_t = np.sqrt(delta_t_pr**2 + delta_t_sl**2)
    return delta_t, sigma_t, delta_t_sl
t_1 = [4.14, 4.45, 4.27]
t_2 = [6.10, 5.81, 5.41]
t_3 = [7.16, 6.70, 7.67]
t_4 = [8.26, 7.88, 7.87]
t_mean = []
t_err = []
sigma_t = []
delta_t_sl = []
for i, t in enumerate([t_1, t_2, t_3, t_4], start = 1):
    t_e, s_t, d_t_s = dt(t)
    t_m = np.mean(t)
    t_err.append(t_e)
    t_mean.append(t_m)
    sigma_t.append(s_t)
    delta_t_sl.append(d_t_s)
print("Среднее время:", ", ".join(f"{i:.1f}" for i in t_mean))
print("Среднеквадратичная?:", ", ".join(f"{i:.2f}" for i in sigma_t))
print("Случайная погрешность:", ", ".join(f"{i:.2f}" for i in delta_t_sl))
print("Полные абсолютные погрешности для среднего времени:", ", ".join(f"{i:.1f}" for i in t_err))
t_mean = np.array(t_mean)
t_err = np.array(t_err)
T = t_mean/10
T_err = t_err/10
y = (t_mean/10)**2
delta_y = 2*t_mean*t_err/100
print("Период:", ", ".join(f"{i:.2f}" for i in T))
print("Полные абсолютные погрешности для периодов:", " ,".join(f"{i:.2f}" for i in T_err))
print("Квадрат периода:", ", ".join(f"{i:.2f}" for i in y))
print("Полные абсолютные погрешности для квадратов периодов:", " ,".join(f"{i:.2f}" for i in delta_y))
M = np.array([0.1, 0.2, 0.3, 0.4])
delta_M = 0.001
x = M
delta_x = delta_M
k, b, sigma_k, sigma_b, r = mnk(x, y, delta_y)
print(f"k = {k:.4f}+-{sigma_k:.4f}")
print(f"b = {b:.4f}+-{sigma_b:.4f}")
print(f"Коэфициент корреляции r = {r:.4f}")
plt.figure(figsize=(6.5, 4.5), dpi = 300)
plt.errorbar(x, y, xerr=delta_x, yerr=delta_y, fmt='o', color = 'green', ecolor='gray', elinewidth=1, capsize=3)
x_mnk = np.linspace(min(x)-0.05, max(x)+0.05, 100)
y_mnk = k*x_mnk+b
legend = (f'$y = ({k:.1f}\\pm {sigma_k:.1f})x + ({b:.2f}\\pm{sigma_b:.2f})$\n$r = {r:.4f}$')
plt.plot(x_mnk, y_mnk, 'r-', linewidth=1.2, label = legend)
plt.xlabel(r'$M$, кг.', fontsize=11)
plt.ylabel(r'$\mathrm{t}^2$, $\mathrm{c}^2$', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(frameon=True, fontsize=9)
plt.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, '2`graph.pdf')
plt.savefig(save_path)
print(f"файл сохранен: {save_path}")
plt.show()
