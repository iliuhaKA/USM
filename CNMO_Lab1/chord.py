import math

def f1(x):
    return math.log(x) - (x - 2)**3 - 5 * math.sin(3 * x)

def f2(x):
    return x**6 - 1.4*x**5 - 22.07*x**4 + 11.292*x**3 + 152.842*x**2 + 28.1318*x - 227.101


def chord(a, b, eps, f):
    if f(a) * f(b) > 0:
        return None  # нет смены знака

    while abs(b - a) > eps:
        x = a - f(a) * (b - a) / (f(b) - f(a))
        print("n")
        if f(a) * f(x) <= 0:
            b = x
        else:
            a = x

    return (a + b) / 2


print("Корень на промежутке: [0.1; 0.5]: ", chord(0.1, 0.5, 1e-6, f1))
print("Корень на промежутке: [0.5; 1]: ", chord(0.5, 1, 1e-6, f1))
print("Корень на промежутке: [2; 2.5]: ", chord(2, 2.5, 1e-6, f1))
print("Корень на промежутке: [3; 3.5]: ", chord(3, 3.5, 1e-6, f1))
print("Корень на промежутке: [3.5; 4]: ", chord(3.5, 4, 1e-6, f1))

print("\n")

print("Корень на промежутке: [-2.5, -2.0]: ", chord(-2.5, -2.0, 1e-6, f2))
print("Корень на промежутке: [1, 1.5]: ", chord(1, 1.5, 1e-6, f2))