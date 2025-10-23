import csv
with open("./Archivos/Variables..csv", 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader
    encabezado = next(lector)   #Next salta la primera fila
    #print(encabezado)
    presion = []
    print(encabezado[3])
    for fila in lector:  #con el for se itera sobre el objeto para leer
        fila[3] = fila[3].replace(',', '.')     #replace sirve para modificar algo que tenga en algo nuevo
        dato = float(fila[3])      
        presion.append(dato)  
print(presion)