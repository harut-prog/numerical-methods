def modified_newton(f, deriv, a, b, *, e=1e-6):
    # корень не найден на этом отрезке
    if f(a) * f(b) > 0:
        return None

    eps = 1e-2 # порог для способа Гарвика
    i = 0 # счётчик для подсчёта количества итераций

    x0 = b
    xn_1 = x0
    xn = x0 + eps # инициализация переменной, чтобы она была в области видимости функции

    # способ Гарвика
    while abs(xn - xn_1) >= eps: # пока разность между итерациями больше порога
        i += 1
        xn_1 = xn
        xn = xn_1 - f(xn_1) / deriv(x0)
        if abs(f(xn)) <= e:
            return xn
        
        print(f'{i} iteration: {xn}')

    # Если разность между итерациями стала меньше порога
    # Продолжаем итерации, пока разность не начнет расти
    while abs(xn - xn_1) < eps: # пока разность между итерациями больше порога
        i += 1
        xn_1 = xn
        xn = xn_1 - f(xn_1) / deriv(x0)
        if abs(f(xn)) <= e:
            return xn
        
        print(f'{i} iteration: {xn}')

    return xn

def linear_interpolation(f, a, b, *, e=1e-6):
    # Корень не найден на этом отрезке
    if f(a) * f(b) > 0:
        return None

    # 1 итерация
    x0 = b
    xn_1 = a
    xn = (x0 * f(xn_1) - xn_1 * f(x0)) / (f(xn_1) - f(x0))
    
    eps = 1e-2  # Порог для способа Гарвика
    i = 0
    # Способ Гарвика
    while abs(xn - xn_1) >= eps:  # Пока разность между итерациями больше порога
        i += 1
        print(f'{i} iteration: {xn}')

        if abs(f(xn)) <= e:
            return xn

        xn_1 = xn
        xn = (x0 * f(xn_1) - xn_1 * f(x0)) / (f(xn_1) - f(x0))

    # Если разность между итерациями стала меньше порога
    # Продолжаем итерации, пока разность не начнет расти
    while abs(xn - xn_1) < eps:  # Пока разность меньше порога
        i += 1
        print(f'{i} iteration: {xn}')

        if abs(f(xn)) <= e:
            return xn

        xn_1 = xn
        xn = (x0 * f(xn_1) - xn_1 * f(x0)) / (f(xn_1) - f(x0))

    return xn

def secant(f, a, b, *, e=1e-6, iterations=100):
    # проверка на существование корня на данном интервале
    if f(a) * f(b) > 0:
        return None
    
    xn = 0 # инициализация переменной, чтобы она была в области видимости функции
    xn_2, xn_1 = b, b - 1 # по поводу xn_1 не уверен, но из-за того, что единственное отличие от метода хорд в том, что функция в обеих точках положительна, то вот
    for _ in range(1, iterations + 1):
        xn = xn_1 - (xn_1 - xn_2) * f(xn_1) / (f(xn_1) - f(xn_2))
        if abs(f(xn)) <= e:
            return xn
        xn_2, xn_1 = xn_1, xn

        print(f'{_} iteration: {xn}')

    return xn

def newton(f, deriv, a, b, *, e=1e-6, iterations=100):
    # проверка на существование корня на данном интервале
    if f(a) * f(b) > 0:
        return None
    
    xn = 0 # инициализируем переменную, чтобы она была в области видимости функции
    xn_1 = b if f(b) > 0 else a # выбираем первоначальное значение, чтобы функция в точке была положительной
    for _ in range(1, iterations + 1):
        xn = xn_1 - f(xn_1) / deriv(xn_1)
        if abs(f(xn)) <= e:
            return xn
        xn_1 = xn

        print(f'{_} iteration: {xn:.6f}')

    return xn

f = lambda x: 3 * x**5 - 1.22 * x**4 - 5.7 * x**3 + 9 * x**2 + 23.5 * x - 55
d = lambda x: 15 * x**4 - 4.88 * x**3 - 17.1 * x**2 + 18 * x + 23.5

point = secant(f, -20, 20, e=1e-14)
if point is not None:
    print()
    print(f'x: {point}, f(x): {f(point)}')
else:
    print('Нет корней')