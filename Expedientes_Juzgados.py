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

    
                

    def buscarExpediente(self,nroExp):
        expendienteBuscado = None
        for elementos in self.colaNormal:
            if elementos.nroExp == nroExp:
                expendienteBuscado = elementos
        for elementos in self.colaUrgente :
            if elementos.nroExp == nroExp:
                expendienteBuscado = elementos

        return expendienteBuscado
    
    
    
    
    def eliminarExpediente(self,nroExp):

        for elementos in self.colaNormal:
            if elementos.nroExp == nroExp:
                self.colaNormal.remove(elementos)

        for elementos in self.colaUrgente:
            if elementos.nroExp == nroExp:
                self.colaUrgente.remove(elementos)
    


#    def cambiaDeEstado(self,nroExp):
#            if self.buscarExpediente(nroExp) == nroExp :
#                if self.estado=="normal":
#                    self.estado = "urgente"
#                    self.colaUrgente.recibirExpediente(nroExp)
#                    self.colaNormal.eliminarExpediente(nroExp)
#                elif self.estado == "urgente":
#                    self.estado="normal"
#                    self.colaUrgente.recibirExpediente(nroExp)
#                    self.colaNormal.eliminarExpediente(nroExp)
#                else:
#                    Exception("El elemento no se encuentra en la cola")
                
                
                
#    def cambiaDeEstado(self,nroExp):
#        
#        aux = []
#        
#        for elementos in self.colaNormal:
#            if elementos.nroExp == nroExp:
#                elementos.prioridad = "urgente"
#                aux.append(elementos)
#                self.colaNormal.remove(elementos)
#                self.colaUrgente.append(aux)
#            
#        for elementos in self.colaUrgente:
#            if elementos.nroExp == nroExp:
#                elementos.prioridad = "normal"
#                aux.append(elementos)
#                self.colaUrgente.remove(elementos)
#                self.colaNormal.append(aux)
                     
            
    def cambiaDeEstado(self,nroExp):
         
         aux = None
         
         if self.buscarExpediente(nroExp).nroExp == nroExp:
             aux = self.buscarExpediente(nroExp)
             if self.buscarExpediente(nroExp).prioridad == "urgente":
                 self.eliminarExpediente(nroExp)
                 aux.prioridad = "normal"
                 self.recibirExpediente(aux)
             else:
                 self.eliminarExpediente(nroExp)
                 aux.prioridad = "urgente"
                 self.recibirExpediente(aux)