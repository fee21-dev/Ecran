"""
Rendez-vous Parent-Professeur avec les professeurs de l'Académie Ninja de Konoha
Auteure: Feerose & Sophie
Date : On s'est plus mais c'est pas grave
Organisateur : rendez vous parent professeur avec le thème de naruto
Plan : 
1. Accueil
2. Sélection des professeurs
3. Remplissage du formulaire
4. Confirmation

"""

#Importation des bibliothèques nécessaires
from tkinter import *
from tkinter import ttk
import tkinter
import pygame
from PIL import Image, ImageTk
from tkinter import messagebox

"""
Toutes les images et la variables attribuées

- Veuillez modifier les chemins d'accès aux images ici
- Il y en a un autre dans la ligne 1373 et ligne 1458

"""
img = Image.open(r"C:\Users\feero\OneDrive\Desktop\cla.png")
img1 = Image.open(r"C:\Users\feero\OneDrive\Desktop\logo.png")
iru = Image.open(r"C:\Users\feero\OneDrive\Desktop\iru.png")
kak = Image.open(r"C:\Users\feero\OneDrive\Desktop\kak.png")
asu = Image.open(r"C:\Users\feero\OneDrive\Desktop\asu.png")
kur = Image.open(r"C:\Users\feero\OneDrive\Desktop\kur.png")
gai = Image.open(r"C:\Users\feero\OneDrive\Desktop\gai.png")
jir = Image.open(r"C:\Users\feero\OneDrive\Desktop\jir.png")
img_og = Image.open(r"C:\Users\feero\OneDrive\Desktop\par1.png")
ten = Image.open(r"C:\Users\feero\OneDrive\Desktop\ten.png")


"""
Création de la 1ère fenêtre : l'accueil

"""

#Création d'une fenêtre ; son initialisation ; ses dimentions ; sa couleur de fond
fenetre = Tk()
fenetre.title("Gestionnaire de réunion Parent-Professeur")
fenetre.geometry('1000x800')

#Mettre le container en plein écran
container = Frame(fenetre)
container.place(x=0, y=0, relwidth=1, relheight=1)
#Couleur de fond et dimentions
panel_accueil = Frame(container, bg='#000099')
panel_accueil.place(x=0, y=0, relwidth=1, relheight=1)

#Création d'un canva et son fond
canvas = Canvas(panel_accueil, width=1000, height=800, bg="#ffff80")
canvas.pack()



"""
Importation, modification et sauvegarde -> variable } images pour l'accueil

"""

