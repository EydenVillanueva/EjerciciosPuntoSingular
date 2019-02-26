#!/usr/bin/env python
# -*- coding: utf-8 -*

'''
Librerias
'''

import sys # usada para terminar la ejecución del programa
import os  # usada para limpiar el cli
import platform # usada para conocer el S.O actual

'''
Variables Globales
'''

#Diccionario con el valor de cada letra a su respectivo significado en código morse
mapa_morse = {
    'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....',
    'i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.',
    'q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v': '...-','w': '.--','x': '-..-',
    'y': '-.--','z': '--..','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....',
    '7': '--...','8': '---..','9': '----.','0': '-----',' ': '   '
}

#caracteres que no se encuentran dentro de las letras aceptadas
caracteres_invalidos = ['ñ','{', '}' ,'/', ',' '$', '%','&','!','¡'
                        '#', '"', '(' ,')', '¿','?','*',']']

#Cadena del menú inicial
menu = '''

   * CODIGO MORSE * 

   Ingrese: 
   1 - Convertir texto a morse
   2 - Convertir morse a texto
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

#Método que comprobará no haya ningun caracter inválido
def hay_invalidos(entrada):
    for v in caracteres_invalidos:
        if entrada.find(v) != -1:
            return True
    return False

#Método para convertir la entrada a su traducción.
def morse(entrada, flag):
    
    #Para evitar errores inesperados comprobamos si hay caracteres invalidos
    if hay_invalidos(entrada):
        return "Ha escrito caracteres inválidos... "
    
    #variable que guardará la traducción
    traduccion = ''
    #convertimos la entrada a minusculas
    entrada = entrada.lower()
    
    #Si el flag es True traduciremos de texto a morse
    if flag:
        #Iteracion caracter por caracter en la entrada
        for e in entrada:
            #Añadimos cada caracter en morse a nuestra variable traduccion
            traduccion+= mapa_morse[e] + ' '
                        
    #De lo contrario traduciremos de morse a texto 
    else:
        #Iteracion por cada letra de codigo morse (estas están separadas por un espacio en blanco)
        for i,e in enumerate(entrada.split(' ')):            
            if e == '':
                #En caso con toparnos con un espacio en blanco que esperamos
                if i%2:
                    traduccion += ' '
                pass
            else:
                #Retornamos la llave de nuestro diccionario mapa_morse (una vocal o número) dado un valor (código morse)
                traduccion += list(mapa_morse.keys())[list(mapa_morse.values()).index(e)]
            
    #Retornamos la traducción
    return traduccion


#Método principal de ejecución
def inicio():
    try:
        #Ciclo infinito hasta que el usuario presione salir
        while True:
            #obtenemos la seleción del usuario y la convertimos a entero
            eleccion = int(input(menu))
                    
            if eleccion == 1:
                limpiar()
                #Imprimimos el resultado a la vez que llamamos a nuestra función morse
                print("\n\n" + morse(input("\n Texto >"), True))
            if eleccion == 2:
                limpiar()
                #Imprimimos el resultado a la vez que llamamos a nuestra función morse
                print("\n\n" + morse(input("\n Morse >"), False))
            if eleccion == 3:
                salir()
        except:
            print("Algo ocurrió..")


if __name__ == "__main__":
    inicio()