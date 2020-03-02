from tkinter import *
from tkinter import messagebox
from functools import partial

objetos=[]

def limpiarVentana(listaObjetos):
    for i in listaObjetos:
        i.destroy()

def mostrarTransiciones():
    global objetos
    transiciones = Text(ventana, width=35, height=10, bd=2)
    transiciones.insert(INSERT, "Mostrando transiciones...")
    transiciones.grid(row=0, columnspan=2, padx=5, pady=5)
    objetos.append(transiciones)

    
def leerDato(entrada):
    dato = entrada.get()
    entrada.delete(0, END)
    if(dato==''):
        messagebox.showerror(message="No se ingreso ningun dato.", title="Error")
    else:
        messagebox.showinfo(message="Dato ingresado correctamente.", title="Ingresar datos.")
    return dato

def ingresarValor(dato):
    global objetos
    automata = Label(ventana, text=dato, bg='white')
    automata.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    datoAutomata = Entry(ventana, bd=2)
    datoAutomata.grid(row=0, column=1, sticky=W, padx=8, pady=5)
    datoAutomata.config(justify='left', state='normal')
    botonIngresar = Button(ventana, text='Ingresar', command=partial(leerDato, datoAutomata))
    botonIngresar.grid(row=1, column=0, sticky=W, padx=8)
    objetos.append(automata)
    objetos.append(datoAutomata)
    objetos.append(botonIngresar)

ventana = Tk()
ventana.title('Automata')
ventana.geometry('300x200+625+300')

barraMenu = Menu(ventana)
menuAutomata = Menu(barraMenu, tearoff=0, bg='white')
menuAutomata.add_command(label="Crear un AFN basico", command = partial(ingresarValor, 'Simbolo'))
menuAutomata.add_command(label = "Cerradura positiva", command = partial(ingresarValor, 'Automata'))
menuAutomata.add_command(label = "Cerradura de Kleene", command = partial(ingresarValor, 'Automata'))
menuAutomata.add_command(label = "Cerradura opcional", command = partial(ingresarValor, 'Automata'))
menuAutomata.add_command(label = "Concatenar", command = partial(ingresarValor, 'Automata'))
menuAutomata.add_command(label = "Unir", command = partial(ingresarValor, 'Automata'))
menuAutomata.add_command(label = "Convertir AFN a AFD", command = partial(ingresarValor, 'Automata'))
menuAutomata.add_command(label = "Mostrar", command=mostrarTransiciones)
barraMenu.add_cascade(label = "AFN", menu=menuAutomata)
menuInterfaz = Menu(barraMenu, tearoff=0, bg='white')
menuInterfaz.add_command(label = "Limpiar", command=partial(limpiarVentana, objetos))
menuInterfaz.add_command(label = "Salir", command=exit)
barraMenu.add_cascade(label = "Interfaz", menu=menuInterfaz)

ventana.config(bg='white', menu=barraMenu)
ventana.mainloop()

root.config(menu = menubar)
root.mainloop()
