from Colas import *
from Pila import *
from Fuero import *

class Expediente : #nuestro TDA Expediente
    
    def __init__(self, nroExp = 0 ,fuero = Fuero, prioridad = Prioridad ,estado = Estado):
        self.nroExp = nroExp
        self.fuero = fuero
        self.prioridad = prioridad
        self.estado = estado

    def __repr__(self):
        aux = "|| Nro Exp: " + str(self.nroExp) + "| tipo: " + str(self.fuero.name) + "| prioridad: " + str(self.prioridad.name) + "| estado: "+ str(self.estado.name) + " || "
        return aux
    

    def esDeEstado(self,tipo): # devuelve true o false si el Expediente es del estado que se le pasa por parametro
        return self.estado == tipo
    
    def getNroExp(self) :
        return self.nroExp

    def esNumeroExp(self,num): #devuelve true o false si el Expediente es nro de expediente que que se pasa por parametro
        return self.nroExp == num

    def setPrioridad(self,tipo):
        self.prioridad = tipo

    def getPrioridad(self):
        return self.prioridad

    def esDePrioridad(self,num):  #devuelve true o false si el Expediente es de la prioridad que se pasa por parametro
        return self.prioridad == num
    
    def esNormal(self):
        return self.esDePrioridad(0)

    def esUrgente(self):
        return self.esDePrioridad(1)



