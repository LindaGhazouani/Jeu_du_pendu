# Explication du jeu du Pendu :

Il s'agit d'un jeu réalisé en Python dans le cadre du cours MGA802 à l'ETS.

L'utilisateur doit deviner un mot choisi au hasard dans un fichier texte.  
L'utilisateur a 6 chances pour trouver le mot. Il doit proposer une lettre a chaque tentative.
Si l’utilisateur n’a plus qu’une seule chance, un indice lui sera affiché pour l'aider à deviner le mot.  
A la fin du jeu, il peut choisir de rejouer ou de quitter le jeu.

# Les fichiers disponibles pour le projet :

- `pendu.py` : script principal du jeu du pendu
- `module_lecture_mots.py` : module fourni par l'enseignante du cours pour la lecture et le nettoyage des mots 
- `ressources/mots_pendu.txt` : fichier texte contenant les mots à deviner

# Etapes à suivre pour l'exécution

1. Assure-toi d’avoir Python installé sur ton ordinateur
2. Clone ce dépôt ou télécharge le
3. Ouvre un terminal (PowerShell si t'es sur Windows)
4. Va dans le dossier du projet avec la commande `cd` (et insere le chemin du dossier)
4. Lance le jeu depuis le terminal avec :

```bash
python pendu.py
```

Fonctionnalités disponibles dans le projet :
- Sélection aléatoire d’un mot depuis le fichier mots_pendu.txt
- Suppression des accents du mot sélectionné
- Affichage progressif du mot à deviner sous forme de tirets (___)
- Décompte et affichage du nombre de chances restantes
- Affichage d’un indice lorsque l’utilisateur n’a plus qu’une seule chance
- Possibilité de rejouer une nouvelle partie à la fin du jeu

Remarques :
Projet réalisé avec PyCharm, en suivant les instructions du cours.
Le module module_lecture_mots.py a été utilisé tel que fourni par l’enseignante.
