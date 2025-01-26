import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, w):
    M = len(x)
    p = np.poly1d(0.0)

    for j in range(M):
        pt = np.poly1d(w[j])
        for k in range(M):
            if k == j:
                continue
            fac = x[j] - x[k]
            pt *= np.poly1d([1.0, -x[k]]) / fac
        p += pt

    return p

x_data = np.arange(1, 21)
y_data = np.array([5, 6, 8, 10, 12, 13, 12, 10, 8, 10, 8, 11, 7, 9, 11, 10, 9, 12, 11, 6])

interpolated_points = []
step = 0.25

for i in range(3):
    xi = np.arange(x_data[i], x_data[i+1] + 0.01, step)
    poly = lagrange(x_data[:6], y_data[:6])
    interpolated_values = poly(xi)
    interpolated_points.append((xi, interpolated_values))

for i in range(3, len(x_data) - 4):
    xi = np.arange(x_data[i], x_data[i+1] + 0.01, step)
    poly = lagrange(x_data[i-2:i+4], y_data[i-2:i+4])
    interpolated_values = poly(xi)
    interpolated_points.append((xi, interpolated_values))

for i in range(len(x_data) - 4, len(x_data) - 1):
    xi = np.arange(x_data[i], x_data[i+1] + 0.01, step)
    poly = lagrange(x_data[-6:], y_data[-6:])
    interpolated_values = poly(xi)
    interpolated_points.append((xi, interpolated_values))


xi_all = np.concatenate([points[0] for points in interpolated_points])
ui_all = np.concatenate([points[1] for points in interpolated_points])


plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'bo', label='Исходные точки')
plt.plot(xi_all, ui_all, 'k.', label='Интерполированный полином')
plt.plot(x_data, y_data, 'r-', label='График по исходным точкам')
plt.plot(xi_all, ui_all, 'g-', label='График по интерполированным точкам')
plt.title('Интерполяция полиномом Лагранжа пятого порядка')
plt.xlabel('x')
plt.ylabel('y', rotation='horizontal')
plt.legend()
plt.grid()
plt.show()
