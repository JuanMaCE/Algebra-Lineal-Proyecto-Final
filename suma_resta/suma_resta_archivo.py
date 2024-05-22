import customtkinter
global edicion
global tipo_de_dato
global lb_datos
matriz_a = []
matriz_b = []
from CTkMessagebox import CTkMessagebox
global filas
global columnas

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
    lb_matriz_a.place(x=10, y=350)

    lb_matriz_b = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 50))
    lb_matriz_b.pack(pady=400, padx=400, )
    lb_matriz_b.place(x=250, y=350)

    lb_matriz_suma_resta = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 50), state="disable")
    lb_matriz_suma_resta.pack(pady=400, padx=400)
    lb_matriz_suma_resta.place(x=550, y=350)

    # ingreso de datos
    ib_ingreso_datos_matriz_a = customtkinter.CTkEntry(master=frame, placeholder_text='Datos Matriz A', width=300,
                                                       height=35, state="disable")
    ib_ingreso_datos_matriz_a.pack(pady=100, padx=10)
    ib_ingreso_datos_matriz_a.place(x=10, y=150)

    ib_ingreso_datos_matriz_b = customtkinter.CTkEntry(master=frame, placeholder_text='Datos Matriz A', width=300,
                                                       height=35, state="disable")
    ib_ingreso_datos_matriz_b.pack(pady=100, padx=10)
    ib_ingreso_datos_matriz_b.place(x=10, y=200)

    ib_ingreso_filas = customtkinter.CTkEntry(master=frame, placeholder_text='Datos F', width=135,
                                              height=35)
    ib_ingreso_filas.pack(pady=100, padx=10)
    ib_ingreso_filas.place(x=10, y=100)

    ib_ingreso_columnas = customtkinter.CTkEntry(master=frame, placeholder_text='Datos C', width=135,
                                                 height=35)
    ib_ingreso_columnas.pack(pady=100, padx=10)
    ib_ingreso_columnas.place(x=175, y=100)
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
        global filas
        filas = ib_ingreso_filas.get()
        global columnas
        columnas = ib_ingreso_columnas.get()
        ib_ingreso_datos_matriz_a.configure(state="normal")
        ib_ingreso_datos_matriz_b.configure(state="normal")

    def agregar_datos_matriz_a():
        dato = ib_ingreso_datos_matriz_a.get()
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
        dato = ib_ingreso_datos_matriz_b.get()
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
    button_ingreso_datos_matriz_a.place(x=350, y=150)

    button_ingreso_datos_matriz_b = customtkinter.CTkButton(master=frame, text='Ingreso Matriz B',
                                                            font=("Arial", 20), fg_color="#3E4446",
                                                            command=lambda: agregar_datos_matriz_b())

    button_ingreso_datos_matriz_b.pack(pady=10, padx=10)
    button_ingreso_datos_matriz_b.place(x=350, y=200)

    # confirmación de datos
    button_ingreso = customtkinter.CTkButton(master=frame, text='Ingreso',
                                             font=("Arial", 20), fg_color="#3E4446",
                                             command=filas_columasn_agregar)

    button_ingreso.pack(pady=10, padx=10)
    button_ingreso.place(x=350, y=100)

    def generar_suma():
        matriz_suma = sumador(matriz_a, matriz_b)
        martiz_suma_impresion = imprimir_matriz(matriz_suma)
        lb_matriz_suma_resta.configure(text="", state="normal")
        lb_matriz_suma_resta.configure(text=martiz_suma_impresion)

    def generar_resta():
        matriz_resta = restador(matriz_a, matriz_b)
        matriz_resta_impresion = imprimir_matriz(matriz_resta)
        lb_matriz_suma_resta.configure(text="", state="normal")
        lb_matriz_suma_resta.configure(text=matriz_resta_impresion)

    button_cofnrimar_resta = customtkinter.CTkButton(master=frame, text="efectuar resta",
                                                     font=("Arial", 20), fg_color="#3E4446",
                                                     command=generar_resta)
    button_cofnrimar_resta.pack(pady=10, padx=10)
    button_cofnrimar_resta.place(x=650, y=275)

    button_confirmar_suma = customtkinter.CTkButton(master=frame, text="efectuar suma",
                                                    font=("Arial", 20), fg_color="#3E4446",
                                                    command=generar_suma)
    button_confirmar_suma.pack(pady=10, padx=10)
    button_confirmar_suma.place(x=500, y=275)
    # exportar archivos txt

    ventana.mainloop()
    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Pila")
    ventana.geometry('950x550')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    return frame


def labels_parte1(frame):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Suma / Resta ',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    lb_filas = customtkinter.CTkLabel(master=frame, text='Ingrese cantidad de filas')
    lb_filas.pack(pady=400, padx=400)
    lb_filas.place(x=10, y=70)

    lb_columnas = customtkinter.CTkLabel(master=frame, text='Ingrese cantidad de Columnas')
    lb_columnas.pack(pady=400, padx=400)
    lb_columnas.place(x=175, y=70)

    lb_matriz_a_title = customtkinter.CTkLabel(master=frame, text='MATRIZ A', font=("Arial", 30))
    lb_matriz_a_title.pack(pady=400, padx=400)
    lb_matriz_a_title.place(x=50, y=275)

    lb_matriz_b_title = customtkinter.CTkLabel(master=frame, text='MATRIZ B', font=("Arial", 30))
    lb_matriz_b_title.pack(pady=400, padx=400)
    lb_matriz_b_title.place(x=300, y=275)

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


def sumador(matriz_a1, matriz_b2):
    matriz_resultante = []
    print(" procedimiento: ")
    for i in range(len(matriz_a1)):
        lista = []
        for j in range(len(matriz_a1[i])):
            a = matriz_a1[i][j]
            b = matriz_b2[i][j]
            suma = float(a) + float(b)
            print("se suma ", matriz_a1[i][j], " y ", matriz_b2[i][j], ", se agrega en la posición x = ", j, "y = ", i)
            lista.append(suma)
        matriz_resultante.append(lista)
    return matriz_resultante


def restador(matriz_a1, matriz_b2):
    matriz_resultante = []
    print(" procedimiento: ")
    for i in range(len(matriz_a1)):
        lista = []
        for j in range(len(matriz_a1[i])):
            a = matriz_a1[i][j]
            b = matriz_b2[i][j]
            resta = float(a) - float(b)
            print("se resta ", matriz_a1[i][j], " y ", matriz_b2[i][j], ", se agrega en la posición x = ", j, "y = ", i)
            lista.append(resta)
        matriz_resultante.append(lista)
    return matriz_resultante