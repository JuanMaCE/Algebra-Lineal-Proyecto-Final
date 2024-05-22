from numpy.linalg import inv
import numpy as np

print("1. Definiendo lista para almacenar los datos de la matriz")
datos = []
print("2. Solicitando la dimensión de la matriz.")
dimension = int(input("Ingrese la dimensión de la matriz (2=2x2, 3=3x3, etc...): "))
print("3. Construyendo la matriz")
for i in range(dimension):
    fila = []
    for j in range(dimension):
        dato = float(input(f"Ingrese el dato de la fila {i+1} y columna {j+1}: "))
        fila.append(dato)
    datos.append(fila)

print("4. Convirtiendo datos en una matriz.")
matriz = np.array(datos)
print("5. Determinando la inversa de la matriz.")
inversa = inv(matriz)
print("La matriz inversa es: \n",inversa)