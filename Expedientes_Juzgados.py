from Colas import *
from Pila import *
from Fuero import *

class Expediente :
    
    def __init__(self, nroExp = 0 ,fuero = Fuero, prioridad = Prioridad ,estado = Estado):
        self.nroExp = nroExp
        self.fuero = fuero
        self.prioridad = prioridad
        self.estado = estado

    def __repr__(self):
        printeo = "|| Nro Exp: " + str(self.nroExp) + "| tipo: " + str(self.fuero.name) + "| prioridad: " + str(self.prioridad.name) + "| estado: "+ str(self.estado.name) + " || "
        return printeo
    

    def esNormal(self):
        return self.prioridad == 0


    def esUrgente(self):
        return self.prioridad == 1

    def esDeEstado(self,tipo):
        return self.estado == tipo
    
    def getNroExp(self) :
        return self.nroExp

    def esNumeroExp(self,num):
        return self.nroExp == num

class Juzgados:
    
    def __init__(self, nombreJuez = None):
        self.colaUrgente = Colas()
        self.colaNormal = Colas()
        self.nombreJuez = nombreJuez
        
   
    def __repr__(self):
        printeo= "Juez: " + str(self.nombreJuez)+ "|" + " URGENTES: "+ str(self.colaUrgente) + " NORMALES: " + str(self.colaNormal)
        return printeo
    
   
    def recibirExpediente(self,exp):
        if exp.prioridad == 0:
            self.colaNormal.encolar(exp)
        elif exp.prioridad ==1:
            self.colaUrgente.encolar(exp)
 

    def primerExpedienteATratar(self):
        dato=None
        if not self.colaUrgente.estaVacia():
            dato=self.colaUrgente.primerElementoFila()
        else:
            dato=self.colaNormal.primerElementoFila()
        return dato
    
    
    
    def tratarExpediente(self):
        aux = None
        if not self.colaUrgente.estaVacia():
            aux = self.colaUrgente.desencolar()
        else:
            aux = self.colaNormal.desencolar()
        return aux    
   
    
    def cantidadTotalExpedientes(self):
        return self.colaNormal.tamanioCola() + self.colaUrgente.tamanioCola()
    
       
    def expedientesPorTipo(self):
        return "cantidad exp cola normal: ", self.colaNormal.tamanioCola(), " cantidad exp cola urgentes: ", self.colaUrgente.tamanioCola()
                
   
    
    def esCritico(self):
        return self.colaNormal.tamanioCola()>=50 or self.colaUrgente.tamanioCola() >= 50 
   

    def enJuicio(self):
        colaEnJuicio = Colas()
        todos = Colas()
        todos = self.colaUrgente.clonarCola()
        colaEstadoNormal = Colas()
        colaEstadoNormal = self.colaNormal.clonarCola()
    
        while not colaEstadoNormal.estaVacia():
            todos.encolar(colaEstadoNormal.desencolar())

        while not todos.estaVacia():
            if todos.primerElementoFila().esDeEstado(Estado.Juicio):
                colaEnJuicio.encolar(todos.desencolar())
            else:
                todos.desencolar()

        return colaEnJuicio.tamanioCola()

    
                

    def buscarExpediente(self,nroExpBuscado):
        expedienteBuscado = None
        todos = Colas()
        todos = self.colaUrgente.clonarCola()
        colaEstadoNormal = Colas()
        colaEstadoNormal = self.colaNormal.clonarCola()
        

        while not colaEstadoNormal.estaVacia():
            todos.encolar(colaEstadoNormal.desencolar())
        
        while not todos.estaVacia() and expedienteBuscado == None:
            if todos.primerElementoFila().esNumeroExp(nroExpBuscado):
                expedienteBuscado = todos.primerElementoFila()
            else:
                todos.desencolar()
        
        return expedienteBuscado
        
    
    # def eliminarExpediente(self,nroExp):

    #     colaAuxUrgente = Colas()
    #     colaAuxUrgente = self.colaUrgente.clonarCola()
    #     colaAuxNormal = Colas()
    #     colaAuxNormal = self.colaNormal.clonarCola()


    #     if self.buscarExpediente(nroExp).nroExp == nroExp :

        


                     
            
    # def cambiaDeEstado(self,nroExp):
         
    #      aux = None
         
    #      if self.buscarExpediente(nroExp).nroExp == nroExp:
    #          aux = self.buscarExpediente(nroExp)
    #          if self.buscarExpediente(nroExp).prioridad == "urgente":
    #              self.eliminarExpediente(nroExp)
    #              aux.prioridad = "normal"
    #              self.recibirExpediente(aux)
    #          else:
    #              self.eliminarExpediente(nroExp)
    #              aux.prioridad = "urgente"
    #              self.recibirExpediente(aux)