import numpy as np

def solve_equations(lst):
    a1, b1, c1 = lst[0][0], lst[0][1], lst[0][2]
    a2, b2, c2 = lst[1][0], lst[1][1], lst[1][2]
    a3, b3, c3 = lst[2][0], lst[2][1], lst[2][2]
    d1, d2, d3 = lst[0][3], lst[1][3], lst[2][3]
  
    # создание матриц
    A = np.array([[a1, b1, c1],
                  [a2, b2, c2],
                  [a3, b3, c3]])

    B = np.array([d1, d2, d3])

    # решение системы уравнений
    solution = np.linalg.solve(A, B)

    return solution[0], solution[1], solution[2]

def newton_system(f1, f2, f3, e=1e-6):
    x, y, z = -2, 1, 3 # задаём начальное приближение
    dx, dy, dz = [e] * 3

    i = 0 # вводим переменную для подсчёта количества итераций
    while not (abs(dx) < e and abs(dy) < e and abs(dz) < e):
        print(f'{i} iteration: x = {x}; y = {y}; z = {z}')

        # запишем в массив нашу систему уравнений и через метод solve_equations решим систему для приращений
        lst = [[f1['dx'](x,y,z), f1['dy'](x,y,z), f1['dz'](x,y,z), -f1['func'](x,y,z)],
               [f2['dx'](x,y,z), f2['dy'](x,y,z), f2['dz'](x,y,z), -f2['func'](x,y,z)],
               [f3['dx'](x,y,z), f3['dy'](x,y,z), f3['dz'](x,y,z), -f3['func'](x,y,z)]]

        dx, dy, dz = solve_equations(lst) # задаём приращение аргументов

        x, y, z = x + dx, y + dy, z + dz
        i += 1

    return x, y, z

f1 = {
    'func': lambda x,y,z: x**2 - x*z + x*y**2 - 8,
    'dx': lambda x,y,z: 2*x - z + y**2,
    'dy': lambda x,y,z: 2*x*y,
    'dz': lambda x,y,z: x
}

f2 = {
    'func': lambda x,y,z: y*z + 2*x**3*y**2 + 9*x*z**2 + 175,
    'dx': lambda x,y,z: 6*x**2*y**2 + 9*z**2,
    'dy': lambda x,y,z: z + 4*x**3*y,
    'dz': lambda x,y,z: y + 18*x*z
}

f3 = {
    'func': lambda x,y,z: x*y*z - 7.5*z**4*x**3 - 4854,
    'dx': lambda x,y,z: y*z - 22.5*z**4*x**2,
    'dy': lambda x,y,z: x*z,
    'dz': lambda x,y,z: x*y - 30*z**3*x**3
}

x, y, z = newton_system(f1, f2, f3)

print()
print(f'''x = {x}; y = {y}; z = {z}
f1(x, y, z) = {f1["func"](x, y, z)}
f2(x, y, z) = {f2["func"](x, y, z)}
f3(x, y, z) = {f3["func"](x, y, z)}''')