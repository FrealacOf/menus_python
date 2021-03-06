from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import * 
import webbrowser
import string
from random import randint, choice
import sys
import time
import os
from ctypes import windll
from time import sleep
from tkinter import messagebox

w=Tk()


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

#############progressbar          33333333333333333333333333333
def new_win():
    # Premiere fenetre
    window = Tk()
    tk_title = "MENU"

    # personaliser la fenetre
    window.geometry('1000x800+550+200')
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
    def server():
        os.system("start /B start cmd.exe @cmd /k py assets/servers/server.py")
        time.sleep(1)
        os.system("start /B start cmd.exe @cmd /k py assets/menus/client.py")


    def minecraft():
        os.system("start /B start cmd.exe @cmd /k py assets/menus/main.py")
        
        

    def tictac():
        new_window = Toplevel()
        lbl = Label(new_window)
        lbl.pack()

        new_window = Tk()
        new_window.iconbitmap("assets\menus\img\logo.ico")
        new_window.title("Tic Tac Game")


        clicked = True
        count = 0




        def disable_all_button():
            b1.config(state=DISABLED)
            b2.config(state=DISABLED)
            b3.config(state=DISABLED)
        
            b4.config(state=DISABLED)
            b5.config(state=DISABLED)
            b6.config(state=DISABLED)

            b7.config(state=DISABLED)
            b8.config(state=DISABLED)
            b9.config(state=DISABLED)  




        def checkifwon():
            global winner
            winner = False
            
            
            if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
                b1.config(bg="red")
                b2.config(bg="red")
                b3.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()
            elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
                b4.config(bg="red")
                b5.config(bg="red")
                b6.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()
            elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
                b7.config(bg="red")
                b8.config(bg="red")
                b9.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()

            ###de haut en bas
            elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
                b1.config(bg="red")
                b4.config(bg="red")
                b7.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()
            elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
                b2.config(bg="red")
                b5.config(bg="red")
                b8.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()
            elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
                b3.config(bg="red")
                b6.config(bg="red")
                b9.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()
            ## SUR LE COTE   
            
            elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
                b1.config(bg="red")
                b5.config(bg="red")
                b9.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()
            elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
                b3.config(bg="red")
                b5.config(bg="red")
                b7.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button() 
            
            
            ### CHECK FOR O WIN
            
            
            elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
                b1.config(bg="red")
                b2.config(bg="red")
                b3.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "O Wins!!")
                disable_all_button()
            elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
                b4.config(bg="red")
                b5.config(bg="red")
                b6.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "O Wins!!")
                disable_all_button()
            elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
                b7.config(bg="red")
                b8.config(bg="red")
                b9.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "O Wins!!")
                disable_all_button()

            ###de haut en bas
            elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
                b1.config(bg="red")
                b4.config(bg="red")
                b7.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "O Wins!!")
                disable_all_button()
            elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
                b2.config(bg="red")
                b5.config(bg="red")
                b8.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "O Wins!!")
                disable_all_button()
            elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
                b3.config(bg="red")
                b6.config(bg="red")
                b9.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "X Wins!!")
                disable_all_button()
            ## SUR LE COTE   
            
            elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
                b1.config(bg="red")
                b5.config(bg="red")
                b9.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "O Wins!!")
                disable_all_button()
            elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
                b3.config(bg="red")
                b5.config(bg="red")
                b7.config(bg="red")
                winner = True
                messagebox.showinfo("Tic Tac Toe", "O Wins!!")
                disable_all_button() 
            
                
                if count == 9 and winner == False:
                    messagebox.showinfo("Tic Tac Toe", "C'est Complet\nPersonne n'a gagnez")


        def b_click(b):
            global clicked, count
            
            if b["text"] == " " and clicked == True:
                b["text"] = "X"
                clicked = False
                count +=1
                checkifwon()
            elif b["text"] == " " and clicked == False:
                b["text"] = "O"
                clicked = True
                count += 1
                checkifwon()
            else:
                messagebox.showerror("Tic Tac Toe", "Hey! Cette zone est deja prise\nPrend une nouvelle zone")
                        
                
                
        def restgame():
            global b1, b2, b3, b4, b5, b6, b7, b8, b9
            global clicked, count
            clicked = True
            count = 0
                        
            b1 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
            b2 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
            b3 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
                    
            b4 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
            b5 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
            b6 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
                    
            b7 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
            b8 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
            b9 = Button(new_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
                    
            b1.grid(row=0, column=0)
            b2.grid(row=0, column=1)
            b3.grid(row=0, column=2)
                
            b4.grid(row=1, column=0)
            b5.grid(row=1, column=1)
            b6.grid(row=1, column=2)
                    
            b7.grid(row=2, column=0)
            b8.grid(row=2, column=1)
            b9.grid(row=2, column=2)  
                
        my_menu = Menu(new_window)
        new_window.config(menu=my_menu)

        options_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Option", menu=options_menu)
        options_menu.add_command(label="Rest Game", command=restgame)


        restgame()
 
        
        
        
        







#################### SCRIPT




    def password():
        tk_title = "PASSWORD GENERATOR"
        
        new_window = Toplevel()
        lbl = Label(new_window)
        lbl.pack()
        new_window.geometry('800x600+550+200')
        new_window.overrideredirect(True) # turns off title bar, geometry
        new_window.title(tk_title)
        new_window.config(background='#2c2f33')



        BLACKDISCORD = '#2c2f33'
        title_bar = Frame(new_window, bg=BLACKDISCORD, relief='raised', bd=0,highlightthickness=0)

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
        close_button = Button(title_bar, text='  X  ', command=new_window.destroy,bg=BLACKDISCORD,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
        title_bar_title = Label(title_bar, text=tk_title, bg=BLACKDISCORD,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

        # a frame for the main area of the window, this is where the actual app will go
        window = Frame(new_window, bg=BLACKDISCORD,highlightthickness=0)

        # pack the widgets
        title_bar.pack(fill=X)
        close_button.pack(side=RIGHT,ipadx=7,ipady=1)
        title_bar_title.pack(side=LEFT, padx=10)
        window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
        #xwin=None
        #ywin=None
        # bind title bar motion to the move window function





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
            


        # frame
        frame = Frame(window, bg='#2c2f33')

        # sous boite
        right_frame = Frame(frame, bg='#2c2f33')

        # ajouter texte
        label_title = Label(right_frame, text="Bienvenue sur le g??n??rateur", font=("AusionPersonalUse", 40), bg='#2c2f33', fg='white')
        label_title.pack()

        # ajouter bouton
        github_buttom = Button(right_frame, text="By FrealacOf", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=open_github_channel, bd=0)
        github_buttom.pack(padx=20, pady=20)

        # ajouter champs/entr??e/input
        password_entry = Entry(right_frame, font=("AusionPersonalUse", 40), bg='#2c2f33', fg='white')
        password_entry.pack()

        # Button password
        generat_password_button = Button(right_frame, text="G??n??rer", font=("AusionPersonalUse", 40), bg='#23272a', fg='white', bd=0, highlightthickness=0, command=generate_password)
        generat_password_button.pack(padx=20, pady=20)
        
        btn2= Button(new_window, text="Close Me", command=lambda: new_window.destroy(), font=("AusionPersonalUse", 10), bg='#23272a', fg='white', bd=0, highlightthickness=0)
        btn2.pack()
        # ajouter
        frame.pack(expand=YES)

        # sous boite a droite
        right_frame.grid(row=0, column=1, sticky=W)

        ################################################ end

    # github button script
    def open_github_channel():
        webbrowser.open_new("https://github.com/FrealacOf")


    # menu  script
    def open_discord_channel():
        webbrowser.open_new("https://discord.gg/4P4q4SQ74a")



    def open_instagram_channel():
        webbrowser.open_new("https://www.instagram.com/frealacofficial_/")



    def fps_games():
        os.system("start /B start cmd.exe @cmd /k py fps-game/connect.py")
        
    # sous boite
    right_frame = Frame(frame, bg='#2c2f33')

    # ajouter texte
    label_title = Label(right_frame, text="Bienvenue sur le menu", font=("AusionPersonalUse", 40), bg='#2c2f33', fg='white')
    label_title.pack()

    # ajouter bouton
    github_buttom = Button(right_frame, text="By FrealacOf", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=open_github_channel, bd=0)
    github_buttom.pack(padx=20, pady=20)

    chat_buttom = Button(right_frame, text="CHAT", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=server, bd=0)
    chat_buttom.pack(padx=20, pady=20)
    
    tictac_buttom = Button(right_frame, text="TIC TAC", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=tictac, bd=0)
    tictac_buttom.pack(padx=20, pady=20)

    minecraft_buttom = Button(right_frame, text="MINECRAFT", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=minecraft, bd=0)
    minecraft_buttom.pack(padx=20, pady=20)
    
    fps_buttom = Button(right_frame, text="FPS GAMES", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=fps_games, bd=0)
    fps_buttom.pack(padx=20, pady=20)

    menu_buttom = Button(right_frame, text="PASSWORD", font=("AusionPersonalUse", 25), bg='#23272a', fg='white', command=password, bd=0)
    menu_buttom.pack(padx=20, pady=20)

    # ajouter
    frame.pack(expand=YES)

    # sous boite a droite
    right_frame.grid(row=0, column=1, sticky=W)
    
    
    
    mainloop()



def bar():

    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    w.destroy()
    new_win()
        
    
progress.place(x=-10,y=235)




#############
# frame 333333333333333333333333
#
###########





'''

def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''
a='#2c2f33'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=20,height=2,text='Get Started',command=bar,border=0,fg=a, bg='white', bd=0, highlightthickness=0)
b1.place(x=130,y=200)


######## Label

l1=Label(w,text='MENU',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(w,text='FREALAC',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=155,y=82)

l3=Label(w,text='LOADING PAGE',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)

  


w.mainloop()


