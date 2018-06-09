# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:31:28 2018

@author: aas8
"""
import Usuarios as us
import Criptografia as cp
import Elementos as el
import datetime

dic_usuarios = {}
#dic_usuarios [login] = (nome,senha, acesso)
dic_usuarios['adm'] = ("Administrador", "adm", 3)
cp.decifrar_usuarios('usuarios.txt', dic_usuarios)
dic_elementos = {}
#dic_elementos [n. de lote] = (nome, marca, data de validade, quantidade)
log = open("log.txt", 'a')

acesso = 0
while acesso < 1 :
    opt = int(input("login[1], cadastro[2], sair[3]: "))
    if opt == 1:
        usr = input("Digite seu login: ")
        psw = input("Digite sua senha: ")
        acesso, usuario = us.login(dic_usuarios, usr, psw)
        if acesso == 0:
            print('FALHA NO LOGIN')
        else:
            log.write(usuario+' efetuou login no sistema.\n')
            print('LOGIN EFETUADO COMO ', usuario)
            break
    elif opt == 2:
        usr = input("Digite seu login: ")
        psw = input("Digite sua senha: ")
        nome = input("Digite seu nome: ")
        msg = us.cadastrar(usr, psw, nome, dic_usuarios)
        print(msg)
    elif opt == 3:
        break

while acesso > 0:
    print("{}: nível de acesso {}".format(usuario, acesso))
    print ("[1]Pesquisar produto")
    print ("[2]Visualizar produtos")
    if acesso > 1:
        print ("[3]Adicionar produto")
        print ("[4]Editar quantidade")
    if acesso > 2:    
        print ("[5]Excluir produto")
        print ("[6]Visualizar usuários")
        print ("[7]Editar acesso de usuário")
        print ("[8]Excluir usuário")
    print ("[0]Sair")
    opt = 1
    while opt > 0:
        opt = int(input("Digite uma opção: "))
        if opt == 1:
            numero = input("Digite o número do lote: ")
            nome = input("Digite o nome do produto: ")
            marca = input("Digite a marca: ")
            data = input("Data (mm/aa): ")        
            el.pesquisar_elemento(dic_elementos, numero, nome, marca, data[2:], data[5:])
        elif opt == 2:
            el.imprimir_elementos
        elif opt == 3 and acesso > 1:
            numero = input("Digite o número do lote: ")
            nome = input("Digite o nome do produto: ")
            marca = input("Digite a marca: ")
            data = input("Data (dd/mm/aa): ")
            qtd = input("Quantidade: ")
            el.adicionar_elemento(dic_elementos, numero, nome, marca, data, quantidade)
            log.write(usuario+' adicionou um produto de lote'+numero+' às {}:{}:{} do dia {}\{}\{}\n'.format(str(agora.hour), str(agora.minute), str(agora.second), str(agora.day), str(agora.month), str(agora.year)))
        elif opt == 4 and acesso > 1:
            numero = input("Digite o número do lote: ")
            if numero in dic_elementos:
                qtd = input("Quantidade: ")
                print(el.atualizar_elemento(dic_elementos, numero, qtd))
                log.write(usuario+' atualizou a quantidade de um produto de lote'+numero+' às {}:{}:{} do dia {}\{}\{}\n'.format(str(agora.hour), str(agora.minute), str(agora.second), str(agora.day), str(agora.month), str(agora.year)))
            else:
                print("Lote não encontrado")
        elif opt == 5 and acesso > 2:
            numero = input("Digite o número do lote: ")
            el.excluir_elemento(dic_elementos, numero)
            log.write(usuario+' Excluiu um produto de lote'+numero+' às {}:{}:{} do dia {}\{}\{}\n'.format(str(agora.hour), str(agora.minute), str(agora.second), str(agora.day), str(agora.month), str(agora.year)))
        elif opt == 6 and acesso > 2:
            lista = us.visualizar_usuarios(dic_usuarios)
            for login in lista:
                print('{}: {} ({})'.format(login, dic_usuarios[login][0], dic_usuarios[login][2]))
        elif opt == 7 and acesso> 2:
            login = input("Login: ")
            nome = input("Nome: ")
            senha = input("Senha: ")
            acesso = int(input("Nível de acesso: "))
            us.editar(dic_usuarios, login, nome, senha, acesso)
            log.write(usuario+' Alterou o acesso do usuário '+login+' às {}:{}:{} do dia {}\{}\{}\n'.format(str(agora.hour), str(agora.minute), str(agora.second), str(agora.day), str(agora.month), str(agora.year)))
        elif opt == 8 and acesso > 2:
            login = input("Login: ")
            us.excluir(dic_usuarios, login)
        elif opt == 0:
            agora = datetime.datetime.now()
            log.write(usuario+' saiu do sistema às {}:{}:{} do dia {}\{}\{}\n'.format(str(agora.hour), str(agora.minute), str(agora.second), str(agora.day), str(agora.month), str(agora.year)))
            break
        else:
            print("Opção inválida!")
    break            
                
    
    cp.criptografar_usuarios(dic_usuarios, 'usuarios.txt')
    log.flush()
    log.close()