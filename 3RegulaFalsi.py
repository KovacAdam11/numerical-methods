# ===============================================
# REGULA FALSI (metóda sečníc na intervale)
# ===============================================

import math

# --- Funkcia f(x) ---
def f(x):
    return x - math.cos(x)   


# --- 1) Vstupné údaje ---
a = float(input("Zadaj a: "))
b = float(input("Zadaj b: "))
eps = float(input("Zadaj eps (napr. 0.001): "))

# --- 2) Kontrola podmienky f(a)*f(b) < 0 ---
if f(a) * f(b) > 0:
    print("Chyba: interval nespĺňa podmienku f(a)*f(b) < 0.")
else:
    # podľa PDF si môžeme zvoliť x0 = a0 pre kontrolu ukončenia 
    x0 = a
    k = 0

    while True:
        # vzorec z algoritmu regula falsi 
        x1 = a - (b - a) / (f(b) - f(a)) * f(a)
        k += 1

        # ukončovacia podmienka |x_{k+1} - x_k| <= eps 
        if abs(f(x1)) <= eps:
            break


        # výber nového intervalu podľa znamienok 
        if f(a) * f(x1) < 0:
            b = x1
        else:
            a = x1

        x0 = x1

    # --- 3) Výstup ---
    print("\n===================================")
    print(f"Koreň rovnice ≈ {x1:.8f}")
    print(f"Počet iterácií: {k}")
    print(f"Konečný interval: <{a:.8f}, {b:.8f}>")
    print("===================================")
