import customtkinter
import numpy as np

global lb_datos
matriz_a = []
matriz_b = []
from CTkMessagebox import CTkMessagebox
global filas
global columnas
import numpy
global lista_a
global contador_a_columnas
global contador_a_filas

global lista_b
global contador_b_columnas
global contador_b_filas


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

    ib_ingreso_datos_matriz_b = customtkinter.CTkEntry(master=frame, placeholder_text='Datos Matriz A', width=300,
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

    ib_ingreso_filas_b = customtkinter.CTkEntry(master=frame, placeholder_text='', width=135,
                                                height=35)
    ib_ingreso_filas_b.pack(pady=100, padx=10)
    ib_ingreso_filas_b.place(x=400, y=100)

    ib_ingreso_columnas_b = customtkinter.CTkEntry(master=frame, placeholder_text='Datos CDS', width=135,
                                                   height=35)
    ib_ingreso_columnas_b.pack(pady=100, padx=10)
    ib_ingreso_columnas_b.place(x=560, y=100)

    global lista_a
    lista_a = []
    global contador_a_columnas
    contador_a_columnas = 0
    global lista_b
    lista_b = []
    global contador_b_columnas
    contador_b_columnas = 0
    global contador_a_filas
    contador_a_filas = 0
    global contador_b_filas
    contador_b_filas = 0

    def filas_columasn_agregar():
        ingreso_columnas_a = ib_ingreso_columnas_a.get()
        ingreso_filas_b = ib_ingreso_filas_b.get()
        if ingreso_columnas_a == ingreso_filas_b:
            global filas
            filas = ib_ingreso_filas_a.get()
            global columnas
            columnas = ib_ingreso_columnas_a.get()

            ib_ingreso_datos_matriz_a.configure(state="normal")
            ib_ingreso_datos_matriz_b.configure(state="normal")
        else:
            CTkMessagebox(title='NO SE PUEDE MULTIPLICAR', message="la cantidad de filas de a y la cantidad de "
                                                                   "columnas de b, no son la misma")

    def agregar_datos_matriz_a():
        dato = float(ib_ingreso_datos_matriz_a.get())
        global lista_a
        lista_a.append(dato)
        global contador_a_columnas
        contador_a_columnas += 1
        global contador_a_filas
        if contador_a_columnas == int(columnas):
            contador_a_filas += 1
            contador_a_columnas = 0
            matriz_a.append(lista_a)
            lista_a = []
        if contador_a_filas == int(filas):
            CTkMessagebox(title='ESTA LLENA LA MATRIZ A', message='NO SE PUEDEN AGREGAR MÁS DATOS')
            matriz_a_impresion = imprimir_matriz(matriz_a)
            lb_matriz_a.configure(text=" ")
            lb_matriz_a.configure(state="disabled")
            lb_matriz_a.configure(text=matriz_a_impresion)
            lb_matriz_a.configure(state="normal")

    def agregar_datos_matriz_b():
        dato = float(ib_ingreso_datos_matriz_b.get())
        global lista_b
        lista_b.append(dato)
        global contador_b_columnas
        contador_b_columnas += 1
        global contador_b_filas
        if contador_b_columnas == int(columnas):
            contador_b_filas += 1
            contador_b_columnas = 0
            matriz_b.append(lista_b)
            lista_b = []
        if contador_b_filas == int(filas):
            CTkMessagebox(title='ESTA LLENA LA MATRIZ A', message='NO SE PUEDEN AGREGAR MÁS DATOS')
            matriz_a_impresion = imprimir_matriz(matriz_b)
            lb_matriz_b.configure(text=" ")
            lb_matriz_b.configure(state="disabled")
            lb_matriz_b.configure(text=matriz_a_impresion)
            lb_matriz_b.configure(state="normal")

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
    button_ingreso.place(x=700, y=100)

    def multiplicar():
        matriz_resultante = "Resultado : " + "\n"
        matriz_resultante += str(np.dot(matriz_a, matriz_b))
        mostrar_multiplicacion = customtkinter.CTkLabel(master=frame, text=matriz_resultante,
                                                        font=("Times New Roman", 50, "bold"))
        mostrar_multiplicacion.pack(pady=400, padx=400)
        mostrar_multiplicacion.place(x=10, y=500)
        ventana.geometry('950x700')

    button_confirmar = customtkinter.CTkButton(master=frame, text='Multiplicar',
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
    ventana.title("Multiplicador de matrices")
    ventana.geometry('950x550')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    return frame


def labels_parte1(frame):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text="Multiplicador",
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400)
    lb_inbreso.place(x=10, y=0)

    lb_filas_matriz_a = customtkinter.CTkLabel(master=frame, text='FILAS MATRIZ A')
    lb_filas_matriz_a.pack(pady=400, padx=400)
    lb_filas_matriz_a.place(x=10, y=70)

    lb_columnas_matriz_a = customtkinter.CTkLabel(master=frame, text='COLUMNAS MATRIZ A')
    lb_columnas_matriz_a.pack(pady=400, padx=400)
    lb_columnas_matriz_a.place(x=180, y=70)

    lb_filas_matriz_b = customtkinter.CTkLabel(master=frame, text='FILAS MATRIZ B')
    lb_filas_matriz_b.pack(pady=400, padx=400)
    lb_filas_matriz_b.place(x=400, y=70)

    lb_columnas_matriz_b = customtkinter.CTkLabel(master=frame, text='COLUMNAS MATRIZ B')
    lb_columnas_matriz_b.pack(pady=400, padx=400)
    lb_columnas_matriz_b.place(x=560, y=70)

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

