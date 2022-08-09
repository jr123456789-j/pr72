import csv

archivo = open("log.txt","r") 
lineas = archivo.readlines()
Autores = []

for texto in lineas:
    if "Author:" in texto:
        variable1 = texto.split("Author:")[1]
        variable2 = variable1.split( )[0]
        if not variable2 in Autores:
            Autores.append(variable2)

print(Autores)

archivo_texto = open("autores.txt", "w")

for autor in Autores:
    archivo_texto.write(autor + "\n")
    
archivo_texto.close()

