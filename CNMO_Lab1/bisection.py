import math
import time

def f1(x):
    return math.log(x) - (x - 2)**3 - 5 * math.sin(3 * x)

def f2(x):
    return x**6 - 1.4*x**5 - 22.07*x**4 + 11.292*x**3 + 152.842*x**2 + 28.1318*x - 227.101


def bisection(a, b, eps, f, max_iter=100000):

    if f(a) * f(b) > 0:
        return None, 0, 0

    start_time = time.perf_counter()
    iterations = 0

    while abs(b - a) > eps and iterations < max_iter:

        c = (a + b) / 2
        iterations += 1

        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c

    end_time = time.perf_counter()

    root = (a + b) / 2
    return root, iterations, end_time - start_time


intervals_f1 = [
    (0.1, 0.5),
    (0.5, 1),
    (2, 2.5),
    (3, 3.5),
    (3.5, 4)
]

intervals_f2 = [
    (-2.5, -2.0),
    (1, 1.5)
]


print("Метод бисекции для f1:\n")

for a, b in intervals_f1:
    root, iters, t = bisection(a, b, 1e-6, f1)

    print(f"[{a}; {b}]")
    print("Корень:", root)
    print("Итераций:", iters)
    print("Время:", f"{t:.7f}", "сек\n")


print("Метод бисекции для f2:\n")

for a, b in intervals_f2:
    root, iters, t = bisection(a, b, 1e-6, f2)

    print(f"[{a}; {b}]")
    print("Корень:", root)
    print("Итераций:", iters)
    print("Время:", f"{t:.7f}", "сек\n")