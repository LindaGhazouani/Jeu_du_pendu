# Jeu du pendu
# Ce code séléctionne un mot d'une façon aléatoire depuis un fichier texte, enlève les accents du mot choisi s'il y en a,
# et demande à l’utilisateur de deviner le mot avec un nombre limité de chances. (a chaque fois il devine une lettre)
# Lu'itilsateur peut rejouer après la fin du jeu (s'il gagne ou il perd)
# Un indice est donné quand il ne reste qu'une seule chance.

import random
from module_lecture_mots import lire_liste_mots, enlever_caracteres_speciaux


# Fonction pour afficher les lettres du mot
def afficher_mot_cache(mot, lettres_trouvees):
    resultat = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            resultat += lettre + " "
        else:
            resultat += "_ "
    return resultat


# Fonction pour deviner le mot
def deviner_le_mot():
    liste_mots = lire_liste_mots()
    if not liste_mots:
        return

    mot_original = random.choice(liste_mots)
    mot_sans_accents = enlever_caracteres_speciaux(mot_original)

    lettres_trouvees = []
    lettres_essayees = []
    chances = 6

    print("\n **** Nouveau jeu du pendu **** ")

    while chances > 0:
        print("\nMot :", afficher_mot_cache(mot_sans_accents, lettres_trouvees))
        print("le nombre de chances restantes est égal à :", chances)

        # Bonus : donner une lettre qui n’est pas dans le mot
        if chances == 1:
            lettres_absentes = [chr(i) for i in range(97, 123) if chr(i) not in mot_sans_accents]
            if lettres_absentes:
                lettre_indice = random.choice(lettres_absentes)
                print("Indice : la lettre", lettre_indice, "n’est pas dans le mot !")

        lettre = input("propose une lettre : ").lower()

        if len(lettre) != 1 or not lettre.isalpha():
            print("entrez une seule lettre !")
            continue

        if lettre in lettres_essayees:
            print("vous avez deja proposé cette lettre !")
            continue

        lettres_essayees.append(lettre)

        if lettre in mot_sans_accents:
            print("vous avez deviner une lettre !")
            lettres_trouvees.append(lettre)
        else:
            print("vous n'avez pas deviner une lettre !")
            chances -= 1

        if all(l in lettres_trouvees for l in mot_sans_accents):
            print("\n vous avez trouvé le mot :", mot_original)
            return

    print("\n le mot à deviner était :", mot_original)


# Fonction pour jouer une partie
def lancer_le_jeu():
    print(" **** jeu du Pendu **** ")
    print("vous devez deviner le mot choisi au hasard du fichier texte fourni, vous avez 6 chances et droit à deviner une lettre à la fois")
    print("un indice sera fourni si tu n'as plus qu'une seule chance.")
    while True:
        deviner_le_mot()
        reponse = input("\nsouhaites tu rejouer ? (oui/non) : ").lower()
        if reponse != 'oui':
            break


# Lancement du jeu
if __name__ == "__main__":
    lancer_le_jeu()
