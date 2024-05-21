import customtkinter
from operacion_vectores_files import suma_vectores
app = customtkinter.CTk()


def open_suma_vectores():
    suma_vectores.main()


def producto_punto_de_vectores():
    pass

def producto_cruz_de_vectores():
    print(" ")


def main_window():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app.title("MENU OPERACIÓN CON VECTORES")
    app.geometry("1000x500")
    app.wm_attributes("-topmost", False)
    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    buttons(frame)

    # botones
    app.mainloop()


def buttons(frame):
    button_suma_vectores = customtkinter.CTkButton(master=frame, text='SUMA VECTORES', height=100, width=150,
                                                   font=("Arial", 20), fg_color="#3E4446", command=open_suma_vectores)

    button_suma_vectores.pack(pady=10, padx=10)
    button_suma_vectores.place(x=50, y=10)

    button_producto_punto_vectores = customtkinter.CTkButton(master=frame, text='Producto Punto Vectores',
                                                             height=100, width=160,
                                                             font=("Arial", 20), fg_color="#3E4446",
                                                             command=producto_punto_de_vectores)

    button_producto_punto_vectores.pack(pady=10, padx=10)
    button_producto_punto_vectores.place(x=50, y=150)

    button_producto_punto_cruz = customtkinter.CTkButton(master=frame, text='Producto Cruz de Vectores',
                                                         height=100, width=210, font=("Arial", 20),
                                                         fg_color="#3E4446", command=producto_cruz_de_vectores)

    button_producto_punto_cruz.pack(pady=10, padx=10)
    button_producto_punto_cruz.place(x=50, y=310)

