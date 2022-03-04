from action import Action
import re



class Encherir(Action):
    """
    La classe Enchérir permet de lancer à un Joueur d'enchérir.
    Elle permet à un Joueur doit annoncer un nombre de dés ou une valeur de dé supérieur à l'enchère précédente.
    """

    def __init__(self) -> None:
        super().__init__()
        self.pari = {
            "nb_des": 0,
            "valeur_des": 0
        }

    def __str__(self) -> str:
        return "Je suis l'action {} et mon pari actuel est {}".format(self.name, self.pari)
        
    """Méthode gérant la logique de l'action : demande le pari du joueur et vérifie qu'il est valide"""
    def lancer(self, action_precedente) -> None:
        pari = demander_pari(True)

        action_valide = verifier_validite(action_precedente, pari)

        while not action_valide:
            action_valide = verifier_validite(action_precedente, pari)
            pari = demander_pari(False)

            
        self.pari["nb_des"], self.pari["valeur_des"] = pari

    
        print(self)

"""
Fonction permettant de demander le pari du Joueur

Renvoie :
 - un tuple contenant le nombre de dés et la valeur de ces derniers pariés par le Joueur
"""
def demander_pari(premiere_fois) -> tuple:
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
et si les valeurs du pari sont autorisés (nombre de dés < 30, 2 <= valeur du dé <= 6)

Renvoie :
 - un booléen égal à True si le pari est valide
"""

def verifier_validite(action_precedente, pari) -> bool:
        nb_des, valeur = pari
        
        enchere_valide = nb_des > action_precedente.pari["nb_des"] and valeur > action_precedente.pari["valeur_des"]
        pari_valide = (nb_des < 30) and (valeur < 6 and valeur > 2)
        
        return enchere_valide and pari_valide
    
    

        
        
  