class Juzgados: # Nuestro TDA de Juzgado
    
    def __init__(self, nombreJuez = None, cantidad= 2): #se puede setear la cantidad critica de expedientes
        self.colaUrgente = Colas()
        self.colaNormal = Colas()
        self.cantidadCritica = cantidad 
        self.nombreJuez = nombreJuez
        
   
    def __repr__(self):
        printeo= "Juez: " + str(self.nombreJuez)+ "|" + " URGENTES: "+ str(self.colaUrgente) + " NORMALES: " + str(self.colaNormal)
        return printeo
    
   
    def recibirExpediente(self,exp): # recibe el expediente y lo encola en la cola correspondiente
        if exp.esNormal() :         #segun si es normal o si es urgente, usando la función encolar de las colas de expedientes
            self.colaNormal.encolar(exp) 
        elif exp.esUrgente():     
            self.colaUrgente.encolar(exp)
 

    def primerExpedienteATratar(self):
        dato=None
        if not self.colaUrgente.estaVacia(): #usando una funcion accesoria de las colas, si la cola de urgentes no 
            dato=self.colaUrgente.primerElementoFila() #está vacia retorna sin desencolar el primer elemento a ser tratado de la de urgentes (que tiene prioridad)
        else:
            dato=self.colaNormal.primerElementoFila()#caso contrario , toma el primero de la cola de los normales
        return dato
    
    
    
    def tratarExpediente(self): # parecida a la funcion anterior, pero en este caso desencola el expediente de la cola urgentes (que es prioridad)
        aux = None                              #si no esta vacia, caso contrario, desencola de la cola con estado normal.
        if not self.colaUrgente.estaVacia():
            aux = self.colaUrgente.desencolar()
        else:
            aux = self.colaNormal.desencolar()
        return aux    
   
    
    def cantidadTotalExpedientes(self): #cantidad total de expedientes sumadando las dos colas
        return self.colaNormal.tamanioCola() + self.colaUrgente.tamanioCola()
    
       
    def expedientesPorTipo(self): #retorna la cantidad de expedientes por tipo de cada una de las colas (urgentes,normales)
        return "cantidad exp cola normal: ", self.colaNormal.tamanioCola(), " cantidad exp cola urgentes: ", self.colaUrgente.tamanioCola()
                
    def cantidadDeExpedientesUrgentes(self): #retorna solo la cantidad e expedientes urgentes
        return self.colaUrgente.tamanioCola()
    
    def esCritico(self): #retorna si un juzgado es critico
        return self.colaNormal.tamanioCola()>= self.cantidadCritica or self.colaUrgente.tamanioCola() >= self.cantidadCritica 
   

    def enJuicio(self):
        colaEnJuicio = Colas()
        todos = Colas()
        todos = self.colaUrgente.clonarCola() #clonamos el contenido de la cola urgente dentro de la cola auxiliar "todos"
        colaEstadoNormal = Colas()
        colaEstadoNormal = self.colaNormal.clonarCola()
    
        while not colaEstadoNormal.estaVacia(): #mientras la cola normal no esta vacia desencola todos y los encola en una cola auxiliar donde estan todos
            todos.encolar(colaEstadoNormal.desencolar())

        while not todos.estaVacia(): #mientras la cola "todos" (donde ahora estan los expedientes de ambas) no este vacia la recorremos
            if todos.primerElementoFila().esDeEstado(Estado.Juicio): #le pregunta al primer elemento de la cola si es de estado "en juicio"
                colaEnJuicio.encolar(todos.desencolar()) #si se cumple, lo desencola de la cola "todos " y lo guarda en la auxiliar "colaEnJuicio"
            else:
                todos.desencolar() #si no se cumple, desencola ese primer elemento para volver a entrar al bucle y volver a preguntar si el
                                    #primer elemento esta "en juicio"
        return colaEnJuicio.tamanioCola() #por ultimo retorna la cantidad total de expedientes que estan en juicio

    def buscarExpediente(self,nroExpBuscado):
        expedienteBuscado = None
        todos = Colas()
        todos = self.colaUrgente.clonarCola() #clonamos la cola de urgentes en "todos" nuevamente
        colaEstadoNormal = Colas()
        colaEstadoNormal = self.colaNormal.clonarCola()
        

        while not colaEstadoNormal.estaVacia(): #mientras la cola normal no esta vacia desencola todos y los encola en una cola auxiliar donde estan todos
            todos.encolar(colaEstadoNormal.desencolar())
        
        while not todos.estaVacia() and expedienteBuscado == None: # recorre mientras la cola "todos" , donde estan todos los elementos no este vacia, y el expediente buscado sea None
            if todos.primerElementoFila().esNumeroExp(nroExpBuscado): #pregunta en la cola de "todos" al primer elemento, el numero y si es el mismo que se pasa por parametro
                expedienteBuscado = todos.primerElementoFila() # si coincide lo guarda en la variable
            else:
                todos.desencolar() #caso contrario , lo desencola , para que se pueda preguntar lo anterior al "nuevo" primer elemento
        
        return expedienteBuscado #retorna el elemento buscado


    def eliminarExpediente(self,nroExpAEliminar):

        colaAuxUrgente = Colas()
        colaAuxNormal = Colas()
   
        if self.buscarExpediente(nroExpAEliminar).esDePrioridad(0): #usando una funcion accesoria consultamos si es de prioridad Normal, si se comple
           
            while not self.colaNormal.estaVacia():                                      #mientras la cola normal no se haya vaciado
                if self.colaNormal.primerElementoFila().nroExp == nroExpAEliminar:      #al primer elemento le preguntamos el numero y si coincide con el que queremos eliminar
                    self.colaNormal.desencolar()                                        #lo desencola
                else:
                    colaAuxNormal.encolar(self.colaNormal.desencolar())                 #caso contrario lo desencola de la cola normal y lo coloca temporalmente en una auxiliar
            
            self.colaNormal = colaAuxNormal  #y luego carga el contenido del auxiliar en la cola normal original , esta vez sin el elemento eliminado
        else:

            while not self.colaUrgente.estaVacia(): # realiza los anteriormente descripto de la misma manera , en este caso recorriendo la cola de urgentes.
                if self.colaUrgente.primerElementoFila().nroExp == nroExpAEliminar:
                    self.colaUrgente.desencolar()
                else:
                    colaAuxUrgente.encolar(self.colaUrgente.desencolar())
            
            self.colaUrgente = colaAuxUrgente #y luego carga el contenido del auxiliar en la cola urgnte original , esta vez sin el elemento eliminado


    def cambiaDeEstado(self,nroExpACambiar): 
        aux = None

        if self.buscarExpediente(nroExpACambiar).nroExp == nroExpACambiar: #usando la funcion anterior buscamos el expediente.Le preguntamos numero y si coincide con el que queremos cambiar entra en el condicional
            aux = self.buscarExpediente(nroExpACambiar)

            if self.buscarExpediente(nroExpACambiar).esDePrioridad(0): #volvemos a invocar la funcion buscarExpediente, al resultado le preguntamos si es de la prioridad deseada, y si es de prioridad "normal"
                self.eliminarExpediente(nroExpACambiar) # elimina el expediente usando la funcion "eliminarExpediente"
                aux.setPrioridad(Prioridad.Urgente) #le cambia la prioridad
                self.recibirExpediente(aux) # y lo recibe la cola de "urgentes"
            else:
                self.eliminarExpediente(nroExpACambiar)    #realiza lo antes descripto pero al reves (de urgente a normal)
                aux.setPrioridad(Prioridad.Normal) 
                self.recibirExpediente(aux)
