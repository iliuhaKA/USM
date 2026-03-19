import numpy as np

EPS = 1e-6
MAX_ITER = 100


# ====== МЕТОД ЯКОБИ ======
def jacobi(eps=EPS, max_iter=MAX_ITER, verbose=True):
    x = np.zeros(4)

    print("=== МЕТОД ЯКОБИ ===\n")

    for k in range(max_iter):
        x_new = np.zeros(4)

        x_new[0] = (0.243 - 0.519*x[1] - 0.364*x[2] - 0.283*x[3]) / 5.401
        x_new[1] = (0.231 - 0.295*x[0] - 0.421*x[2] - 0.278*x[3]) / 4.830
        x_new[2] = (0.721 - 0.524*x[0] - 0.397*x[1] - 0.389*x[3]) / 3.723
        x_new[3] = (0.220 - 0.503*x[0] - 0.264*x[1] - 0.248*x[2]) / 4.286

        diff = np.linalg.norm(x_new - x, ord=np.inf)

        if verbose:
            print(f"Итерация {k+1}:")
            print(f"x1 = {x_new[0]:.6f}, x2 = {x_new[1]:.6f}, x3 = {x_new[2]:.6f}, x4 = {x_new[3]:.6f}")
            print(f"||x_new - x|| = {diff:.7f}\n")

        if diff < eps:
            print("Сходимость достигнута\n")
            return x_new, k+1

        x = x_new

    print("Достигнут лимит итераций\n")
    return x, max_iter


# ====== МЕТОД ГАУССА–ЗЕЙДЕЛЯ ======
def gauss_seidel(eps=EPS, max_iter=MAX_ITER, verbose=True):
    x = np.zeros(4)

    print("=== МЕТОД ГАУССА–ЗЕЙДЕЛЯ ===\n")

    for k in range(max_iter):
        x_old = x.copy()

        x[0] = (0.243 - 0.519*x[1] - 0.364*x[2] - 0.283*x[3]) / 5.401
        x[1] = (0.231 - 0.295*x[0] - 0.421*x[2] - 0.278*x[3]) / 4.830
        x[2] = (0.721 - 0.524*x[0] - 0.397*x[1] - 0.389*x[3]) / 3.723
        x[3] = (0.220 - 0.503*x[0] - 0.264*x[1] - 0.248*x[2]) / 4.286

        diff = np.linalg.norm(x - x_old, ord=np.inf)

        if verbose:
            print(f"Итерация {k+1}:")
            print(f"x1 = {x[0]:.6f}, x2 = {x[1]:.6f}, x3 = {x[2]:.6f}, x4 = {x[3]:.6f}")
            print(f"||x_new - x|| = {diff:.7f}\n")

        if diff < eps:
            print("Сходимость достигнута\n")
            return x, k+1

    print("Достигнут лимит итераций\n")
    return x, max_iter


# ====== ЗАПУСК ======
jacobi_result, jacobi_iters = jacobi()
print("ИТОГ (Якоби):")
print(f"x = {jacobi_result}")
print(f"Итераций: {jacobi_iters}\n")

print("="*50, "\n")

gs_result, gs_iters = gauss_seidel()
print("ИТОГ (Гаусс–Зейдель):")
print(f"x = {gs_result}")
print(f"Итераций: {gs_iters}")