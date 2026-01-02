"Code de l'écran d'accueil"

from tkinter import * "du module tkinter importe"
import tkinter
import pygame " on importe pygame"
from PIL import Image, ImageTk

fenetre = Tk() "Creation d'une fenetre"
fenetre.title("Gestionnaire de réunion Parent-Professeur")"On intitule la fenetre"
fenetre.geometry('1000x800')  "On lui donne des dimensions"
fenetre.configure(bg='#000099') "La couleur du fond est initialisé"


canvas = Canvas(fenetre, width=1000, height=800,bg="#ffff80") "On crée un canvas et on colore son fond"
#py -3.11 "C:\Users\feero\OneDrive\Desktop\Untitled-1.py"
canvas.pack()


img = Image.open(r"C:\Users\feero\OneDrive\Desktop\cla.png") "On importe une image"

img = img.resize((800, 500), Image.LANCZOS) "On modifie la taille de l'image"

photo2 = ImageTk.PhotoImage(img) "On sauvegarde l'image dans une variable photo2"

canvas.create_image(100, 100, anchor=NW, image=photo2) "On place l'image aux coordonnés x = 100 et y = 100"
img1 = Image.open(r"C:\Users\feero\OneDrive\Desktop\logo.png") "On importe une image"

img1 = img1.resize((300, 200), Image.LANCZOS) "On modifie la taille de l'image"

photo1 = ImageTk.PhotoImage(img1) "On sauvegarde l'image dans une variable photo2"

canvas.create_image(365, 100, anchor=NW, image=photo1) "On place l'image aux coordonnés x = 100 et y = 100"
canvas.photo1 = photo1
canvas.photo2 = photo2

label = Label(
    fenetre,
   text="Gestionnaire de réunion Parent-Professeur",
    bg="#ff6600",
    font=("System", 20)) "On crée une ligne de texte"
label.place(x=360, y=30) "On lui donne les coordonnées suivantes"
label = Label(fenetre,text="ACCUEIL",bg="#faf9f9",font=("System", 40)) "On crée une ligne de texte"
label.place(x=525, y=300) "On lui donne les coordonnées suivantes"
Entrer = Button(canvas,text="Entrer",font=("System", 16),bg="#A4E4FF") "On crée un bouton"
entrer_id = canvas.create_window(470, 385, window=Entrer, anchor="nw") "On lui donne les coordonnées suivantes"
canvas.tag_raise(entrer_id)

Politique = canvas.create_text(508, 445,  text="Politique de l'Académie des Ninjas",font=("Yu Gothic UI", 10),fill="white"  "On crée le texte sur un canvas"                                                                                                                                                                                                                                                                   )

canvas.tag_bind(Politique, "<Button-1>") "On lui associe un evenement clique gauche"
canvas.config(cursor="hand2") "Change le curseur de la souris en main"

pygame.init() "On initialise pygame"
pygame.mixer.init(frequency=44100) " On initialise le module audio de Pygame"

def play(): "Crée une fonction play"
    pygame.mixer.music.load(r"C:\Users\feero\OneDrive\Desktop\naruto.mp3") "On importe le fichier Naruto"
    pygame.mixer.music.play(loops=-1) "Lance la musique dans une boucle infiniee"
    pygame.mixer.music.set_volume(1)"On définit le volume"

play_button = Button(canvas, text="Musique", font=("Segoe UI Black", 22), fg="white",bg="#FF9447",relief=GROOVE, command=play)"On crée un bouton"
canvas.create_window(730, 510, window=play_button, anchor="nw") "on lui associe des coordonnées"



fenetre.mainloop() "On ferme la fenêtre"
