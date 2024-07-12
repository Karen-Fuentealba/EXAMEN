import random
import csv

def generar_sueldo(lista):
    for indice in range(10):
        trabajador =  'trabajador' + str(indice + 1)
        sueldo = f"{random.randint(300000, 2500000):03}
        dic = {"trabajador": trabajador, "sueldo": sueldo}
        lista.append(dic)
        print (lista)

def clasificar_empleados(lista):
    bajos = []
    medios = []
    altos = []
    for trabajador in lista:
        if trabajador ["sueldo"]

