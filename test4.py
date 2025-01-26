import numpy as np
import matplotlib.pyplot as plt

# Определение полиномов Чебышева
def chebyshev_polynomials(n: int, x: np.ndarray) -> list[np.ndarray]:
    T = [np.ones_like(x, dtype=float), x.astype(float)]
    for i in range(2, n + 1):
        T.append(2 * x * T[i - 1] - T[i - 2])

    return T

# Аппроксимация методом наименьших квадратов
def least_squares_approximation(x: np.ndarray, y: np.ndarray, n: int) -> np.ndarray:
    T = chebyshev_polynomials(n, x)
    A = np.zeros((n + 1, n + 1))
    B = np.zeros(n + 1)

    for i in range(n + 1):
        for j in range(n + 1):
            A[i, j] = np.sum(T[i] * T[j])
        
        B[i] = np.sum(y * T[i])

    coeffs = np.linalg.solve(A, B)

    return coeffs


x_data = np.arange(1, 21)
y_data = np.array([5, 6, 8, 10, 12, 13, 12, 10, 8, 10, 8, 11, 7, 9, 11, 10, 9, 12, 11, 6])
coeffs = least_squares_approximation(x_data, y_data, 6)


T = chebyshev_polynomials(6, x_data)
y_approx = np.zeros_like(x_data, dtype=float)
for i in range(7):
    y_approx += coeffs[i] * T[i]
error = np.sum((y_data - y_approx) ** 2)


plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'o', label='Исходные данные')
plt.plot(x_data, y_approx, label='Аппроксимация', color='red')
plt.xlabel('x')
plt.ylabel('y', rotation='horizontal')
plt.title('Аппроксимация методом наименьших квадратов с использованием полиномов Чебышева 6 порядка')
plt.legend()
plt.grid(True)
plt.show()

# Вывод коэффициентов и суммы квадратов отклонений
print(coeffs, error, sep='\n')
