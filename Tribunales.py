from Colas import *
from Pila import *
from Fuero import *
from Expedientes_Juzgados import *
import numpy as np


class EdificioTribunales: #Nuestro TDA de Eificio De Tribunales
    
    def __init__(self,pisos = 0,oficinas = 0):
        self.pisos= pisos
        self.oficinas=oficinas
        self.edificio = np.empty((pisos,oficinas),Juzgados)


    def __repr__(self):
        return str(self.edificio)
    
    def getPiso(self):
        return self.pisos
    
    def getOficinasPorPiso(self): #devuelve la cantidad de oficinas por piso
        return self.oficinas
    
    def getJuzgado(self,piso,oficina):
        return self.edificio[piso][oficina]
    
    
    def establecerJuzgado(self,piso,oficina,juzgado): #establece juzgado en piso y oficina , indicando el juzgado. Lo agrega en la posicion dada
        self.edificio[piso][oficina] = juzgado

    def oficinaVacia(self,piso,oficina):
        return self.edificio[piso][oficina] == None
    
    def cantExpUrgPorOficina(self,piso,oficina): #funcion accesoria que retorna la cantidad de expedientes urgentes segun el piso y la oficina por parámetro
        return self.edificio[piso][oficina].cantidadDeExpedientesUrgentes()
    
    def esJuez(self,piso, oficina, nombre): #funcion accesoria para consultar si en la posicion dada se encuentra el juez que viene por parametro
        return self.edificio[piso][oficina].getNombreJuez() == nombre  
        
    
    #esta operacion debía ser recursiva, pero no logramos resolverla de esa manera, de todas maneras lo hicimos de forma iterativa
    def cantidadDeJuzgadosCriticos(self,piso):
        
        cantJuzgadosCriticos=0
        
        for i in range(self.getOficinasPorPiso()): #recorremos las oficinas del piso
            if not self.oficinaVacia(piso,i): #si la oficina no esta vacia (quedando piso fijo por parametro y cambiando i cada ves que entra al for)
               if self.edificio[piso][i].esCritico(): #consulta en esas coordenadas (juzgado-oficina) si el mismo es critico
                   cantJuzgadosCriticos+=1 # si lo es agrega 1 a la variable, por cada vez que un juzgado esta en estado critico
                   
        return cantJuzgadosCriticos #retorna la cantidad de juzgados criticos en ese piso
            
    #a partir de este punto nos damos cuenta que usamos los "for" para recorrer eledificio (matriz) y repetimos el codigo en cada una de las funciones siguiente, pero 
    #no supimos como hacer para crear una funcion que realize esto y sea llamada desde cada una de las funciones siguientes ¿Es posible crear una función que recorra el edificio
    #y que sea llamada cada vez que se necesita?

    def buscaJuzgado(self,juez): #nuestra funcion de busqueda de juzgadoa partir del nombre del juez.

        auxPiso=None
        auxOficina=None

        for piso in range(len(self.edificio)): # recorremos la matriz por piso y oficina
            for oficina in range(len(self.edificio[0])):

                if not self.oficinaVacia(piso,oficina): # nos aseguramos que la oficina no esta vacia en la posicion dada
                    if self.esJuez(piso,oficina,juez): #si la oficina no esta vacia comparamos con el nombre del juez que pasamos por parametro (self.edificio[piso][oficina].nombreJuez == juez)
                        auxPiso = [piso] #si lo encuentra, guarda las posiciones en variables auxiliares
                        auxOficina = [oficina]
                
        return auxPiso, auxOficina #retorna las variables con las posiciones del juez encontrado
      
    
    def juzgadoMenosRecargado(self): #nuestra funcion de juzgado menos recargado
        cantidadDeUrgentesMinima = 99999999 #lo inicializamos en un numero grande porque supimos como hacer que la primera vez que se ejecute tome el primer valor
        auxPiso = None
        auxOficina = None

        for piso in range(len(self.edificio)):#recorremos el edificio(matriz)
            for oficina in range(len(self.edificio[0])): 
                if not self.oficinaVacia(piso,oficina): #si la oficina no esta vacia
                    if cantidadDeUrgentesMinima > self.cantExpUrgPorOficina(piso,oficina): #y la cantidad guardada en la variable es mayor a la cantidad de urgentes obtenida en ese piso
                        cantidadDeUrgentesMinima = self.cantExpUrgPorOficina(piso, oficina) # esa cantidad obtenida es el nuevo minimo
                        auxPiso = [piso] #guardando la ubicacion en las variables para luego retornarla
                        auxOficina = [oficina]
                        

        return auxPiso, auxOficina #retorna la posicion del juzgado menos recargado


    def mesaDeEntradas(self,pilaExpedientes,juez): #funcion de mesa de entrada (incompleta)
        
        expedienteARecibir = None
        
        for piso in range(len(self.edificio)):  #se recorre el edificio (matriz)
            for oficina in range(len(self.edificio[0])):
                if not self.oficinaVacia(piso,oficina): #si la oficina no está vacia
                    if self.esJuez(piso,oficina,juez):#si es el juez que le indicamos por parametro (#anterior self.edificio[piso][oficina].nombreJuez == juez)
                        while not pilaExpedientes.estaVacia(): # mientras la pila de expedientes no esté vacia
                            expedienteARecibir = pilaExpedientes.desapilarElemento() #lo desapilamos y lo guardamos en una variable
                            self.edificio[piso][oficina].recibirExpediente(expedienteARecibir) # y lo vamos recibiendo en la posicion donde se encontró el juez de turno


    def moverExpediente(self,nroExp,juezOrigen,juezDestino): #funcion de mover expediente
        
        expAMover = None
        
        for piso in range(len(self.edificio)): #se recorre el edificio (matriz)
            for oficina in range(len(self.edificio[0])):
                if not self.oficinaVacia(piso,oficina): #si la oficina no esta vacia
                    if self.esJuez(piso,oficina,juezOrigen): #y coincide con el juez de origen #anterior self.edificio[piso][oficina].nombreJuez == juezOrigen:
                        expAMover = self.edificio[piso][oficina].buscarExpediente(nroExp) #invocamos a la funcion de busqueda de expediente para luego el resultado se guarde en una variable auxiliar
                        self.edificio[piso][oficina].eliminarExpediente(nroExp) #eliminamos el expediente encontrado de donde fue hallado 
                        
        
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[0])):
                if not self.oficinaVacia(piso,oficina):
                    if self.esJuez(piso,oficina,juezDestino):#si coincide con el juez destino.. (anterior self.edificio[piso][oficina].nombreJuez == juezDestino:)
                        self.edificio[piso][oficina].recibirExpediente(expAMover) #la oficina del juez destino recibe el expediente anteriormente encontrado y que estaba guardado en la variable auxiliar
                        
                        
        
        
        
        
    
    

        
    
   





