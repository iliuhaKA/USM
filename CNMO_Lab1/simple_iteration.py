import math

def f1(x):
    return math.log(x) - (x - 2)**3 - 5 * math.sin(3 * x)

def f2(x):
    return x**6 - 1.4*x**5 - 22.07*x**4 + 11.292*x**3 + 152.842*x**2 + 28.1318*x - 227.101


def simple_iteration(x0, eps, f, lambd):
    while True:
        x1 = x0 + lambd * f(x0)

        if abs(x1 - x0) < eps:
            return x1

        x0 = x1


print("Simple iteration f1:", simple_iteration(1, 1e-6, f1, -0.05))
print("Simple iteration f2:", simple_iteration(1.5, 1e-6, f2, -0.002))