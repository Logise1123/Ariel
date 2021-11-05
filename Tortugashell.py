//Tortuga shell
//Python 3






from turtle import * 
reset()
def Instrucciones():
    print("Cuadrado(Tamaño) se usa para crear un cuadrado de X por X")
    print("Circulo(Tamaño) se usa para crear un circulo de X tamaño")
    print("Poligono(Lados, Longitud de lado) se usa para crear un poligono cerrado de X lados y de X tamaño por lado")
    print("Borrar() se usa para borrar")
    print("Dibujo(Dibujo) se usa para crear un dibujo")
    print("Comandos: F = Adelante")
    print("B = Atras")
    print("R = Derecha")
    print("L = Izquierda")
    print("U = Pintar")
    print("D = Dejar de pintar")
    print("Introducir: comando + valor separado por el caracter: -")
def Cuadrado(Tamaño):             
    for i in range(4):
        forward(Tamaño)
        left(90) 
def Circulo(Tamaño):
    for i in range(24):
        forward(Tamaño)
        left(15)
def Poligono(Lados,Longitud_de_lado):
    for i in range(Lados):
        forward(Longitud_de_lado)
        left(360 / Lados)
def Borrar():
    clear()
def Controlador(do, val):
    do = do.upper()
    if do == "F":
        forward(val)
    elif do == "B":
        backward(val)
    elif do == "R":
        right(val)
    elif do == "L":
        left(val)
    elif do == "U":
        penup()
    elif do == "D":
        pendown()
    elif do == "C":
        clear()
def Dibujo(Dibujo):
    Borrar()
    lista_comando = Dibujo.split("-")
    for comando in lista_comando:
        Longitud = len(comando)
        if Longitud == 0:
            continue
        tipo_comando = comando[0]
        num = 0
        if Longitud > 1:
            num_string = comando[1:]
            num = int(num_string)
        Controlador(tipo_comando,num)
Instrucciones()
    
        
        

