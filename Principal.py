# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:31:28 2018

@author: aas8
"""
import Usuarios
import Criptografia as cp
from datetime import date

dic_usuarios = {}
#dic_usuarios [login] = (nome,senha, acesso)
dic_usuarios['adm'] = ("Administrador", "1245678", 3)
dic_usuarios["aas8"] = ("Adriana", "aas8", 3)

dic_elementos = {}
#dic_elementos [n. de lote] = (nome, marca, data de validade, quantidade)
acesso = 0
while acesso < 1 :
    opt = int(input("login[1], cadastro[2], sair[3]: "))
    if opt == 1:
        usr = input("Digite seu login: ")
        psw = input("Digite sua senha: ")
        acesso, usuario = Usuarios.login(dic_usuarios, usr, psw)
        if acesso == 0:
            print('FALHA NO LOGIN')
        else:
            print('LOGIN EFETUADO COMO ', usuario)
            break
    elif opt == 2:
        usr = input("Digite seu login: ")
        psw = input("Digite sua senha: ")
        nome = input("Digite seu nome: ")
        msg = Usuarios.cadastro(usr, psw, nome, dic_usuarios)
        print(msg)
    elif opt == 3:
        break
    
cp.criptografar_usuarios(dic_usuarios, 'usuarios.txt')