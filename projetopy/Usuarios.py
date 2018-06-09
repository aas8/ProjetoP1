# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 12:10:37 2018

@author: aas8
"""

def login(dicionario, login, senha):
    '''
    retorna o nível de acesso e login, ou 0 e uma string vazia, em caso de falha
    '''
    if login in dicionario:
        if senha == dicionario[login][1]:
            return dicionario[login][2], login
        else:
            return 0, ''
    else:
        return 0, ''
    

def cadastrar(login, senha, nome, dicionario):
    if login in dicionario:
        return "Usuário já existe"
    else:
        dicionario [login] = (nome, senha, 1)
        return "Usuário cadastrado com sucesso!"

def editar(dicionario, login, nome2, senha2, acesso2):
    if login in dicionario:
        if nome2 != dicionario[login][0]:
            dicionario[login] = ((nome2), dicionario[login][1], dicionario[login][2])
        if senha2 != dicionario[login][1]:
             dicionario[login] = (dicionario[login][0], (senha2), dicionario[login][2])
        if acesso2 != dicionario[login][2]:
             dicionario[login] = (dicionario[login][0], dicionario[login][1], acesso2)
    else:
        return "Usuário inexistente"
                    
def excluir(dicionario, login):
    if login in dicionario:
        aux = dicionario.pop(login)
        del aux
        return "Usuário excluído com sucesso!"
    else:
        return "Login inválido!"

def visualizar_usuarios(dicionario):
    lista = []
    for login in dicionario:
        lista.append(login)
    lista.sort()
    return lista
       