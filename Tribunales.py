from Colas import *
from Pila import *
from Fuero import *
from Expedientes_Juzgados import *
import numpy as np


class EdificioTribunales:
    
    def __init__(self,pisos = 0,oficinas = 0):
        self.edificio = np.empty((pisos,oficinas),Juzgados)


    def __repr__(self):
        return str(self.edificio)
    
    def establecerJuzgado(self,piso,oficina,juzgado):
        self.edificio[piso][oficina] = juzgado
        
    
        
    
        












