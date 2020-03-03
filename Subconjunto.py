from Estado import Estado
from Transicion import Transicion
from TransicionSubconjunto import TransicionSubconjunto
from Cola import Cola

class Subconjunto(object):
    def __init__(self, id = -1):
        self.idS = id
        self.simb = 'Epsilon'
        # self.subEstados = []
        self.subEstados = set()
        self.edos = []
        self.transiciones = []
        self.clearSub()
        self.token = -1

    def getSimb(self):
        return self.simb

    def setSimb(self, c):
        self.simb = c
        return

    def setIdS(self, id):
        self.idS = id
        return
    
    def getIdS(self):
        return self.idS

    def setToken(self, t):
        self.token = t
        return

    def clearSub(self):
        self.edos.clear()
        self.subEstados.clear()
        self.transiciones.clear()
        return

    def addSubEstados(self, edo):
        self.subEstados.add(edo)
        return

    def addEdo(self, edo):
        self.edos.append(edo)
        return
    
    def addTransicion(self, simb, subc):
        self.transiciones.append(TransicionSubconjunto(simb, subc))
        return

    def isRepeated(self, edos):
        return self.subEstados == edos

    def printEdos(self):
        print (self.edos)
        return

    def printSubconjunto(self):
        print("Subconjunto S", self.idS)
        print("SubEstados: ")
        for sub in self.subEstados:
            print(sub.getIdEdo())
        
        print("Estados en el subconjunto: ")
        for edo in self.edos:
            print("Estado: ", edo.getIdEdo())