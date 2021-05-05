from tkinter import*
import os
top = Tk()
top.geometry("200x100")
def main():
     file = "alala.txt"
     os.system(file)
b = Button(top,text = "tutoriel", command = main)

b.pack()

top.mainloop()