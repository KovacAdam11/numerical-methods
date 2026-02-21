# ===============================================
# GAUSS-SEIDELOVA METÓDA
# ===============================================

# riadková norma vektora = max(|xi|)
def norma_inf(v):
    return max(abs(x) for x in v)

# Gauss-Seidel
def gauss_seidel(A, b, x0, eps, max_iter=1000):
    n = len(A)
    x = x0[:]  # kópia
    k = 0

    while k < max_iter:
        x_old = x[:]

        # výpočet nového vektora (používame už nové hodnoty)
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))        # j < i -> nové x
            s2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))  # j > i -> staré x

            x[i] = (b[i] - s1 - s2) / A[i][i]

        k += 1

        # ukončenie ||x(k+1) - x(k)|| <= eps  
        diff = [x[i] - x_old[i] for i in range(n)]
        if norma_inf(diff) <= eps:
            return x, k

    return x, k


# ==========================
# VSTUPY 
# ==========================

A = [
    [7, 2, -3],
    [1, 10, 2],
    [4, 3, -8]
]

b = [14, 20, 16]

# počiatočná aproximácia   
x0 = [0, 0, 0]

eps = float(input("Zadaj eps (napr. 0.001): "))

x, it = gauss_seidel(A, b, x0, eps)

print("\n===================================")
print("Riešenie (x):")
for i, xi in enumerate(x):
    print(f"x{i+1} = {xi:.6f}")
print(f"Počet iterácií: {it}")
print("===================================")
