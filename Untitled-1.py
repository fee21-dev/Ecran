

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
def ouvrir_regle(event = None):
    fenetre = Toplevel()
    fenetre.title("Réunion")
    fenetre.geometry("600x400")
    fenetre.configure(bg="#FF9620")

    # Titre
    title_label = Label(
        fenetre,
        text="Règle pour la Réunion Parent - Professeur",
        bg="#FF9620",
        font=("Arial", 16, "bold")
    )
    title_label.place(x=10,y=50)

    # Texte
    text_label = Label(
        fenetre,
        text=(
            "Ne pas ramener d'arme\n"
            "Respecter les horaires\n"
            "Être poli\n"
            "Ne pas tuer votre enfant\n"
            "Apporter le nécessaire de document\n"
            "Ne pas faire n'importe quoi\n"
            "Ne pas rater la salle"
        ),
        bg="#FF9620",
        justify=LEFT
    )
    text_label.place(x=20,y=50)

    # Case à cocher
    agree_var = BooleanVar(master=fenetre)
    checkbutton = Checkbutton(
        fenetre,
        text="J'accepte toutes les règles",
        variable=agree_var,
        bg="#FF9620"
    )
    checkbutton.place(x=40,y=50)
    fenetre.protocol("WM_DELETE_WINDOW", lambda: None) 
    
    bouton = Button(
        fenetre,
        text="Fermer",
        command=fenetre.destroy,
        bg="#3139DE",
        fg="white"
    )
    bouton.place(x=50, y=20)
Politique = canvas.create_text(508, 445,  text="Politique de l'Académie des Ninjas",font=("Yu Gothic UI", 10),fill="white"                                                                                                                                                                                                                                                                      )


canvas.tag_bind(Politique, "<Button-1>",ouvrir_regle)
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