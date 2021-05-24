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


def clear(): #fonction pour nettoyer la fenetre
    for widgets in f.winfo_children():
        widgets.destroy()
        widgets.pack_forget()
    f.configure(bg='teal')
    f.pack()


f = Frame(fenetre)
f.configure(bg='teal')
f.pack(expand=TRUE, fill=BOTH)


def fenjeu(): #menu pour jouer ou editer une histoire
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

def editeur(): #editeur de jeu
    clear()
    Label(f, text="Éditeur de jeu", font=font1, bg="cyan").pack(padx=10, pady=10)

    backbutton1 = Button(f, bg="red", command=fenedit, text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)

    cadre1= LabelFrame(f, text="Votre jeu", bg='light gray', padx=10, pady=10)
    cadre1.pack()
    cadre1.place(relx=0.5, rely = 0.55, anchor = "center")

    canvas = Canvas(cadre1, height = 400, width = 800) #cadre qui contient les zones d'input
    scrollbar = Scrollbar(cadre1, orient = "vertical", command = canvas.yview)
    global scroll_frame
    scroll_frame = Frame(canvas)
    scroll_frame.bind(
        "<Configure>",
        lambda e:canvas.configure(scrollregion=canvas.bbox("all"))
    )

    titre1 = Label(scroll_frame)
    titre1.grid(row=0, column=0, pady=(0, 10), padx=(0, 10))
    titre1.configure(text='ID')

    titre2 = Label(scroll_frame)
    titre2.grid(row=0, column=1, pady=(0, 10), padx=(0, 10))
    titre2.configure(text='Description')

    titre3 = Label(scroll_frame)
    titre3.grid(row=0, column=2, pady=(0, 10), padx=(0, 10))
    titre3.configure(text='choix 1')

    titre4 = Label(scroll_frame)
    titre4.grid(row=0, column=3, pady=(0, 10), padx=(0, 10))
    titre4.configure(text='lien1')

    titre5 = Label(scroll_frame)
    titre5.grid(row=0, column=4, pady=(0, 10), padx=(0, 10))
    titre5.configure(text='Choix 2')

    titre6 = Label(scroll_frame)
    titre6.grid(row=0, column=5, pady=(0, 10), padx=(0, 10))
    titre6.configure(text='lien2')

    titre7 = Label(scroll_frame)
    titre7.grid(row=0, column = 8, pady=(0, 10), padx=(0, 10))
    titre7.configure(text='Suppr.')

    #frame au dessus pour les options
    header_frame = Frame(f, bg = "light gray", width = 500, height = 50, pady = 10)
    header_frame.place(anchor = "center", relx = 0.5, rely = 0.1)
    header_frame.pack()

    add_bouton = Button(header_frame, text = "ajouter une ligne", command = addBox)
    add_bouton.pack(pady = 5)
    del_bouton = Button(header_frame, text="supprimer une ligne", command=delete_row)
    del_bouton.pack(pady = 5)

    canvas.create_window((0,0), window = scroll_frame, anchor = "nw")
    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.pack(side = "left", fill = "both", expand = True)
    scrollbar.pack(side = "right", fill="y")




checks = [] #liste des boutons cochés

def delete_row():
    for rowno, row in reversed(list(enumerate(all_entries))):
        print(all_entries[rowno].val.get())
        if all_entries[rowno].val.get() == 1:
            for i in row:
                i.destroy()
                all_entries.pop(rowno)

i=1


