#Necesita que el archivo de texto con el log este en el mismo directorio que el archivo python.
import re
archivo = open("log.txt","r") 
lineas = archivo.readlines()
mails = []
mailsRepetidos = []

for texto in lineas:
    mail = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', texto)
    if mail:
        
        repetido = False
        if mail in mailsRepetidos:
            repetido = True

        if repetido == False:
            mailsRepetidos.append(mail)
            mails.append(mail)
        

print(mails)

archivo_texto = open("mails.txt", "w")

for lista in mails:
    for mail in lista:
        archivo_texto.write(mail + "\n")
    
archivo_texto.close()




    
