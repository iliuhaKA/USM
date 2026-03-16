import math
import time

def f1(x):
    return math.log(x) - (x - 2)**3 - 5 * math.sin(3 * x)

def df1(x):
    return 1/x - 3*(x-2)**2 - 15 * math.cos(3*x)


def f2(x):
    return x**6 - 1.4*x**5 - 22.07*x**4 + 11.292*x**3 + 152.842*x**2 + 28.1318*x - 227.101


def df2(x):
    return (
        6*x**5
        - 7*x**4
        - 88.28*x**3
        + 33.876*x**2
        + 305.684*x
        + 28.1318
    )


def newton(x0, eps, f, df, max_iter=100000):

    start_time = time.perf_counter()
    iterations = 0

    while iterations < max_iter:
        x1 = x0 - f(x0) / df(x0)
        iterations += 1

        if abs(x1 - x0) < eps:
            end_time = time.perf_counter()
            return x1, iterations, end_time - start_time

        x0 = x1

    return None, iterations, None


root1, iter1, time1 = newton(1, 1e-6, f1, df1)
root2, iter2, time2 = newton(1.5, 1e-6, f2, df2)

print("Newton f1:")
print("Корень:", root1)
print("Итераций:", iter1)
print("Время:", f"{time1:.7f}", "сек")

print("\nNewton f2:")
print("Корень:", root2)
print("Итераций:", iter2)
print("Время:", f"{time2:.7f}", "сек")