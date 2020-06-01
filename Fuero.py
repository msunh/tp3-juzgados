from enum import Enum


class Fuero(int,Enum):
    Civil = 0
    Penal = 1
    Laboral = 2
    Familia = 3
    Comercial = 4


class Prioridad(int,Enum) :
    Normal = 0
    Urgente = 1


class Estado(int,Enum) :
    Investigacion = 0
    Juicio = 1