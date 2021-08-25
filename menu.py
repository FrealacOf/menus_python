from tkinter import * 
import webbrowser
import string
from random import randint, choice
import sys
import time
import os
from ctypes import windll
from time import sleep

# Premiere fenetre
window = Tk()
tk_title = "MENU"

# personaliser la fenetre
window.geometry("1080x720")
window.overrideredirect(True) # turns off title bar, geometry
window.title(tk_title)
window.config(background='#2c2f33')

window.minimized = False # only to know if root is minimized
window.maximized = False # only to know if root is maximized

# color
BLACKDISCORD = '#2c2f33'

# frame
frame = Frame(window, bg='#2c2f33')
title_bar = Frame(window, bg=BLACKDISCORD, relief='raised', bd=0,highlightthickness=0)

# SCRIPT
def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
                               # even when using root.overrideredirect(True)

    # Some WindowsOS styles, required for task bar integration
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())



def minimize_me():
    window.attributes("-alpha",0) # so you can't see the window when is minimized
    window.minimized = True       


def deminimize(event):

    window.focus() 
    window.attributes("-alpha",1) # so you can see the window when is not minimized
    if window.minimized == True:
        window.minimized = False     




        # put a close button on the title bar
close_button = Button(title_bar, text='  X  ', command=window.destroy,bg=BLACKDISCORD,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
title_bar_title = Label(title_bar, text=tk_title, bg=BLACKDISCORD,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)


# a frame for the main area of the window, this is where the actual app will go
window = Frame(window, bg=BLACKDISCORD,highlightthickness=0)

# pack the widgets
title_bar.pack(fill=X)
close_button.pack(side=RIGHT,ipadx=7,ipady=1)
title_bar_title.pack(side=LEFT, padx=10)
window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
#xwin=None
#ywin=None
# bind title bar motion to the move window function

def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=BLACKDISCORD





def get_pos(event): # this is executed when the title bar is clicked to move the window

    if window.maximized == False:
        
        xwin = window.winfo_x()
        ywin = window.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event): # runs when window is dragged
            window.config(cursor="fleur")
            window.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


        def release_window(event): # runs when window is released
            window.config(cursor="arrow")
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        window.maximized = not window.maximized
        
        
        


title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 


# button effects in the title bar when hovering over buttons

close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)




# resize the window width =======================================================================

resizex_widget = Frame(window,bg=BLACKDISCORD,cursor='sb_h_double_arrow')
resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)


def resizex(event):

    xwin = window.winfo_x()

    difference = (event.x_root - xwin) - window.winfo_width()

    if window.winfo_width() > 150 : # 150 is the minimum width for the window
        try:
            window.geometry(f"{ window.winfo_width() + difference }x{ window.winfo_height() }")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                window.geometry(f"{ window.winfo_width() + difference }x{ window.winfo_height() }")
            except:
                pass


    resizex_widget.config(bg=BLACKDISCORD)

resizex_widget.bind("<B1-Motion>",resizex)



# resize the window height =======================================================================



resizey_widget = Frame(window,bg=BLACKDISCORD,cursor='sb_v_double_arrow')
resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)

def resizey(event):

    ywin = window.winfo_y()

    difference = (event.y_root - ywin) - window.winfo_height()

    if window.winfo_height() > 150: # 150 is the minimum height for the window
        try:
            window.geometry(f"{ window.winfo_width()  }x{ window.winfo_height() + difference}")
        except:
            pass
    else:
        if difference > 0: # so the window can't be too small (150x150)
            try:
                window.geometry(f"{ window.winfo_width()  }x{ window.winfo_height() + difference}")
            except:
                pass

    resizex_widget.config(bg=window)

resizey_widget.bind("<B1-Motion>",resizey)





# some settings
window.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
window.after(10, lambda: set_appwindow(window)) # to see the icon on the task bar


# END


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

# sous boite a droite
right_frame.grid(row=0, column=1, sticky=W)

# afficher
window.mainloop()
