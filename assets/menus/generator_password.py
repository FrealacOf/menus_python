from tkinter import *
import webbrowser
import string
from random import randint, choice
import sys
import time
import os


# github button script
def open_github_channel():
    webbrowser.open_new("https://github.com/FrealacOf")


# menu  script
def open_discord_channel():
    webbrowser.open_new("https://discord.gg/4P4q4SQ74a")


def open_instagram_channel():
    webbrowser.open_new("https://www.instagram.com/frealacofficial_/")


# generate_password button script 
def generate_password():
    password_min = 9
    password_max = 16
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# Premiere fenetre
window = Tk()

# personaliser la fenetre
window.title("Générateur de MDP")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("assets\img\logo.ico")
window.config(background='#2c2f33')

# frame
frame = Frame(window, bg='#2c2f33')

# sous boite
right_frame = Frame(frame, bg='#2c2f33')

# creation d'image
width = 100
height = 100
image = PhotoImage(file="assets\img\password_img.png").zoom(10).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#2c2f33', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# ajouter texte
label_title = Label(right_frame, text="Bienvenue sur le générateur", font=("AusionPersonalUse", 40), bg='#2c2f33', fg='white')
label_title.pack()

# ajouter bouton
github_buttom = Button(right_frame, text="By FrealacOf", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=open_github_channel, bd=0)
github_buttom.pack(padx=20, pady=20)

# ajouter champs/entrée/input
password_entry = Entry(right_frame, font=("AusionPersonalUse", 40), bg='#2c2f33', fg='white')
password_entry.pack()

# Button password
generat_password_button = Button(right_frame, text="Générer", font=("AusionPersonalUse", 40), bg='#23272a', fg='white', bd=0, highlightthickness=0, command=generate_password)
generat_password_button.pack(padx=20, pady=20)

# ajouter
frame.pack(expand=YES)

# barre de menu
menu_bar = Menu(window)

# menus listes
# menu 1
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Menu", menu=file_menu)

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
