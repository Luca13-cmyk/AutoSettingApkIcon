# -*- coding: utf-8 -*-
import os
import sys
pwd = str(sys.argv[1])
nome = str(sys.argv[2])
if len(sys.argv) != 3:
    print("use - AutoSettingApkIcon.py [PATH] [NAME]")
    sys.exit()
def simbolik():
     os.system("ln -sf" + " " + pwd + " " + "/usr/bin/"+ nome)
def IconDesk():
    icon = input("Digite o caminho do ícone: ")
    catego = input("Digite a categória do app: ")
    os.system("echo   '[Desktop Entry]\nVersion = 1.0\nType = Application\nTerminal = false\nName =" + nome + "\nExec = /usr/bin/" + nome + "\nIcon =" + icon + "\nCategories =" + catego +   ";' " + "> /usr/share/applications/" + nome + ".desktop") 
simbolik() 
IconDesk()   



