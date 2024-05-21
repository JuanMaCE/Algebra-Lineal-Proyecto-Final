import numpy as np
# 97 = A
# 122 = Z
# 32 = " "
import datetime


def transponer(matriz):
    print("transponer")
    contador = 0
    contador_2 = 0
    new_matriz = []
    lista_1 = []
    lista_2 = []
    lista_3 = []

    for fila in matriz:
        contador += 1
        lista = fila
        contador_2 = 0

        for dato in lista:
            contador_2 += 1
            if contador_2 == 1:
                lista_1.append(dato)
            elif contador_2 == 2:
                lista_2.append(dato)
            elif contador_2 == 3:
                lista_3.append(dato)
    new_matriz.append(lista_1)
    new_matriz.append(lista_2)
    new_matriz.append(lista_3)
    print("esta es la transpuesta")
    return new_matriz


def main():
    texto = str(input(" ingrese el texto a encriptar "))
    matriz = []
    contador = 0
    contador_extra = 0
    lista = []
    cantidad_de_caracteres = len(texto)
    relleno = 0
    if cantidad_de_caracteres % 3 != 0:
        relleno = (cantidad_de_caracteres % 3)
    resta = len(texto) - relleno
    print("resta  ", resta)

    for i in range(len(texto)):
        contador_extra += 1
        contador += 1
        letra = str(texto[i])
        if letra == " ":
            conversion_a_numero = 27
            lista.append(conversion_a_numero)
        else:
            conversion_a_numero = ord(letra) - 96
            lista.append(conversion_a_numero)
        if contador == 3:
            matriz.append(lista)
            lista = []
            contador = 0
    if len(lista) == 2:
        lista.append(32)
    elif len(lista) == 1:
        lista.append(32)
        lista.append(32)
    matriz.append(lista)
    transpuesta = transponer(matriz)
    print(" ")
    print(matriz)
    print(" ")
    print("transpuesta de la matriz ")
    print(transpuesta)
    matriz_inversa = []
    lista_inversa = []
    contador = 0
    for i in range(9):
        contador += 1
        x = int(input("ingrese los valores de la matriz: "))
        lista_inversa.append(x)
        if (contador % 3 == 0) or contador == 9:
            contador = 0
            matriz_inversa.append(lista_inversa)
            lista_inversa = []

    print(" los datos de su matriz inversa son: ", matriz_inversa)
    transpuesta_de_la_inversa = transponer(matriz_inversa)
    print(transpuesta_de_la_inversa)
    print("su matriz inversa es :")
    print(transpuesta_de_la_inversa)
    print(" resultados ")
    matriz_resultante = np.dot(transpuesta_de_la_inversa, transpuesta)
    print("su valor resultante ")
    print(matriz_resultante)

    inversa = np.linalg.inv(transpuesta_de_la_inversa)
    print(" descrifrado ")
    desmatrizado = np.dot(inversa, matriz_resultante)
    last_matriz =  np.transpose(desmatrizado)
    texto = " "
    print(" desmatrizado: ")
    print(last_matriz)
    for dato in last_matriz:
        lista = dato
        for dato_2 in lista:
            if round(dato_2) == 27:
                texto += " "
            else:
                suma = 96 + round(dato_2)
                texto += chr(suma)
    print("este es el mensjae decifrado :", texto)
    return




