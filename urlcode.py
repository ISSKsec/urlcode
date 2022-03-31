#!/usr/bin/python3

import requests, argparse, sys, signal, socket
import urllib.parse
#from pwn import *

#pip install requests
#Ctrl C Es para controlar la salida del programa.


##Pon la direccion url o la ip del servidor. 

ConnectionInfo = argparse.ArgumentParser()
ConnectionInfo.add_argument("URL o IP",  default=socket.gethostname())
ConnectionInfoParsed = ConnectionInfo.parse_args()

animacion = """
           █    ██  ██▀███   ██▓     ▄████▄   ▒█████  ▓█████▄ ▓█████ 
           ██  ▓██▒▓██ ▒ ██▒▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ 
          ▓██  ▒██░▓██ ░▄█ ▒▒██░    ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   
          ▓▓█  ░██░▒██▀▀█▄  ▒██░    ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ 
          ▒▒█████▓ ░██▓ ▒██▒░██████▒▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒
          ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░
          ░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░
           ░░░ ░ ░   ░░   ░   ░ ░   ░        ░ ░ ░ ▒   ░ ░  ░    ░
             ░        ░         ░  ░░ ░          ░ ░     ░       ░  ░
                          ░                  ░
"""
print("\033[1;31m"+animacion+'\033[0;m')

def exit(frame, sig):
	print(" \n{*} Saliendo...")
	sys.exit(1)
signal.signal(signal.SIGINT, exit)

def _action():
# Variables
	argv = sys.argv[1]
	server = argv
	req = requests.get(server)

	print("Elige una opcion:\n[1] Codigo fuente\n[2] Headers\n[3] Codigo\ de estado\n[4] Url encodear\n[5] Url decodear")
	question = int(input("Elige un numero: "))
	if question == 1:
		print("Codigo fuente")
		print(req.text)
	elif question == 2:
		print("Headers")
		print(req.headers)
	elif question == 3:
		print("Codigo de estado")
		print(req.status_code)
	elif question == 4:
		print("Url encode")
		print(urllib.parse.quote(server))
	elif question ==5:
		print("Url decode")
		print(urllib.parse.unquote(server))
	else:
		print("Seleccion no valida")
		return _action()

if __name__ == '__main__':
	 _action()
#Script
