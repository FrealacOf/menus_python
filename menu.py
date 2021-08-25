from tkinter import *
import webbrowser
import string
from random import randint, choice
import sys
import time
import os

# script menu2
def chat():
    os.system("start /B start cmd.exe @cmd /k py assets/servers/server.py")
    time.sleep(1)
    os.system("start /B start cmd.exe @cmd /k py assets/menus/client.py")

def password():
    os.system("start /B start cmd.exe @cmd /k py assets/menus/generator_password.py")


# github button script
def open_github_channel():
    webbrowser.open_new("https://github.com/FrealacOf")


# menu  script
def open_discord_channel():
    webbrowser.open_new("https://discord.gg/4P4q4SQ74a")


def open_instagram_channel():
    webbrowser.open_new("https://www.instagram.com/frealacofficial_/")


# Premiere fenetre
window = Tk()

# personaliser la fenetre
window.title("MENUS")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("assets\img\logo.ico")
window.config(background='#2c2f33')

# frame
frame = Frame(window, bg='#2c2f33')

# sous boite
right_frame = Frame(frame, bg='#2c2f33')

# ajouter texte
label_title = Label(right_frame, text="Bienvenue sur le menu", font=("AusionPersonalUse", 40), bg='#2c2f33', fg='white')
label_title.pack()

# ajouter bouton
github_buttom = Button(right_frame, text="By FrealacOf", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=open_github_channel, bd=0)
github_buttom.pack(padx=20, pady=20)

chat_buttom = Button(right_frame, text="CHAT", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=chat, bd=0)
chat_buttom.pack(padx=20, pady=20)

menu_buttom = Button(right_frame, text="PASSWORD", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=password, bd=0)
menu_buttom.pack(padx=20, pady=20)

# ajouter
frame.pack(expand=YES)

# barre de menu
menu_bar = Menu(window)

# menus listes
# menu 1
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command=window.quit)

# menu 2
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="github", command=open_github_channel)
file_menu.add_command(label="discord", command=open_discord_channel)
file_menu.add_command(label="instagram", command=open_instagram_channel)

menu_bar.add_cascade(label="Support", menu=file_menu)
# configurer les menus
# menu 1
window.config(menu=menu_bar)

# sous boite a droite
right_frame.grid(row=0, column=1, sticky=W)

# afficher
window.mainloop()
