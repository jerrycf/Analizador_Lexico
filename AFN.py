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
        # S = Subconjunto(simb)
        return 

    def toAFD(self):
        # Se checan todas las transiciones con Epsilon en el estado inicial
        # y se agregan a la cola para evaluarlos después
        print("Funcion para convertir el AFN general a AFD")
        subconjuntos = [] # Donde se guardan los subconjuntos para generar el AFD final
        alfabetoActual = set()
        A = Cola() # Cola para evaluar los subconjuntos 
        simbActual = 'Epsilon'
        cont = 0
        S = Subconjunto(cont)
        S.addSubEstados(self.edoIni)
        # Se agregan a una cola todos los estados que transiciona el estado inicial
        for tran in self.edoIni.transiciones:
            print("Transicion desde el edoIni para AFD: ", tran.getEdo().getIdEdo())
            A.add(tran.getEdo())
            S.addEdo(tran.getEdo())
            # print("edoIni -> ", tran.getEdo().getIdEdo())
        SEdoIni = Estado(cont)
        # Se recorre la cola para buscar todas las transiciones de epsilon
        while not A.isEmpty():
            #edo = A.pop()
            S = A.pop()
            print("edoIni -> ", S.getIdEdo())
            for tran in S.transiciones:
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
                        Snew = Subconjunto()
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

    def toAFD2(self):
        # simbActual = 'Epsilon'
        subconjuntos = [] # Aqui se guardan los subconjuntos finales para crear el AFD
        inQ = Cola() # Cola para ir evaluando los estados que se van encontrando
        A = Cola() # Cola de los subconjuntos que se deben de analizar.
        subConTemp = []
        alfabetoAct = set() # Alfabeto momentario para saber si ya se ha encontrado un mismo símbolo antes
        cont = 0
        # Se crea una instancia de subconjunto para empezar la busqueda.
        S = Subconjunto(cont)
        cont += 1
        S.addSubEstados(self.edoIni) # Se agrega el estado inicial para 
        # poder después empezar a realizar las busquedas con Epsilon y otros símbolos
        S.setSimb('Epsilon')
        subconjuntos.append(S)
        A.add(S)
        print("Empieza la cola con el estado inicial.")
        # Evaular todos los subconjuntos pendientes en la Cola A 
        while not A.isEmpty():
            S = A.pop()
            print("Empezando a evaluar S", S.getIdS())
            alfabetoAct.clear()
            for subEdo in S.subEstados:
                print("SubEstado de S", S.getIdS(), ": ", subEdo.getIdEdo())
                self.resetChecked()
                inQ.add(subEdo)
                # Se realiza la busqueda de las transiciones Epsilon y otros símbolos de este estado
                while not inQ.isEmpty():
                    edo = inQ.pop()
                    if not edo.isChecked():
                        # Se marca el estado como visitado.
                        edo.checked = True
                        # Se agrega al arreglo de estados del subconjunto.
                        S.addEdo(edo)

                        for estado in self.edosAceptacion:
                            if estado == edo:
                                S.setToken(edo.getToken())
                        # Se recorren las transiciones del estado actual.
                        for trans in edo.transiciones:
                            # Checar si es una transicion Epsilon o de un nuevo simbolo.
                            if trans.simb == 'Epsilon':
                                inQ.add(trans.getEdo())
                                print("Edo agregado a inQ para evaluar después: ", trans.getEdo().getIdEdo())
                            else: # Si no es Epsilon, se debe de agregar un nuevo subconjunto
                                # checando que el estado a agregar no haya sido evaluado antes.
                                # Si se encuentra un simbolo repetido, se debe de agregar el estado
                                # al set subEstados del subconjunto que pertenece dicho símbolo.
                                print("Nuevo simbolo a evaluar: ", trans.simb)
                                if trans.simb in alfabetoAct:
                                    # Simbolo ya encontrado, se le agrega un subestado a su subconjunto correspondiente.
                                    for subc in subconjuntos:
                                        if subc.getSimb() == trans.simb:
                                            subc.addSubEstados(trans.getEdo())
                                            break
                                else:
                                    # Simbolo nuevo, se crea un nuevo subconjunto con este simbolo y se guarda en un arreglo
                                    # para posteriormente evaluarlos en la Cola A.
                                    Snew = Subconjunto(cont)
                                    cont += 1
                                    Snew.setSimb(trans.simb)
                                    Snew.addSubEstados(trans.getEdo())
                                    S.addTransicion(trans.simb, Snew)
                                    subconjuntos.append(Snew)
                                    A.add(Snew)
                for subcon in subconjuntos:                    
                    if subcon.subEstados == S.subEstados:
                        S.addTransicion(subcon.getSimb(), subcon)
                        break
            if cont > 10:
                for subcon in subconjuntos:
                    subcon.printSubconjunto()
                exit(0)
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
