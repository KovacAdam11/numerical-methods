# ===============================================
# LICHOBEŽNÍKOVÁ METÓDA + dvojitý prepočet
# ===============================================

import math

# --- Funkcia f(x) ---
# ZMENÍŠ LEN TOTO podľa zadania
def f(x):
    return math.exp(x)   # príklad z PDF: f(x)=e^x 


def lichobeznikova_integral(a, b, m):
    # h = (b-a)/m 
    h = (b - a) / m

    # I(h) = h/2 * ( f(a) + 2*sum f(a+i*h) + f(b) ) 
    s = 0.0
    for i in range(1, m):
        s += f(a + i * h)

    return (h / 2) * (f(a) + 2 * s + f(b))


# --- Vstupy od používateľa ---
a = float(input("Zadaj a: "))
b = float(input("Zadaj b: "))
m = int(input("Zadaj počiatočný počet dielov m (napr. 4): "))
eps = float(input("Zadaj eps (napr. 0.01): "))

# --- 1) prvý výpočet I1(h) ---
I1 = lichobeznikova_integral(a, b, m)

# --- 2) dvojitý prepočet (2m) až kým |I2 - I1| <= eps 
k = 0
while True:
    m = 2 * m
    I2 = lichobeznikova_integral(a, b, m)
    k += 1

    if abs(I2 - I1) <= eps:
        break

    I1 = I2

print("\n===================================")
print(f"I ≈ {I2:.8f}")
print(f"Použité m = {m}")
print(f"Počet zdvojnásobení: {k}")
print("===================================")
