from Estado import Estado
from Cola import Cola
from Transicion import Transicion

class AFD(object):
    def __init__(self, id = -1):
        # Tal vez se puedan usar simples listas en lugar de sets
        self.id = id
        self.edosAFD = set()
        self.edosAceptacion = set()
        self.edoIni = Estado()
        self.transiciones = set()
        # Checar si se necesita una variable para el lexema

    def setId(self, id):
        self.id = id
        return

    def addTransicion(self, char, edo):
        self.transiciones.add(Transicion(char, edo))
        return

    def printAFD(self):
        for edo in self.edosAFD:
            edo.checked = False
        
        q = Cola()
        q.add(self.edoIni)
        while not q.isEmpty():
            edo = q.pop()
            edo.printEdo()
            if not edo.sinTransiciones():
                for trans in edo.transiciones:
                    if not trans.getEdo().isChecked():
                        trans.getEdo().checked = True
                        q.add(trans.getEdo())
        print("Estado inicial de automata: ", self.edoIni.getIdEdo())
        return 
