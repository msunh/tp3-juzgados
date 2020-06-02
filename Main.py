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
#expediente6 = Expediente(7,"penal", "normal", "investigacion")
#expediente7 = Expediente(8,"penal", "normal", "juicio")


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


# expediente1 = Expediente(2,"civil", "normal", "investigacion")
# expediente2 = Expediente(4,"penal","urgente", "juicio")
# expediente3 = Expediente(23,"civil","urgente","investigacion")
# expediente4 = Expediente(40,"familia" ,"normal", "investigacion")
# expediente5 = Expediente(80,"penal", "normal", "investigacion")
# expediente6 = Expediente(83,"penal", "normal", "investigacion")
# expediente7 = Expediente(85,"penal", "normal", "juicio")

# print()
# print("Contenido de los Juzgados: ")
# juzgado1 = Juzgados()

# juzgado1.recibirExpediente(expediente1)
# juzgado1.recibirExpediente(expediente2)
# #juzgado1.recibirExpediente(expediente3)
# #juzgado1.recibirExpediente(expediente4)
# #juzgado1.recibirExpediente(expediente5)
# #juzgado1.recibirExpediente(expediente6)
# #juzgado1.recibirExpediente(expediente7)


# print(juzgado1)
# print()
# #print(juzgado1.primerExpedienteATratar())
# #juzgado1.tratarExpediente()

# print("La cantidad total de expedientes es : ",juzgado1.cantidadTotalExpedientes()) 
# print()
# print("la cantidad de expedientes por tipo es: ", juzgado1.expedientesPorTipo())
# print()
# print("Es critico?: ", juzgado1.esCritico())
# print()
# print("Cantidad de expedientes en Juicio: ", juzgado1.enJuicio())
# print()

# #buscar expediente numero:
# print(juzgado1.buscarExpediente(80))

# juzgado1.cambiaDeEstado(2)

# print(juzgado1)







