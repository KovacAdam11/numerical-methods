# ===============================================
# OBDĹŽNIKOVÁ METÓDA (stredy intervalov) + dvojitý prepočet
# ===============================================

import math

# --- Funkcia f(x) ---
def f(x):
    return math.exp(x)   # príklad z PDF: f(x)=e^x  


def obdlznikova_integral(a, b, m):
    # h = (b-a)/m  
    h = (b - a) / m
    s = 0.0
    # I(h) = h * sum_{i=1..m} f( (x_{i-1}+x_i)/2 )  
    for i in range(1, m + 1):
        x_im1 = a + (i - 1) * h
        x_i = a + i * h
        stred = (x_im1 + x_i) / 2
        s += f(stred)
    return h * s


# --- Vstupy od používateľa ---
a = float(input("Zadaj a: "))
b = float(input("Zadaj b: "))
m = int(input("Zadaj počiatočný počet dielov m (napr. 4): "))
eps = float(input("Zadaj eps (napr. 0.01): "))

# --- 1) prvý výpočet I1(h) ---
I1 = obdlznikova_integral(a, b, m)

# --- 2) dvojitý prepočet (h/2, 2m) až kým |I1 - I2| <= eps  
k = 0
while True:
    m = 2 * m
    I2 = obdlznikova_integral(a, b, m)
    k += 1

    if abs(I2 - I1) <= eps:
        break

    I1 = I2

print("\n===================================")
print(f"I ≈ {I2:.8f}")
print(f"Použité m = {m}")
print(f"Počet zdvojnásobení: {k}")
print("===================================")
