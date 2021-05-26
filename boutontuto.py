from tkinter import *
import os

def main():
     file = "tuto.txt"
     os.system(file)
b = Button(text = "tutoriel", command = main)

b.pack()
b.place()

