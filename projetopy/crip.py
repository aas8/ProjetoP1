# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:30:50 2018

@author: aas8
"""

def recuperar_chaves(arq):
    arquivo = open (arq, 'r')
    linha = arquivo.readline()
    arquivo.close()
    aux = ''
    for c in linha:
        if c != ' ':
            aux += c
        else:
            num1 = int(aux)
            aux = ''
    num2 = int(aux)
    return num1, num2

def criptografar_string(string, e, n):
    codigo = ''
    for x in string:
        y = (ord(x)**e)%n
        codigo += str(y)+'#'
    return codigo

def decifrar_codigo(string, d, n):
    texto = ''
    aux = ''
    for c in string:
        if c != '#' and c != '\n':
            aux += c
        elif c != '\n':
            y = int(aux)
            aux = ''
            x = chr((y**d)%n)
            texto += x
    return texto