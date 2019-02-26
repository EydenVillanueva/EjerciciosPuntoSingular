#!/usr/bin/env python
# -*- coding: utf-8 -*

class Cuadrado():
    '''
    Clase Cuadrado para realizar operaciones de cálculo de área y perímetro
    '''
    
    lado = 0 # atributo lado del cuadrado
    
    #Constructor de la clase Cuadrado.
    #Recibe como atributo un número entero que hace refencia a la longitud de un lado.
    #Asignamos por defecto 0 al atributo lado
    def __init__(self, lado = 0):
        self.lado = lado
    
    #Método para retornar un mejor mensaje para imprimir
    def __str__(self):
        return "Objeto Cuadrado"
    
    #Método que retorna el área del cuadrado.
    def calcular_area(self):
        return self.lado * self.lado
    
    #Método que retorna el perímetro del cuadrado
    def calcular_perimetro(self):
        return self.lado * 4
    
class Cubo(Cuadrado):
    '''
    Clase Cubo para realizar operaciones de cálculo de volumen y perímetro
    (Hereda de la clase Cuadrado)
    
    NOTA: Al ser un Cubo, se da por hecho que todos los lados tienen la misma longitud (incluso el ancho)
    '''
    
    #Constructor de la clase Cubo.
    #Recibe como atributo un número entero que hace refencia a la longitud de un lado.
    def __init__(self, lado = 0):
        self.lado = lado
        
    #Método para retornar un mejor mensaje para imprimir
    def __str__(self):
        return "Objeto Cubo"    
    
    #Método que retorna el volumen del cubo. Hace uso del método heredado calcular_area de su clase
    #superior o padre
    def calcular_volumen(self):
        return self.calcular_area() * self.lado
    
    def calcular_perimetro(self):
        return self.lado * 12