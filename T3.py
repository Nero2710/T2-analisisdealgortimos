import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    
laberinto = [
    [1, 1, 1, 99, 1, 1, 1, 99, 1],
    [1, 99, 1, 1, 1, 1, 99, 1, 1],
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [99, 99, 99, 1, 99, 99, 99, 99, 99],
    [-2, 99, 1, 1, 1, 1, 99, 1, 1],
    [1, 1, -1, 1, 99, 1, 1, 1, 99],
    [99, 1, 1, 1, 1, 1, 99, 1, 1],
    ['F', 1, 1, 1, 1, 99, 1, 1, 1]
]

FILAS = len(laberinto)
COLUMNAS = len(laberinto[0])


inicio = (0, 0)  
energia_inicial = 18


def encontrar_fin(matriz):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if matriz[i][j] == 'F':
                return (i, j)
    return None

fin = encontrar_fin(laberinto)


solucion = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]


def resolver(x, y, energia):
    
    if x < 0 or x >= FILAS or y < 0 or y >= COLUMNAS:
        return False

    
    if laberinto[x][y] == 99:
        return False

    
    if (x, y) == fin:
        solucion[x][y] = 1
        return True

    
    valor = laberinto[x][y]
    nueva_energia = energia

    if isinstance(valor, int):
        if valor > 0:
            nueva_energia -= valor
        elif valor < 0:
            nueva_energia -= valor   

    
    if nueva_energia < 0:
        return False

    
    solucion[x][y] = 1

   
    movimientos = [ (0,-1), (-1,0), (0,1), (1,0) ]

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if solucion[nx][ny] == 0:  
            if resolver(nx, ny, nueva_energia):
                return True

   
    solucion[x][y] = 0
    return False



def mostrar_matriz(mat):
    for fila in mat:
        print(fila)
    print()



print("\n=== LABERINTO ORIGINAL ===")
mostrar_matriz(laberinto)

print("Buscando camino...\n")

if resolver(inicio[0], inicio[1], energia_inicial):
    print("¡Camino encontrado! (1 indica el camino)")
    mostrar_matriz(solucion)
else:
    print("No existe camino posible con 18 unidades de energía.")