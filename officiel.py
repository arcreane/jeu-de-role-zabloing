from tkinter import *
from csv import *
from tkinter import filedialog as fd
from game import gamewindow
import csv

fenetre = Tk()
fenetre.geometry("1920x1080")
fenetre.state("zoomed")
fenetre.title("v0.1")
font1 = ('Comic Sans MS', 40, 'bold italic')

edittable = PhotoImage(file="Textures/edittable.png")
playbook = PhotoImage(file="Textures/book.png")

global rowinfo, mobinfo, iteminfo
etape = 1

all_entries = []
mobinfo = []
iteminfo = []


def fentuto():
    fentuto = Tk()
    fentuto.geometry("900x500")
    fentuto.title("Tuto")
    f3 = Frame(fentuto)
    f3.configure(bg="teal")
    f3.pack(expand=TRUE, fill=BOTH)

    file = open("tuto.txt") #ouvre le fichier txt et prends le contenu pour l'afficher
    data8 = file.read()
    file.close()
    Results=Text(f3, height=400, width=800)
    Results.insert("1.0",data8)
    Results.pack()


def clear(): #fonction pour nettoyer la fenetre
    for widgets in f.winfo_children():
        widgets.destroy()
        widgets.pack_forget()
    f.configure(bg='teal')
    f.pack()


f = Frame(fenetre)
f.configure(bg='teal')
f.pack(expand=TRUE, fill=BOTH)



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
    global scroll_frame #setup de la grille qui peut se scroll
    scroll_frame = Frame(canvas)
    scroll_frame.bind(
        "<Configure>",
        lambda e:canvas.configure(scrollregion=canvas.bbox("all"))
    )

    #nom des colonnes de contenus
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
    save_bouton = Button(header_frame, text="Sauvegarder", command= saveinput)
    save_bouton.pack(pady = 5)

    canvas.create_window((0,0), window = scroll_frame, anchor = "nw")
    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.pack(side = "left", fill = "both", expand = True)
    scrollbar.pack(side = "right", fill="y")



def saveinput():  # enregistrer les données dans le CSV

    choix1 = str(ent2.get())
    lien1 = ent3.get()
    choix2 = str(ent4.get())
    lien2 = ent5.get()

    with open("histoire1.csv", 'a', newline='', encoding = 'UTF-8') as f: #ecrit dans le CSV les differentes variables
        dict_writer = DictWriter(f, fieldnames=['etape', 'description', 'choix1', 'lien1', 'choix2',
                                                        'lien2', 'mobs', 'items'])

        dict_writer.writerow({
            'etape' : rowinfo,
            'description' : textdesc,
            'choix1' : choix1,
            'lien1' : lien1,
            'choix2' : choix2,
            'lien2' : lien2,
            'mobs' : mobinfo,
            'items' : iteminfo,
            })

checks = [] #liste des boutons cochés

def delete_row(): #est sensé verfier si une case est cochée sur une ligne, et retourne 1 si coché
    for rowno, row in reversed(list(enumerate(all_entries))):
        print(all_entries[rowno].val.get())
        l = list(scroll_frame.grid_slaves(row=rowno))
        if all_entries[rowno].val.get() == 1:
            for w in l:
                w.grid_forget()



def addBox(): #bouton pour ajouter une ligne au tableau

    presentrow = len(all_entries)
    next_row = presentrow + 1

    global checks
    global ent2
    global ent3
    global ent4
    global ent5
    var = IntVar()

    numero = Label(scroll_frame, text=str(next_row))
    numero.grid(row=next_row, column=0, pady=(0, 10), padx=(0, 10))

    #differentes zones d'input

    ent1 = Button(scroll_frame, text = "Description", command= lambda :[description(), rownumber()])
    ent1.grid(row=next_row, column=1, pady=(0, 10), padx=(0, 10))
    ent2 = Entry(scroll_frame, width="20")
    ent2.grid(row=next_row, column=2, pady=(0, 10), padx=(0, 10))
    ent3 = Entry(scroll_frame, width="5")
    ent3.grid(row=next_row, column=3, pady=(0, 10), padx=(0, 10))
    ent4 = Entry(scroll_frame, width="20")
    ent4.grid(row=next_row, column=4, pady=(0, 10), padx=(0, 10))
    ent5 = Entry(scroll_frame, width="5")
    ent5.grid(row=next_row, column=5, pady=(0, 10), padx=(0, 10))


    def rownumber():  # on trouve la ligne du bouton appuyé
        global rowinfo
        rowinfo = boutMob.grid_info()["row"]
        global f2
        champEtape = Label(f2, text="Etape actuelle : " +str(rowinfo))
        champEtape.pack( pady=10)
        champEtape.place(relx = 0.9, rely = 0.9, anchor = "center")


    boutMob = Button(scroll_frame, text = "MOBS", width = 10, command = lambda:[mobedit(),rownumber()])
    boutMob.grid(row = next_row, column = 6, pady=(0, 10), padx=(0, 10))
    boutItem = Button(scroll_frame, text = "ITEMS", width=10, command = lambda  :[itemedit(), rownumber()])
    boutItem.grid(row = next_row, column = 7, pady=(0, 10), padx=(0, 10))

    #tentative pour le bouton delete row
    delcheck = Checkbutton(scroll_frame, variable = var)
    delcheck.grid(row = next_row, column = 8, pady = (0,10), padx = (0,5))

    delcheck.val = var
    checks.append(delcheck)
    all_entries.append(delcheck)

