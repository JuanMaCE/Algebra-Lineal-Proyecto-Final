from multiplicador_de_matrices import multiplicador
matriz_a = []
matriz_b = []


def main():
    print(" bievenido a suma de matrices ")
    print(" ingreso de matrices ")
    filas_a = int(input("ingrese la cantidad de filas de la matrices: "))
    columnas_a = int(input("ingrese la cantidad de columnas de la matrices: "))

    filas_b = int(input("ingrese la cantidad de filas de la matriz B: "))
    columnas_b = int(input("ingrese la cantidad de columnas de la matriz B: "))
    if columnas_a == filas_b:
        for x in range(filas_a):
            lista = []
            for y in range(columnas_a):
                dato = float(input("ingrese el dato: "))
                lista.append(dato)
            matriz_a.append(lista)
        print(" datos llenos ")
        print(matriz_a)
        for x in range(filas_b):
            lista = []
            for y in range(columnas_b):
                dato = float(input("ingrese el dato: "))
                lista.append(dato)
            matriz_b.append(lista)
        print(" datos llenos ")
        print(matriz_b)
        print(" datos: ")
        print("matriz a ")
        print(imprimir_matriz(matriz_a))
        print("matriz b ")
        print(imprimir_matriz(matriz_b))
        print(" ")
        print("dato 0, 1: ", matriz_a[0][1])

        suma = 0
        for listas in matriz_a:
            for i in listas:
                print(i)


    return


def imprimir_matriz(matriz):
    texto = " "
    for i in matriz:
        linea = " "
        contador = 0
        for x in i:
            if contador == 0:
                linea += str(x)
            else:
                linea += " - " + str(x)
            contador += 1
        texto += linea + "\n"
    return texto


main()
