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

