import numpy as np
import customtkinter
from CTkMessagebox import CTkMessagebox

global matriz_inversa
matriz_inversa = []
global contador
contador = 0
global lista
lista = []


def transponer(matriz):
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
    ventana = cargar_datos()
    frame = frame1(ventana)
    # color = "#3E4446"
    labels_parte1(frame)

    ib_valores_de_la_matriz = customtkinter.CTkEntry(master=frame, placeholder_text='DATOS', width=300,
                                                     height=35)
    ib_valores_de_la_matriz.pack(pady=100, padx=10)
    ib_valores_de_la_matriz.place(x=10, y=75)

    ib_ingreso_texto_a_encriptar = customtkinter.CTkEntry(master=frame, placeholder_text='TEXTO', width=300,
                                                          height=35, state="disable")
    ib_ingreso_texto_a_encriptar.pack(pady=100, padx=10)
    ib_ingreso_texto_a_encriptar.place(x=10, y=125)

    def ingresar_datos_matriz_inversa():
        global contador
        contador += 1
        global lista
        global matriz_inversa
        if contador <= 9:
            lista.append(int(ib_valores_de_la_matriz.get()))
            if contador % 3 == 0:
                print("llegue aca")
                matriz_inversa.append(lista)
                lista = []
            if contador == 9:
                CTkMessagebox(title='ESTA LLENA LA MATRIZ A', message='NO SE PUEDEN AGREGAR MÁS DATOS')
                ib_ingreso_texto_a_encriptar.configure(state="normal")
                print(matriz_inversa)

    def mostrar():
        global matriz_inversa
        matriz = []
        contador = 0
        contador_extra = 0
        lista = []
        cantidad_de_caracteres = len(ib_ingreso_texto_a_encriptar.get())
        relleno = 0
        if cantidad_de_caracteres % 3 != 0:
            relleno = (cantidad_de_caracteres % 3)
        resta = cantidad_de_caracteres - relleno
        print("resta  ", resta)
        texto = ib_ingreso_texto_a_encriptar.get()
        for i in range(len(ib_ingreso_texto_a_encriptar.get())):
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
        print(" los datos de su matriz inversa son: ", matriz_inversa)
        transpuesta_de_la_inversa = transponer(matriz_inversa)
        print(transpuesta_de_la_inversa)
        print("su matriz inversa es :")
        print(transpuesta_de_la_inversa)
        print(" resultados ")
        matriz_resultante = np.dot(transpuesta_de_la_inversa, transpuesta)
        print("su valor resultante ")
        lb_cifrado = customtkinter.CTkLabel(master=frame, text=str(matriz_resultante),
                                            font=("Times New Roman", 50, "bold"))
        lb_cifrado.pack(pady=400, padx=400, )
        lb_cifrado.place(x=10, y=500)

        print(matriz_resultante)

        inversa = np.linalg.inv(transpuesta_de_la_inversa)
        print(" descrifrado ")
        desmatrizado = np.dot(inversa, matriz_resultante)
        last_matriz = np.transpose(desmatrizado)
        new_text = " "
        print(" desmatrizado: ")
        print(last_matriz)
        for dato in last_matriz:
            lista = dato
            for dato_2 in lista:
                if round(dato_2) == 27:
                    new_text += " "
                else:
                    suma = 96 + round(dato_2)
                    new_text += chr(suma)
        print("este es el mensjae decifrado :", new_text)
        ventana.geometry('950x700')


    button_ingresar_datos = customtkinter.CTkButton(master=frame, text='Ingresar datos Matriz',
                                                    font=("Arial", 20), fg_color="#3E4446",
                                                    command=ingresar_datos_matriz_inversa)

    button_ingresar_datos.pack(pady=10, padx=10)
    button_ingresar_datos.place(x=325, y=75)

    button_confirmar = customtkinter.CTkButton(master=frame, text='Mostar Resultados',
                                               font=("Arial", 20), fg_color="#3E4446",
                                               command=mostrar)

    button_confirmar.pack(pady=10, padx=10)
    button_confirmar.place(x=325, y=125)



    ventana.mainloop()
    return

def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Cifrado")
    ventana.geometry('950x550')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    return frame

def labels_parte1(frame):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Cifrado',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

