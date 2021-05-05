from tkinter import *
from math import *
from tkinter.filedialog import *

fenetre = Tk()
fenetre.geometry("1920x1080")
fenetre.title("v0.1")
font1=('Comic Sans MS', 40, 'bold italic')

edittable = PhotoImage(file = "edittable.png")
playbook = PhotoImage(file="book.png")

def clear():
    for widgets in f.winfo_children():
        widgets.destroy()
        widgets.pack_forget()
    f.configure(bg='teal')
    f.pack()

f=Frame(fenetre)
f.configure(bg='teal')
Label(f,text="Bienvenue dans TextGameEngine", font = font1, bg = "cyan").pack(padx = 4, pady= 4,side = TOP)

button1 = Button(f, command=clear, text ='Jouer à un jeu', image = playbook, compound = BOTTOM, width = 150, cursor='heart')
button2 = Button(f, command=lambda:[clear(), fenedit()],text ="Accéder à l'éditeur" , image = edittable, compound = BOTTOM, width = 150, cursor="heart")
button1.pack( padx=5, pady=5)
button2.pack( padx=5, pady=5)
button1.place(x=760, y=340, anchor=CENTER)
button2.place(x=760, y=480, anchor=CENTER)
f.pack(expand=TRUE, fill=BOTH)

def fenjeu():
    Label(f, text="Menu du lecteur d'histoires", font=font1, bg="cyan").pack(padx=10, pady=10)

def fenedit():
    Label(f, text="Menu de l'éditeur de jeu", font = font1, bg = "cyan").pack(padx = 10,pady=10)




fenetre.mainloop()
