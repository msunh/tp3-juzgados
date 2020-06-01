# class ExpedientesNormales:
#     def __init__(self,)




# class ExpedientesUrgentes:
#     def __init__(self,)


class Expediente :
    
    def __init__(self,nroExp , tipoExp=" ",prioridad=" ",estado=""):
        self.nroExp = nroExp
        self.tipoExp = tipoExp
        self.prioridad = prioridad
        self.estado = estado
        
   
    
    def __repr__(self):
        printeo = "|| Nro Exp: " + str(self.nroExp) + "| tipo: " + str(self.tipoExp) + "| prioridad: " + str(self.prioridad) + "| estado: "+ str(self.estado) + " || "
        return printeo
    

class Juzgados:
    
    
    def __init__(self):
        self.colaUrgente = []
        self.colaNormal = []
#        self.nombre=nombre
        
   
    def __repr__(self):
        printeo= "URGENTES: "+ str(self.colaUrgente) + " NORMALES: " + str(self.colaNormal)
        return printeo
    
   
    
    def recibirExpediente(self,exp):
        if exp.prioridad == "normal" :
            self.colaNormal.append(exp)
        elif exp.prioridad =="urgente" :
            self.colaUrgente.append(exp)
            
    
   
    
    def primerExpedienteATratar(self):
        dato=None
        if not len(self.colaUrgente)==0:
            dato=self.colaUrgente[0]
        else:
            dato=self.colaNormal[0]
        return dato
    
    
    
    def tratarExpediente(self):
        if not len(self.colaUrgente) == 0:
            self.colaUrgente.pop(0)
        else:
            self.colaNormal.pop(0)
            
   
    
    def cantidadTotalExpedientes(self):
        return len(self.colaNormal) + len(self.colaUrgente)
    
    
    
    
    def expedientesPorTipo(self):
        return "cantidad exp cola normal: ", len(self.colaNormal), " cantidad exp cola urgentes: ", len(self.colaUrgente)
                
   
    
    def esCritico(self):
        return len(self.colaNormal)>=50 or len(self.colaUrgente) >= 50 
    
   
    
    def enJuicio(self):
        sumaExpNormal=0
        sumaExpUrg=0
        for elementos in self.colaNormal:
            if elementos.estado == "juicio":
                sumaExpNormal+=1
        
        
        for elementos in self.colaUrgente :
            if elementos.estado == "juicio":
                sumaExpUrg+=1
        
        return(sumaExpNormal+sumaExpUrg)
                

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
                 
             
         
         
         
    

expediente1 = Expediente(2,"civil", "normal", "investigacion")
expediente2 = Expediente(4,"penal","urgente", "juicio")
expediente3 = Expediente(23,"civil","urgente","investigacion")
expediente4 = Expediente(40,"familia" ,"normal", "investigacion")
expediente5 = Expediente(80,"penal", "normal", "investigacion")
expediente6 = Expediente(83,"penal", "normal", "investigacion")
expediente7 = Expediente(85,"penal", "normal", "juicio")

print()
print("Contenido de los Juzgados: ")
juzgado1 = Juzgados()

juzgado1.recibirExpediente(expediente1)
juzgado1.recibirExpediente(expediente2)
#juzgado1.recibirExpediente(expediente3)
#juzgado1.recibirExpediente(expediente4)
#juzgado1.recibirExpediente(expediente5)
#juzgado1.recibirExpediente(expediente6)
#juzgado1.recibirExpediente(expediente7)


print(juzgado1)
print()
#print(juzgado1.primerExpedienteATratar())
#juzgado1.tratarExpediente()

print("La cantidad total de expedientes es : ",juzgado1.cantidadTotalExpedientes()) 
print()
print("la cantidad de expedientes por tipo es: ", juzgado1.expedientesPorTipo())
print()
print("Es critico?: ", juzgado1.esCritico())
print()
print("Cantidad de expedientes en Juicio: ", juzgado1.enJuicio())
print()

#buscar expediente numero:
print(juzgado1.buscarExpediente(80))

juzgado1.cambiaDeEstado(2)

print(juzgado1)







