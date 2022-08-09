import re

def esComentario(linea):
    if linea.find("commit") and linea.find("Author") and linea.find("Date"):
            if re.search('[a-zA-Z]', texto):
                return True  

    return False

archivo = open("log.txt","r") 
lineas = archivo.readlines()
Comentarios = []

for texto in lineas:
        temp = []
        if esComentario(texto):
            temp.append(texto)
            indice = lineas.index(texto)
            while (texto != lineas[-1] and esComentario(lineas[indice+1])):
                if lineas[indice+1] != '\n':
                    temp.append(lineas[indice+1])
                indice += 1

        if len(temp) != 0:
            Comentarios.append(temp)

print(Comentarios)
print(len(Comentarios))

archivo_texto = open("comentarios.txt", "w")

for comentario in Comentarios:
    if isinstance(comentario, list):
        for subelemento in comentario:
            archivo_texto.write(subelemento + "\n")
    else:
        archivo_texto.write(comentario + "\n")
    
archivo_texto.close()