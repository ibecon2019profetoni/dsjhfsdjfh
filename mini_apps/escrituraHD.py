"""
    Python escritura en Disco
    -------------------------
    Puede leer y escribir archivos con la función (open)
    Los archivos pueden ser de texto o binarios
    Manejadores:
    * r = read
    * w = write
    * a = append
    * r+ = read and write
    Se deben cerrar los archivos con el método (close)
    Una de las mejores maneras de manejar archivos es con (with)
"""

nombre = input('Tu Nombre: ')

# * Escritura
with open('file.txt', 'w') as f:
    for i in range(5):
        f.write(f'{nombre}\n')
    f.close()

# f = open('file.txt', 'w')
# f.write('ULTIMO')
# f.close()

# Lectura
with open('file.txt', 'r') as f:
    for linea in f:
        print(linea)
    f.close()
