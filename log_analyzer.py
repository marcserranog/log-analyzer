import os
import re

# Ruta de la carpeta que contiene los archivos de logs
carpeta_logs = "logs"

# Patrón para encontrar los errores en los logs
patron_error = re.compile(r'<CAMPO1>ERR</CAMPO1>.*<CAMPO5>(.*?)</CAMPO5>.*<CAMPO9>(.*?)</CAMPO9>')

# Contador de errores y lista para almacenar las fechas y descripciones de los errores
contador_errores = 0
errores = []

# Iterar sobre cada archivo en la carpeta
for archivo in os.listdir(carpeta_logs):
    if archivo.endswith(".log"):  # Solo procesar archivos con extensión .log
        ruta_archivo = os.path.join(carpeta_logs, archivo)
        
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            # Buscar todas las coincidencias de errores en el archivo
            coincidencias = patron_error.findall(contenido)
            
            # Contabilizar y guardar cada error encontrado
            for coincidencia in coincidencias:
                contador_errores += 1
                fecha = coincidencia[0]
                descripcion = coincidencia[1]
                errores.append((fecha, descripcion))

# Mostrar los resultados
print(f"Número total de errores encontrados: {contador_errores}")
print("Detalles de los errores:")
for fecha, descripcion in errores:
    print(f"Fecha: {fecha}, Descripción: {descripcion}")
