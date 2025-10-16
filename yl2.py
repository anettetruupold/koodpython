# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

#  PI ≈ 3.14



raadius = int(input("Sisesta ringi raadius (täisarv): "))

PI = 3.14
pindala = PI * raadius * raadius 
umbermoot = 2 * PI * raadius   

print("Ringi pindala on:", pindala)
print("Ringi ümbermõõt on:", umbermoot)


