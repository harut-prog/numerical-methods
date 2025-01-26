def dichotomy(f, a, b, e=1e-6):
    # проверка на существование корня на данном интервале
    if f(a) * f(b) > 0:
        return None
    
    i = 0 # счётчик для вывода числа итераций
    mid = 0 # создаём переменную для того, чтобы она была в области видимости функции
    while abs(b - a) > e:
        i += 1
        
        mid = (a + b) / 2
        print(f'{i} iteration: {mid}')

        if f(mid) == 0:
            return mid

        if f(a) * f(mid) <= 0:
            b = mid
        else:
            a = mid
        
    return mid

f = lambda x: 3 * x**5 - 1.22 * x**4 - 5.7 * x**3 + 9 * x**2 + 23.5 * x - 55

point = dichotomy(f, -20, 20)
if point is not None:
    print()
    print(f'x: {point}, f(x): {f(point)}')
else:
    print('Нет корней')