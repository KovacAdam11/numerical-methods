# ===============================================
# NEWTONOVA METÓDA 
# ===============================================

import math

def f(x):
    return x - math.cos(x)

def f1(x, h=0.000001):
    return (f(x + h) - f(x - h)) / (2 * h)

def f2(x, h=0.000001):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

a0 = float(input("Zadaj a0: "))
b0 = float(input("Zadaj b0: "))
eps = float(input("Zadaj eps: "))

# vyber x0
if f(a0) * f2(a0) > 0:
    x = a0
elif f(b0) * f2(b0) > 0:
    x = b0
else:
    print("Chyba: Podmienka f(x)*f''(x) > 0 neplatí ani pre a0 ani pre b0.")
    exit()

x0 = x  # uložíme PÔVODNÉ x0

k = 0
max_iter = 1000

while k < max_iter:
    df = f1(x)

    if abs(df) < 1e-12:
        print("Chyba: f'(x) je príliš malé.")
        exit()

    x_next = x - f(x) / df
    k += 1

    if abs(x_next - x) <= eps:
        break

    x = x_next

print("\n===================================")
print(f"Zvolené x0 = {x0:.2f}")                 
print(f"Koreň rovnice ≈ {x_next:.11f} ± {eps:.11f}") 
print(f"Počet iterácií: {k}")
print("===================================")
