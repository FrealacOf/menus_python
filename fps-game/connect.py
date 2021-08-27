import sys
import time
import os

f = open('ip_port_to_connect.txt', 'r')
f2 = open('ip_port_to_connect.txt', 'w')

#### SERVEUR OUI OU NON
reponse = input("Voulez-vous connecter ? [o/n] ")
reponse = reponse.strip().lower()
if reponse.startswith('o'):
    f2.write("o\nPseudo15\n")
    print("OK, vous allez vous connecter avec la template")
    print("Le jeu ce lance")
    time.sleep(1)
    os.system("start /B start cmd.exe @cmd /k py server.py")
    time.sleep(2)
    os.system("start /B start cmd.exe @cmd /k py client.py")
elif reponse.startswith('n') or reponse == '':
    print("Au revoir")
    f2.write("no")
else:
    print("Répondez par 'o' ou 'n'")

    
    
#### PSEUDO
print("")
print("Veulliez prendre un pseudo ")
pseudo = input("> ")
print("Votre pseudo > " + pseudo)
f2.write(pseudo + "\n")
 
 
#### IP DU SERVEUR
print("")
print("Veulliez mettre l'ip ")
ip = input("> ")
print("L'ip du serveur > " + ip)
f2.write(ip + "\n")
 
 
#### PORT DU SERVEUR
print("")
print("Veulliez mettre le port ")
port = input("> ")
print("Le port du serveur > " + port)
f2.write(port)
f.close()
f2.close()

#### RESULTAT
print("")
print("")
print("> Connection : " + reponse + "\n> Pseudo : " + pseudo + "\n> L'ip : " + ip + "\n> Port du serveur : " + port )
print("")
print("")
print("Le jeu ce lance")
time.sleep(1)
os.system("start /B start cmd.exe @cmd /k py server.py")
time.sleep(2)
os.system("start /B start cmd.exe @cmd /k py client.py")
