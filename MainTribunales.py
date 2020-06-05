from Tribunales import *
from Pila import *
import numpy as np


edificio1 = EdificioTribunales(3,3)
print("Edificio vacio: ")
print()
print(edificio1)

juzgado1 = Juzgados("Juarez")
juzgado2 = Juzgados("Morty")
juzgado3 = Juzgados("Rick")
juzgado4 = Juzgados("Chubaca")
juzgado5 = Juzgados("Pipo")


expediente1 = Expediente(1, Fuero.Civil, Prioridad.Urgente, Estado.Juicio )
expediente2 = Expediente(2,Fuero.Comercial, Prioridad.Urgente, Estado.Juicio)
expediente3 = Expediente(3,Fuero.Familia, Prioridad.Normal, Estado.Investigacion)
expediente4 = Expediente(4,Fuero.Laboral,Prioridad.Urgente,Estado.Juicio)
expediente5 = Expediente(5,Fuero.Penal ,Prioridad.Normal, Estado.Investigacion)
expediente6 = Expediente(6,Fuero.Familia,Prioridad.Urgente,Estado.Juicio)
expediente7 = Expediente(7,Fuero.Penal,Prioridad.Urgente,Estado.Juicio)
expediente8 = Expediente(8,Fuero.Laboral,Prioridad.Urgente,Estado.Juicio)
expediente9 = Expediente(9,Fuero.Civil,Prioridad.Normal,Estado.Investigacion)
expediente10 = Expediente(10,Fuero.Laboral,Prioridad.Urgente,Estado.Investigacion)
expediente11 = Expediente(11,Fuero.Penal,Prioridad.Urgente,Estado.Investigacion)
expediente12 = Expediente(12,Fuero.Civil,Prioridad.Normal,Estado.Investigacion)
expediente13 = Expediente(13,Fuero.Civil,Prioridad.Urgente,Estado.Investigacion)
expediente14 = Expediente(14,Fuero.Civil,Prioridad.Urgente,Estado.Investigacion)

#Expedientes para la pila
expediente15 = Expediente(15,Fuero.Penal,Prioridad.Urgente,Estado.Juicio)
expediente16 = Expediente(16,Fuero.Laboral,Prioridad.Normal,Estado.Investigacion)
expediente17 = Expediente(17,Fuero.Civil,Prioridad.Urgente,Estado.Investigacion)

pilaDeExpedientes = Pila()
pilaDeExpedientes.apilarElemento(expediente15)
pilaDeExpedientes.apilarElemento(expediente16)
pilaDeExpedientes.apilarElemento(expediente17)



juzgado1.recibirExpediente(expediente1) #juzgado con 3 urgentes, juez Juarez
juzgado1.recibirExpediente(expediente10)
juzgado1.recibirExpediente(expediente11)

juzgado2.recibirExpediente(expediente3) #tiene 1 normal y 2 urgentes, juez Morty
juzgado2.recibirExpediente(expediente13)
juzgado2.recibirExpediente(expediente14)



juzgado3.recibirExpediente(expediente4) #tiene un solo expediente urgente , juez Rick


juzgado4.recibirExpediente(expediente5) #2 urgentes y 2 normales, juez Chubaca
juzgado4.recibirExpediente(expediente7)
juzgado4.recibirExpediente(expediente8)
juzgado4.recibirExpediente(expediente9)

# juzgado5.recibirExpediente(pilaDeExpedientes) #juez pipo recibe expediente pila


edificio1.establecerJuzgado(2,1,juzgado1)
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
print("El juzgado menos cargado se encuentra en la posicion: ",edificio1.juzgadoMenosRecargado())
print()
# print(edificio1.getOficina())
print("Cantidad juzgados criticos por piso: ", edificio1.cantidadDeJuzgadosCriticos(2))
# edificio1.moverExpediente(4,"Rick","Juarez") DESCOMENTAR!!!!!!!!!!!!!!!!!
print()
print(edificio1)
print()
print("Pila de expedientes: ", pilaDeExpedientes)
edificio1.mesaDeEntradas(pilaDeExpedientes,"Rick")
print()
print(edificio1)