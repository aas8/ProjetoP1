# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:23:35 2018

@author: aas8
"""
def compara_data(arq):
    arquivo = open(arq, 'r')
    linha = arquivo.readline()
    arquivo.close()
    string = ""
    

def recupera_data(string):
    c = -1
    data = ''
    while string[c] != ' ':
        data += string[c]
        c -= 1
    return data

def recupera_login (string):
    pass