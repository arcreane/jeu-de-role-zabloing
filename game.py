from tkinter import *
from tkinter.messagebox import *
import csv

def gamewindow():
    fenetre2 = Tk()
    fenetre2.geometry("1300x800")
    fenetre2.title("Votre première histoire")
    font1 = ('Comic Sans MS', 40, 'bold italic')

    etape = 1
    f = Frame(fenetre2)
    f.configure(bg='teal')
    f.pack(expand=TRUE, fill=BOTH)


    Label(f, text="Une histoire atypique...", font=font1, bg="cyan").pack(padx=10, pady=10)
    backbutton1 = Button(f, bg="red", text="RETOUR", width=7, height=3)
    backbutton1.pack(padx=4, pady=4)
    backbutton1.place(x=50, y=30)

    with open('textbook.csv', newline='', encoding = 'ASCII') as f:
        reader = csv.reader(f)
        biglist = list(reader)


    def display(etape): #gerer le end et quit et clear a chaqsue fois que le bouton est cliqué

        global lien1, lien2
        lien1 = biglist[int(etape) - 1][3]
        lien2 = biglist[int(etape - 1)][5]

        def endcheck1():
            global lien1
            if lien1 == "end":
                showinfo("GAME OVER", "Fin de la partie!")
                fenetre2.destroy()

            else :
                pass
        def endcheck2():
            global lien1
            if lien2 == "end":
                showinfo("GAME OVER", "Fin de la partie!")
                fenetre2.destroy()

            else :
                pass


        desc1 = biglist[int(etape)-1][1]
        choixuno = biglist[int(etape)-1][2]
        choixdos = biglist[int(etape)-1][4]


        descframe = Frame(fenetre2)
        desclabel = Label(descframe, text = desc1)
        desclabel.pack(padx = 20, pady = 20)

        descframe.pack()
        descframe.place(relx = 0.5, rely = 0.4, anchor = "center")

        choix1 = Button(fenetre2,text=choixuno, command = lambda:[endcheck1(), all_forget(), display(int(lien1))])
        choix1.pack(padx = 10)
        choix1.place(relx = 0.4, rely = 0.5, anchor = 'center')

        choix2 = Button(fenetre2, text = choixdos, command = lambda : [endcheck2(), all_forget(), display(int(lien2))])
        choix2.pack(padx = 10)
        choix2.place(relx = 0.6, rely = 0.5, anchor = 'center')

        if choixuno == "":
            choix1.destroy()
            choix2.place(relx = 0.5, rely = 0.5)
        elif choixdos == "":
            choix2.destroy()
            choix1.place(relx = 0.5, rely = 0.5)

        def all_forget():
            descframe.destroy()
            choix1.destroy()
            choix2.destroy()
    display(etape)



