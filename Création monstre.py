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

all_entries = []



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
    cadre1.place(relx=0.5, rely = 0.55, anchor = "center")

    canvas = Canvas(cadre1, height = 400, width = 600)
    scrollbar = Scrollbar(cadre1, orient = "vertical", command = canvas.yview)
    global scroll_frame
    scroll_frame = Frame(canvas)
    scroll_frame.bind(
        "<Configure>",
        lambda e:canvas.configure(scrollregion=canvas.bbox("all"))
    )

    header_frame = Frame(f, bg = "light gray", width = 500, height = 50, pady = 10)
    header_frame.place(anchor = "center", relx = 0.5, rely = 0.1)
    header_frame.pack()

    add_bouton = Button(header_frame, text = "ajouter une ligne", command = addBox)
    add_bouton.pack()



    canvas.create_window((0,0), window = scroll_frame, anchor = "nw")
    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.pack(side = "left", fill = "both", expand = True)
    scrollbar.pack(side = "right", fill="y")


def addBox():
    next_column = len(all_entries)
    next_row = next_column + 1

    numero = Label(scroll_frame, text=str(next_column + 1))
    numero.grid(row=next_row, column=0, pady=(0, 10), padx=(0, 10))

    ent1 = Entry(scroll_frame, width="15")
    ent1.grid(row=next_row, column=1, pady=(0, 10), padx=(0, 10))
    ent2 = Entry(scroll_frame, width="15")
    ent2.grid(row=next_row, column=2, pady=(0, 10), padx=(0, 10))
    ent3 = Entry(scroll_frame, width="5")
    ent3.grid(row=next_row, column=3, pady=(0, 10), padx=(0, 10))
    ent4 = Entry(scroll_frame, width="15")
    ent4.grid(row=next_row, column=4, pady=(0, 10), padx=(0, 10))
    ent5 = Entry(scroll_frame, width="5")
    ent5.grid(row=next_row, column=5, pady=(0, 10), padx=(0, 10))

    all_entries.append(ent1)



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
    button3 = Button(f, command=mobedit, text='Créer un monstre', width=100, height=5,
                     cursor='star', activebackground="gold")
    button1.pack(padx=5, pady=5)
    button2.pack(padx=5, pady=5)
    button1.place(relx=0.5, y=340, anchor="center")
    button2.place(relx=0.5, y=480, anchor="center")
    button3.pack(padx=5, pady=5)
    button1.place(relx=0.5, y=220, anchor="center")

    tuto1 = Button(f, bg="gold", text="Tutoriel", command=tuto)
    tuto1.pack()
    tuto1.place(relx=0.9, rely = 0.9, anchor="center")

def mobedit():
    popup = Tk()
    popup.geometry("600x400")
    popup.title("Mob creator")
    popframe=Frame(popup)

    Label(popframe, text="Bienvenue dans TextGameEngine", font=font1, bg="cyan").pack(padx=4, pady=4, side=TOP)

    champLabel = Label(popframe, text="Nom du monstre : ")
    champLabel.pack()
    global maZone
    maZone = Entry(popframe, width=40)
    maZone.insert(0, "Entrez le nom ici")
    maZone.pack()
    monBouton = Button(popframe, text="Valider", command=valider)
    monBouton.pack()
    popframe.pack(bg="red", expand=TRUE, fill=BOTH)


def valider():
    Statmob = maZone.get()
    print (Statmob)


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

