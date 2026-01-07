# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# stringi meetodid, list

text = input("Sisesta tekst: ")

text = text.strip()

print(text) 

if len(text) < 7 or len(text) % 2 == 0:  
    print("vähemalt 7 ja paarituarvuline")

else:
    i = int(len(text) / 2) 

    print(text[i-1 : i+2])








