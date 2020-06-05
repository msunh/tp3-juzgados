class Colas: # nuestro TDA de colas de expedientes
    
    def __init__(self):
        self.cola=[] # creo la cola
    
    def __repr__(self): #imprime la cola con su contenido
        return str(self.cola)    
    

    def estaVacia(self):
        return len(self.cola) == 0 #devuelve true si la cola esta vacia


    def encolar(self,elemento): #agrega un elemento a la cola
        self.cola.insert(0,elemento)
        
   
    def desencolar(self):
        aux = None
        
        if not self.estaVacia():
            aux = self.cola.pop() #desencola tomando el ultimo elemento de la lista
        return aux

   
    def vaciarCola(self):
        self.cola.clear() #eliminar todo el contenido de la misma
        
            
    def primerElementoFila(self):
        aux= None

        if not self.estaVacia():
            aux = self.cola[len(self.cola)-1] #si no esta vacia devuelve el primer elemento de la cola
        return aux


    def clonarCola(self):
        aux = Colas()

        for elemento in self.cola:
            aux.encolar(elemento)  #recorre los elementos de la cola y los encola en la nueva
        return aux


    def tamanioCola(self):
        return len(self.cola) 

 
 