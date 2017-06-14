from tkinter import *
 
vtn = Tk()



vtn.geometry("640x480")



import math

def mostrar(ventana): ventana.deiconify()

def ejecutar(f): vtn.after(700,f)

def area_triangulo(b,h):
    area=b*h/2
    return area
def area_cuadrado(l):
    area= l**2
    return area
def area_pentagono(p,h):
    area= p*h/2
    return area

def abrirOpcion1():
    v1=Tk()
    v1.title("AREA Y PERIMETRO DE UNA FIGURA")
    v1.geometry("640x480")
    lbl=Label(v1, text="""AREA Y PERIMETRO DE UNA FIGURA """,justify = LEFT,padx = 0).pack()
    b3=Button(v1,text="Triangulo",command=triangulo).pack()
    b4=Button(v1,text="Cuadrado",command=cuadrado).pack()
    b5=Button(v1,text="Pentagono",command=pentagono).pack()

def abrirOpcion2():
    v2=Tk()
    v2.title("Animacion")
    v2.geometry("640x480")  
    lbl=Label(v2, text="""ANIMACION""",justify = LEFT,padx = 0).pack()
    
def triangulo():
    t=Tk()
    t.title("Triangulo")
    t.geometry("640x480")

    lbl3=Label(t, text="""Ingrese la base:  """,justify = LEFT,padx = 20).pack()
    lbl4=Label(t, text="""Ingrese la altura:  """,justify = LEFT,padx = 20).pack()
def cuadrado():
    c=Tk()
    c.title("Cuadrado")
    c.geometry("640x480")
    lbl5=Label(c, text="Ingrese el lado del cuadrado:  ",justify = LEFT,padx = 20).pack()
def pentagono():
    p=Tk()
    p.title("Pentagono")
    p.geometry("640x480")
    lbl6=Label(p, text="Ingrese el apotema del pentagono:  """,justify = LEFT,padx = 20).pack()
    lbl7=Label(p, text="Ingrese el perimetro del pentagono:  """,justify = LEFT,padx = 20).pack()
    

Label(vtn, text="""ESCOJA UNA OPCION: """,justify = LEFT,padx = 20).pack()

b1=Button(vtn,text="Opcion 1",command=abrirOpcion1).pack()

b2=Button(vtn,text="Opcion 2",command=abrirOpcion2).pack()


mainloop()
