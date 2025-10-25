import os, csv, statistics, matplotlib.pyplot as plt

def listar():
    ruta = input("Ruta (Enter para actual): ")
    if ruta == "": ruta = os.getcwd()
    for f in os.listdir(ruta):
        print(f)

def procesar_txt():
    ruta = input("Archivo .txt: ")
    print("1. Contar palabras y caracteres")
    print("2. Reemplazar palabra")
    print("3. Histograma de vocales")
    op = input("Opción: ")

    if not os.path.exists(ruta):
        print("No existe el archivo."); return

    with open(ruta, "r", encoding="utf-8") as a:
        texto = a.read()

    if op == "1":
        print("Palabras:", len(texto.split()))
        print("Caracteres con espacios:", len(texto))
        print("Caracteres sin espacios:", len(texto.replace(" ", "")))

    elif op == "2":
        buscar = input("Palabra a buscar: ")
        nueva = input("Nueva palabra: ")
        nuevo = texto.replace(buscar, nueva)
        with open(ruta, "w", encoding="utf-8") as a:
            a.write(nuevo)
        print("Palabra reemplazada con éxito.")

    elif op == "3":
        texto = texto.lower()
        vocales = ["a","e","i","o","u"]
        conteo = [texto.count(v) for v in vocales]
        plt.bar(vocales, conteo, color="orange")
        plt.title("Histograma de Vocales")
        plt.show()

def procesar_csv():
    ruta = input("Archivo .csv: ")
    print("1. Mostrar primeras 15 filas")
    print("2. Calcular estadísticas de una columna")
    print("3. Graficar columna")
    op = input("Opción: ")

    if not os.path.exists(ruta):
        print("No existe el archivo."); return

    with open(ruta, newline="", encoding="utf-8") as a:
        lector = list(csv.reader(a))

    if op == "1":
        for fila in lector[:15]:
            print(fila)

    elif op == "2":
        col = int(input("Número de columna: "))
        datos = []
        for fila in lector[1:]:
            try: datos.append(float(fila[col]))
            except: pass
        if len(datos) > 0:
            print("Cantidad:", len(datos))
            print("Promedio:", statistics.mean(datos))
            print("Mediana:", statistics.median(datos))
            print("Máximo:", max(datos))
            print("Mínimo:", min(datos))
            if len(datos)>1: print("Desv.Est:", statistics.stdev(datos))
        else:
            print("No hay datos numéricos válidos.")

    elif op == "3":
        col = int(input("Número de columna: "))
        datos = []
        for fila in lector[1:]:
            try: datos.append(float(fila[col]))
            except: pass
        if len(datos) > 0:
            plt.scatter(range(len(datos)), datos)
            plt.title("Gráfico de Dispersión")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
            plt.show()
        else:
            print("No hay datos válidos para graficar.")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Listar archivos")
    print("2. Procesar .txt")
    print("3. Procesar .csv")
    print("4. Salir")
    op = input("Opción: ")
    if op=="1": listar()
    elif op=="2": procesar_txt()
    elif op=="3": procesar_csv()
    elif op=="4": break
    else: print("Opción no válida.")
