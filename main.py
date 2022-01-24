from functools import partial
from fonctions import fonctions_boutons
import tkinter


# Taille des éléments
width_fenetre = "1055"
height_fenetre = "750"


# Affichage et parametre de la fenetre
fenetre = tkinter.Tk()
fenetre.title("Jeu de la vie")
fenetre.geometry(f"{width_fenetre}x{height_fenetre}")
fenetre.resizable(width=False, height=False)
fenetre.configure(background="#F5D2E5")


# Lettres et numéro des boutons
lettres_de_lalphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
]
numero_possible = [
    "01", "02", "03", "04", "05", "06", 
    "05", "06", "07", "08", "09", "10",
    "11", "12", "14", "15", "16", "17",
    "18", "19", "20", "21", "22", "23",
    "24", "25",
]


def main():
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
                command=partial(fonctions_boutons, text),
            )
            btn.place(
                x=i * espace_multiplie_entre_boutons,
                y=compteur_de_lignes * espace_multiplie_entre_boutons,
            )
            index_du_numero = index_du_numero + 1
        compteur_de_lignes = compteur_de_lignes + 1
        compteur_de_lettre = compteur_de_lettre + 1


main()
# Mainloop : A toujours mettre à la fin
fenetre.mainloop()
    