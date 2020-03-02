from Estado import Estado
from Cola import Cola
from Transicion import Transicion

class AFD(object):
    def __init__(self):
        # Tal vez se puedan usar simples listas en lugar de sets
        self.edosAFD = set()
        self.edosAceptacion = set()
        self.edoIni = Estado()
        # Checar si se necesita una variable para el lexema
        
        
