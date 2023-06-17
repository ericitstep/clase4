# Realice un script en python que tome como primer argumento un archivo csv y
# como segundo argumento el nombre de una columna de ese archivo y proceda a
# imprimir todos los valores de dicha columna.


# Imprime todos los valores de una columna específica de un archivo CSV.

# Parámetros:
# - csv_file (str): Ruta al archivo CSV.
# - columna (str): Nombre de la columna a imprimir.

import csv
import sys

def imprimirColumna(csv_file, columna):
    
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                valor = row[columna]
                print(valor)
    except FileNotFoundError:
        print(f"El archivo '{csv_file}' no existe.")
    except KeyError:
        print(f"La columna '{columna}' no existe en el archivo CSV.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python script.py archivo.csv nombre_columna")
    else:
        csv_file = sys.argv[1]
        columna = sys.argv[2]
        imprimirColumna(csv_file, columna)