#Photo2
img = img.resize((800, 500), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(img)
#Placement de l'image sur le canva
canvas.create_image(100, 100, anchor=NW, image=photo2)

#Photo1
img1 = img1.resize((300, 200), Image.LANCZOS)
photo1 = ImageTk.PhotoImage(img1)
#Placement de l'image sur le canva
canvas.create_image(365, 100, anchor=NW, image=photo1)

#Les deux photos sur le canva
canvas.photo1 = photo1
canvas.photo2 = photo2



"""
Création des labels et boutons de l'accueil

"""

#Création d'un label avec du texte, une couleur de fond et une police
label = Label(panel_accueil,
              text="Gestionnaire de réunion Parent-Professeur",
              bg="#ff6600",
              font=("System", 20)
              )
label.place(x=360, y=30)
label = Label(panel_accueil,
              text="ACCUEIL",
              bg="#faf9f9",
              font=("System", 40)
              )
label.place(x=525, y=300)


#Création d'un panel pour l'écran de sélection des professeurs
panel1 = Frame(container,
               bg="#955B43",
               bd=0,
               highlightthickness=0
               )
panel1.place(x=0, y=0, relwidth=1, relheight=1)
#Création d'un canva pour le panel des professeurs
canva_panel1 = Canvas(panel1, width=1400, height=1000, bg="#955B43", highlightthickness=0)
canva_panel1.place(x=0, y=10)


#Titre du panel
Label(panel1,
      text="Les Professeurs de l'académie",
      font=("Modern", 40),bg="#FFF2A7"
      ).place(x=380, y=15)


#Importation des images des professeurs
#Iruka
iru = iru.resize((230, 500), Image.LANCZOS)
photoiru = ImageTk.PhotoImage(iru)
#Placement de l'image sur le canva
image_coord = canva_panel1.create_image(10, 75, anchor=NW, image=photoiru)
canva_panel1.photoiru = photoiru

#Kakashi
kak = kak.resize((190, 500), Image.LANCZOS)
photokak = ImageTk.PhotoImage(kak)
image_coord = canva_panel1.create_image(220, 75, anchor=NW, image=photokak)
canva_panel1.photokak = photokak

#Asuma
asu = asu.resize((290, 560), Image.LANCZOS)
photoasu = ImageTk.PhotoImage(asu)
image_coord = canva_panel1.create_image(350, 15, anchor=NW, image=photoasu)
canva_panel1.photoasu = photoasu

#Kurenai
kur = kur.resize((260, 500), Image.LANCZOS)
photokur = ImageTk.PhotoImage(kur)
image_coord = canva_panel1.create_image(580, 88, anchor=NW, image=photokur)
canva_panel1.photokur = photokur

#Gai
gai = gai.resize((230, 500), Image.LANCZOS)
photogai = ImageTk.PhotoImage(gai)
image_coord = canva_panel1.create_image(825, 78, anchor=NW, image=photogai)
canva_panel1.photogai = photogai

#Jiraya
jir = jir.resize((260, 520), Image.LANCZOS)
photojir = ImageTk.PhotoImage(jir)
image_coord = canva_panel1.create_image(1020, 48, anchor=NW, image=photojir)
canva_panel1.photojir = photojir


#Création des boutons pour chaque professeur avec leur fonction associée
Iruka = Button(
    canva_panel1,
    text="Iruka-Sensei",
    font=("System", 16),
    bg="#F0FFA4"
)

iruka_id = canva_panel1.create_window(
    90, 450,   
    window=Iruka,
    anchor="nw")

canva_panel1.tag_raise(iruka_id)
def ouvrir_iruka():
    fen = Toplevel()  
    fen.title("Lettre pour Iruka-sensei")
    fen.geometry("1200x800")

    #Déclaration des variables pour les champs de saisie
    #Pour le nom/clan = des lettres ou mots etc
    nom = StringVar()
    clan = StringVar()
    jour = StringVar(value='Lundi')
    heure = StringVar(value='08:00')

    
    panel = Frame(fen)
    panel.pack(fill="both", expand=True)

    canvas = Canvas(panel)
    canvas.pack(fill="both", expand=True)

    
    TEXT_OFFSET_X = 200
    TEXT_Y = 175
    TEXT_WIDTH = 820

    
    entry_nom = Entry(panel, textvariable=nom, width=25)
    entry_jour = OptionMenu(panel, jour, 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche')
    entry_heure = OptionMenu(panel, heure, *[f'{h:02d}:00' for h in range(0, 24)])
    entry_clan = Entry(panel, textvariable=clan, width=25)
    
    #Fonction de validation et création du billet de confirmation
    def valider_iruka():
        #Vérification du nom et du clan non vides -> erreur
        if not nom.get().strip() or not clan.get().strip():
            messagebox.showerror("Erreur", "Veuillez remplir le nom et le clan!")
            return
        
        #Créer un billet de confirmation
        billet = Toplevel(fen)
        billet.title("Confirmation du rendez-vous")
        billet.geometry("600x400")
        
        #Contenu du billet
        texte_billet = f"""
        CONFIRMATION DE RENDEZ-VOUS
        ---------------------------
        
        Professeur : Iruka-sensei
        
        Étudiant : {nom.get()}
        Clan : {clan.get()}
        
        Jour : {jour.get()}
        Heure : {heure.get()}
        
        ---------------------------
        Rendez-vous confirmé!
        """

        #Affichage du billet
        canvas = Canvas(billet)
        canvas.pack(fill=BOTH, expand=True)

        def redraw_billet(event=None):
            canvas.delete("all")

            win_width = canvas.winfo_width()
            win_height = canvas.winfo_height()

            image = ten.resize((win_width, win_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            canvas.image = photo
            canvas.create_image(0, 0, anchor=NW, image=photo)

            TEXT_X = 70 + TEXT_OFFSET_X

            canvas.create_text(
                TEXT_X, TEXT_Y,
                text = texte_billet,
                font = ("Serif", 10),
                fill = "black",
                justify = CENTER,
                width = TEXT_WIDTH
            )

        canvas.bind("<Configure>", redraw_billet)


        #Bouton OK pour fermer le billet + la fenêtre principale
        boutton_ok = Button(billet, text="Voir Retour", command=lambda: [billet.destroy(), fen.destroy()])
        boutton_ok.pack(pady=5)

    bouton = Button(panel, text="Valider", command=valider_iruka)

    
    def redraw(event=None):
        canvas.delete("all")
        
        win_width = canvas.winfo_width()
        win_height = canvas.winfo_height()
        
        image = img_og.resize((win_width, win_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, -50, anchor=NW, image=photo)
        
        TEXT_X = 60 + TEXT_OFFSET_X
        
        
        canvas.create_text(
            TEXT_X, TEXT_Y,
            anchor=NW,
            text="Cher Iruka-sensei,\nNous sommes les parents de",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_window(TEXT_X + 300, TEXT_Y + 30, window=entry_nom)  

        canvas.create_text(
            TEXT_X, TEXT_Y + 80,
            anchor=NW,
            text="Qui est élève de votre classe à l’Académie ninja de Konoha." \
                "\nNous nous permettons de vous écrire car nous souhaiterions convenir d’un " \
                "rendez-vous parents-professeurs afin de discuter de ses progrès, "
                "de son comportement, et de son utilisation excessive du jutsu.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 180,
            anchor=NW,
            text="Notre enfant nous a récemment rapporté qu'il a été exclue due aux bavardages en classe.",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 300, TEXT_Y + 180, anchor=NW)

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 220,
            anchor=NW,
            text="Nous sommes disponibles le",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 210 + 25, TEXT_Y + 226, window=entry_jour)  

        canvas.create_text(
            TEXT_X + 360, TEXT_Y + 220,
            anchor=NW,
            text="à partir de",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 470 + 16, TEXT_Y + 226, window=entry_heure)

        canvas.create_text(
            TEXT_X, TEXT_Y + 260,
            anchor=NW,
            text="mais restons bien entendu flexibles selon votre emploi du temps chargé de sensei.\n"
                 "Nous vous remercions par avance pour votre patience, votre pédagogie et "
                 "votre dévouement envers les jeunes ninjas du village caché de Konoha.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 380 - 30,  
            anchor=NW,
            text="Le Clan :",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 135, TEXT_Y + 380 - 30 + 9, window=entry_clan)  

        
        canvas.create_window(TEXT_X + 740, TEXT_Y + 350, window=bouton)

    canvas.bind("<Configure>", redraw)
Iruka.config(command=ouvrir_iruka)


Kakashi = Button(
    canva_panel1,
    text="Kakashi-Sensei",
    font=("System", 16),
    bg="#F0FFA4"
)

kakashi_id = canva_panel1.create_window(
    260, 450,   
    window=Kakashi,
    anchor="nw")

canva_panel1.tag_raise(kakashi_id)
def ouvrir_ka():
    fen = Toplevel()  
    fen.title("Lettre pour Kakashi-sensei")
    fen.geometry("1200x800")

    
    #Déclaration des variables pour les champs de saisie
    #Pour le nom/clan = des lettres ou mots etc
    nom = StringVar()
    clan = StringVar()
    jour = StringVar(value='Lundi')
    heure = StringVar(value='14:00')

    
    panel = Frame(fen)
    panel.pack(fill="both", expand=True)

    canvas = Canvas(panel)
    canvas.pack(fill="both", expand=True)

    
    TEXT_OFFSET_X = 200
    TEXT_Y = 175
    TEXT_WIDTH = 820

    
    entry_nom = Entry(panel, textvariable=nom, width=25)
    entry_jour = OptionMenu(panel, jour, 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche')
    entry_heure = OptionMenu(panel, heure, *[f'{h:02d}:00' for h in range(14, 18)])
    entry_clan = Entry(panel, textvariable=clan, width=25)
    
    def valider_kakashi():
        # Vérifier que le nom et le clan ne sont pas vides
        if not nom.get().strip() or not clan.get().strip():
            messagebox.showerror("Erreur", "Veuillez remplir le nom et le clan!")
            return
        
        # Créer un billet de confirmation
        billet = Toplevel(fen)
        billet.title("Confirmation du rendez-vous")
        billet.geometry("600x400")
        
        # Contenu du billet
        texte_billet = f"""
        CONFIRMATION DE RENDEZ-VOUS
        ---------------------------
        
        Professeur : Kakashi-sensei
        
        Étudiant : {nom.get()}
        Clan : {clan.get()}
        
        Jour : {jour.get()}
        Heure : {heure.get()}
        
        ---------------------------
        Rendez-vous confirmé!
        """
        
        #Affichage du billet
        canvas = Canvas(billet)
        canvas.pack(fill=BOTH, expand=True)

        def redraw_billet(event=None):
            canvas.delete("all")

            win_width = canvas.winfo_width()
            win_height = canvas.winfo_height()

            image = ten.resize((win_width, win_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            canvas.image = photo
            canvas.create_image(0, 0, anchor=NW, image=photo)

            TEXT_X = 70 + TEXT_OFFSET_X

            canvas.create_text(
                TEXT_X, TEXT_Y,
                text = texte_billet,
                font = ("Serif", 10),
                fill = "black",
                justify = CENTER,
                width = TEXT_WIDTH
            )

        canvas.bind("<Configure>", redraw_billet)
        
        btn_ok = Button(billet, text="OK", command=lambda: [billet.destroy(), fen.destroy()])
        btn_ok.pack(pady=5)
    
    bouton = Button(panel, text="Valider", command=valider_kakashi)

    
    def redraw(event=None):
        canvas.delete("all")
        
        win_width = canvas.winfo_width()
        win_height = canvas.winfo_height()
        
        image = img_og.resize((win_width, win_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, -50, anchor=NW, image=photo)
        
        TEXT_X = 60 + TEXT_OFFSET_X
        
        
        canvas.create_text(
            TEXT_X, TEXT_Y,
            anchor=NW,
            text="Cher Kakashi-sensei,\nNous sommes les parents de",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_window(TEXT_X + 300, TEXT_Y + 30, window=entry_nom)  

        canvas.create_text(
            TEXT_X, TEXT_Y + 80,
            anchor=NW,
            text="Qui est élève de votre classe à l’Académie ninja de Konoha." \
                "\nNous nous permettons de vous écrire car nous souhaiterions convenir d’un " \
                "rendez-vous parents-professeurs afin de discuter de ses progrès, "
                "de son comportement, et de son utilisation excessive du jutsu.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 180,
            anchor=NW,
            text="Notre enfant nous a récemment rapporté qu'il a été exclue de l'académie.",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 300, TEXT_Y + 180, anchor=NW)

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 220,
            anchor=NW,
            text="Nous sommes disponibles le",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 210 + 25, TEXT_Y + 226, window=entry_jour)  

        canvas.create_text(
            TEXT_X + 360, TEXT_Y + 220,
            anchor=NW,
            text="à partir de",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 470 + 16, TEXT_Y + 226, window=entry_heure)

        canvas.create_text(
            TEXT_X, TEXT_Y + 260,
            anchor=NW,
            text="mais restons bien entendu flexibles selon votre emploi du temps chargé de sensei.\n"
                 "Nous vous remercions par avance pour votre patience, votre pédagogie et "
                 "votre dévouement envers les jeunes ninjas du village caché de Konoha.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 380 - 30,  
            anchor=NW,
            text="Le Clan :",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 135, TEXT_Y + 380 - 30 + 9, window=entry_clan)  

        
        canvas.create_window(TEXT_X + 740, TEXT_Y + 350, window=bouton)

    canvas.bind("<Configure>", redraw)
Kakashi.config(command=ouvrir_ka)


Asuma = Button(
    canva_panel1,
    text="Asuma-Sensei",
    font=("System", 16),
    bg="#F0FFA4"
)

asuma_id = canva_panel1.create_window(
    441, 450,   
    window=Asuma,
    anchor="nw")

canva_panel1.tag_raise(asuma_id)
def ouvrir_a():
    fen = Toplevel() 
    fen.title("Lettre pour Asuma-sensei")
    fen.geometry("1200x800")

    
    #Déclaration des variables pour les champs de saisie
    #Pour le nom/clan = des lettres ou mots etc
    nom = StringVar()
    clan = StringVar()
    jour = StringVar(value='Mercredi')
    heure = StringVar(value='08:00')

    
    panel = Frame(fen)
    panel.pack(fill="both", expand=True)

    canvas = Canvas(panel)
    canvas.pack(fill="both", expand=True)

    
    TEXT_OFFSET_X = 200
    TEXT_Y = 175
    TEXT_WIDTH = 820

    
    entry_nom = Entry(panel, textvariable=nom, width=25)
    entry_jour = OptionMenu(panel, jour, 'Mercredi', 'Samedi', 'Dimanche')
    entry_heure = OptionMenu(panel, heure, *[f'{h:02d}:00' for h in range(8, 18)])
    entry_clan = Entry(panel, textvariable=clan, width=25)
    
    def valider_asuma():
        # Vérifier que le nom et le clan ne sont pas vides
        if not nom.get().strip() or not clan.get().strip():
            messagebox.showerror("Erreur", "Veuillez remplir le nom et le clan!")
            return
        
        # Créer un billet de confirmation
        billet = Toplevel(fen)
        billet.title("Confirmation du rendez-vous")
        billet.geometry("600x400")
        
        # Contenu du billet
        texte_billet = f"""
        CONFIRMATION DE RENDEZ-VOUS
        ---------------------------
        
        Professeur : Asuma-sensei
        
        Étudiant : {nom.get()}
        Clan : {clan.get()}
        
        Jour : {jour.get()}
        Heure : {heure.get()}
        
        ---------------------------
        Rendez-vous confirmé!
        """
        
        #Affichage du billet
        canvas = Canvas(billet)
        canvas.pack(fill=BOTH, expand=True)

        def redraw_billet(event=None):
            canvas.delete("all")

            win_width = canvas.winfo_width()
            win_height = canvas.winfo_height()

            image = ten.resize((win_width, win_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            canvas.image = photo
            canvas.create_image(0, 0, anchor=NW, image=photo)

            TEXT_X = 70 + TEXT_OFFSET_X

            canvas.create_text(
                TEXT_X, TEXT_Y,
                text = texte_billet,
                font = ("Serif", 10),
                fill = "black",
                justify = CENTER,
                width = TEXT_WIDTH
            )

        canvas.bind("<Configure>", redraw_billet)
        
        btn_ok = Button(billet, text="OK", command=lambda: [billet.destroy(), fen.destroy()])
        btn_ok.pack(pady=5)
    
    bouton = Button(panel, text="Valider", command=valider_asuma)

    
    def redraw(event=None):
        canvas.delete("all")
        
        win_width = canvas.winfo_width()
        win_height = canvas.winfo_height()
        
        image = img_og.resize((win_width, win_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, -50, anchor=NW, image=photo)
        
        TEXT_X = 60 + TEXT_OFFSET_X
        
        
        canvas.create_text(
            TEXT_X, TEXT_Y,
            anchor=NW,
            text="Cher Asuma-sensei,\nNous sommes les parents de",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_window(TEXT_X + 300, TEXT_Y + 30, window=entry_nom)  

        canvas.create_text(
            TEXT_X, TEXT_Y + 80,
            anchor=NW,
            text="Qui est élève de votre classe à l’Académie ninja de Konoha." \
                "\nNous nous permettons de vous écrire car nous souhaiterions convenir d’un " \
                "rendez-vous parents-professeurs afin de discuter de ses progrès, "
                "de son comportement, et de son utilisation excessive du jutsu.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 180,
            anchor=NW,
            text="Notre enfant nous a récemment rapporté que vous fumez trop et qu'il y a un risque de cancer.",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 300, TEXT_Y + 180, anchor=NW)

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 220,
            anchor=NW,
            text="Nous sommes disponibles le",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 210 + 25, TEXT_Y + 226, window=entry_jour)  

        canvas.create_text(
            TEXT_X + 360, TEXT_Y + 220,
            anchor=NW,
            text="à partir de",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 470 + 16, TEXT_Y + 226, window=entry_heure)

        canvas.create_text(
            TEXT_X, TEXT_Y + 260,
            anchor=NW,
            text="mais restons bien entendu flexibles selon votre emploi du temps chargé de sensei.\n"
                 "Nous vous remercions par avance pour votre patience, votre pédagogie et "
                 "votre dévouement envers les jeunes ninjas du village caché de Konoha.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 380 - 30,  
            anchor=NW,
            text="Le Clan :",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 135, TEXT_Y + 380 - 30 + 9, window=entry_clan)  

        
        canvas.create_window(TEXT_X + 740, TEXT_Y + 350, window=bouton)

    canvas.bind("<Configure>", redraw)
Asuma.config(command=ouvrir_a)


K = Button(
    canva_panel1,
    text="Kurenai-Sensei",
    font=("System", 16),
    bg="#F0FFA4"
)

k_id = canva_panel1.create_window(
    651, 450,   
    window=K,
    anchor="nw")

canva_panel1.tag_raise(k_id)
def ouvrir_k():
    fen = Toplevel()  
    fen.title("Lettre pour Kurenai-sensei")
    fen.geometry("1200x800")

    #Déclaration des variables pour les champs de saisie
    #Pour le nom/clan = des lettres ou mots etc
    nom = StringVar()
    clan = StringVar()
    jour = StringVar(value='Mercredi')
    heure = StringVar(value='08:00')

    
    panel = Frame(fen)
    panel.pack(fill="both", expand=True)

    canvas = Canvas(panel)
    canvas.pack(fill="both", expand=True)

    
    TEXT_OFFSET_X = 200
    TEXT_Y = 175
    TEXT_WIDTH = 820

    
    entry_nom = Entry(panel, textvariable=nom, width=25)
    entry_jour = OptionMenu(panel, jour, 'Mercredi', 'Samedi', 'Dimanche')
    entry_heure = OptionMenu(panel, heure, *[f'{h:02d}:00' for h in range(8, 18)])
    entry_clan = Entry(panel, textvariable=clan, width=25)
    
    def valider_kurenai():
        # Vérifier que le nom et le clan ne sont pas vides
        if not nom.get().strip() or not clan.get().strip():
            messagebox.showerror("Erreur", "Veuillez remplir le nom et le clan!")
            return
        
        # Créer un billet de confirmation
        billet = Toplevel(fen)
        billet.title("Confirmation du rendez-vous")
        billet.geometry("600x400")
        
        # Contenu du billet
        texte_billet = f"""
        CONFIRMATION DE RENDEZ-VOUS
        ---------------------------
        
        Professeur : Kurenai-sensei
        
        Étudiant : {nom.get()}
        Clan : {clan.get()}
        
        Jour : {jour.get()}
        Heure : {heure.get()}
        
        ---------------------------
        Rendez-vous confirmé!
        """
        
        #Affichage du billet
        canvas = Canvas(billet)
        canvas.pack(fill=BOTH, expand=True)

        def redraw_billet(event=None):
            canvas.delete("all")

            win_width = canvas.winfo_width()
            win_height = canvas.winfo_height()

            image = ten.resize((win_width, win_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            canvas.image = photo
            canvas.create_image(0, 0, anchor=NW, image=photo)

            TEXT_X = 70 + TEXT_OFFSET_X

            canvas.create_text(
                TEXT_X, TEXT_Y,
                text = texte_billet,
                font = ("Serif", 10),
                fill = "black",
                justify = CENTER,
                width = TEXT_WIDTH
            )

        canvas.bind("<Configure>", redraw_billet)
        
        btn_ok = Button(billet, text="OK", command=lambda: [billet.destroy(), fen.destroy()])
        btn_ok.pack(pady=5)
    
    bouton = Button(panel, text="Valider", command=valider_kurenai)

    
    def redraw(event=None):
        canvas.delete("all")
        
        win_width = canvas.winfo_width()
        win_height = canvas.winfo_height()
        
        image = img_og.resize((win_width, win_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, -50, anchor=NW, image=photo)
        
        TEXT_X = 60 + TEXT_OFFSET_X
        
        
        canvas.create_text(
            TEXT_X, TEXT_Y,
            anchor=NW,
            text="Cher Kurenai-sensei,\nNous sommes les parents de",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_window(TEXT_X + 300, TEXT_Y + 30, window=entry_nom)  

        canvas.create_text(
            TEXT_X, TEXT_Y + 80,
            anchor=NW,
            text="Qui est élève de votre classe à l’Académie ninja de Konoha." \
                "\nNous nous permettons de vous écrire car nous souhaiterions convenir d’un " \
                "rendez-vous parents-professeurs afin de discuter de ses progrès, "
                "de son comportement, et de son utilisation excessive du jutsu.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 180,
            anchor=NW,
            text="Notre enfant nous a récemment rapporté qu'il a été traumatiser lors d'un genjutsu raté.",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 300, TEXT_Y + 180, anchor=NW)

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 220,
            anchor=NW,
            text="Nous sommes disponibles le",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 210 + 25, TEXT_Y + 226, window=entry_jour)  

        canvas.create_text(
            TEXT_X + 360, TEXT_Y + 220,
            anchor=NW,
            text="à partir de",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 470 + 16, TEXT_Y + 226, window=entry_heure)

        canvas.create_text(
            TEXT_X, TEXT_Y + 260,
            anchor=NW,
            text="mais restons bien entendu flexibles selon votre emploi du temps chargé de sensei.\n"
                 "Nous vous remercions par avance pour votre patience, votre pédagogie et "
                 "votre dévouement envers les jeunes ninjas du village caché de Konoha.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 380 - 30,  
            anchor=NW,
            text="Le Clan :",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 135, TEXT_Y + 380 - 30 + 9, window=entry_clan)  

        
        canvas.create_window(TEXT_X + 740, TEXT_Y + 350, window=bouton)

    canvas.bind("<Configure>", redraw)
K.config(command=ouvrir_k)


G = Button(
    canva_panel1,
    text="Gai-Sensei",
    font=("System", 16),
    bg="#F0FFA4"
)

g_id = canva_panel1.create_window(
    878, 450,   
    window=G,
    anchor="nw")

canva_panel1.tag_raise(g_id)
def ouvrir_g():
    fen = Toplevel() 
    fen.title("Lettre pour Gai-sensei")
    fen.geometry("1200x800")


    
    #Déclaration des variables pour les champs de saisie
    #Pour le nom/clan = des lettres ou mots etc
    nom = StringVar()
    clan = StringVar()
    jour = StringVar(value='Lundi')
    heure = StringVar(value='08:00')

    
    panel = Frame(fen)
    panel.pack(fill="both", expand=True)

    canvas = Canvas(panel)
    canvas.pack(fill="both", expand=True)

    
    TEXT_OFFSET_X = 200
    TEXT_Y = 175
    TEXT_WIDTH = 820

    
    entry_nom = Entry(panel, textvariable=nom, width=25)
    entry_jour = OptionMenu(panel, jour, 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi')
    entry_heure = OptionMenu(panel, heure, *[f'{h:02d}:00' for h in range(0, 24)])
    entry_clan = Entry(panel, textvariable=clan, width=25)
    
    def valider_gai():
        # Vérifier que le nom et le clan ne sont pas vides
        if not nom.get().strip() or not clan.get().strip():
            messagebox.showerror("Erreur", "Veuillez remplir le nom et le clan!")
            return
        
        # Créer un billet de confirmation
        billet = Toplevel(fen)
        billet.title("Confirmation du rendez-vous")
        billet.geometry("600x400")
        
        # Contenu du billet
        texte_billet = f"""
        CONFIRMATION DE RENDEZ-VOUS
        ---------------------------
        
        Professeur : Gai-sensei
        
        Étudiant : {nom.get()}
        Clan : {clan.get()}
        
        Jour : {jour.get()}
        Heure : {heure.get()}
        
        ---------------------------
        Rendez-vous confirmé!
        """
        
        #Affichage du billet
        canvas = Canvas(billet)
        canvas.pack(fill=BOTH, expand=True)

        def redraw_billet(event=None):
            canvas.delete("all")

            win_width = canvas.winfo_width()
            win_height = canvas.winfo_height()

            image = ten.resize((win_width, win_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            canvas.image = photo
            canvas.create_image(0, 0, anchor=NW, image=photo)

            TEXT_X = 70 + TEXT_OFFSET_X

            canvas.create_text(
                TEXT_X, TEXT_Y,
                text=texte_billet,
                font=("Serif", 10),
                fill="black",
                justify=CENTER,
                width=TEXT_WIDTH
            )

        canvas.bind("<Configure>", redraw_billet)

        btn_ok = Button(billet, text="OK", command=lambda: [billet.destroy(), fen.destroy()])
        btn_ok.pack(pady=5)
    
    bouton = Button(panel, text="Valider", command=valider_gai)

    
    def redraw(event=None):
        canvas.delete("all")
        
        win_width = canvas.winfo_width()
        win_height = canvas.winfo_height()
        
        image = img_og.resize((win_width, win_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, -50, anchor=NW, image=photo)
        
        TEXT_X = 60 + TEXT_OFFSET_X
        
        
        canvas.create_text(
            TEXT_X, TEXT_Y,
            anchor=NW,
            text="Cher Gai-sensei,\nNous sommes les parents de",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_window(TEXT_X + 300, TEXT_Y + 30, window=entry_nom)  

        canvas.create_text(
            TEXT_X, TEXT_Y + 80,
            anchor=NW,
            text="Qui est élève de votre classe à l’Académie ninja de Konoha." \
                "\nNous nous permettons de vous écrire car nous souhaiterions convenir d’un " \
                "rendez-vous parents-professeurs afin de discuter de ses progrès, "
                "de son comportement, et de son utilisation excessive du jutsu.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 180,
            anchor=NW,
            text="Notre enfant nous a récemment rapporté qu'il vous trouvait beaucoup trop intrusive.",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 300, TEXT_Y + 180, anchor=NW)

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 220,
            anchor=NW,
            text="Nous sommes disponibles le",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 210 + 25, TEXT_Y + 226, window=entry_jour)  

        canvas.create_text(
            TEXT_X + 360, TEXT_Y + 220,
            anchor=NW,
            text="à partir de",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 470 + 16, TEXT_Y + 226, window=entry_heure)

        canvas.create_text(
            TEXT_X, TEXT_Y + 260,
            anchor=NW,
            text="mais restons bien entendu flexibles selon votre emploi du temps chargé de sensei.\n"
                 "Nous vous remercions par avance pour votre patience, votre pédagogie et "
                 "votre dévouement envers les jeunes ninjas du village caché de Konoha.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 380 - 30,  
            anchor=NW,
            text="Le Clan :",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 135, TEXT_Y + 380 - 30 + 9, window=entry_clan)  

        
        canvas.create_window(TEXT_X + 740, TEXT_Y + 350, window=bouton)

    canvas.bind("<Configure>", redraw)
G.config(command=ouvrir_g)


J = Button(
    canva_panel1,
    text="Jiraya",
    font=("System", 16),
    bg="#F0FFA4"
)

j_id = canva_panel1.create_window(
    1125, 450,   
    window=J,
    anchor="nw")

canva_panel1.tag_raise(j_id)
def ouvrir_j():
    fen = Toplevel()  
    fen.title("Lettre pour l'Ermite pas net")
    fen.geometry("1200x800")

    #Déclaration des variables pour les champs de saisie
    #Pour le nom/clan = des lettres ou mots etc
    nom = StringVar()
    clan = StringVar()
    jour = StringVar(value='Samedi')
    heure = StringVar(value='18:00')

    
    panel = Frame(fen)
    panel.pack(fill="both", expand=True)

    canvas = Canvas(panel)
    canvas.pack(fill="both", expand=True)


    
    TEXT_OFFSET_X = 200
    TEXT_Y = 175
    TEXT_WIDTH = 820

    
    entry_nom = Entry(panel, textvariable=nom, width=25)
    entry_jour = OptionMenu(panel, jour, 'Samedi', 'Dimanche')
    entry_heure = OptionMenu(panel, heure, *[f'{h:02d}:00' for h in range(18, 24)])
    entry_clan = Entry(panel, textvariable=clan, width=25)
    
    def valider_jiraya():
        # Vérifier que le nom et le clan ne sont pas vides
        if not nom.get().strip() or not clan.get().strip():
            messagebox.showerror("Erreur", "Veuillez remplir le nom et le clan!")
            return
        
        # Créer un billet de confirmation
        billet = Toplevel(fen)
        billet.title("Confirmation du rendez-vous")
        billet.geometry("600x400")
        
        # Contenu du billet
        texte_billet = f"""
        CONFIRMATION DE RENDEZ-VOUS
        ---------------------------
        
        Professeur : Jiraya-sensei
        
        Étudiant : {nom.get()}
        Clan : {clan.get()}
        
        Jour : {jour.get()}
        Heure : {heure.get()}
        
        ---------------------------
        Rendez-vous confirmé!
        """
        
        #Affichage du billet
        canvas = Canvas(billet)
        canvas.pack(fill=BOTH, expand=True)

        def redraw_billet(event=None):
            canvas.delete("all")

            win_width = canvas.winfo_width()
            win_height = canvas.winfo_height()

            image = ten.resize((win_width, win_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            canvas.image = photo
            canvas.create_image(0, 0, anchor=NW, image=photo)

            TEXT_X = 70 + TEXT_OFFSET_X

            canvas.create_text(
                TEXT_X, TEXT_Y,
                text=texte_billet,
                font=("Serif", 10),
                fill="black",
                justify=CENTER,
                width=TEXT_WIDTH
            )

        canvas.bind("<Configure>", redraw_billet)

        btn_ok = Button(billet, text="OK", command=lambda: [billet.destroy(), fen.destroy()])
        btn_ok.pack(pady=5)
    
    bouton = Button(panel, text="Valider", command=valider_jiraya)

    
    def redraw(event=None):
        canvas.delete("all")
        
        win_width = canvas.winfo_width()
        win_height = canvas.winfo_height()
        
        image = img_og.resize((win_width, win_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, -50, anchor=NW, image=photo)
        
        TEXT_X = 60 + TEXT_OFFSET_X
        
        
        canvas.create_text(
            TEXT_X, TEXT_Y,
            anchor=NW,
            text="Cher Jiraya-sensai,\nNous sommes les parents de",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_window(TEXT_X + 300, TEXT_Y + 30, window=entry_nom)  

        canvas.create_text(
            TEXT_X, TEXT_Y + 80,
            anchor=NW,
            text="Qui est sous votre tutelle depuis peu." \
                "\nNous nous permettons de vous écrire car nous souhaiterions convenir d’un " \
                "rendez-vous parents-professeurs afin de discuter de ses progrès, "
                "de son comportement, et de son utilisation excessive du jutsu.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 180,
            anchor=NW,
            text="Notre enfant nous a récemment rapporté que vous teniez des propos obscènes.",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 300, TEXT_Y + 180, anchor=NW)

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 220,
            anchor=NW,
            text="Nous sommes disponibles le",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 210 + 25, TEXT_Y + 226, window=entry_jour)  

        canvas.create_text(
            TEXT_X + 360, TEXT_Y + 220,
            anchor=NW,
            text="à partir de",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 470 + 16, TEXT_Y + 226, window=entry_heure)

        canvas.create_text(
            TEXT_X, TEXT_Y + 260,
            anchor=NW,
            text="mais restons bien entendu flexibles selon votre mode de vie en tant qu'Hermite.\n"
                 "Nous vous remercions par avance pour votre patience, votre pédagogie et "
                 "votre dévouement envers les jeunes ninjas du village caché de Konoha.",
            font=("Times New Roman", 12),
            width=TEXT_WIDTH
        )

        
        canvas.create_text(
            TEXT_X, TEXT_Y + 380 - 30,  
            anchor=NW,
            text="Le Clan :",
            font=("Times New Roman", 12)
        )
        canvas.create_window(TEXT_X + 135, TEXT_Y + 380 - 30 + 9, window=entry_clan)  

        
        canvas.create_window(TEXT_X + 740, TEXT_Y + 350, window=bouton)


    canvas.bind("<Configure>", redraw)
J.config(command=ouvrir_j)


"""
Vérification avant de rentrer

"""

def verifier_entrer():
    global regles_ok
    if not regles_ok:
        # Si les règles ne sont pas acceptées, ouvrir la fenêtre des règles
        ouvrir_regle()
    else:
        # Sinon, laisser l'utilisateur entrer
        panel1.tkraise()

Entrer = Button(canvas,text="Entrer",font=("System", 16),bg="#A4E4FF",command=verifier_entrer)
entrer_id = canvas.create_window(470, 385, window=Entrer, anchor="nw")
canvas.tag_raise(entrer_id)


"""
La fenêtre des règles + la case à cocher pour accepter les règles

"""
#Variable globale pour suivre si les règles ont été acceptées
regles_ok = False

#Création d'une fonction pour ouvrir une nouvelle fenêtre avec les règles
def ouvrir_regle(img):
    fenetre = Toplevel()
    fenetre.title("Réunion")
    fenetre.geometry("1000x800")
    
    #Charger l'image pour l'arrière plan
    img = Image.open(r"C:\Users\feero\OneDrive\Desktop\cla.png")
    img = img.resize((800, 500), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    
    #Créer un canvas pour l'arrière plan
    canvas = Canvas(fenetre, width=1000, height=800, bg="#FF9620")
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(150, 100, anchor=NW, image=photo)

    fenetre.photo = photo


    #Titre
    title_label = Label(
        fenetre,
        text="Règle pour la Réunion Parent - Professeur",
        bg="#FF9620",
        font=("Arial", 20, "bold")
    )
    title_label.place(x=260,y=100)

    #Texte
    text_label = Label(
        fenetre,
        text=(
            "- Ne pas ramener d'arme\n"
            "- Respecter les horaires\n"
            "- Être poli\n"
            "- Ne pas tuer votre enfant\n"
            "- Apporter le nécessaire de document\n"
            "- Ne pas faire n'importe quoi\n"
            "- Ne pas rater la salle"
            ),
        bg="#FF9620",
        font=("Arial", 30),
        justify=LEFT)
    text_label.place(x=225, y=250)

    #Case à cocher
    agree_var = BooleanVar(master=fenetre)
    #Fonction pour fermer la fenêtre lorsque la case est cochée
    def case_ok():
        global regles_ok
        if agree_var.get():
            regles_ok = True
            fenetre.destroy()
            #Permet d'accéder au panel1, c'est-à-dire l'écran de sélection des professeurs
            panel1.tkraise()
    
    checkbutton = Checkbutton(
        fenetre,
        text="J'accepte toutes les règles",
        variable=agree_var,
        command=case_ok,
        bg="#FF9620",
        font=("Arial", 20)
    )
    checkbutton.place(x=300,y=600)
    
    #Bouton Fermer
    bouton = Button(
        fenetre,
        text="Fermer",
        command=fenetre.destroy,
        bg="#3139DE",
        fg="white"
    )
    bouton.place(x=50, y=20)
Politique = canvas.create_text(508, 445,  text="Politique de l'Académie des Ninjas",font=("Yu Gothic UI", 10),fill="white")

#Boutton pour ouvrir la fenêtre des règles
canvas.tag_bind(Politique, "<Button-1>",ouvrir_regle)
canvas.config(cursor="hand2")


"""
Création de la musique de fond

"""

#Musique de fond
pygame.init()
pygame.mixer.init(frequency=44100)

def play():
    pygame.mixer.music.load(r"C:\Users\feero\OneDrive\Desktop\naruto.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(1) 

play_button = Button(canvas, text="Musique", font=("Segoe UI Black", 22), fg="white",bg="#FF9447",relief=GROOVE, command=play)
canvas.create_window(730, 510, window=play_button, anchor="nw")

#Premier plan = accueil
panel_accueil.tkraise()

#Boucle principale
fenetre.mainloop()