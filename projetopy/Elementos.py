# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 13:02:30 2018

@author: aas8
"""
from datetime import date
#dic_elementos [n. de lote] = (nome, marca, data de validade, quantidade)

def adicionar_elemento(dicionario, numero, nome, marca, quantidade, dia, mes, ano):
    if numero.isdigit():
        if numero in dicionario:
            return "Número de lote já cadastrado!"
        else:
            dicionario[numero] = (nome, marca, date(ano, mes, dia), quantidade)
            return "Cadastrado com sucesso!"
    else:
        return "Número de lote inválido"

def pesquisar_elemento(dicionario, numero, nome, marca, mes, ano): 
    if numero != '':
        if numero in dicionario:
            return [numero]
        else:
            return []
    else:
        resultados = []
        for numero in dicionario:
            if (nome == '') or (nome == dicionario[numero][0]):
                if (marca == '') or (marca == dicionario[numero][1]):
                    if (not mes.isdigit()) or (int(mes) == dicionario[numero][2].month):
                        if (not ano.isdigit()) or (int(ano) == dicionario[numero][2].year):
                            resultados.append(numero)
        return resultados

def atualizar_elemento(dicionario, numero, num):
    if numero.isdigit() and (len(num) or num[1:].isdigit() > 0):
        if numero in dicionario:
            if num[0] == "+":
                dicionario[numero] = (dicionario[numero][0], dicionario[numero][1], dicionario[numero][2], dicionario[numero][3]+int(num[1:]))
            elif num[0] == "-":
                dicionario[numero] = (dicionario[numero][0], dicionario[numero][1], dicionario[numero][2],dicionario[numero][3]-int(num[1:]))
            else:
                dicionario[numero] = (dicionario[numero][0], dicionario[numero][1], dicionario[numero][2], int(num))
        return "Lote atualizado"
    else:
        return "Quantidade inválida!"

def excluir_elemento(dicionario,numero):
    if numero.isdigit():
        if numero in dicionario:
            aux = dicionario.pop(numero)
            del aux
            return "Elemento excluído com sucesso!"
        else:
            return "Elemento inválido!"
    else:
        return "Número de lote inválido!"
    
def visualizar_elementos(dicionario):
    lista = []
    for numero in dicionario:
        lista.append(numero)