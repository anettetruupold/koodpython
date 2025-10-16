# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse. (round)
# 1 euro = 15.6466 krooni


krooni = int(input("Sisesta summa kroonides: "))
euro = krooni / 15.6466
print("Summa eurodes on:", round(euro, 2))

