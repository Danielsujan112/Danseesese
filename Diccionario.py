# Crear el diccionario inicial con información ficticia
informacion_personal = {
    "nombre": "Norman Hernandez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Profesor"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# (Aunque la clave "profesion" ya existe, se puede actualizar o confirmar su valor)
informacion_personal["profesion"] = "Profesor de matematicas"

# Verificar si la clave "telefono" existe; si no, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad"
informacion_personal.pop("edad", 30)

# Imprimir el diccionario final
print(informacion_personal)
