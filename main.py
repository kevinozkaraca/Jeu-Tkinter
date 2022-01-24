from functools import partial
from fonctions_damier import fonctions_damier
from fonctions_menu import fonctions_menu
from fonctions_demarrer import fonctions_demarrer
import tkinter
from tkinter import Menu

# Affichage et parametre de la fenetre
fenetre = tkinter.Tk()
fenetre.title("Jeu de la vie")
fenetre.configure(background="#A5F2A5")
fenetre.attributes('-fullscreen', True)
fenetre.iconbitmap('images/icon.ico')


# Lettres et numéro des boutons (Index)
lettres_de_lalphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
]
numero_possible = [
    "01", "02", "03", "04", "05", "06", "05", 
    "06", "07", "08", "09", "10", "11", "12",
    "14", "15", "16", "17", "18", "19", "20", 
    "21", "22", "23", "24", "25",
]


def damier_de_boutons():
    # Parametre des boutons et de la boucle d'affichage
    font_des_boutons = "Arial"
    taille_de_font_boutons = 7
    hauteur_des_boutons = 2
    largeur_des_boutons = hauteur_des_boutons * 2
    espace_multiplie_entre_boutons = 30
    compteur_de_lignes = 0
    compteur_de_lettre = 0
    index_du_numero = 1
    # Boucle d'affichage des boutons
    while compteur_de_lettre < 25:
        for i in range(26):
            text = f"{lettres_de_lalphabet[compteur_de_lettre]}{numero_possible[i]}"
            btn = tkinter.Button(
                fenetre,
                text=text,
                textvariable=f"{lettres_de_lalphabet[compteur_de_lettre]}{numero_possible[i]}",
                font=(font_des_boutons, taille_de_font_boutons),
                height=hauteur_des_boutons,
                width=largeur_des_boutons,
                command=partial(fonctions_damier, text),
            )
            btn.place(
                x=10+i * espace_multiplie_entre_boutons,
                y=10+ compteur_de_lignes * espace_multiplie_entre_boutons,
            )
            index_du_numero = index_du_numero + 1
        compteur_de_lignes = compteur_de_lignes + 1
        compteur_de_lettre = compteur_de_lettre + 1

 
    
# Création du menu
barre_de_menu = Menu(fenetre)
# Création du menu
filemenu = Menu(barre_de_menu, tearoff=0)
filemenu.add_command(label="Recommencer", command=fonctions_menu)
filemenu.add_command(label="Retour", command=fonctions_menu)
barre_de_menu.add_cascade(label="Fichier", menu=filemenu)
barre_de_menu.add_command(label="Quitter", command=fenetre.quit)
# Affichage du menu
fenetre.config(menu=barre_de_menu)
 
bouton_demarrer = tkinter.Button(fenetre, text ="Cliquez ici!",command=fonctions_demarrer)
bouton_demarrer.place(x=800,y=10)

damier_de_boutons()
# Mainloop : A toujours mettre à la fin
fenetre.mainloop()
    