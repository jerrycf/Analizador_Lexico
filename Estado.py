from Transicion import Transicion
class Estado(object):
    def __init__(self, id=-1):
        self.inicial = False
        self.aceptacion = False
        self.idEdo = id
        self.transiciones = set()
        self.transiciones.clear()
        self.token = -1
        self.checked = False

    def getIdEdo(self):
        return self.idEdo

    def getToken(self):
        return self.token
    
    def setIdEdo(self, id):
        self.idEdo = id
    
    def setAceptacion(self, accept):
        self.aceptacion = accept

    def setInicial(self, ini):
        self.inicial = ini

    def setToken(self, t):
        self.token = t
    
    def addTransicion(self, char, edo):
        self.transiciones.add(Transicion(char, edo))

    def isAceptacion(self):
        return self.aceptacion
    
    def isInicial(self):
        return self.inicial

    def isChecked(self):
        return self.checked

    def sinTransiciones(self):
        # Pregunta si el set está vacio
        if not self.transiciones:
            return True
        # El set no esta vacio
        return False
    
    def printEdo(self):
        print("idEdo: ", self.idEdo, " Transiciones: ")
        # Preguntamos si el estado actual contiene transiciones o no
        if self.sinTransiciones():
            print("Estado sin transiciones\n")
        else:
            for t in self.transiciones:
                t.printTransicion()