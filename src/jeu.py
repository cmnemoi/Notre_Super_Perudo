from action import Action
from encherir import Encherir
from joueur import Joueur


class Jeu:
    """
    La classe Jeu gère la logique du jeu dans sa fonction lancer().
    """

    """Constructeur appelé pour construire un Objet Jeu"""
    def __init__(self, nb_joueurs) -> None:
        self.joueurs = [Joueur() for i in range(nb_joueurs)] #Liste contenant les Joueurs particpant au jeu
        self.nb_joueurs = nb_joueurs

    """Fonction permettant de lancer le jeu et de gérer tous les évènements"""
    def lancer(self) -> None:
        nb_tours = 2
        while self.nb_joueurs >= 2 and nb_tours > 0:

            action_precedente = self.joueurs[0].jouer()
        
            for joueur in self.joueurs[1:]:
                action_precedente = joueur.jouer(action_precedente)

            nb_tours -= 1
            print("Nombre de tours restants : {}".format(str(nb_tours)))

    def determiner_ordre_joueurs(self) -> list():
        """To do"""

    def calculer_actions_possibles(self) -> None:
        """To do"""

    """Fonction qui élimine les joueurs de la partie s'ils n'ont plus de dés"""
    def eliminer_joueurs(self) -> tuple:
        for joueur in self.joueurs:
            if joueur.nb_des < 1:
                self.joueurs -= 1
        
    """
    En cas de Paco
    """
    def reveler_des(self, action_precdente) -> None:
        """To do"""

    def enlever_de(self, perdant) -> None:
        perdant.nb_des -= 1

    def calculer_perdant(self, joueur_1, joueur_2) -> Joueur:
        """To do"""