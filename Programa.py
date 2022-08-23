from tkinter import *
from tkinter import messagebox

def autores():
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
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#---------------------------------------

def mails():
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
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#---------------------------------------

def commits():
    str = open("log.txt","r").read()
    lista=str.split("commit")
    print(lista[:2])
    print(len(lista)-1)

    archivo_texto = open("commits.txt", "w")

    for commit in lista:
        archivo_texto.write(commit + "\n")
        
    archivo_texto.close()
#---------------------------

def comentarios():
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
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#----------------------------------------

def fechas():
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
    messagebox.showinfo('Mensaje', 'Datos generados en la consola.')
#----------------------

window = Tk()  
window.geometry('640x480')  

window.title("Procesamiento de logs")

botonautores = Button(window,
	text = 'Generar lista de Autores',
    bg = 'LightBlue',
	command = autores)  
botonautores.pack()  

botonmails = Button(window,
	text = 'Generar lista de Mails',
    bg = 'LightBlue',
	command = mails)  
botonmails.pack()  

botoncomentarios = Button(window,
	text = 'Generar lista de Comentarios',
    bg = 'LightBlue',
	command = comentarios)  
botoncomentarios.pack()  

botonfechas = Button(window,
	text = 'Dias con mas commits',
    bg = 'LightBlue',
	command = fechas)  
botonfechas.pack()  

botoncommits = Button(window,
	text = 'Generar lista de commits',
    bg = 'LightBlue',
	command = commits)  
botoncommits.pack()  

window.mainloop()

