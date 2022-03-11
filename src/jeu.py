from action import Action
from encherir import Encherir
from joueur import Joueur
from dudo import Dudo

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
            ##joueurs
            numero_joueur_precedent = 0
            
            action_precedente = self.joueurs[0].jouer()
            numero_joueur_precedent = 0
            
            for index, joueur in enumerate(self.joueurs[1:]):
                action_actuelle = None
                action_actuelle = joueur.jouer(action_precedente)
                
                if isinstance(action_actuelle, Dudo):
                    self.gerer_dudo(numero_joueur_precedent, action_precedente)

                action_precedente = action_actuelle
                numero_joueur_precedent = index
                    
            nb_tours -= 1
            print("Nombre de tours restants : {}".format(str(nb_tours)))

    def determiner_ordre_joueurs(self) -> list():
        """To do"""

    def calculer_actions_possibles(self) -> None:
        """To do"""

    """Fonction qui élimine les joueurs de la partie s'ils n'ont plus de dés"""
    def eliminer_joueurs(self) -> None:
        for joueur in self.joueurs:
            if joueur.nb_des < 1:
                self.joueurs -= 1
        
    """
    En cas de Dudo
    """

    """Fonction qui permet de réveler publiquement tous les dés des joueurs"""
    def reveler_des(self) -> None:
        des_sur_la_table = [] 
        for joueur in self.joueurs:
            des_sur_la_table.extend(joueur.des) #on ajoute aux dés sur la table les dés de chaque joueur

        print("Dés sur la table : {}".format(des_sur_la_table))

    """Fonction qui permet d'enlever un dé au perdant d'un paco"""
    def enlever_de(self, perdant) -> None:
        perdant.nb_des -= 1

    """Fonction qui permet de vérifier si le joueur qui a joué un paco a tort"""

    def pari_faux(self, action_precedente) -> bool:
        cpt=0
        for i in range(self.nb_joueurs):
            cpt+=self.joueurs[i].des.count(action_precedente.pari['valeur_des'])
            cpt+=self.joueurs[i].des.count(1)
        if cpt < action_precedente.pari['nb_des']:
            return True
        else:
            return False


    """Fonction qui permet de vérifier qui perd un Paco et enlève un dé au perdant (combine les deux fonctions précédentes)"""  
    def gerer_dudo(self, numero_joueur_precedent, action_precedente) -> None:
        self.reveler_des()

        #si le pari annoncé est faux, on enlève un dé au joueur qui a fait le pari
        #si non on enlève un dé au joueur qui a annoncé Dudo
        if self.pari_faux(action_precedente):
            self.enlever_de(self.joueurs[numero_joueur_precedent])
            print("{} avait tort ! Il perd un dé.".format(self.joueurs[numero_joueur_precedent]))
        else:
            self.enlever_de(self.joueurs[numero_joueur_precedent + 1])
            print("{} avait tort ! Il perd un dé.".format(self.joueurs[numero_joueur_precedent + 1]))
