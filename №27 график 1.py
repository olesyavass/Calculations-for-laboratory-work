import numpy as np
import os
import matplotlib.pyplot as plt
def mnk(x, y, delta_y):#x t^2 у это h
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mean_xx = np.mean(x*x)
    mean_yy = np.mean(y*y)
    mean_xy = np.mean(x*y)
    V = mean_xx - mean_x**2
    U = mean_yy - mean_y**2
    k = (mean_xy - mean_x*mean_y)/V
    b = mean_y - k*mean_x
    sigma_y = delta_y
    sigma_k = sigma_y*np.sqrt(1/V)
    sigma_b = sigma_y*np.sqrt((mean_x**2)/V)
    r = (mean_xy - mean_x*mean_y)/np.sqrt(U*V)
    return k, b, sigma_k, sigma_b, r
def dt(t):
    N = len(t)
    t_mean = np.mean(t)
    delta_t_pr = 0.1
    sigma_t = np.sqrt(np.sum((t-t_mean)**2)/(N*(N-1)))
    delta_t_sl = sigma_t*2.77
    delta_t = np.sqrt(delta_t_pr**2 + delta_t_sl**2)
    return delta_t
h = np.array([10, 15, 20, 25, 30])
delta_h = 0.1
t_1 = np.array([0.892, 0.809, 0.913, 0.758, 0.876])
t_2 = np.array([0.990, 0.955, 0.965, 1.026, 1.050])
t_3 = np.array([1.299, 1.202, 1.232, 1.225, 1.179])
t_4 = np.array([1.235, 1.304, 1.328, 1.246, 1.366])
t_5 = np.array([1.402, 1.501, 1.395, 1.415, 1.385])
t_mean = []
t_err = []
for i, t in enumerate([t_1, t_2, t_3, t_4, t_5], start = 1):
    t_m = np.mean(t)
    t_e = dt(t)
    t_mean.append(t_m)
    t_err.append(t_e)
print("Среднее время:", ", ".join(f"{i:.3f}" for i in t_mean))
print("Полные абсолютные погрешности для среднего времени:", ", ".join(f"{i:.3f}" for i in t_err))
t_mean = np.array(t_mean)
t_err = np.array(t_err)
x = t_mean**2
delta_x = 2*t_mean*t_err
print("Квадрат среднего времени:", ", ".join(f"{i:.3f}" for i in x))
print("Полные абсолютные погрешности для квадратов среднего времени:", " ,".join(f"{i:.3f}" for i in delta_x))
y = h
delta_y = delta_h
k, b, sigma_k, sigma_b, r = mnk(x, y, delta_y)
print(f"k = {k:.3f} +- {sigma_k:.3f}")
print(f"b = {b:.3f} +- {sigma_b:.3f}")
print(f"Коэфициент корреляции r = {r:.3f}")
plt.figure(figsize = (6.5, 4.5), dpi = 300)
plt.errorbar(x, y, xerr = delta_x, yerr = delta_y, fmt = 'o', markersize = 3, color = 'purple', ecolor = 'grey', elinewidth = 1, capsize = 3)
x_mnk = np.linspace(min(x)-0.05, max(x)+0.05, 100)
y_mnk = k*x_mnk + b
legend = (f'$y = ({k:.3f}\\pm{sigma_k:.3f})x + ({b:.3f}\\pm{sigma_b:.3f})$\n$r = {r:.3f}$')
plt.plot(x_mnk, y_mnk, 'r-', linewidth = 1.2, label = legend)
plt.xlabel(r'$t^2$, $\mathrm{c}^2$', fontsize = 11)
plt.ylabel(r'$h$, $\mathrm{cм}$', fontsize = 11)
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.legend(frameon = True, fontsize = 9)
plt.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "h_t2.pdf")
plt.savefig(save_path)
print(f'Файл сохранен: {save_path}')
plt.show()
