from action import Action

class Dudo(Action):
    def __init__(self, joueur) -> None:
        super().__init__(joueur)

    def lancer(self, action_precdente, palifico = False) -> Action:
        """To do"""
        self.annonce_challenge(action_precdente)

        return self

    """pas besoin de vérifier la validité du pari d'un Dudo"""
    #fonction qui donne si proposition   menteur est vrai ou fausse
    def verifier_validite(self, action_precedente, pari) -> None:
        pass

    """Pas de pari lors d'un Paco"""
    def demander_pari(self, premiere_fois) -> None:
        pass

    def annonce_challenge(self, action_precedente) -> None:
        print("{} pense que {} se trompe !".format(self.joueur, action_precedente.joueur))        
