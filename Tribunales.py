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

    def oficinaVacia(self,piso,oficina):
        return self.edificio[piso][oficina] == None
    
    
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
        cantidadDeUrgentes = 0
        auxPiso = None
        auxOficina = None

        for piso in range(len(self.edificio)):
            for oficina in range(len(self.edificio[0])): 

                if not self.oficinaVacia(piso,oficina):

                    if cantidadDeUrgentes < self.edificio[piso][oficina].cantidadDeExpedientesUrgentes()
                        cantidadDeUrgentes = self.edificio[piso][oficina].cantidadDeExpedientesUrgentes()
                        



    # def cantidadDeJuzgadosCriticos(self,piso):
    #     cantidadDeJuzgadosCriticos(piso) + cantidadDeJuzgadosCriticos(piso-1)
        
    
    # def juzgadoMenosRecargado():
       
    #     cantExp = 0
    #     for piso in self.edificio:
    #         for oficina in self.edificio:
    #             edificio[piso][oficina].colaUrgente.tamanioCola()
    #             cantExp + self.colaUrgente.tamanioCola()
        
    #     return cantExp









