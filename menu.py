import funciones as ff
import os
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
diccionario = {}
while True:
    print ("*********MENÚ*********")
    print ('[1] - Asignar sueldos')
    print ('[2] - Clasificar sueldos')
    print ('[3] - Ver estadísticas')
    print ('[4] - Reporte de sueldos')
    print ('[5] - Salir del programa')

    op = input('Ingrese su opción: ')
    if op == '1':
        os.system ('cls')
        ff.generar_sueldo(trabajadores)
    elif op == '2':
        os.system ('cls')
    elif op == '3':
        os.system ('cls')
    elif op == '4':
        os.system ('cls')
    elif op == '5':
        os.system ('cls')
        print ('Sale de programa')
    else:
        print ("la opción ingresada no es válida, intente nuevamente: ")
        os.system ('cls')



