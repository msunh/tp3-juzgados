from Colas import *
from Pila import *
from Fuero import *
from Expedientes_Juzgados import *
                 
 #MAIN            

expediente1 = Expediente(1, Fuero.Civil, Prioridad.Urgente, Estado.Juicio )
expediente2 = Expediente(2,Fuero.Comercial, Prioridad.Urgente, Estado.Juicio)
expediente3 = Expediente(3,Fuero.Familia, Prioridad.Normal, Estado.Investigacion)
expediente4 = Expediente(4,Fuero.Laboral,Prioridad.Urgente,Estado.Juicio)
expediente5 = Expediente(5,Fuero.Penal ,Prioridad.Normal, Estado.Investigacion)
expediente6 = Expediente(6,Fuero.Laboral,Prioridad.Normal,Estado.Juicio)
expediente7 = Expediente(7,Fuero.Familia,Prioridad.Urgente,Estado.Investigacion)



print(expediente1)
print(expediente1.esNormal())
print(expediente1.esUrgente())
#pilas
print()
juzgado1 = Juzgados("Juanjo")
print() 
print("Juzgado: ", juzgado1)
print()    

juzgado1.recibirExpediente(expediente1)
juzgado1.recibirExpediente(expediente2)
juzgado1.recibirExpediente(expediente3)
juzgado1.recibirExpediente(expediente4)
juzgado1.recibirExpediente(expediente5)
juzgado1.recibirExpediente(expediente6)

print()
print(juzgado1)
print()
print("El Primer Expediente A Tratar es: ", juzgado1.primerExpedienteATratar())
print()
#desencolo y saco de la fila
#print("Tratar expediente: ", juzgado1.tratarExpediente())
print()
print(juzgado1)
print()
print("La Cantidad Total De Exp. es:", juzgado1.cantidadTotalExpedientes())
print()
print(juzgado1.expedientesPorTipo())
print() 
print("Es Critico?: ", juzgado1.esCritico())  
print()
print("Cantidad de expedientes en Juicio: ", juzgado1.enJuicio())
print()
print("El expediente buscado es :",juzgado1.buscarExpediente(2))
print()
juzgado1.eliminarExpediente(5)
print()
print(juzgado1)
#print("es de la prioridad: ", juzgado1.buscarExpediente(5).esDePrioridad(1))
print()
#expediente1.setPrioridad(Prioridad.Normal)
print()
juzgado1.cambiaDeEstado(1)
print()
print(juzgado1)
print()
print(juzgado1.cantidadDeExpedientesUrgentes())
print()
juzgado1.recibirExpediente(expediente7)
print(juzgado1.cantidadDeExpedientesUrgentes())









