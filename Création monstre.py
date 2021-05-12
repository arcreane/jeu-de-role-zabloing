#ligne 89
def mobedit():
    clear()
    Label(f, text="Menu de création de monstres", font=font1, bg="cyan").pack(padx=10, pady=10)

    backbutton1 = Button(f, bg="red", command=fenedit, text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)

    def valider():
        print("Bonjour ")
    champLabel = Label(f, text="Nom du monstre : ")
    champLabel.pack()
    maZone = Entry(f, width=30)
    maZone.insert(0, "Entrez le nom ici")
    maZone.pack()
    monBouton = Button(f, text="Valider", command=valider)
    monBouton.pack()
