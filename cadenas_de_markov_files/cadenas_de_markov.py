import customtkinter
import numpy as np
global lb_datos
matriz_a = []
matriz_b = []
from CTkMessagebox import CTkMessagebox
global filas
global columnas
global lista_a
global contador_a_columnas
global contador_b



def devolver_lista_como_texto(pila):
    return str(pila.transversal())


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    # color = "#3E4446"
    labels_parte1(frame)

    lb_matriz_a = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 50))
    lb_matriz_a.pack(pady=400, padx=400, )
    lb_matriz_a.place(x=10, y=275)

    lb_matriz_b = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 50))
    lb_matriz_b.pack(pady=400, padx=400, )
    lb_matriz_b.place(x=400, y=275)

    lb_matriz_multiplicacion = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 50), state="disable")
    lb_matriz_multiplicacion.pack(pady=400, padx=400)
    lb_matriz_multiplicacion.place(x=550, y=350)

    # ingreso de datos
    ib_ingreso_datos_matriz_a = customtkinter.CTkEntry(master=frame, placeholder_text='Datos Matriz A', width=300,
                                                       height=35, state="disable")
    ib_ingreso_datos_matriz_a.pack(pady=100, padx=10)
    ib_ingreso_datos_matriz_a.place(x=10, y=150)

    ib_ingreso_datos_matriz_b = customtkinter.CTkEntry(master=frame, placeholder_text='Ingreso de datos Matriz B', width=300,
                                                       height=35, state="disable")
    ib_ingreso_datos_matriz_b.pack(pady=100, padx=10)
    ib_ingreso_datos_matriz_b.place(x=400, y=150)

    ib_ingreso_filas_a = customtkinter.CTkEntry(master=frame, placeholder_text=' ', width=135,
                                                height=35)
    ib_ingreso_filas_a.pack(pady=100, padx=10)
    ib_ingreso_filas_a.place(x=10, y=100)

    ib_ingreso_columnas_a = customtkinter.CTkEntry(master=frame, placeholder_text='', width=135,
                                                   height=35)
    ib_ingreso_columnas_a.pack(pady=100, padx=10)
    ib_ingreso_columnas_a.place(x=175, y=100)

    ib_cantidad_de_dias = customtkinter.CTkEntry(master=frame, placeholder_text='',
                                                 width=135,
                                                 height=35)
    ib_cantidad_de_dias.pack(pady=100, padx=10)
    ib_cantidad_de_dias.place(x=400, y=100)

    global lista_a
    lista_a = []
    global contador_a_columnas
    contador_a_columnas = 0
    global contador_b
    contador_b = 0

    def filas_columasn_agregar():
        global filas
        filas = ib_ingreso_filas_a.get()
        global columnas
        columnas = ib_ingreso_columnas_a.get()

        ib_ingreso_datos_matriz_a.configure(state="normal")
        ib_ingreso_datos_matriz_b.configure(state="normal")

    def agregar_datos_matriz_a():
        dato = float(ib_ingreso_datos_matriz_a.get())
        global lista_a
        global contador_a_columnas
        contador_a_columnas += 1
        if contador_a_columnas <= (int(ib_ingreso_columnas_a.get()) * int(ib_ingreso_filas_a.get())):
            lista_a.append(dato)
            if contador_a_columnas % int(ib_ingreso_columnas_a.get()) == 0:
                matriz_a.append(lista_a)
                lista_a = []
            if contador_a_columnas == (int(ib_ingreso_columnas_a.get()) * int(ib_ingreso_filas_a.get())):
                CTkMessagebox(title='ESTA LLENA LA MATRIZ A', message='NO SE PUEDEN AGREGAR MÁS DATOS')
                lb_matriz_a.configure(text=imprimir_matriz(matriz_a))

    def agregar_datos_matriz_b():
        dato = float(ib_ingreso_datos_matriz_b.get())
        global contador_b
        contador_b += 1
        print(contador_b, int(ib_ingreso_columnas_a.get()))
        if contador_b <= int(ib_ingreso_columnas_a.get()):
            lista_b = []
            lista_b.append(dato)
            matriz_b.append(lista_b)
        if contador_b == int(ib_ingreso_columnas_a.get()):
            print(matriz_b)
            CTkMessagebox(title='ESTA LLENA LA MATRIZ A', message='NO SE PUEDEN AGREGAR MÁS DATOS')
            lb_matriz_b.configure(text=imprimir_matriz(matriz_b))

    button_ingreso_datos_matriz_a = customtkinter.CTkButton(master=frame, text='Ingreso Matriz A',
                                                            font=("Arial", 20), fg_color="#3E4446",
                                                            command=lambda: agregar_datos_matriz_a())

    button_ingreso_datos_matriz_a.pack(pady=10, padx=10)
    button_ingreso_datos_matriz_a.place(x=10, y=200)

    button_ingreso_datos_matriz_b = customtkinter.CTkButton(master=frame, text='Ingreso Matriz B',
                                                            font=("Arial", 20), fg_color="#3E4446",
                                                            command=lambda: agregar_datos_matriz_b())

    button_ingreso_datos_matriz_b.pack(pady=10, padx=10)
    button_ingreso_datos_matriz_b.place(x=400, y=200)

    # confirmación de datos
    button_ingreso = customtkinter.CTkButton(master=frame, text='Ingreso',
                                             font=("Arial", 20), fg_color="#3E4446",
                                             command=filas_columasn_agregar)

    button_ingreso.pack(pady=10, padx=10)
    button_ingreso.place(x=560, y=100)

    def multiplicar():
        dias = int(ib_cantidad_de_dias.get())
        resultado = np.dot(matriz_a, matriz_b)
        for i in range(dias):
            resultado = np.dot(matriz_a, resultado)
            print("\nResultado de la multiplicación:", " no; ", i + 1)
            print(resultado)
        print(" ")
        print(" los porcenjates del dia" + str(dias) + "son: ")
        for i in resultado:
            for x in i:
                porcentaje = round(x, 3) * 100
                print("%", porcentaje)

    button_confirmar = customtkinter.CTkButton(master=frame, text='Calcular',
                                               font=("Arial", 20), fg_color="#3E4446",
                                               command=multiplicar)

    button_confirmar.pack(pady=10, padx=10)
    button_confirmar.place(x=700, y=200)


    # exportar archivos txt

    ventana.mainloop()
    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Cadenas de markov")
    ventana.geometry('950x550')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    return frame


