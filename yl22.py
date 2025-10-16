# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)
import math

raadius = int(input("Sisesta ringi raadius: "))


ringi_pindala = math.pi * (raadius ** 2)
ringi_umbermoot = 2 * math.pi * raadius


print("Ringi pindala on:", round(ringi_pindala, 2))
print("Ringi ümbermõõt on:", round(ringi_umbermoot, 2))

