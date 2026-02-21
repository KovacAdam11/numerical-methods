# ===============================================
# BISEKCIA (metóda polenia intervalov)
# ===============================================

import math

# --- Funkcia f(x) ---
def f(x):
    return x - math.cos(x)   


# --- 1) Vstupné údaje ---
a = float(input("Zadaj a: "))
b = float(input("Zadaj b: "))
eps = float(input("Zadaj eps (napr. 0.001): "))

# kontrola podmienky z bisekcie: f(a)*f(b) < 0
if f(a) * f(b) > 0:
    print("Chyba: interval nespĺňa podmienku f(a)*f(b) < 0.")
else:
    # --- 2) Iteračný proces ---
    k = 0
    while (b - a) > eps:   # veľkosť intervalu <= eps
        x = (a + b) / 2
        k += 1

        if f(x) == 0:
            break
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

    # posledná aproximácia
    x = (a + b) / 2

    # --- 3) Výstup výsledku ---
    print("\n===================================")
    print(f"Koreň rovnice ≈ {x:.8f}")
    print(f"Počet iterácií: {k}")
    print(f"Interval: <{a:.8f}, {b:.8f}>")
    print("===================================")
