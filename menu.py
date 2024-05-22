import customtkinter
from suma_resta import suma_resta_archivo
from multiplicador_de_matrices import multiplicacion_de_matrices
app = customtkinter.CTk()
from operacion_vectores_files import menu_operacion_con_vectores
from cifrado_files import cifrado
from cadenas_de_markov_files import cadenas_de_markov


def suma_resta():
    suma_resta_archivo.main()


def open_multiplicador():
    multiplicacion_de_matrices.main()


def determinante_de_una_matriz():
    print(" ")


def rango_de_una_matriz():
    print(" ")


def cifrado_por_matrices():
    cifrado.main()


def cadenas_de_markov_open():
    cadenas_de_markov.main()


def open_operaciones_con_vectores():
    menu_operacion_con_vectores.main_window()


def main_window():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app.title("MENU")
    app.geometry("1000x500")
    app.wm_attributes("-topmost", False)
    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    buttons(frame)

    # botones
    app.mainloop()


def buttons(frame):
    button_suma_resta = customtkinter.CTkButton(master=frame, text='SUMA / RESTA', height=100, width=150,
                                                font=("Arial", 20), fg_color="#3E4446", command=suma_resta)

    button_suma_resta.pack(pady=10, padx=10)
    button_suma_resta.place(x=50, y=10)

    button_multiplicador = customtkinter.CTkButton(master=frame, text='Multiplicador', height=100, width=160,
                                                   font=("Arial", 20), fg_color="#3E4446", command=open_multiplicador)

    button_multiplicador.pack(pady=10, padx=10)
    button_multiplicador.place(x=50, y=150)

    button_determinante_de_una_matriz = customtkinter.CTkButton(master=frame, text='Determinante de una Matriz',
                                                                height=100, width=210, font=("Arial", 20),
                                                                fg_color="#3E4446", command=determinante_de_una_matriz)

    button_determinante_de_una_matriz.pack(pady=10, padx=10)
    button_determinante_de_una_matriz.place(x=50, y=310)

    button_rango_de_una_matriz = customtkinter.CTkButton(master=frame, text='Rango de una matriz', height=100,
                                                         width=210, font=("Arial", 20), fg_color="#3E4446",
                                                         command=rango_de_una_matriz)

    button_rango_de_una_matriz.pack(pady=10, padx=10)
    button_rango_de_una_matriz.place(x=300, y=10)

    button_cifrado_por_matric = customtkinter.CTkButton(master=frame, text='Cifrado por matrices',
                                                        height=100, width=210,
                                                        font=("Arial", 20), fg_color="#3E4446",
                                                        command=cifrado_por_matrices)

    button_cifrado_por_matric.pack(pady=10, padx=10)
    button_cifrado_por_matric.place(x=300, y=150)

    button_cadenas_markov = customtkinter.CTkButton(master=frame, text='Cadenas de Markov', height=100, width=210,
                                                    font=("Arial", 20), fg_color="#3E4446",
                                                    command=cadenas_de_markov_open)

    button_cadenas_markov.pack(pady=10, padx=10)
    button_cadenas_markov.place(x=300, y=310)

    button_operacion_con_vectores = customtkinter.CTkButton(master=frame, text='Operación con Vectores',
                                                            height=100, width=210,
                                                            font=("Arial", 20), fg_color="#3E4446",
                                                            command=open_operaciones_con_vectores)

    button_operacion_con_vectores.pack(pady=10, padx=10)
    button_operacion_con_vectores.place(x=650, y=10)


main_window()
