from action import Action
import re

class Paco(Action):
    def __init__(self, joueur) -> None:
        super().__init__(joueur)
        self.pari = {
            "nb_des": 0,
            "valeur_des": 1
        }

    def lancer(self, action_precedente, palifico = False) -> None:
        pari = self.demander_pari(True)

        action_valide = self.verifier_validite(action_precedente, pari)

        while not action_valide:
            pari = self.demander_pari(False)
            action_valide = self.verifier_validite(action_precedente, pari)
                
        self.pari["nb_des"], self.pari["valeur_des"] = pari
        
        return self

    """
    Fonction permettant de vérifier si un pari est valide
    Un pari est valide si le nombre de Pacos est supérieur au précédent

    Renvoie :
    - un booléen égal à True si le pari est valide
    """
    def verifier_validite(self, action_precedente, pari) -> None:
        """To do"""
        nb_des, valeur = pari

        return nb_des >= action_precedente.pari['nb_des']


    """
    Fonction permettant de demander le pari du Joueur

    Renvoie :
    - un entier contenant le nombre de paco pariés par le Joueur
    """
    def demander_pari(self, premiere_fois) -> tuple:
        if not premiere_fois:
            print("Vous n'avez pas augmenté l'enchère ou saisi un nombre de dés / valeur de dés invalide :(")

        message = """Saississez votre pari (par exemple : "Je pense qu'il y a 4 Pacos à cette table")\n"""
        pari = re.findall(r'\d+', input(message))[0] #on extrait le chiffre avec une regex

        while len(pari) < 1 : #s'il n'y a aucun chiffre
            print("Saisie invalide (aucun nombre trouvé)")
            pari = re.findall(r'\d+', input(message))[0]

        pari = int(pari) #on convertit en entier pour les comparaisons plus tard

        return (int(pari), 1)

    
      