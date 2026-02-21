# ===============================================
# JACOBIHO METÓDA
# ===============================================

# riadková norma vektora = max(|xi|)
def norma_inf(v):
    return max(abs(x) for x in v)

def jacobi(A, b, x0, eps, max_iter=1000):
    n = len(A)
    x_old = x0[:]   # x^(k)
    k = 0

    while k < max_iter:
        x_new = [0.0] * n   # x^(k+1)

        for i in range(n):
            s = 0.0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x_old[j]

            x_new[i] = (b[i] - s) / A[i][i]

        k += 1

        # ukončenie ||x(k+1) - x(k)|| <= eps
        diff = [x_new[i] - x_old[i] for i in range(n)]
        if norma_inf(diff) <= eps:
            return x_new, k

        x_old = x_new

    return x_old, k


# ==========================
# VSTUPY
# ==========================
A = [
    [7, 2, -3],
    [1, 10, 2],
    [4, 3, -8]
]

b = [14, 20, 16]

x0 = [0, 0, 0]   # počiatočná aproximácia

eps = float(input("Zadaj eps (napr. 0.001): "))

x, it = jacobi(A, b, x0, eps)

print("\n===================================")
print("Riešenie (x):")
for i, xi in enumerate(x):
    print(f"x{i+1} = {xi:.6f}")
print(f"Počet iterácií: {it}")
print("===================================")
