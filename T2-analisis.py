def generar_matriz(filas, columnas):
    matriz = []
    print("\nIngrese las palabras (de 4 letras cada una):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            palabra = input(f"Palabra en posición ({i+1},{j+1}): ").lower()
            while len(palabra) != 4 or not palabra.isalpha():
                print(" Error: la palabra debe tener exactamente 4 letras (solo letras).")
                palabra = input(f"Palabra en posición ({i+1},{j+1}): ").lower()
            fila.append(palabra)
        matriz.append(fila)
    return matriz

# Mostrar la matriz en forma rectangular
def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))
    print()

# Verificar si una palabra tiene al menos una vocal
def tiene_vocal(palabra):
    for v in "aeiou":
        if v in palabra:
            return True
    return False

# Algoritmo divide y vencerás generalizado
def contar_palabras_con_vocal(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Caso base: matriz de 1x1
    if filas == 1 and columnas == 1:
        return 1 if tiene_vocal(matriz[0][0]) else 0

    # Caso base: una sola fila
    if filas == 1:
        mitad = columnas // 2
        izquierda = [matriz[0][:mitad]]
        derecha = [matriz[0][mitad:]]
        return contar_palabras_con_vocal(izquierda) + contar_palabras_con_vocal(derecha)

    # Caso base: una sola columna
    if columnas == 1:
        mitad = filas // 2
        arriba = matriz[:mitad]
        abajo = matriz[mitad:]
        return contar_palabras_con_vocal(arriba) + contar_palabras_con_vocal(abajo)

    # División general: 4 submatrices
    mitad_filas = filas // 2
    mitad_columnas = columnas // 2

    sub1 = [fila[:mitad_columnas] for fila in matriz[:mitad_filas]]   # superior izquierda
    sub2 = [fila[mitad_columnas:] for fila in matriz[:mitad_filas]]   # superior derecha
    sub3 = [fila[:mitad_columnas] for fila in matriz[mitad_filas:]]   # inferior izquierda
    sub4 = [fila[mitad_columnas:] for fila in matriz[mitad_filas:]]   # inferior derecha

    return (contar_palabras_con_vocal(sub1) +
            contar_palabras_con_vocal(sub2) +
            contar_palabras_con_vocal(sub3) +
            contar_palabras_con_vocal(sub4))

# Programa principal
def main():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    matriz = generar_matriz(filas, columnas)
    print("\nMatriz ingresada:\n")
    mostrar_matriz(matriz)

    total = contar_palabras_con_vocal(matriz)
    print(f" Cantidad de palabras que tienen al menos una vocal: {total}")

# Ejecutar
if __name__ == "__main__":
    main()
