from Estado import Estado
from Transicion import Transicion
from Cola import Cola

class Subconjunto(object):
    def __init__(self, c="Epsilon"):
        self.idS = -1
        self.simb = c
        #self.subEstados = []
        self.subEstados = set()
        self.edos = []
        self.clearSub()

    def getSimb(self):
        return self.simb

    def setIdS(self, id):
        self.idS = id
        return

    def clearSub(self):
        self.edos.clear()
        self.subEstados.clear()
        return

    def addSubEstados(self, edo):
        self.subEstados.add(edo)
        return

    def addEdo(self, edo):
        self.edos.append(edo)
        return

    def isRepeated(self, edos):
        return self.subEstados == edos

    def printEdos(self):
        print (self.edos)
        return

    def printSubconjunto(self):
        print("Subconjunto S", self.idS, "con transicion: ", self.simb)
        print("SubEstados: ")
        for sub in self.subEstados:
            print(sub.getIdEdo())
        
        print("Estados en el subconjunto: ")
        for edo in self.edos:
            print("Estado: ", edo.getIdEdo())