from datetime import datetime
from collections import Counter

archivo = open("log.txt","r") 
lineas = archivo.readlines()

fechasCommits = []

for linea in lineas:
    if "Date:" in linea:
        stringFecha = linea[8:-1]
        fecha = datetime.strptime(stringFecha, "%a %b %d %X %Y %z")
        fechasCommits.append(fecha.weekday())
        
cnt = Counter(fechasCommits)
print(cnt.most_common())
