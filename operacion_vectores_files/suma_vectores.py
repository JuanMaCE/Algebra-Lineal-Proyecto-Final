import matplotlib.pyplot as plt
import customtkinter
app = customtkinter.CTk()


def main():

    ventana = cargar_datos()
    frame = frame1(ventana)
    labels_parte1(frame)

    # cordenadas

    punto_x_a = customtkinter.CTkEntry(master=frame, placeholder_text='', width=300,
                                       height=35)
    punto_x_a.pack(pady=100, padx=10)
    punto_x_a.place(x=100, y=100)

    punto_y_a = customtkinter.CTkEntry(master=frame, placeholder_text="", width=300)
    punto_y_a.pack(pady=400, padx=400, )
    punto_y_a.place(x=100, y=140)

    punto_x_b = customtkinter.CTkEntry(master=frame, placeholder_text='', width=300)
    punto_x_b .pack(pady=100, padx=10)
    punto_x_b .place(x=100, y=180)

    punto_y_b = customtkinter.CTkEntry(master=frame, placeholder_text='', width=300,
                                       height=35)
    punto_y_b.pack(pady=100, padx=10)
    punto_y_b.place(x=100, y=220)

    def generar_grafico():
        ventana.geometry('550x550')
        punto_resultante_x = int(punto_x_a.get()) + int(punto_x_b.get())
        punto_resultante_y = int(punto_y_a.get()) + int(punto_y_b.get())

        plt.quiver([0, int(punto_x_a.get()), 0], [0, int(punto_y_a.get()), 0], [int(punto_x_a.get()),
                                                                                int(punto_x_b.get()),
                   punto_resultante_x],
                   [int(punto_y_a.get()), int(punto_y_b.get()), punto_resultante_y],
                   color=['blue', 'red', 'green'], scale_units='xy', angles='xy', scale=1)
        plt.xlim(0, punto_resultante_x)
        plt.ylim(0, punto_resultante_y)

        plt.axvline(x=0)
        plt.axhline(y=0)

        plt.show()
        texto_suma_x = punto_x_a.get() + " + " + punto_x_b.get() + " = " + str(punto_resultante_x)
        texto_suma_y = punto_y_a.get() + " + " + punto_y_b.get() + " = " + str(punto_resultante_y)
        cordenada_final = "(" + str(punto_resultante_x) + ", " + str(punto_resultante_y) + ")"

        lb_datos_x_suma = customtkinter.CTkLabel(master=frame, text=str(texto_suma_x),
                                                 font=("Times New Roman", 50, "bold"))
        lb_datos_x_suma.pack(pady=400, padx=400)
        lb_datos_x_suma.place(x=10, y=350)

        lb_datos_y_suma = customtkinter.CTkLabel(master=frame, text=texto_suma_y, font=("Times New Roman", 50, "bold"))
        lb_datos_y_suma.pack(pady=400, padx=400)
        lb_datos_y_suma.place(x=10, y=400)

        lb_datos_resultante = customtkinter.CTkLabel(master=frame, text=cordenada_final,
                                                     font=("Times New Roman", 50, "bold"))
        lb_datos_resultante.pack(pady=400, padx=400)
        lb_datos_resultante.place(x=10, y=450)

    button_confirmar = customtkinter.CTkButton(master=frame, text="efectuar suma",
                                               font=("Arial", 20), fg_color="#3E4446",
                                               command=generar_grafico)
    button_confirmar.pack(pady=10, padx=10)
    button_confirmar.place(x=10, y=275)

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("SUMA DE VECTORES")
    ventana.geometry('550x350')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    return frame


def labels_parte1(frame):
    lb_title = customtkinter.CTkLabel(master=frame, text='SUMA DE VECTORES ',
                                      font=("Times New Roman", 50, "bold"))
    lb_title.pack(pady=400, padx=400, )
    lb_title.place(x=10, y=0)

    lb_datos_x_a = customtkinter.CTkLabel(master=frame, text='Vector A[X]', font=("Times New Roman", 15, "bold"))
    lb_datos_x_a.pack(pady=400, padx=400)
    lb_datos_x_a.place(x=10, y=100)

    lb_datos_y_a = customtkinter.CTkLabel(master=frame, text='Vector A[Y]', font=("Times New Roman", 15, "bold"))
    lb_datos_y_a.pack(pady=400, padx=400)
    lb_datos_y_a.place(x=10, y=140)

    lb_datos_x_b = customtkinter.CTkLabel(master=frame, text='Vector B[X]', font=("Times New Roman", 15, "bold"))
    lb_datos_x_b.pack(pady=400, padx=400)
    lb_datos_x_b.place(x=10, y=180)

    lb_datos_y_b = customtkinter.CTkLabel(master=frame, text='Vector B[Y]', font=("Times New Roman", 15, "bold"))
    lb_datos_y_b.pack(pady=400, padx=400)
    lb_datos_y_b.place(x=10, y=220)
