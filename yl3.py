# {yl3
# Kirjuta programm, 
# mis küsib kasutajalt täisarvu n vahemikus 1-9.
#  Arvuta n + nn + nnn väärtus ja väljasta see. 
# (Näiteks kui kasutaja sisestab 2,
#  siis on vaja väljastada tulemus 2 + 	22 + 222 = 246).
#  Ära kasuta korrutamistehet. 
# Ülesanne on lahendatav ainult liitmise operaatorit kasutades.

n = int(input("Sisesta täisarv 1-9: "))

if n < 1 or n > 9:
    print("Palun sisesta number 1 kuni 9.")

else:
    s = str(n)               
    nn = int(s + s)         
    nnn = int(s + s + s)    
    tulemus = (n + nn + nnn)  

    print(f"{n} + {nn} + {nnn} = {tulemus}")




