# ===============================================
# LAGRANGEOV INTERPOLAČNÝ POLYNÓM
# ===============================================

def lagrange(x_points, y_points, x):
    n = len(x_points)
    P = 0.0

    for i in range(n):
        L = 1.0
        for j in range(n):
            if j != i:
                L *= (x - x_points[j]) / (x_points[i] - x_points[j])
        P += y_points[i] * L

    return P


# --- VSTUPY OD POUŽÍVATEĽA ---
n = int(input("Zadaj počet bodov n: "))

x_points = []
y_points = []

for i in range(n):
    xi = float(input(f"Zadaj x{i}: "))
    yi = float(input(f"Zadaj y{i}: "))
    x_points.append(xi)
    y_points.append(yi)

x = float(input("Zadaj x, v ktorom chceš vypočítať P(x): "))

# --- VÝPOČET ---
Px = lagrange(x_points, y_points, x)

print("\n===================================")
print(f"P({x:.8f}) = {Px:.8f}")
print("===================================")
