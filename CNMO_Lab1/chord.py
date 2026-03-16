import math
import time


def f1(x):
    return math.log(x) - (x - 2) ** 3 - 5 * math.sin(3 * x)


def f2(x):
    return x ** 6 - 1.4 * x ** 5 - 22.07 * x ** 4 + 11.292 * x ** 3 + 152.842 * x ** 2 + 28.1318 * x - 227.101


def chord(a, b, eps, f, max_iter=100000):
    if f(a) * f(b) > 0:
        return None, 0, 0

    start_time = time.perf_counter()
    iterations = 0
    x_old = a

    while iterations < max_iter:
        x = a - f(a) * (b - a) / (f(b) - f(a))
        iterations += 1

        if abs(x - x_old) < eps:
            end_time = time.perf_counter()
            return x, iterations, end_time - start_time

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        x_old = x

    return None, iterations, None


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

print("Метод хорд для f1:")

for a, b in intervals_f1:
    root, iters, t = chord(a, b, 1e-6, f1)
    print(f"[{a}; {b}]")
    print("Корень:", root)
    print("Итераций:", iters)
    print("Время:", f"{t:.7f}", "сек\n")

print("Метод хорд для f2:")

for a, b in intervals_f2:
    root, iters, t = chord(a, b, 1e-6, f2)
    print(f"[{a}; {b}]")
    print("Корень:", root)
    print("Итераций:", iters)
    print("Время:", f"{t:.7f}", "сек\n")