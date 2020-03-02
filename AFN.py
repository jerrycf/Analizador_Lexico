from Estado import Estado
from Transicion import Transicion
from Cola import Cola
from Subconjunto import Subconjunto
class AFN(object):
    def __init__(self, c="Epsilon"):
        self.alfabeto = set()
        self.edosAceptacion = set()
        self.edosAFN = set()        
        self.cleanAFN() # Funcion para vaciar todos los sets y dejar el edoIni como null
        self.idCont = 0 # Contador específico para poner los ids de cada estado en el AFN
        self.edoIni = Estado()
        '''if c == None:
            self.edoIni = None
        else:
            '''   
        # Se instancia un estado final ef
        ef = Estado()
        ef.setAceptacion(True)
        # Se instancia un estado inicial
        self.edoIni.setInicial(True)
        # Se agrega la transicion del estado inicial al estado final
        self.edoIni.addTransicion(c, ef)
        # Se agregan los estados en sus respectivos sets
        self.edosAceptacion.add(ef)
        self.edosAFN.add(self.edoIni)
        self.edosAFN.add(ef)
        self.alfabeto.add(c)
    
    def cleanAFN(self):
        self.edosAFN.clear()
        self.edosAceptacion.clear()
        self.alfabeto.clear()
        self.edoIni = None
        return

    def resetIdCont(self):
        self.idCont = 1
        return

    def resetChecked(self):
        for edo in self.edosAFN:
            edo.checked = False
        return

    def setIds(self): 
        ''' Problema al poner los ids de un estado cuando 2 estados anteriores 
        apuntan a un mismo estado, incrementa doble debido a que dos 
        estados repiten el procedimiento.
        '''
        for edos in self.edosAFN:
            edos.checked = False
        
        q = Cola()
        q.add(self.edoIni)
        cont = 0
        while not q.isEmpty():
            estado = q.pop()
            estado.setIdEdo(cont)
            cont += 1
            if not estado.transiciones == []:
                for trans in estado.transiciones:
                    if not trans.getEdo().isChecked():
                        trans.getEdo().checked = True
                        q.add(trans.getEdo())
        return

    def setIdsProfundidad(self, edo):
        if not edo.isChecked():
            edo.setIdEdo(self.idCont)
            self.idCont += 1
            edo.checked = True
            for e in edo.transiciones:
                self.setIdsProfundidad(e.getEdo())
        return
    
    def isEmpty(self):
        return self.edosAFN == set()
    
    def AFNbasico(self, c):
        e1 = Estado()
        e2 = Estado()
        e1.setInicial(True)
        e2.setAceptacion(True)
        e1.addTransicion(c, e2)
        self.alfabeto = self.alfabeto.union(c)
        self.edoIni = e1
        self.edosAceptacion.clear()
        self.edosAceptacion.add(e2)
        self.edosAFN.clear()
        self.edosAFN.add(e1)
        self.edosAFN.add(e2)

        return self

    def cerr_pos(self):
        ei = Estado()
        ef = Estado()
        ei.setInicial(True)
        ef.setAceptacion(False)
        for edo in self.edosAceptacion:
            edo.setAceptacion(False)
            edo.addTransicion("Epsilon", ef)
            edo.addTransicion("Epsilon", self.edoIni)
        
        self.edoIni.setInicial(False)
        ei.addTransicion("Epsilon", self.edoIni)
        self.edosAceptacion.clear()
        self.edosAceptacion.add(ef)
        self.edosAFN.add(ei)
        self.edosAFN.add(ef)
        self.edoIni = ei
        print("Automata con cerradura positiva finalizado")
        return

    def cerr_kleen(self):
        ei = Estado()
        ef = Estado()
        ei.setInicial(True)
        ef.setAceptacion(False)
        for edo in self.edosAceptacion:
            edo.setAceptacion(False)
            edo.addTransicion("Epsilon", ef)
            edo.addTransicion("Epsilon", self.edoIni)
        
        self.edoIni.setInicial(False)
        ei.addTransicion("Epsilon", self.edoIni)
        ei.addTransicion("Epsilon", ef)
        self.edosAceptacion.clear()
        self.edosAceptacion.add(ef)
        self.edosAFN.add(ei)
        self.edosAFN.add(ef)
        self.edoIni = ei
        print("Automata con cerradura Kleen finalizado")
        return
    
    def cerr_opc(self):
        ei = Estado()
        ef = Estado()
        ei.setInicial(True)
        ef.setAceptacion(False)
        for edo in self.edosAceptacion:
            edo.setAceptacion(False)
            edo.addTransicion("Epsilon", ef)
        
        self.edoIni.setInicial(False)
        ei.addTransicion("Epsilon", self.edoIni)
        ei.addTransicion("Epsilon", ef)
        self.edosAceptacion.clear()
        self.edosAceptacion.add(ef)
        self.edosAFN.add(ei)
        self.edosAFN.add(ef)
        self.edoIni = ei
        print("Automata con cerradura Kleen finalizado")
        return

    def unirAFN(self, f2):
        # Checar los edos iniciales de cada automata, se mantienen como true
        e1 = Estado()
        e2 = Estado()
        self.edoIni.setAceptacion(False)
        f2.edoIni.setAceptacion(False)

        e1.addTransicion("Epsilon", self.edoIni)
        e1.addTransicion("Epsilon", f2.edoIni)

        for e in self.edosAceptacion:
            e.addTransicion("Epsilon", e2)
            e.setAceptacion(False)
        
        for e in f2.edosAceptacion:
            e.addTransicion("Epsilon", e2)
            e.setAceptacion(False)

        e2.setAceptacion(True)
        self.alfabeto = self.alfabeto.union(f2.alfabeto)
        self.edosAFN = self.edosAFN.union(f2.edosAFN)
        self.edosAFN.add(e1)
        self.edosAFN.add(e2)
        self.edosAceptacion.clear()
        self.edosAceptacion.add(e2)
        self.edoIni = e1
        f2 = None
        return self
    
    def concatenar(self, f2):
        for e in self.edosAceptacion:
            e.transiciones = e.transiciones.union(f2.edoIni.transiciones)
            e.setAceptacion(False)

        f2.edoIni.transiciones.clear()
        self.alfabeto = self.alfabeto.union(f2.alfabeto)
        self.edosAceptacion.clear()
        self.edosAceptacion = self.edosAceptacion.union(f2.edosAceptacion)
        self.edosAFN = self.edosAFN.union(f2.edosAFN)
        self.edosAFN.remove(f2.edoIni)
        f2 = None
        return self
    
    def creaSubconjunto(self, simb):
        print("Funcion para recorrer los estados con el simbolo dado para crear un subconjunto")
        S = Subconjunto(simb)
        return S

    def toAFD(self):
        # Se checan todas las transiciones con Epsilon en el estado inicial
        # y se agregan a la cola para evaluarlos después
        print("Funcion para convertir el AFN general a AFD")
        subconjuntos = [] # Donde se guardan los subconjuntos
        alfabetoActual = set()
        A = Cola()
        simbActual = 'Epsilon'
        print("EdoIni: ", self.edoIni.getIdEdo())
        
        S = Subconjunto()
        cont = 0
        S.setIdS(cont)
        S.addSubEstados(self.edoIni)
        # Se agregan a una cola todos los estados que transiciona el estado inicial
        for tran in self.edoIni.transiciones:
            print("Transicion desde el edoIni para AFD: ", tran.getEdo().getIdEdo())
            A.add(tran.getEdo())
            S.addEdo(tran.getEdo())
            #print("edoIni -> ", tran.getEdo().getIdEdo())
        SEdoIni = Estado(cont)
        # Se recorre la cola para buscar todas las transiciones de epsilon
        while not A.isEmpty():
            edo = A.pop()
            print("edoIni -> ", edo.getIdEdo())
            for tran in edo.transiciones:
                # Hay que marcar los estados, si no se puede llegar a ciclar o agregar 
                # subconjuntos repetidos 
                if tran.simb == simbActual or tran.simb == 'Epsilon':
                    # Se sigue la transicion del simbolo actual, se agrega el estado al que apunta a la cola
                    A.add(tran.getEdo())
                    S.addEdo(tran.getEdo())
                else:
                    # Checar si el estado no ha sido analizado antes
                    # Se encontró un nuevo símbolo, se debe de crear un nuevo subconjunto con dicho símbolo
                    # si es que ese símbolo no ha sido agregado antes.
                    if tran.simb not in alfabetoActual:
                        alfabetoActual.add(tran.simb)
                        # crear una instancia de subconjunto por cada nuevo símbolo que se encuentra
                        Snew = Subconjunto(tran.simb)
                        Snew.setIdS(cont)
                        Snew.addSubEstados(tran.getEdo())
                        subconjuntos.append(Snew)
                        # Crear un estado para representar el nuevo subconjunto creado
                        Sedo = Estado(cont)
                        cont += 1
                        SEdoIni.addTransicion(tran.simb, Sedo)
                    else:
                        print("Simbolo ", simbActual, " ya encontrado")
                        # *Buscar en el arreglo de subconjuntos el correspondiente 
                        # para agregarle el estado en subEstados
                        for subconjunto in subconjuntos:
                            if subconjunto.getSimb() == simbActual:
                                subconjunto.addSubEstados(tran.getEdo())
        # *Crear un estado para representar S0
        subconjuntos.insert(0, S)
        for subconjunto in subconjuntos: 
            subconjunto.printSubconjunto()


        # subconjuntos.append(S)
        print("Simbolos encontrados: ", alfabetoActual)
        
        
        return

    def printAFN(self):
        for edos in self.edosAFN:
            edos.checked = False
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

        print("Estados de aceptación de automata: ")
        for accepts in self.edosAceptacion:
            print(accepts.getIdEdo())
        
        print("Total Estados: ", len(self.edosAFN))
        return

    def printProfundidad(self, edo):
        if not edo.isChecked():
            edo.printEdo()
            edo.checked = True
            for e in edo.transiciones:
                self.printProfundidad(e.getEdo())
        return
