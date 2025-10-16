# yl4
# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi
#  (ära kasuta min funktsiooni). 
# (muutuja - variable, tingimus - condition, if-lause - if statement)


a = int(input("Sisesta esimene täisarv: "))
b = int(input("Sisesta teine täisarv: "))


if a < b:
    miinimum = a
else:
    miinimum = b

print("Miinimum on:", miinimum)



