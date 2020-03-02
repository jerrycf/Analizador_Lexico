#LIBRERIAS Y CLASES IMPORTADAS
from Estado import Estado
from AFN import AFN
from Transicion import Transicion
from time import sleep
from Cola import Cola

#VARIABLES GLOBALES
afns = []
afnGen = None
#FUNCIONES
def printMenu():
    print('''Ingrese la opción que desee realizar:
1) Crear un AFN Básico
2) Cerradura positiva de un AFN
3) Cerradura Kleen de un AFN
4) Cerradura opcional de un AFN
5) Concatenar 2 AFN
6) Unir 2 AFN
7) Mostrar los AFN
8) Unir todos los AFNs actuales
9) Convertir AFN a AFD
10) Mostrar tabla de transiciones del AFD
otro) salir 
''')
def crearAFNBasico():
    print("Funcion para crear un AFN Basico")
    simb = input("Ingrese un simbolo para la transicion de este afn: ")
    f = AFN(simb)
    f.setIds()
    afns.append(f)
    print("Cantidad de afns catuales: ", len(afns))
    # f1.printAFN()

def cerr_pos():
    print("Funcion para cerradura positiva a un AFN")
    ind = int(input("ingrese el AFN que desea realizar cerradura positiva: ")) - 1
    if 0 <= ind < len(afns):
        afns[ind].cerr_pos()
        '''for edos in afns[ind].edosAFN:
            edos.checked = False
        afns[ind].setIdsProfundidad(afns[ind].edoIni)
        afns[ind].resetIdCont()'''
        afns[ind].setIds()
        print("Cerradura positiva correctamente realizada")

def cerr_kleen():
    print("Funcion para cerradura positiva a un AFN")
    ind = int(input("ingrese el AFN que desea realizar cerradura de kleen: ")) - 1
    if 0 <= ind < len(afns):
        afns[ind].cerr_kleen()
        afns[ind].setIds()
        print("Cerradura kleen correctamente realizada")

def cerr_opc():
    print("Funcion para cerradura opcional de un automata")
    ind = int(input("ingrese el AFN que desea realizar cerradura opcional: ")) - 1
    if 0 <= ind < len(afns):
        afns[ind].cerr_opc()
        '''afns[ind].resetChecked()
        afns[ind].setIdsProfundidad(afns[ind].edoIni)
        afns[ind].resetIdCont()'''
        afns[ind].setIds()
        print("Cerradura kleen correctamente realizada")
    
def concatenarAFN():
    print("Funcion para concatenar AFNs")
    print("Funcion para unir AFNs")
    ind1 = int(input("Ingrese el AFN principal: ")) - 1
    ind2 = int(input("Ingrese el AFN con el que desea concatenar el anterior: ")) - 1
    if 0 <= ind1 < len(afns) and 0 <= ind2 < len(afns):
        afns[ind1].concatenar(afns[ind2])
        afns[ind1].setIds()
        afns.remove(afns[ind2])
        print("AFNS concatenados exitosamente")
    else:
        print("posiciones de AFNs no válidos")

def unirAFN():
    print("Funcion para unir AFNs")
    ind1 = int(input("Ingrese el AFN principal: ")) - 1
    ind2 = int(input("Ingrese el AFN con el que desea unir el anterior: ")) - 1
    if 0 <= ind1 < len(afns) and 0 <= ind2 < len(afns):
        afns[ind1].unirAFN(afns[ind2])
        afns[ind1].setIds()
        afns.remove(afns[ind2])
        print("AFNS unidos exitosamente")
    else:
        print("posiciones de AFNs no válidos")

def mostrarAFNs():
    print("Funcion para mostrar los AFN")
    print("Numero de AFNs actuales: ", len(afns))
    cont = 1
    for automata in afns:
        print("Autonamata No. ", cont)
        automata.printAFN()
        #automata.printProfundidad(automata.edoIni)
        cont += 1

def unirTodosAFNs():
    # Se crea un nuevo automata general donde contenga todos los 
    afnGen = AFN()
    afnGen.cleanAFN()
    afnGen.edoIni = Estado()
    afnGen.edoIni.setInicial(True)
    afnGen.edosAFN.add(afnGen.edoIni)
    contToken = 10
    for automata in afns:
        # Se asignan las transiciones del estado inicial del afn general a los estados iniciales de cada automata
        afnGen.edoIni.addTransicion("Epsilon", automata.edoIni)
        automata.edoIni.setInicial(False)
        # Se agregan todos los estados al set de estados del afn general
        afnGen.edosAFN = afnGen.edosAFN.union(automata.edosAFN)
        # Por cada estado de aceptacion de cada automata, se asigna un Token de 10 en 10
        for edoAccept in automata.edosAceptacion:
            edoAccept.setToken(contToken)
            contToken += 10
        # Se agregan los estados respectivos al set de estados de aceptacion del afn general 
        afnGen.edosAceptacion = afnGen.edosAceptacion.union(automata.edosAceptacion)
        # Se agrega el alfabeto al set de alfabetos del afn general
        afnGen.alfabeto = afnGen.alfabeto.union(automata.alfabeto)
    
    # Una vez que se tiene el afn general, se asignan los ids 
    afnGen.setIds()
    print("Todos los afns unidos a uno general")

    print("Automata general final:")
    afnGen.printAFN()

    # Se imprimen las transiciones del automata inicial
    print("Transiciones del automata inicial: ", len(afnGen.edoIni.transiciones))
    for trans in afnGen.edoIni.transiciones:
        print("Id edo: ", trans.getEdo().getIdEdo())
    
    # Se imprimen los estados de aceptacion con sus respectivos tokens
    print("Numero de estados de aceptacion: ", len(afnGen.edosAceptacion))
    for edosAccept in afnGen.edosAceptacion:
        print("id: ", edosAccept.getIdEdo(), " con Token: ", edosAccept.getToken())
    print("Numero de estados totales: ", len(afnGen.edosAFN))

    # Se imprime el afabeto final del automata
    print("Alfabeto final del automata: ")
    for simbs in afnGen.alfabeto:
        print(simbs)
    
    return afnGen


def convertAFNtoAFD():
    afnGen.printAFN()
    if afnGen.isEmpty():
        print("No se tiene un automata general para poder realizar esta accion.")
        return
    
    #afnGen.printAFN()
    afnGen.toAFD()  
    

#MAIN CODE
# AFNs = set()
if __name__ == "__main__":
    printMenu()
    op = int(input())
    while op >0 and op <= 10:
        if op == 1:
            crearAFNBasico()
        if op == 2:
            cerr_pos()
        if op == 3: 
            cerr_kleen()
        if op == 4: 
            cerr_opc()
        if op == 5:
            concatenarAFN()
        if op == 6:
            unirAFN()
        if op == 7:
            mostrarAFNs()
        if op == 8:
            afnGen = unirTodosAFNs()
        if op == 9:
            convertAFNtoAFD()
        # sleep(1)
        printMenu()
        op = int(input())