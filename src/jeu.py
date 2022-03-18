from action import Action
from joueur import Joueur
from encherir import Encherir
from dudo import Dudo
from palifico import Palifico
from paco import Paco

class Jeu:
    """
    La classe Jeu gère la logique du jeu dans sa fonction lancer().
    """

    """Constructeur appelé pour construire un Objet Jeu"""
    def __init__(self, nb_joueurs) -> None:
        self.joueurs = [Joueur() for i in range(nb_joueurs)] #Liste contenant les Joueurs particpant au jeu
        self.nb_joueurs = nb_joueurs
        self.palifico = False

    """Fonction permettant de lancer le jeu et de gérer tous les évènements"""
    def lancer(self) -> None:
        nb_tours = 99

        while self.nb_joueurs >= 2 and nb_tours > 0:
            
            if self.palifico:
                print("Palifico!")
                
            #on fait jouer le premier joueur à part par ce qu'il n'y a pas d'action précédente + plus simple
            self.joueurs[0].actions_autorisees = {"Enchérir":Encherir(self.joueurs[0])} #le premier joueur ne peut qu'enchérir
            action_precedente = self.joueurs[0].jouer()
            numero_joueur_precedent = 0

            self.lancer_tour(action_precedente, numero_joueur_precedent)

            self.eliminer_joueurs()
                    
            nb_tours -= 1
            print("Nombre de tours restants : {}\n".format(str(nb_tours)))

    def determiner_ordre_joueurs(self) -> list():
        """To do"""

    """Fonction permettant de calculer l'état de la partie : Palifico ou normal
    Si le perdant du dernier tour n'a plus qu'un dé ou n'a plus de dé on est en normal
    sinon en Palifico
    """
    def etat_partie(self, perdant=Joueur()):
       if perdant.nb_des == 1:
          self.palifico = True

       elif (perdant.nb_des > 1) or (perdant.nb_des == 0) :
          self.palifico = False
        

    def calculer_actions_possibles(self, joueur, le_tour_est_palifico) -> None:
        if self.palifico:
            joueur.actions_autorisees = {"Enchérir": Encherir(joueur), "Dudo": Dudo(joueur)}

    def lancer_tour(self, action_precedente, numero_joueur_precedent) -> None:
        if self.palifico:
            print("Palifico!")

        for index, joueur in enumerate(self.joueurs[1:]):

            self.calculer_actions_possibles(joueur, self.palifico)
            action_actuelle = None
            action_actuelle = joueur.jouer(action_precedente, self.palifico)
                
            if isinstance(action_actuelle, Dudo):
                self.gerer_dudo(numero_joueur_precedent, action_precedente)
                break

            action_precedente = action_actuelle
            numero_joueur_precedent = index

  
    """
    En cas de Dudo
    """

    """Fonction qui élimine les joueurs de la partie s'ils n'ont plus de dés"""
    def eliminer_joueurs(self) -> None:
        for joueur in self.joueurs:
            if joueur.nb_des < 1:
                self.joueurs.remove(joueur)
                self.nb_joueurs -= 1
        

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
        if isinstance(action_precedente, Encherir):
            
            cpt=0
            for i in range(self.nb_joueurs):
                cpt+=self.joueurs[i].des.count(action_precedente.pari['valeur_des'])
                cpt+=self.joueurs[i].des.count(1)
            if cpt < action_precedente.pari['nb_des']:
                return True
            else:
                return False
        
        elif isinstance(action_precedente, Paco):
            cpt=0
            for i in range(self.nb_joueurs):
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
            perdant = self.joueurs[numero_joueur_precedent]
        else:
            perdant = self.joueurs[numero_joueur_precedent + 1]

        self.enlever_de(perdant)
        self.etat_partie(perdant)
        print("{} avait tort ! Il perd un dé.\n".format(perdant))