def labels_parte1(frame):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text="Cadenas de Markov",
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400)
    lb_inbreso.place(x=10, y=0)

    lb_filas_matriz_a = customtkinter.CTkLabel(master=frame, text='FILAS MATRIZ A')
    lb_filas_matriz_a.pack(pady=400, padx=400)
    lb_filas_matriz_a.place(x=10, y=70)

    lb_columnas_matriz_a = customtkinter.CTkLabel(master=frame, text='COLUMNAS MATRIZ A')
    lb_columnas_matriz_a.pack(pady=400, padx=400)
    lb_columnas_matriz_a.place(x=180, y=70)

    lb_cantidad_de_dias = customtkinter.CTkLabel(master=frame, text='CANTIDAD DE DÍAS')
    lb_cantidad_de_dias.pack(pady=400, padx=400)
    lb_cantidad_de_dias.place(x=400, y=70)


def imprimir_matriz(matriz):
    texto = " "
    for i in matriz:
        linea = ""
        contador = 0
        for x in i:
            if contador == 0:
                linea += str(x)
            else:
                linea += " | " + str(x)
            contador += 1
        texto += linea + "\n"
    return texto


def multiply_matrices(A, B):
    # Comprobar si la multiplicación es posible
    if len(A[0]) != len(B):
        raise ValueError(
            "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

    # Dimensiones de las matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Crear la matriz resultante con ceros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Realizar la multiplicación de matrices
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C
