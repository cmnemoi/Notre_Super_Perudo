"""Il s'agit de ce script qu'il faut lancer pour démarrer le jeu."""

from jeu import Jeu

if __name__ == "__main__":
    nb_joueurs = 2
    Jeu(nb_joueurs).lancer()