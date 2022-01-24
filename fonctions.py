# Variables pour cibler les boutons

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


# Fonction print - test

def fonctions_boutons(text):
    if lettres_de_lalphabet[0] in text:
        print("je clique sur un A")
    if numero_possible[0] in text:
        print("je clique sur un 01")
    if text == "A01":
        print("Hello je suis le bouton  ", text)
    if text == "A02":
        print("Hello je suis le bouton  ", text)

