class Multiplicacion:
    def __init__(self, matriz_a, matriz_b):
        self.matriz_a = matriz_a
        self.matriz_b = matriz_b
        self.resultado = []

    def multiplicar(self):
        for i in self.matriz_a:
            print(i)

    def imprimir_matriz(self, matriz):
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
