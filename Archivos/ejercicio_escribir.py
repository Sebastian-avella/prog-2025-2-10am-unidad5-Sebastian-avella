import csv
Nombre = ['sebastian','camilo','miguel']
Edad = ['18','19','20']
Pais = ['colombia','panama','españa']
with open('C:\\Users\\B09S202est\\Documents\\programacion-2025\\prog-2025-2-10am-unidad5-Sebastian-avella\\salidas.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['John', 25, 'Nueva York'])
    escritor.writerow(['Jane', 30, 'Los Ángeles'])
    escritor.writerow(Nombre)
    escritor.writerow(Edad)
    escritor.writerow(Pais)
