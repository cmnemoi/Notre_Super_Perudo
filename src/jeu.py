from action import Action
from encherir import Encherir
from joueur import Joueur



class Jeu:
    """
    La classe Jeu gère la logique du jeu dans sa fonction lancer().
    """

    """Constructeur appelé pour construire un Objet Jeu"""
    def __init__(self) -> None:
        self.joueurs = [Joueur() for i in range(2)] #Liste contenant les Joueurs particpant au jeu
        self.nb_joueurs = 2 

    """Fonction permettant de lancer le jeu et de gérer tous les évènements"""
    def lancer(self) -> None:
        nb_tours = 3
        while self.nb_joueurs >= 2 or nb_tours > 1:

            action_precedente = None

            for joueur in self.joueurs:
                action_precedente = joueur.jouer(action_precedente)

            nb_tours -= 1
            print("Nombre de tours restants : {}".format(str(nb_tours)))