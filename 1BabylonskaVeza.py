# ===============================================
# BABYLONSKÁ METÓDA – výpočet druhej odmocniny √S
# ===============================================

import math

# --- 1) Vstupné údaje ---
S = float(input("Zadaj číslo S (>0): "))
x = float(input("Zadaj počiatočný odhad x0 (>0): "))
eps = float(input("Zadaj požadovanú presnosť ε (>0): "))

# --- 2) Iteračný proces ---
k = 0

while True:
    x_next = 0.5 * (x + S / x)
    k += 1

    if abs(x_next - x) < eps:
        break

    x = x_next

# --- 3) Výstup výsledku ---
skutocna = math.sqrt(S)
chyba = abs(x_next - skutocna)

print("\n===================================")
print(f"Odmocnina zo {S:.1f} ≈ {x_next:.8f}")
print(f"Požadovaná presnosť bola splnená (ε = {eps:.8f})")
print(f"Počet iterácií: {k}")
print(f"Porovnanie s math.sqrt(S): {skutocna:.8f}")
print(f"Absolútna chyba: {chyba:.20f}")
print("===================================")
