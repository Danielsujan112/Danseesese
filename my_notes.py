# Abrir el archivo 'my_notes.txt' en modo escritura ("w")
archivo = open("my_notes.txt", "w")

# Escribir al menos tres líneas de notas personales en el archivo
archivo.write("Nota 1: Estudiar para el examen de Programacion.\n")
archivo.write("Nota 2: Revisar el código de la tarea.\n")
archivo.write("Nota 3: Investigar sobre manejo de archivos en Python.\n")

# Cerrar el archivo después de escribir
archivo.close()

# Abrir el archivo 'my_notes.txt' en modo lectura ("r")
archivo = open("my_notes.txt", "r")

# Leer el contenido del archivo línea por línea utilizando readline()
linea = archivo.readline()
while linea != "":
    # Mostrar cada línea leída en la consola
    print(linea.strip())  # Utilizamos strip() para eliminar los saltos de línea
    linea = archivo.readline()

# Cerrar el archivo después de leer
archivo.close()