def description(): #fenetre pour rentrer la description d'une étape
    global rowinfo
    fendesc = Tk()
    fendesc.geometry("900x500")
    fendesc.title("Description de l'étape")
    global f2
    f2 = Frame(fendesc)
    f2.configure(bg="teal")
    f2.pack(expand=TRUE, fill=BOTH)

    Label(f2, text="Description", font=font1, bg="cyan").pack(padx=10, pady=10)
    zonedesc = Text(f2)
    zonedesc.pack(pady = 10, )
    zonedesc.place(anchor = "center", relx = 0.5, rely= 0.5,height = "300", width = "400")

    def valider():
        global textdesc
        textdesc = str(zonedesc.get("1.0", "end-1c"))


    boutValider = Button(f2, text="Valider", command=valider)
    boutValider.pack(pady=10)
    boutValider.place(relx = 0.5, rely = 0.9)



def mobedit():  # fenetre création de mob
    global rowinfo
    fenmonstre = Tk()
    fenmonstre.geometry("900x500")
    fenmonstre.title("Bestiaire")
    global f2
    f2 = Frame(fenmonstre)
    f2.configure(bg="teal")
    f2.pack(expand=TRUE, fill=BOTH)

    Label(f2, text="Menu de création de monstres", font=font1, bg="cyan").pack(padx=10, pady=10)

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
        global mobinfo
        mobinfo = []
        mobetape = rowinfo
        mobname = maZone.get()
        mobvie = mobVie.get()
        mobatk = mobATK.get()
        mobinfo.extend([mobetape,mobname,mobvie,mobatk])


    boutValider = Button(f2, text="Valider", command=valider)
    boutValider.pack(pady=10)

def itemedit():  # fenetre création d'item

    fenitem = Tk()
    fenitem.geometry("900x500")
    fenitem.title("Armurerie")
    global f2
    f2 = Frame(fenitem)
    f2.configure(bg="teal")
    f2.pack(expand=TRUE, fill=BOTH)

    Label(f2, text="Menu de création des items", font=font1, bg="cyan").pack(padx=10, pady=10)


    champNom = Label(f2, text="Nom de l'item : ")
    champNom.pack(pady=10)
    maZone = Entry(f2, width=30)
    maZone.insert(0, "Entrez le nom ici")
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
        global iteminfo
        iteminfo = []
        itemetape = rowinfo
        itemname = maZone.get()
        itematk = itemATK.get()
        itemdef = itemDEF.get()
        iteminfo.extend([itemetape, itemname, itematk,itemdef])

    boutValider = Button(f2, text="Valider", command=valider)
    boutValider.pack(pady=10)


def fenedit(): #pour acceder à l'éditeur
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

    tuto1 = Button(f, bg="gold", text="Tutoriel", command=fentuto)
    tuto1.pack()
    tuto1.place(relx=0.9, rely = 0.9, anchor="center")



def fenjeu(): #menu pour jouer ou editer une histoire
    clear()
    Label(f, text="Menu du lecteur d'histoires", font=font1, bg="cyan").pack(padx=10, pady=10)

    backbutton1 = Button(f, bg="red", command=menu, text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)

    button1 = Button(f, command= gamewindow, text='Jouer à une histoire', width=100, height=5,
                     cursor='star', activebackground="gold")
    button2 = Button(f, command=fd.askopenfile, text="Continuer une partie", width=100, height=5,
                     cursor="star", activebackground="gold")
    button1.pack(padx=5, pady=5)
    button2.pack(padx=5, pady=5)
    button1.place(relx=0.5, y=340, anchor="center")
    button2.place(relx=0.5, y=480, anchor="center")


def menu(): #menu d'accueil principal
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
