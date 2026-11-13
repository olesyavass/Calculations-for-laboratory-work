import numpy as np
import os
import matplotlib.pyplot as plt
def fit_mnk(x, y, delta_y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mean_xx = np.mean(x**2)
    mean_xy = np.mean(x * y)
    mean_yy = np.mean(y**2)
    
    V = mean_xx - mean_x**2
    U = mean_yy - mean_y**2
    
    k = (mean_xy - mean_x * mean_y) / V
    b = mean_y - k * mean_x
    
    sigma_y = np.mean(delta_y)
    sigma_k = sigma_y * np.sqrt(1.0 / V)
    sigma_b = sigma_y * np.sqrt(mean_x**2 / V)
    r = (mean_xy - mean_x * mean_y) / np.sqrt(V * U)
    
    return k, b, sigma_k, sigma_b, r
t1 = np.array([0, 135, 302, 654])
t2 = np.array([0, 140, 328, 756])
t3 = np.array([0, 143, 345, 820])
t_mean = (t1+t2+t3)/3
A0 = 4
A = np.array([4, 3, 2, 1])
delta_y = np.sqrt((0.1/A0)**2 + (0.1/A)**2)
y = np.log(A0/A)
sum_sq = (t1-t_mean)**2+(t2-t_mean)**2+(t3-t_mean)**2
S_t = np.sqrt(sum_sq/6)
delta_t_sl = S_t*4.3
delta_t = np.sqrt(delta_t_sl**2+0.2**2)
delta_t[0] = 0.2
k, b, sigma_k, sigma_b, r = fit_mnk(t_mean, y, delta_y)
tau = 1/k
sigma_tau = sigma_k/k**2
print(f"Коэффициент затухания gamma = ({k*1e3:.2f} ± {sigma_k*1e3:.2f})*10^-3 * с^-1")
print(f"Время затухания tau = ({tau:.0f} ± {sigma_tau:.0f}) с")
print(f"Коэффициент корреляции r = {r:.4f}")
plt.figure(figsize=(6.5, 4.5), dpi=300)
plt.errorbar(t_mean, y, xerr=delta_t, yerr=delta_y, fmt='o', color='navy',
             ecolor='gray', elinewidth=1, capsize=3)
t_line = np.linspace(-15, 800, 100)
legend = (
    rf'$y = ({k*1e3:.2f} \pm {sigma_k*1e3:.2f})\cdot 10^{{-3}} t + ({b:.2f} \pm {sigma_b:.2f})$' + '\n' +
    rf'$\gamma = ({k*1e3:.2f} \pm {sigma_k*1e3:.2f})\cdot 10^{{-3}}\ \mathrm{{c}}^{{-1}},\ r = {r:.4f}$'
)
plt.plot(t_line, k * t_line + b, 'r-', linewidth=1.2, label=legend)
plt.xlabel(r'$t_{\mathrm{сред}}$, с', fontsize=11)
plt.ylabel(r'$\ln(A_0 / A)$', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(frameon=True, fontsize=9)
plt.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, '3graph.pdf')
plt.savefig(save_path)
print(f"Файл сохранен: {save_path}")

plt.show()
