from Tribunales import *
import numpy as np


edificio1 = EdificioTribunales(3,3)
print(edificio1)

juzgado1 = Juzgados("Juanjo")
expediente1 = Expediente(1, Fuero.Civil, Prioridad.Urgente, Estado.Juicio )
expediente2 = Expediente(2,Fuero.Comercial, Prioridad.Urgente, Estado.Juicio)
expediente3 = Expediente(3,Fuero.Familia, Prioridad.Normal, Estado.Investigacion)
expediente4 = Expediente(4,Fuero.Laboral,Prioridad.Urgente,Estado.Juicio)
expediente5 = Expediente(5,Fuero.Penal ,Prioridad.Normal, Estado.Investigacion)
expediente6 = Expediente(6,Fuero.Laboral,Prioridad.Normal,Estado.Juicio)
juzgado1.recibirExpediente(expediente1)

edificio1.establecerJuzgado(0,1,juzgado1)
print()
print(edificio1)
print()
print("juzgado en posicion: " ,edificio1.getJuzgado(0,1))
print(edificio1.buscaJuzgado("Juanjo"))
# print("esta oficina esta vacia?",edificio1.oficinaVacia(0,3))