from Tribunales import *
import numpy as np


edificio1 = EdificioTribunales(3,3)
print("Edificio vacio: ")
print()
print(edificio1)

juzgado1 = Juzgados("Juarez")
juzgado2 = Juzgados("Morty")
juzgado3 = Juzgados("Rick")
juzgado4 = Juzgados("Chubaca")

expediente1 = Expediente(1, Fuero.Civil, Prioridad.Urgente, Estado.Juicio )
expediente2 = Expediente(2,Fuero.Comercial, Prioridad.Urgente, Estado.Juicio)
expediente3 = Expediente(3,Fuero.Familia, Prioridad.Normal, Estado.Investigacion)
expediente4 = Expediente(4,Fuero.Laboral,Prioridad.Urgente,Estado.Juicio)
expediente5 = Expediente(5,Fuero.Penal ,Prioridad.Normal, Estado.Investigacion)
expediente6 = Expediente(6,Fuero.Laboral,Prioridad.Normal,Estado.Juicio)

juzgado1.recibirExpediente(expediente1)
juzgado2.recibirExpediente(expediente3)
juzgado3.recibirExpediente(expediente4)
juzgado4.recibirExpediente(expediente5)

edificio1.establecerJuzgado(0,1,juzgado1)
edificio1.establecerJuzgado(0,2,juzgado3)
edificio1.establecerJuzgado(1,2,juzgado4)  
edificio1.establecerJuzgado(2,0,juzgado2)

 

print()
print("Edificio Con Oficinas: ")
print()
print(edificio1)
print()
print("juez en posicion: " ,edificio1.getJuzgado(0,1))
print()
print("Busca Juzgado del Juez y no lo encuentra: ", edificio1.buscaJuzgado("Carlos"))
print()
print("esta oficina esta vacia?: ",edificio1.oficinaVacia(0,0))
print()
print("Busca Juzgado del Juez y lo encuentra en la posicion: ", edificio1.buscaJuzgado("Chubaca"))
print()
