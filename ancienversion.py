from tkinter import *
from math import *
from tkinter.filedialog import *




fenetre = Tk()
fenetre.geometry("1280x720")
fenetre.title("v0.1")
label = Label(fenetre)
label.pack()
font1=('Comic Sans MS', 40, 'bold italic')

def clear():
    for widget in canvas.winfo_children():
        widget.destroy()
        canvas.delete("all")
    canvas.configure(background = "teal")
    canvas.pack()

canvas = Canvas(fenetre, width=1280, height=720, background='teal')
txt = canvas.create_text(640 , 200, text="Bienvenue dans TextGameEngine !", font=font1, fill="gold", anchor=CENTER)
canvas.pack()
button1 = Button(canvas, command = clear, text ='Jouer à un jeu', height = 2, width = 25, cursor='heart')
button2 = Button(canvas, command= lambda :[clear(),fenedit()], text ="Accéder à l'éditeur" ,  height = 2, width = 25, cursor="heart")
button1.pack( padx=5, pady=5)
button2.pack( padx=5, pady=5)
button1.place(x=640, y=340, anchor=CENTER)
button2.place(x=640, y=400, anchor=CENTER)

def fenedit():
    frame1 = Frame(canvas, borderwidth = 5, relief = GROOVE)
    frame1.pack(side=LEFT)
    Label(frame1, text="Vous êtes dans l'éditeur de jeu.", font = font1, bg = "cyan").pack(padx = 10,pady=10)


fenetre.mainloop()
