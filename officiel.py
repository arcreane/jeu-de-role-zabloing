from tkinter import *
from math import *
import os
from tkinter import filedialog as fd

fenetre = Tk()
fenetre.geometry("1920x1080")
fenetre.state("zoomed")
fenetre.title("v0.1")
font1 = ('Comic Sans MS', 40, 'bold italic')

edittable = PhotoImage(file="Textures/edittable.png")
playbook = PhotoImage(file="Textures/book.png")


def tuto():
    file = "tuto.txt"
    os.system(file)


def clear():
    for widgets in f.winfo_children():
        widgets.destroy()
        widgets.pack_forget()
    f.configure(bg='teal')
    f.pack()


f = Frame(fenetre)
f.configure(bg='teal')
f.pack(expand=TRUE, fill=BOTH)


def fenjeu():
    clear()
    Label(f, text="Menu du lecteur d'histoires", font=font1, bg="cyan").pack(padx=10, pady=10)

    backbutton1 = Button(f, bg="red", command=menu, text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)

    button1 = Button(f, command= fd.askopenfile, text='Jouer à une histoire', width=100, height=5,
                     cursor='star', activebackground="gold")
    button2 = Button(f, command=fd.askopenfile, text="Continuer une partie", width=100, height=5,
                     cursor="star", activebackground="gold")
    button1.pack(padx=5, pady=5)
    button2.pack(padx=5, pady=5)
    button1.place(relx=0.5, y=340, anchor="center")
    button2.place(relx=0.5, y=480, anchor="center")

def editeur():
    clear()
    Label(f, text="Éditeur de jeu", font=font1, bg="cyan").pack(padx=10, pady=10)

    backbutton1 = Button(f, bg="red", command=fenedit, text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)

    cadre1= LabelFrame(f, text="Votre jeu", bg='light gray', padx=10, pady=10)
    cadre1.pack()
    cadre1.place(relx=0.5, rely = 0.5, anchor = "center")

    canvas = Canvas(cadre1, height = 400, width = 600)
    scrollbar = Scrollbar(cadre1, orient = "vertical", command = canvas.yview)
    scroll_frame = Frame(canvas)
    scroll_frame.bind(
        "<Configure>",
        lambda e:canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0,0), window = scroll_frame, anchor = "nw")
    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.pack(side = "left", fill = "both", expand = True)
    scrollbar.pack(side = "right", fill="y")





def fenedit():
    clear()
    Label(f, text="Menu de l'éditeur de jeu", font=font1, bg="cyan").pack(padx=10, pady=10)

    backbutton1 = Button(f,bg="red", command=menu, text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)

    button1 = Button(f, command=editeur, text='Créer une histoire', width=100, height=5,
                     cursor='star', activebackground="gold")
    button2 = Button(f, command=fd.askopenfile, text="Continuer de modifier une histoire", width=100, height=5,
                     cursor="star", activebackground="gold")
    button1.pack(padx=5, pady=5)
    button2.pack(padx=5, pady=5)
    button1.place(relx=0.5, y=340, anchor="center")
    button2.place(relx=0.5, y=480, anchor="center")

    tuto1 = Button(f, bg="gold", text="Tutoriel", command=tuto)
    tuto1.pack()
    tuto1.place(relx=0.9, rely = 0.9, anchor="center")


def menu():
    clear()
    Label(f, text="Bienvenue dans TextGameEngine", font=font1, bg="cyan").pack(padx=4, pady=4, side=TOP)
    button1 = Button(f, command=fenjeu, text='Jouer à un jeu', image=playbook, compound=BOTTOM, width=150,
                     cursor='heart', activebackground="lime")
    button2 = Button(f, command=fenedit, text="Accéder à l'éditeur", image=edittable, compound=BOTTOM, width=150,
                     cursor="heart",activebackground="green")
    button1.pack(padx=5, pady=5)
    button2.pack(padx=5, pady=5)
    button1.place(relx=0.5, y=340, anchor="center")
    button2.place(relx=0.5, y=480, anchor="center")



menu()

fenetre.mainloop()
