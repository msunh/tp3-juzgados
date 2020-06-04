from Colas import *
from Pila import *
from Fuero import *
from Expedientes_Juzgados import *
import numpy as np


class EdificioTribunales:
    
    def __init__(self,pisos = 0,oficinas = 0):
        self.pisos= pisos
        self.oficinas=oficinas
        self.edificio = np.empty((pisos,oficinas),Juzgados)


    def __repr__(self):
        return str(self.edificio)
    
    def getPiso(self):
        return self.pisos
    
    def getOficina(self):
        return self.oficinas
    
    def getJuzgado(self,piso,oficina):
        return self.edificio[piso][oficina]
    
    
    def establecerJuzgado(self,piso,oficina,juzgado):
        self.edificio[piso][oficina] = juzgado

    
    # def cantidadDeJuzgadosCriticos(self,piso):
    #     cantidadDeJuzgadosCriticos(piso) + cantidadDeJuzgadosCriticos(piso-1)
        
    
    # def juzgadoMenosRecargado():
       
    #     cantExp = 0
    #     for piso in self.edificio:
    #         for oficina in self.edificio:
    #             edificio[piso][oficina].colaUrgente.tamanioCola()
    #             cantExp + self.colaUrgente.tamanioCola()
        
    #     return cantExp
    
    
    
    def oficinaVacia(self,piso,oficina):
        return self.edificio[piso][oficina] == None
            
          
    def buscaJuzgado(self,juez):
        
        posicion=None
        
        for piso in range(len(self.edificio)-1):
            for oficina in range(len(self.edificio[0])-1):
                if self.oficinaVacia(piso,oficina):
                    posicion= None
                elif not self.oficinaVacia(piso,oficina): 
                    if self.edificio[piso][oficina].nombreJuez == juez:
                        posicion = self.edificio[piso][oficina]
                
        return posicion  
        












