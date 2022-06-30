Empezando el código, lo que hice fue importar la librería tkinter, será la interfaz con la que trabajaré,
Luego defino dos variables, "clase y promedioClase" que serán llenadas luego con el comando append.
La variable v será la variable que nos servirá para crear la ventana en la que se trabajará.
Se usa tkinter.Tk() para crear una ventana.
v.title se usa para darle un nombre a la ventana.
v.geometry se usa para definir el tamaño de la ventana apenas se inicie el código.
v.configure(background="gray10") es el color de fondo que tendrá la ventana.

_v = tkinter.Tk()  
v.title("Menú") 
v.geometry("600x400") 
v.configure(background="gray10")

Empiezo definiendo variables con ver_notas, esta mostrará las notas en la ventana, al inicio se usa el comando pack_forget porque anteriormente se está en un menú con widgets, lo que hace ese comando es eliminar los widgets de la ventana y digitalizar los de la función actual.
Se crea una función anidada para poder borrar el pack del widget de ver notas al momento de finalizar.

_def ver_notas():
    t1.pack_forget()  # Borra los widgets del menú (mejor con función), con pack se imprime en la pantalla, antes solo se define
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

   _def borrar_b1n():  # Función para borrar el botón
        b1n.pack_forget()  # Forget sirve para olvidar el pack del widget
        menu()  # Vuelve al menú

   _b1n = tkinter.Button(v, text=f"Las notas de la clase son: {clase}", fg="black", bg="green yellow",
                         font="Courier, 20", width=50, height=50, command=borrar_b1n)  # Se usa la variable de la ventana para especificar que ahí irá el widget
    b1n.pack()

El comando "pack" sirve para poder digitalizar una varibale creada anteriormente en el código, primero se define y luego se digitaliza, es como una función, esta variable puede verse como una entrada (Entry) texto (Label) o botón (Button) cada una con características especiales.
Label solo muestra texto, Button es un botón con el que se puede interactuar y Entry funciona como una input.

_Botón1.pack()
Entrada1.pack()
Texto1.pack()

Para definir la variable se usa su nombre, tkinter(alguno de los 3 recursos) y dentro de los paréntesis, las características, en este caso, usé "v" para que se pueda digitalizar en mi ventana, text= para que muestre un texto y antes de eso usé un format para que se pueda ver los elementos en lista, fg sirve para darle color al texto, bg para definir su fondo, font para establecer una fuente de letra y luego el tamaño que se desea, with y height para definir el tamaño del widget y command= para poder ejecutar una función al momento de presionar un botón.

_Botón = tkinter.Button(ventana, text="Texto", fg="color_del_texto", bg="color_del_fondo", font="fuente_de_letra, tamaño_de_letra", command=función_a_usar)}
Entrada = tkinter.Entry(ventana, text="Texto", fg="color_del_texto", bg="color_del_fondo", font="fuente_de_letra, tamaño_de_letra")
Texto = tkinter.Label(ventana, text="Texto", fg="color_del_texto", bg="color_del_fondo", font="fuente_de_letra, tamaño_de_letra")


Para ver el promedio hice lo mismo que ver notas, usé un format, fuente de letra, tamaño, y características similares, solo varía la variable usada en format, también creé una función para borrar el botón una vez usado y volver al menú.

Para el promedio, sumé todos los elementos de la lista clase y los dividí entre la cantidad de elementos que hay en la listal clase, luego se lleva a la lista vacía definida al inicio llamada "promedioClase"
También se usó una fucnión para borrar el botón y volver al menú, darle una fuente de letra, color, tamaño, etc.

_def promedio():
    t1.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

   _def borrar_bp1():
        bp1.pack_forget()
        menu()

   _prom = sum(clase) / len(clase)  # Se suman todos los elementos de clase y se divide entre la cantidad de elementos de clase
   promedioClase.append(prom)
   bp1 = tkinter.Button(v, text=f"El promedio es de {promedioClase}",fg="black", bg="green yellow", font="Courier, 20", width=50, height=50, command=borrar_bp1)
   bp1.pack()

Para registrar notas usé una función anidada llamada registrar_notas, la cual contiene código, al inicio la variable n será igual a la variable e1n.get en formato de números enteros ((nombre_de_variable).get()) sirve para tomar el valor de una entrada (Entry) y poder usarlo con una variable, así como un input.
Usé if para crear condiciones, en este caso,si n es 123, creará una función y seguirá con el código, hasta que cumpla otra condición y pueda ser llevado a la lista vacía "clase" o no.
Dentro de esa función hice otra la cual también sirve para borrar el botón que se generará al terminar la línea de código, el botón que sale es usado para imprimir las notas de clase previamente escritas.

_def notas():

   _def registrar_notas():

   _n = float(e1n.get())  # n es igual a la entrada en valor de entero
       if n == 123:  # si n es 123 entonces se muestran las notas
            def borrar_e2n():
                e2n.pack_forget()
            e2n = tkinter.Button(v, text=f"Las notas de la clase son {clase}", fg="black", bg="green yellow", font="Courier, 20", command=borrar_e2n)
            e2n.pack()

   _elif n < 0 or n > 20:  # si n es menor a 0 o mayor a 20 sale un boton pidiendo nota valida
            def borrar_e3n():
                e3n.pack_forget()
            e3n = tkinter.Button(v, text="Ingrese nota válida",fg="white", bg="red",font="Courier, 20", command=borrar_e3n)
            e3n.pack()
        else:
            clase.append(n)  # En caso de cumplir con condiciones, entra el valor digitado a la lista


Finalmente, la última condición es que si n es menor a 0 o mayor a 20, no podrá ser añadido a la lista, creando un botón y una función para borrar el botón.
En caso de cumplir con todas las condiciones, se añade la nota a la lista vacía, las notas pueden estar en formato decimal.
Al iniciar la función principal, se borran los widgets del menú.
Creé una función para ayudar a la función de notas a regresar al menú, no fue necesaria.
Al final como dije, primero se definen los widgets (no importa si están fuera de las funciones) y luego se citan con su respectivo comando (nombre_del_widget).pack().
Ya para finalizar, creé la función menú para que pueda retornar al menú una vez citada e imprima los widgets, esta función es usada una vez es iniciado el código.
Al final, usé el comando v.tkinter.mainloop ya que es el responsable de llevar todo el registro de lo que sucede en la ventana.
