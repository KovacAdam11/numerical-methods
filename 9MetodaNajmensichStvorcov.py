# ===============================================
# METÓDA NAJMENŠÍCH ŠTVORCOV - PRIAMKA
# ===============================================

n = int(input("Zadaj počet bodov n: "))

x = []
y = []

for i in range(n):
    xi = float(input(f"Zadaj x{i+1}: "))
    yi = float(input(f"Zadaj y{i+1}: "))
    x.append(xi)
    y.append(yi)

# sumy pre normálne rovnice
S1 = n
Sx = sum(xi for xi in x)
Sx2 = sum(xi**2 for xi in x)
Sy = sum(yi for yi in y)
Sxy = sum(x[i] * y[i] for i in range(n))

# determinant
D = S1 * Sx2 - Sx * Sx

if D == 0:
    print("Chyba: nedá sa vypočítať (determinant je 0). Skús iné body.")
else:
    # koeficienty c1, c2
    c1 = (Sy * Sx2 - Sx * Sxy) / D
    c2 = (S1 * Sxy - Sx * Sy) / D

    # funkcia priamky
    def phi(xv):
        return c1 + c2 * xv

    # MSE
    mse = sum((phi(x[i]) - y[i])**2 for i in range(n)) / n

    print("\n===================================")
    print(f"c1 = {c1:.8f}")
    print(f"c2 = {c2:.8f}")
    print(f"Priamka: φ(x) = {c1:.8f} + {c2:.8f} * x")
    print(f"MSE = {mse:.8f}")
    print("===================================")
