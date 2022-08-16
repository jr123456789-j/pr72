from datetime import datetime
from collections import Counter

archivo = open("log.txt","r") 
lineas = archivo.readlines()

fechasCommits = []

for linea in lineas:
    if "Date:" in linea:
        stringFecha = linea[8:-1]
        fechasCommits.append(datetime.strptime(stringFecha, "%a %b %d %X %Y %z"))
        
cnt = Counter()
for fecha in fechasCommits:
    cnt[fecha.day, fecha.month, fecha.year] += 1

print(cnt)

