ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos"
#\ se usa para comandos de texto
nombre_archivo = "ejercicio2.txt"
modo = "x" # solo escritura - sobreescribe
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
frase = input("nombre: ")
edad = int(input("ingrese la edad: "))
estatura = float(input("ingrese la altura: "))
fp.write(frase + "\n")
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura))
fp.write("\n")
#solicitar una varibale entera y una float al usuario y
#la escriben en el archivo
fp.close()
