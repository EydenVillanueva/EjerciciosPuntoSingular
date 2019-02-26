#!/usr/bin/env python
# -*- coding: utf-8 -*

'''
Librerias
'''

import math # usada por su método floor que redondea un número flotante
import sys # usada para terminar la ejecución del programa
import os  # usada para limpiar el cli
import platform # usada para conocer el S.O actual

'''
Variables Globales
'''

unidad_romana = ['' , 'I' , 'II' , 'III' , 'IV' , 'V' , 'VI' , 'VII' , 'VIII' , 'IX']
decena_romana =['' , 'X' , 'XX' , 'XXX' , 'XL' , 'L' , 'LX' , 'LXX' , 'LXXX' , 'XC']
centena_romana = ['' , 'C' , 'CC' , 'CCC' , 'CD' , 'D' , 'DC' , 'DCC' , 'DCCC' , 'CM']

valores_decimales = { 'I' : 1, 'V': 5, 'X':10 , 'L': 50, 'C': 100, 'D': 500, 'M': 100}


#Cadena del menú inicial
menu = '''

   * Números Romanos * 

   Ingrese: 
   1 - Convertir arábigo a romano
   2 - Convertir romano a arábigo
   3 - Salir
   
   > '''


'''
Métodos
'''

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

def romano_valido(numero):
    if ('IIII' in numero or 'VVVV' in numero or 'XXXX' in numero 
        or 'LLLL' in numero or 'CCCC' in numero or 'DDDD' in numero): return False
    return True

#Método que nos convertirá un número romano a arábigo y viceversa
def a_romano(numero):

    #Comprobar los límites del número
    if not (numero > 0 and numero <= 1000):
        return "Número fuera de los límites"
    
    #Comprobamos "manualmente" el número 1000 ya que la 'M' no está declarada
    #dentro de nuestras variables globales
    if(numero == 1000):
        return 'M'
    
    #Con el residuó de la división entre 10 obtenemos las unidades de cualquier número
    uni = numero % 10
    
    # obtenemos las decenas del redondeo (hacia abajo) de la divison del número entre 10
    # (qué nos eliminara las unidades dejando a las decenas como unidades) y con el residuó
    # de la división entre 10 (como en la línea anterior).
    # Ejem. 995 / 10 = 99.5, al redondearlo = 99 , obteniendo su residuó entre 10 = 9
    dec = int(math.floor( numero / 10 ) % 10)
    
    #Aplicamos el mismo principio de las decenas pero ahora dividiendo entre 100 y sin aplicar el residuó
    # ya que esto no es necesario
    #Ejem. 995 / 100 = 9.95, al redondearlo = 9, número de centenas = 9
    cen = int(math.floor( numero / 100 ))
    
    #Dependiendo del número de digitos del número ingresado es la cantidad
    # de posiciones decimales que se van a imprimir
    # Cada lista (centena_romana,decena_romana, etc) será accesada por el índice obtenido segun su valor
    if numero >= 100: return str(centena_romana[cen] + decena_romana[dec] + unidad_romana[uni])
    elif numero >= 10: return str(decena_romana[dec] + unidad_romana[uni])
    else: return str(unidad_romana[uni])
    
def a_arabigo(numero):
    #Volvemos nuestro número romano mayúscula
    numero = numero.upper()
    
    #Comprobamos que el número romano sea valido
    if not(romano_valido(numero)):
        return "Número romano incorrecto"    
    
    #retornamos mil manualmente
    if numero == 'M':
        return 1000;
    if numero[0] == 'M':
        return 0
    
    #Variable que guardará la conversión
    resultado = 0
    #lista para comparar valores anteriores
    numeros = []
    for i, a in enumerate(numero):
        #Obtenemos el valor decimal de nuestro simbolo
        actual = valores_decimales[a]
        #Añadimos a nuestra lista el valor
        numeros.append(actual)
        #comprobamos que el numero añadido sea mayor al anterior
        # de lo contrario debemos restarlos
        if i >= 1 and numeros[i] > numeros[i-1]:   
            resultado += numeros[i] - numeros[i-1] - numeros[i-1]
        else:
            #Realizo la suma 
            resultado += actual
            
    return resultado

#Método principal de ejecución
def inicio():
    try:
        #Ciclo infinito hasta que el usuario presione salir
        while True:
            #obtenemos la seleción del usuario y la convertimos a entero
            eleccion = int(input(menu))
                    
            if eleccion == 1:
                limpiar()
                #Imprimimos el resultado a la vez que llamamos a nuestra función a_romano
                print("\n\n" + a_romano(int(input("\n Número Arábigo > "))))
            if eleccion == 2:
                limpiar()
                #Imprimimos el resultado a la vez que llamamos a nuestra función a_arabigo
                print("\n\n" + str(a_arabigo(input("\n Número Romano > "))))
                
            if eleccion == 3:
                salir()
    except:
        print('Ha ingresado algo indebido...')
    
if __name__ == "__main__":
    inicio()