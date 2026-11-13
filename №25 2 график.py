import os
import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.1, 0.2, 0.3, 0.4])
delta_x = 0.001
t = np.array([4.29, 6.81, 7.17, 8.00])
delta_t = 0.2
y = (t/10)**2
delta_y = (2*t/100)*delta_t
N = len(x)
mean_x = np.mean(x)
mean_y = np.mean(y)
mean_xx = np.mean(x**2)
mean_xy = np.mean(x*y)
mean_yy = np.mean(y**2)
V = mean_xx - mean_x**2
k = (mean_xy - mean_x*mean_y)/V
b = mean_y - k*mean_x
res = y - (k*x+b)
sigma_y = np.mean(delta_y)
sigma_k = sigma_y*np.sqrt(1/V)
sigma_b = sigma_y*np.sqrt(mean_xx/V)
U = mean_yy - mean_y**2
r = (mean_xy - mean_x*mean_y)/np.sqrt(V*U)
print(f"k = {k:.4f}+-{sigma_k:.4f}")
print(f"b = {b:.4f}+-{sigma_b:.4f}")
print(f"Коэфициент корреляции r = {r:.4f}")
plt.figure(figsize=(6.5, 4.5), dpi = 300)
plt.errorbar(x, y, xerr=delta_x, yerr=delta_y, fmt='o', color = 'green', ecolor='gray', elinewidth=1, capsize=3)
x_mnk = np.linspace(min(x)-0.05, max(x)+0.05, 100)
y_mnk = k*x_mnk+b
legend = (f'$y = ({k:.2f}\\pm {sigma_k:.2f})x + ({b:.2f}\\pm{sigma_b:.2f})$\n$r = {r:.4f}$')
plt.plot(x_mnk, y_mnk, 'r-', linewidth=1.2, label = legend)
plt.xlabel(r'$M$, кг.', fontsize=11)
plt.ylabel(r'$\mathrm{T}^2$, $\mathrm{c}^2$', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(frameon=True, fontsize=9)
plt.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, '2graph.pdf')
plt.savefig(save_path)
print(f"Файл сохранен: {save_path}")
plt.show()
