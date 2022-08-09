str = open("log.txt","r").read()
lista=str.split("commit")
print(lista[:2])
print(len(lista)-1)

archivo_texto = open("commits.txt", "w")

for commit in lista:
    archivo_texto.write(commit + "\n")
    
archivo_texto.close()


