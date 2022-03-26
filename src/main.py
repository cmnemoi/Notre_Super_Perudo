"""Il s'agit de ce script qu'il faut lancer pour démarrer le jeu."""

from jeu import Jeu

if __name__ == "__main__":
    print("Jeu créé par Yann, François, Gauthier et Charles")
    nb_joueurs = 0
    while nb_joueurs < 2 or nb_joueurs > 6:
        nb_joueurs = int(input("Choisissez le nombre de joueurs (entre 2 et 6) :"))

    Jeu(nb_joueurs).lancer()