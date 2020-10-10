#!/usr/bin/python3
import PySimpleGUI as db
from random import *

import subprocess, os, socket, pty

class geradorpass:
    def __init__(self):
         db.theme('DarkBlue13')
        #layout
         base = [
             [db.Text('                                     Gere sua Senha Segua AQUI!', size=(0, 1))],
             [db.Text('')],
             [db.Text('Usuário/Email: '), db.Input(size=(28, 2), key='user')],
             [db.Text('')],
             [db.Text('Quantidade de Caractéres:', size=(44, 1)),    db.Combo(values=list(
                 range(40)), key='Total_caracteres', default_value=1, size=(12,10))],
             [db.Text('')],
             [db.Checkbox('Encrypt'), db.Checkbox('Forte')],
             [db.Output(size=(70, 17))],
             [db.Button('Gerar Senha')]

         ]
        # corpo
         self.janela = db.Window('Generate Password').layout(base)

    def iniciacao(self):
        while True:
            momento, valores = self.janela.read()
            if momento == db.WINDOW_CLOSED:
                
                break
            if momento == 'Gerar Senha':
                senha_real = self.criar(valores)
                usu = valores['user']
                print('----------------------')
                print(f'Usuário:   {usu}')
                print()
                print(f'Senha:   {senha_real}')
                print('----------------------')
                print()
                self.salvar(usu, senha_real)
                
                
    def criar(self, valores):
        senha_lista = 'QWERTYUIOPLÇJHGFDSAZXCVBNMqwertyuiopçlkjhgfdsazxcvbnm!@#$%*()><;[]{}==++?|'
        senha_base = choices(senha_lista, k=(valores['Total_caracteres']))
        senha_criacao = ''.join(senha_base)
        return senha_criacao

    def salvar(self, usu, senha_real):
        with open('senhas_salvas.txt', 'a', newline='') as aq:
                aq.write(f'Usuário:   {usu}   | Senha:   {senha_real}         \n\n')

    

tela = geradorpass()
tela.iniciacao()


