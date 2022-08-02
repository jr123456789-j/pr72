str = open("log.txt","r").read()
lista=str.split("commit")
print(len(lista)-1)