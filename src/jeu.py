from action import Action
from joueur import Joueur
from encherir import Encherir
from dudo import Dudo
from palifico import Palifico
from paco import Paco
from random import randrange

class Jeu:
    """
    La classe Jeu gère la logique du jeu dans sa fonction lancer().
    """

    """Constructeur appelé pour construire un Objet Jeu"""
    def __init__(self, nb_joueurs) -> None:
        self.joueurs = [Joueur() for i in range(nb_joueurs)] #Liste contenant les Joueurs particpant au jeu
        self.nb_joueurs = nb_joueurs
        self.palifico = False
        self.premier_joueur = None

    """Fonction permettant de lancer le jeu et de gérer tous les évènements"""
    def lancer(self) -> None:
        numero_tour = 1

        while self.nb_joueurs >= 2:

            for joueur in self.joueurs:
                joueur.lancer_des()

            if self.palifico:
                print("Palifico!")
                
            #on fait jouer le premier joueur à part par ce qu'il n'y a pas d'action précédente + plus simple
            if numero_tour ==  1 :
                self.premier_joueur = self.determiner_premier_joueur()
                self.premier_joueur.actions_autorisees = {"Enchérir":Encherir(self.premier_joueur)} #le premier joueur ne peut qu'enchérir
                action_precedente = self.premier_joueur.jouer()
                numero_joueur_precedent = self.joueurs.index(self.premier_joueur)

            self.lancer_tour(action_precedente, numero_joueur_precedent)

            self.eliminer_joueurs()
                    
            numero_tour += 1
            print("Numéro du tour : {}\n".format(str(numero_tour)))


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

        for index, joueur in enumerate(self.joueurs[(numero_joueur_precedent+1) % self.nb_joueurs:]):

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
            

    def gerer_dudo(self, numero_joueur_precedent, action_precedente) -> None:
        self.reveler_des()

        #si le pari annoncé est faux, on enlève un dé au joueur qui a fait le pari
        #si non on enlève un dé au joueur qui a annoncé Dudo
        if self.pari_faux(action_precedente):
            self.enlever_de(self.joueurs[numero_joueur_precedent])
            print("{} avait tort ! Il perd un dé.".format(self.joueurs[numero_joueur_precedent]))
            self.etat_partie(self,self.joueurs[numero_joueur_precedent])
            if self.joueurs[numero_joueur_precedent].nb_des > 1:
                self.premier_joueur=self.joueurs[numero_joueur_precedent]
            else :
                self.premier_joueur=self.joueurs[numero_joueur_precedent + 1]    
                
        else:
            self.enlever_de(self.joueurs[numero_joueur_precedent + 1])
            print("{} avait tort ! Il perd un dé.".format(self.joueurs[numero_joueur_precedent + 1]))
            self.etat_partie(self,self.joueurs[numero_joueur_precedent]) 
              

        self.eliminer_joueurs()

        for joueur in self.joueurs:
            joueur.lancer_des()

    def determiner_premier_joueur(self) -> Joueur:
        #retirage des dés
        tirage_de_des=[]
        for i in range(self.nb_joueurs*2): #pour chaque tirage de dé
            d=randrange(1,7) # on choisit un nombre au hasard
            tirage_de_des.append(d) #on ajoute chaque tirage à la liste
         

        #recalcul des sommes
        somme_des_tirages_de_des=[]
        for j in range(0,self.nb_joueurs*2,2): #pour chaque tirage de dé
            somme_des_tirages_de_des.append(tirage_de_des[j]+tirage_de_des[j+1]) #on fait la somme des 2 tirages
        for p in range(len(somme_des_tirages_de_des)):
            print("Somme du joueur {} ({}) : {}".format(p+1, self.joueurs[p], somme_des_tirages_de_des[p])) #on affiche les sommes de tirages


        #détermination du premier joueur
        index_premier_joueur=somme_des_tirages_de_des.index(max(somme_des_tirages_de_des))#le numéro du premier joueur est l'index de la plus grosse somme

        print("Le joueur {} ({}) commence !".format(index_premier_joueur+1, self.joueurs[index_premier_joueur]))
        return self.joueurs[index_premier_joueur]