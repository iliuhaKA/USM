import math
import time


def f1(x):
    return math.log(x) - (x - 2) ** 3 - 5 * math.sin(3 * x)


def f2(x):
    return x ** 6 - 1.4 * x ** 5 - 22.07 * x ** 4 + 11.292 * x ** 3 + 152.842 * x ** 2 + 28.1318 * x - 227.101


def simple_iteration(x0, eps, f, lambd, max_iter=100000):
    start_time = time.perf_counter()
    iterations = 0

    while iterations < max_iter:
        x1 = x0 + lambd * f(x0)
        iterations += 1

        if abs(x1 - x0) < eps:
            end_time = time.perf_counter()
            return x1, iterations, end_time - start_time

        x0 = x1

    return None, iterations, None


root1, iter1, time1 = simple_iteration(1, 1e-6, f1, -0.05)
root2, iter2, time2 = simple_iteration(1.5, 1e-6, f2, -0.002)

print("Simple iteration f1:")
print("Корень:", root1)
print("Итераций:", iter1)
print("Время:", f"{time1:.7f}", "сек")

print("\nSimple iteration f2:")
print("Корень:", root2)
print("Итераций:", iter2)
print("Время:", f"{time2:.7f}", "сек")