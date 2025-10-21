lista = ["la groupie", "4 babys", "Esclava remix", "RX", "Sexo, sudor y calor"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
modo = "w"
nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\"+ nombre_archivo, modo, encoding="utf-8")
for i in lista:
    fp.write(i+"\n")
fp.close()