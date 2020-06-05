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
       
    def recorrerEdificio(self):
        pisoAux = None
        oficinaAux = None
        
        for piso in range(len(self.edificio)):
            pisoAux = piso
            for oficina in range(len(self.edificio[0])):
                oficinaAux = oficina 
                
        
    
    #esta operacion debía ser recursiva, pero no logramos resolverla, de todas maneras lo hicimos de forma iterativa
    def cantidadDeJuzgadosCriticos(self,piso):
        
        cantJuzgadosCriticos=0
        
        for i in range(self.getOficinasPorPiso()): #recorremos las oficinas del piso
            if not self.oficinaVacia(piso,i): #si la oficina no esta vacia (quedando piso fijo por parametro y cambiando i cada ves que entra al for)
               if self.edificio[piso][i].esCritico(): #consulta en esas coordenadas (juzgado-oficina) si el mismo es critico
                   cantJuzgadosCriticos+=1 # si lo es agrega 1 a la variable, por cada vez que un juzgado esta en estado critico
                   
        return cantJuzgadosCriticos #retorna la cantidad de juzgados criticos en ese piso
            
    

    def buscaJuzgado(self,juez):

        auxPiso=None
        auxOficina=None

        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[0])):

                if not self.oficinaVacia(piso,oficina):
                    if self.edificio[piso][oficina].nombreJuez == juez:
                        
                        auxPiso = [piso]
                        auxOficina = [oficina]
                
        return auxPiso, auxOficina 

    
    
    def juzgadoMenosRecargado(self):
        cantidadDeUrgentesMinima = 99999999
        auxPiso = None
        auxOficina = None

        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[0])): 
                if not self.oficinaVacia(piso,oficina):
                    if cantidadDeUrgentesMinima > self.cantExpUrgPorOficina(piso,oficina):
                        cantidadDeUrgentesMinima = self.cantExpUrgPorOficina(piso, oficina)
                        auxPiso = [piso]
                        auxOficina = [oficina]
                        

        return auxPiso, auxOficina
    
    
    
    def mesaDeEntradas(self,pilaExpedientes,juez):
        
        expedienteARecibir = None
        
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[0])):
                if not self.oficinaVacia(piso,oficina):
                    if self.edificio[piso][oficina].nombreJuez == juez:
                        while not pilaExpedientes.estaVacia():
                            expedienteARecibir = pilaExpedientes.desapilarElemento()
                            self.edificio[piso][oficina].recibirExpediente(expedienteARecibir)
    
    
    
    
    
    
    def moverExpediente(self,nroExp,juezOrigen,juezDestino):
        
        expAMover = None
        
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[0])):
                if not self.oficinaVacia(piso,oficina):
                    if self.edificio[piso][oficina].nombreJuez == juezOrigen:
                        expAMover = self.edificio[piso][oficina].buscarExpediente(nroExp)
                        self.edificio[piso][oficina].eliminarExpediente(nroExp)
                        
        
        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[0])):
                if not self.oficinaVacia(piso,oficina):
                    if self.edificio[piso][oficina].nombreJuez == juezDestino:
                        self.edificio[piso][oficina].recibirExpediente(expAMover)
                        
                        
        
        
        
        
    
    

        
    
   





