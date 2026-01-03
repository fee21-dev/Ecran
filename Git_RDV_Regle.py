from tkinter import *

fenetre = Tk()
fenetre.title("Réunion")
fenetre.configure(bg="#FF9620")

# Titre
title_label = Label(fenetre, text="Règle pour la Réunion Parent - Professeur", bg="#FF9620", font=("Arial", 16, "bold"))
title_label.pack(pady=10) #pady = met 10 pixels d'espace vertical (en haut et en bas)

#Texte en bas
text_label = Label(fenetre, text="Ne pas ramener d'arme\n Respecter les horaires\n Être poli\n Ne pas tuer votre enfant\n Apporter le nécessaire de document\n Ne pas faire n'importe quoi \n Ne pas rater la salle", bg="#FF9620", justify=LEFT)
text_label.pack(pady=10)

#Valider
agree_var = BooleanVar() #Variable pour stocker l'état de la case à cocher
checkbutton = Checkbutton(fenetre, text="J'accepte toutes les règles", variable=agree_var, bg="#FF9620")
checkbutton.pack(pady=10)

#Fermer
bouton = Button(fenetre, text="Fermer", command=fenetre.quit, bg="#3139DE")
bouton.pack(pady=10)

fenetre.mainloop()
