ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
nombre_archivo = "./archivos/Texto.txt"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    #leer todas la lineas de una lista
    lista = archivo.readlines()

#se imprime la lista elemneto por elemento
for c in lista:
    print(c)