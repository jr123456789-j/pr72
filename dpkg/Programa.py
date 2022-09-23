from tkinter import *
from tkinter import messagebox
import calendar

# meses en que se registraron eventos, tipos de eventos: configure, status, ...

def mesesEventos():
    archivo = open("log.txt","r") 
    lineas = archivo.readlines()

    Meses = []

    for texto in lineas:
        mes = texto[5] + texto[6]
        if not mes in Meses:
            Meses.append(mes)

    print(Meses)

    archivo_texto = open("mesesEventos.txt", "w")

    for mes in Meses:
        archivo_texto.write(calendar.month_name[int(mes)] + "\n")
        
    archivo_texto.close()

    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#---------------------------------------

def configure():
    listaConfigures = []
    archivo = open("log.txt","r") 
    lineas = archivo.readlines()

    for texto in lineas:
        if "configure " in texto:
            listaConfigures.append(texto)

    archivo_texto = open("configures.txt", "w")

    for conf in listaConfigures:
        archivo_texto.write(conf[19:] + "\n")
    
    print(listaConfigures)
    archivo_texto.close()   
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#---------------------------------------

def status():
    listaStatus = []
    archivo = open("log.txt","r") 
    lineas = archivo.readlines()

    for texto in lineas:
        if "status " in texto:
            listaStatus.append(texto)

    archivo_texto = open("statuses.txt", "w")

    for conf in listaStatus:
        archivo_texto.write(conf[19:] + "\n")
        
    archivo_texto.close()   
    print(listaStatus)
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#---------------------------

def install():
    listainstall = []
    archivo = open("log.txt","r") 
    lineas = archivo.readlines()

    for texto in lineas:
        if "install " in texto:
            listainstall.append(texto)

    archivo_texto = open("install.txt", "w")

    for conf in listainstall:
        archivo_texto.write(conf[19:] + "\n")
        
    archivo_texto.close()   
    print(listainstall)
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
#----------------------------------------

window = Tk()  
window.geometry('640x480')  

window.title("Procesamiento de logs")

botonEventos = Button(window,
	text = 'Meses en los cuales se registraron eventos',
    bg = 'LightBlue',
	command = mesesEventos)  
botonEventos.pack()  

botonConfigure = Button(window,
	text = 'Eventos configure',
    bg = 'LightBlue',
	command = configure)  
botonConfigure.pack()  

botonCommand = Button(window,
	text = 'Eventos status',
    bg = 'LightBlue',
	command = status)  
botonCommand.pack()  

botonInstall = Button(window,
	text = 'Eventos install',
    bg = 'LightBlue',
	command = install)  
botonInstall.pack()  

window.mainloop()

