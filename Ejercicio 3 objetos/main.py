#!/usr/bin/env python
# -*- coding: utf-8 -*

'''
Librerias
'''
import sys # usada para terminar la ejecución del programa
import os  # usada para limpiar el cli
import platform # usada para conocer el S.O actual

'''
Clases
'''
from clases import Cuadrado, Cubo


'''
Variables Globales
'''

#Cadena del menú inicial
menu = '''

   * De Cubos y Cuadrados * 

   Lado > '''


'''
Métodos
'''
#Cadena del submenú operaciones
def menu_operaciones_cadena(lado):
    return '''

   * Operaciones * 
   
   Lado = {0}
   
   Ingrese: 
   1 - Calcular Volumen
   2 - Calcular Perímetro
   3 - Calcular Área
   4 - Atras
   5 - Salir
   
   > '''.format(lado)

#Limpia el cli para una mejor experiencia de navegación
def limpiar():
    #Identificamos el S.O en el que estamos
    if platform.system() == 'Windows':
        #Limpiamos cli en windows
        os.system('cls')
    else:
        #Limpiamos cli en Linux o Mac
        os.system('clear')
       

#Método que nos limpiará el cli y terminará la ejecución del programa
def salir():
    #Limpiamos el cli
    limpiar()
    #Mensaje de despedida
    print('Adios...')
    #Terminamos la ejecución de nuestro programa
    sys.exit()    


#Submenú para las operaciones
def menu_operaciones(lado):
    #Ciclo infinito hasta que el usuario presione salir
    while True:
        #obtenemos la seleción del usuario y la convertimos a entero
        eleccion = int(input(menu_operaciones_cadena(lado)))
                
        if eleccion == 1:
            limpiar()
            #Creamos nuestra clase Cubo
            c = Cubo(lado)
            #Impresión del área
            print("\n Volumen: " + str(c.calcular_volumen()))
            
        if eleccion == 2:
            limpiar()
            #Creamos nuestra clase Cuadrado
            c = Cuadrado(lado)
            #Impresión del área
            print("\n Perímetro: " + str(c.calcular_perimetro()))
            
        if eleccion == 3:
            limpiar()
            #Creamos nuestra clase Cuadrado
            c = Cuadrado(lado)
            #Impresión del área
            print("\n Área: " + str(c.calcular_area()))
            
        if eleccion == 4:
            limpiar()
            return 0
            
        if eleccion == 5:
            salir()



#Método principal de ejecución
def inicio():
    
    #Ciclo infinito hasta que el usuario presione salir
    while True:
        #obtenemos la seleción del usuario y la convertimos a entero
        lado = int(input(menu))
        #Abrimos el menú
        menu_operaciones(lado)
   
        
    
if __name__ == "__main__":
    inicio()