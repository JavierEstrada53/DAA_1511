# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QlL0WJULQPpyb2eaHd46ITJaN9IyeI99
"""

#Javier Figueroa Estrada
#DAA_1511

def busqueda_patron(cadena, patron_a_buscar):
    for r in range(len(cadena) - len(patron_a_buscar) ):
        for j in range(len(patron_a_buscar)):
            if patron_a_buscar[j] == entrada[ r + j ]:
                pass
            else:
                break
            if j + 1 == len(patron_a_buscar) and entrada[r + j] == patron_a_buscar[j]:
                print(f'Se encontró el patrón en la posición: {r} ')



entrada = '1110010001101110100011001111000110001110001110001110100011010001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001110001101000111110101010100111100011000'
patron_a_buscar = '1010101'
busqueda_patron(entrada, patron_a_buscar)