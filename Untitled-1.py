

from tkinter import *
import tkinter
import pygame
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.title("Gestionnaire de réunion Parent-Professeur")
fenetre.geometry('1000x800')  
fenetre.configure(bg='#000099') 


canvas = Canvas(fenetre, width=1000, height=800,bg="#ffff80")
#py -3.11 "C:\Users\feero\OneDrive\Desktop\Untitled-1.py"
canvas.pack()


img = Image.open(r"C:\Users\feero\OneDrive\Desktop\cla.png")

img = img.resize((800, 500), Image.LANCZOS)

photo2 = ImageTk.PhotoImage(img)

canvas.create_image(100, 100, anchor=NW, image=photo2)
img1 = Image.open(r"C:\Users\feero\OneDrive\Desktop\logo.png")

img1 = img1.resize((300, 200), Image.LANCZOS)

photo1 = ImageTk.PhotoImage(img1)

canvas.create_image(365, 100, anchor=NW, image=photo1)
canvas.photo1 = photo1
canvas.photo2 = photo2

label = Label(
    fenetre,
   text="Gestionnaire de réunion Parent-Professeur",
    bg="#ff6600",
    font=("System", 20))
label.place(x=360, y=30)
label = Label(fenetre,text="ACCUEIL",bg="#faf9f9",font=("System", 40))
label.place(x=525, y=300)
Entrer = Button(canvas,text="Entrer",font=("System", 16),bg="#A4E4FF")
entrer_id = canvas.create_window(470, 385, window=Entrer, anchor="nw")
canvas.tag_raise(entrer_id)

Politique = canvas.create_text(508, 445,  text="Politique de l'Académie des Ninjas",font=("Yu Gothic UI", 10),fill="white"                                                                                                                                                                                                                                                                      )



canvas.tag_bind(Politique, "<Button-1>")
canvas.config(cursor="hand2")

pygame.init()
pygame.mixer.init(frequency=44100)

def play():
    pygame.mixer.music.load(r"C:\Users\feero\OneDrive\Desktop\naruto.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(1) 

play_button = Button(canvas, text="Musique", font=("Segoe UI Black", 22), fg="white",bg="#FF9447",relief=GROOVE, command=play)
canvas.create_window(730, 510, window=play_button, anchor="nw")



fenetre.mainloop()