def mobedit():  # fenetre création de mob

    fenmonstre = Tk()
    fenmonstre.geometry("900x500")
    fenmonstre.title("Bestiaire")
    f2 = Frame(fenmonstre)
    f2.configure(bg="teal")
    f2.pack(expand=TRUE, fill=BOTH)

    Label(f2, text="Menu de création de monstres", font=font1, bg="cyan").pack(padx=10, pady=10)

    champEtape = Label(f2, text="Etape actuelle : ")
    champEtape.pack(pady=10)
    champNom = Label(f2, text="Nom du monstre : ")
    champNom.pack(pady=10)
    maZone = Entry(f2, width=30)
    maZone.insert(0, "Entrez le nom ici")
    maZone.pack(pady=10)
    champPV = Label(f2, text="PV du monstre : ")
    champPV.pack(pady=10)
    mobVie = Entry(f2, width=30)
    mobVie.insert(0, "Entrez les PV ici")
    mobVie.pack(pady=10)
    champATK = Label(f2, text="Attaque du monstre : ")
    champATK.pack(pady=10)
    mobATK = Entry(f2, width=30)
    mobATK.insert(0, "Entrez l'attaque ici")
    mobATK.pack(pady=10)

    def valider():
        mobetape = "etape du monstre"
        mobname = maZone.get()
        mobvie = mobVie.get()
        mobatk = mobATK.get()

    boutValider = Button(f2, text="Valider", command=valider)
    boutValider.pack(pady=10)

def itemedit():  # fenetre création d'item

    fenitem = Tk()
    fenitem.geometry("900x500")
    fenitem.title("Armurerie")
    f2 = Frame(fenitem)
    f2.configure(bg="teal")
    f2.pack(expand=TRUE, fill=BOTH)

    Label(f2, text="Menu de création des items", font=font1, bg="cyan").pack(padx=10, pady=10)


    champEtape = Label(f2, text="Etape actuelle : ")
    champEtape.pack(pady=10)
    champNom = Label(f2, text="Nom de l'item : ")
    champNom.pack(pady=10)
    maZone = Entry(f2, width=30)
    maZone.insert(0, "Entrez le nom ici'")
    maZone.pack(pady=10)
    champAtk = Label(f2, text="Attaque de l'item : ")
    champAtk.pack(pady=10)
    itemATK = Entry(f2, width=30)
    itemATK.insert(0, "Entrez l'attaque ici")
    itemATK.pack(pady=10)
    champNom = Label(f2, text="Défense de l'item : ")
    champNom.pack(pady=10)
    itemDEF = Entry(f2, width=30)
    itemDEF.insert(0, "Entrez la défense ici")
    itemDEF.pack(pady=10)

    def valider():
        itemetape = "etape de l'item"
        itemname = maZone.get()
        itematk = itemATK.get()
        itemdef = itemDEF.get()

    boutValider = Button(f2, text="Valider", command=valider)
    boutValider.pack(pady=10)


def addBox(): #bouton pour ajouter une ligne au tableau

    next_column = len(all_entries)
    next_row = next_column + 1

    global checks
    var = IntVar()

    numero = Label(scroll_frame, text=str(next_row))
    numero.grid(row=next_row, column=0, pady=(0, 10), padx=(0, 10))

    ent1 = Entry(scroll_frame, width="25")
    ent1.grid(row=next_row, column=1, pady=(0, 10), padx=(0, 10))
    ent2 = Entry(scroll_frame, width="20")
    ent2.grid(row=next_row, column=2, pady=(0, 10), padx=(0, 10))
    ent3 = Entry(scroll_frame, width="5")
    ent3.grid(row=next_row, column=3, pady=(0, 10), padx=(0, 10))
    ent4 = Entry(scroll_frame, width="20")
    ent4.grid(row=next_row, column=4, pady=(0, 10), padx=(0, 10))
    ent5 = Entry(scroll_frame, width="5")
    ent5.grid(row=next_row, column=5, pady=(0, 10), padx=(0, 10))

    def rownumber():  # on chope la ligne du bouton appuyé
        global rowinfo
        rowinfo = boutMob.grid_info()["row"]


    boutMob = Button(scroll_frame, text = "MOBS", width = 10, command = lambda:[mobedit(),rownumber()])
    boutMob.grid(row = next_row, column = 6, pady=(0, 10), padx=(0, 10))
    boutItem = Button(scroll_frame, text = "ITEMS", width=10, command = lambda  :[itemedit(), rownumber()])
    boutItem.grid(row = next_row, column = 7, pady=(0, 10), padx=(0, 10))

    delcheck = Checkbutton(scroll_frame, variable = var)
    delcheck.grid(row = next_row, column = 8, pady = (0,10), padx = (0,5))

    delcheck.val = var
    checks.append(delcheck)

    all_entries.append(delcheck)



def fenedit():
    clear()
    all_entries.clear()
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
