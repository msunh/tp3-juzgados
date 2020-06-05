
class Pila: # nuestro Tda de Pilas


    def __init__(self):
        self.pila = []


    def __repr__(self):
        return str(self.pila)


    def estaVacia(self):
        return len(self.pila) == 0

    def apilarElemento(self,elemento):
        self.pila.append(elemento) #apila elemento


    def desapilarElemento(self):
        aux = None

        if not self.estaVacia() :
            aux = self.pila.pop() #desapila el elemento, lo guarda en aux y lo devuelve 
        return aux


    def topePila(self):
        aux = None

        if not self.estaVacia():
            aux = self.pila[len(self.pila)-1] #retorna el dato arriba de todo de la pila
        return aux



    def clonarPila(self):
        aux = Pila()

        for elemento in self.pila :
            aux.pila.append(elemento)
        return aux



    def tamanioPila(self): #devuelve el tamanio de la pila
        return len(self.pila) 

