from tkinter import *
from math import *
from tkinter import filedialog as fd

fenetre = Tk()
fenetre.geometry("1920x1080")
fenetre.title("v0.1")
font1 = ('Comic Sans MS', 40, 'bold italic')

edittable = PhotoImage(file="edittable.png")
playbook = PhotoImage(file="book.png")


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
    button1.place(x=760, y=340, anchor=CENTER)
    button2.place(x=760, y=480, anchor=CENTER)

def editeur():
    clear()
    Label(f, text="Éditeur de jeu", font=font1, bg="cyan").pack(padx=10, pady=10)

    backbutton1 = Button(f, bg="red", command=fenedit, text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)




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
    button1.place(x=790, y=340, anchor=CENTER)
    button2.place(x=790, y=480, anchor=CENTER)


def menu():
    clear()
    Label(f, text="Bienvenue dans TextGameEngine", font=font1, bg="cyan").pack(padx=4, pady=4, side=TOP)
    button1 = Button(f, command=fenjeu, text='Jouer à un jeu', image=playbook, compound=BOTTOM, width=150,
                     cursor='heart', activebackground="lime")
    button2 = Button(f, command=fenedit, text="Accéder à l'éditeur", image=edittable, compound=BOTTOM, width=150,
                     cursor="heart",activebackground="green")
    button1.pack(padx=5, pady=5)
    button2.pack(padx=5, pady=5)
    button1.place(x=760, y=340, anchor=CENTER)
    button2.place(x=760, y=480, anchor=CENTER)


menu()

fenetre.mainloop()
