from action import Action
from encherir import Encherir
from dudo import Dudo
from paco import Paco
import random


class Joueur:

    """
    La classe Joueur représente l'un des joueurs du jeu.
    Un Joueur peut lancer ces dés et ses Actions (autorisées).

    Paramètres :
    - A FAIRE nom : nom du joueur
    """

    """Constructeur"""

    def __init__(self) -> None:
        self.name = random.choice(["Alice", "Bob", "Charlie", "David", "Excalibur", "Fabrice", "Gabriel", "Histoire","Isabelle", "Jardim", "Kamel", "Laurent", "Mathieu", "Nicolas", "Olive", "Patrick", "Quentin", "Rasoir", "Sébastien", "Thomas", "Valentin", "Xavier"])
        self.des = [None,None]
        self.nb_des = 2
        self.actions_autorisees = {
                                    "Enchérir": Encherir(self),
                                    "Paco": Paco(self),
                                    "Dudo": Dudo(self)
                                    
                                  }

    """Méthode permettant d'afficher l'objet dans la console avec print()"""
    def __str__(self) -> str:
        return self.name

    """Méthode renvoyant l'action choisie par l'utilisateur"""
    def action(self, nom_action) -> Action:
        return self.actions_autorisees[nom_action]

    """Méthode permettant à un joueur de lancer ces dés."""
    def lancer_des(self) -> None:
        self.des = [random.randint(1,6) for i in range(self.nb_des)]

    """Méthode permettant à un joueur de jouer : lancer ces dés puis choisir une Action"""
    def jouer(self, action_precedente = None, palifico = False) -> Action:
        if action_precedente is None:
            action_precedente = Encherir(self)

        print('\n\n\n\n\n\n')
        print("Lancer de dé de {} : {}".format(self,self.des))

        nom_action = demander_action(True, self)

        while nom_action not in self.actions_autorisees:
            nom_action = demander_action(False, self)

        return self.action(nom_action).lancer(action_precedente, palifico)


"""
La fonction demander_action() permet de demander à l'utilisateur quelle Action
il souhaite effectuer

Paramètres :
- premiere_fois : booléen indiquant si c'est la premier fois qu'on demande à l'utilsateur de jouer. 
                  Si non, l'utilisateur s'est trompé et on affiche alors un message
- joueur : Joueur en train de jouer

Renvoie :
 - le nom de l'action choisie par l'utilisateur
"""

def demander_action(premiere_fois, joueur) -> str:
    if not premiere_fois:
        print("Action invalide ! (attention à la casse)")

    actions_possibles = list(joueur.actions_autorisees.keys())

    print("Actions possibles : {}".format(actions_possibles))
   
    return input("Choisissez une action :\n")