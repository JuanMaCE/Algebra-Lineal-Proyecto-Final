import customtkinter as ctk
import numpy as np
from CTkMessagebox import CTkMessagebox

global matriz_a, entradas, dimension

matriz_a = []
entradas = []


def calcular_determinante():
    try:
        datos = []
        for i in range(dimension):
            fila = []
            for j in range(dimension):
                dato = float(entradas[i][j].get())
                fila.append(dato)
            datos.append(fila)

        matriz = np.array(datos)
        determinante = np.linalg.det(matriz)
        lb_resultado.configure(text=f"La determinante de la matriz es: {determinante:.2f}")
    except Exception as e:
        CTkMessagebox(title='Error', message=str(e))


def filas_columnas_agregar():
    global dimension, entradas, matriz_a
    dimension = int(ib_dimension.get())
    entradas = [[None for _ in range(dimension)] for _ in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            entry = ctk.CTkEntry(master=frame)
            entry.place(x=10 + j * 50, y=150 + i * 50)
            entradas[i][j] = entry


def main():
    global frame, lb_resultado, ib_dimension

    ventana = cargar_datos()
    frame = frame1(ventana)
    labels_parte1(frame)

    ib_dimension = ctk.CTkEntry(master=frame, placeholder_text='Dimensión', width=135, height=35)
    ib_dimension.place(x=10, y=100)

    button_ingreso = ctk.CTkButton(master=frame, text='Establecer Dimensión', font=("Arial", 20), fg_color="#3E4446",
                                   command=filas_columnas_agregar)
    button_ingreso.place(x=160, y=100)

    button_calcular = ctk.CTkButton(master=frame, text='Calcular Determinante', font=("Arial", 20), fg_color="#3E4446",
                                    command=calcular_determinante)
    button_calcular.place(x=380, y=100)

    lb_resultado = ctk.CTkLabel(master=frame, text="", font=("Arial", 20))
    lb_resultado.place(x=10, y=300)

    ventana.mainloop()


def cargar_datos():
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')
    ventana = ctk.CTkToplevel()
    ventana.grab_set()
    ventana.title("Cálculo del Determinante")
    ventana.geometry('700x400')
    return ventana


def frame1(ventana):
    frame = ctk.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    return frame


def labels_parte1(frame):
    lb_titulo = ctk.CTkLabel(master=frame, text="Cálculo del Determinante de una Matriz",
                             font=("Times New Roman", 30, "bold"))
    lb_titulo.pack(pady=10)
    lb_titulo.place(x=10, y=10)


if __name__ == "__main__":
    main()