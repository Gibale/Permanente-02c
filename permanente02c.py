import tkinter  # Importamos la librería
clase = []  # Lista vacía para rellenarla con append
promedioClase = []

v = tkinter.Tk()  # Crear ventana con la variable "v"
v.title("Menú")  # Ponerle un título a la ventana
v.geometry("600x400")  # Definir tamaño de la ventana
v.configure(background="gray10")  # Color del fondo de la ventana


def ver_notas():
    t1.pack_forget()  # Borra los widgets del menú (mejor con función), con pack se imprime en la pantalla, antes solo se define
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

    def borrar_b1n():  # Función para borrar el botón
        b1n.pack_forget()  # Forget sirve para olvidar el pack del widget
        menu()  # Vuelve al menú

    b1n = tkinter.Button(v, text=f"Las notas de la clase son: {clase}", fg="black", bg="green yellow",
                         font="Courier, 20", width=50, height=50, command=borrar_b1n)  # Se usa la variable de la ventana para especificar que ahí irá el widget
    b1n.pack()

def ver_promedio():
    t1.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

    def borrar_b1p():
        b1p.pack_forget()
        menu()

    b1p = tkinter.Button(v, text=f"El promedio de la clase es de {promedioClase}", fg="black", bg="green yellow", font="Courier, 20", width=50, height=50, command=borrar_b1p)
    b1p.pack()


def promedio():
    t1.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

    def borrar_bp1():
        bp1.pack_forget()
        menu()

    prom = sum(clase) / len(clase)  # Se suman todos los elementos de clase y se divide entre la cantidad de elementos de clase
    promedioClase.append(prom)
    bp1 = tkinter.Button(v, text=f"El promedio es de {promedioClase}",fg="black", bg="green yellow", font="Courier, 20", width=50, height=50, command=borrar_bp1)
    bp1.pack()


def notas():

    def registrar_notas():

        n = float(e1n.get())  # n es igual a la entrada en valor de entero
        if n == 123:  # si n es 123 entonces se muestran las notas
            def borrar_e2n():
                e2n.pack_forget()
            e2n = tkinter.Button(v, text=f"Las notas de la clase son {clase}", fg="black", bg="green yellow", font="Courier, 20", command=borrar_e2n)
            e2n.pack()

        elif n < 0 or n > 20:  # si n es menor a 0 o mayor a 20 sale un boton pidiendo nota valida
            def borrar_e3n():
                e3n.pack_forget()
            e3n = tkinter.Button(v, text="Ingrese nota válida",fg="white", bg="red",font="Courier, 20", command=borrar_e3n)
            e3n.pack()
        else:
            clase.append(n)  # En caso de cumplir con condiciones, entra el valor digitado a la lista

    t1.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

    def regresar_menu():  # Funcion para regresar al menu, se borran los widgets y aparecen los del menu
        t1n.pack_forget()
        e1n.pack_forget()
        c1n.pack_forget()
        menu.pack_forget()
        t1.pack()
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()

    t1n = tkinter.Label(v, text="Ingrese notas", fg="white", bg="gray10", font="Courier, 20")  # Se definen los widgets
    e1n = tkinter.Entry(v, fg="black", bg="gray85", font="Courier, 20")
    c1n = tkinter.Button(v, text="Click para registrar", fg="white", bg="gray10", font="Courier, 20", command=registrar_notas)
    menu = tkinter.Button(v, text="Regresar al menú",fg="white", bg="gray10", font="Courier, 20", command=regresar_menu)
    t1n.pack()
    e1n.pack()
    c1n.pack()
    menu.pack()


def menu():
    t1.pack()
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()


b1 = tkinter.Button(v, text="Ingresar notas", fg="white", bg="gray10", font="Courier, 20", command=notas)
b2 = tkinter.Button(v, text="Calcular promedio", fg="white", bg="gray10", font="Courier, 20", command=promedio)
b3 = tkinter.Button(v, text="Ver promedio", fg="white", bg="gray10", font="Courier, 20", command=ver_promedio)
b4 = tkinter.Button(v, text="Ver notas", fg="white", bg="gray10", font="Courier, 20", command=ver_notas)
t1 = tkinter.Label(v, text="Bienvenido profesor/a", fg="white", font="Courier, 20", bg="gray10")

menu()
v.mainloop()  # Lleva el registro de todo lo que sucede en la ventana
