class TransicionSubconjunto(object):
    def __init__(self, simb, subc):
        self.simb = simb
        self.subconjunto = subc
    
    def getSimb(self):
        return self.simb
    
    def getSubconjunto(self):
        return self.subconjunto

    def setSimb(self, c):
        self.simb = c
    
    def setSubconjunto(self, subc):
        self.subconjunto = subc

    def isEpsilon(self):
        if self.simb == 'Epsilon':  
            return True
        return False
    
    def printTransicion(self):
        print ("con ", self.simb, " a ", self.subconjunto.getIdS(), "\n")