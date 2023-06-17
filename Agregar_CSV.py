# Script en python que toma como primer argumento un archivo csv y
# como segundo argumento un numero  y agregar este numero en el ultimo renglon de cada 
# columna de ese archivo y proceda a imprimir todos los valores de dicha scolumna. 

import sys
import csv

def agregaNumeroFinal(archivo_csv, numero):
    # Abrir el archivo CSV en modo lectura
    with open(archivo_csv, 'r') as archivo:
        # Leer el contenido del archivo CSV
        filas = csv.reader(archivo)
        
        # Iterar sobre cada fila del archivo CSV
        for fila in filas:
            # Iterar sobre cada valor en la fila
            for indice, valor in enumerate(fila):
                # Agregar el número al final de cada valor
                fila[indice] = f'{valor}{numero}'
                
            # Imprimir los valores de la fila
            print(fila)

# Obtener los argumentos de la línea de comandos
archivo_csv = sys.argv[1]
numero = sys.argv[2]

# Llamar a la función para agregar el número al archivo CSV
agregaNumeroFinal(archivo_csv, numero)
