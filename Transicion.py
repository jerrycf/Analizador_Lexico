#from Estado import Estado
class Transicion(object):
    def __init__(self, simb, edo):
        self.simb = simb
        self.edo = edo
    
    def getTrans(self):
        return self.simb
    
    def getEdo(self):
        return self.edo

    def setTrans(self, c):
        self.simb = c
    
    def setEdo(self, edo):
        self.edo = edo

    def isEpsilon(self):
        if self.simb == 'Epsilon':  
            return True
        return False
    
    def printTransicion(self):
        print ("con ", self.simb, " a ", self.edo.getIdEdo(), "\n")