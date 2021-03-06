from action import Action
from paco import Paco
import re

class Encherir(Action):
    """
    La classe Enchérir permet de lancer à un Joueur d'enchérir.
    Elle permet à un Joueur doit annoncer un nombre de dés ou une valeur de dé supérieur à l'enchère précédente.
    """

    def __init__(self, joueur) -> None:
        super().__init__(joueur)
        self.pari = {
            "nb_des": 0,
            "valeur_des": 0
        }
        
    """Méthode gérant la logique de l'action : demande le pari du joueur et vérifie qu'il est valide"""
    def lancer(self, action_precedente, palifico) -> Action:
        pari = self.demander_pari(True)

        action_valide = self.verifier_validite(action_precedente, pari, palifico)

        while not action_valide:
            pari = self.demander_pari(False)
            action_valide = self.verifier_validite(action_precedente, pari, palifico)
                
        self.pari["nb_des"], self.pari["valeur_des"] = pari
        
        return self

    """
    Fonction permettant de demander le pari du Joueur

    Renvoie :
    - un tuple contenant le nombre de dés et la valeur de ces derniers pariés par le Joueur
    """
    def demander_pari(self, premiere_fois) -> tuple:
            if not premiere_fois:
                print("Vous n'avez pas augmenté l'enchère ou saisi un nombre de dés / valeur de dés invalide :(")

            message = """Saississez votre pari (par exemple : "Je pense qu'il y a au moins 4 dés de valeur 5 à cette table")\n"""
            paris = re.findall(r'\d+', input(message))

            while len(paris) < 2 : 
                print("Saisie invalide (pas assez de nombres trouvés)")
                message = """Saississez votre pari (par exemple : "Je pense qu'il y a au moins 4 dés de valeur 5 à cette table")\n"""
                paris = re.findall(r'\d+', input(message))
            
        
            resultat = (int(paris[0]), int(paris[1]))
            return resultat

    """
    Fonction permettant de vérifier si un pari est valide
    Un pari est valide si l'enchère est valide (les valeurs sont supérieures à l'enchère précedente) 
    et si les valeurs du pari sont autorisés (nombre de dés < 30, 1 <= valeur du dé <= 6)

    Renvoie :
    - un booléen égal à True si le pari est valide
    """

    def verifier_validite(self, action_precedente, pari, palifico) -> bool:
            nb_des, valeur = pari
            
            if isinstance(action_precedente, Encherir):
                nb_des, valeur = pari
                
                if palifico :
                    enchere_valide = nb_des > action_precedente.pari["nb_des"] and valeur == action_precedente.pari["valeur_des"]
                    pari_valide = (nb_des < 30) and (valeur <= 6 and valeur >= 1)                
                else:
                    enchere_valide = nb_des > action_precedente.pari["nb_des"] or valeur > action_precedente.pari["valeur_des"]
                    pari_valide = (nb_des < 30) and (valeur <= 6 and valeur >= 1)
                
                return enchere_valide and pari_valide
            
            elif isinstance(action_precedente, Paco):
                return nb_des < 2*action_precedente.pari['nb_des']+1