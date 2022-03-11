from action import Action

class Paco(Action):
    def __init__(self, joueur) -> None:
        super().__init__(joueur)

    def lancer(self) -> None:
        """To do"""

    def verifier_validite(self, action_precedente, pari) -> None:
        """To do"""
        
    def demander_pari(self, premiere_fois) -> tuple:
        """To do"""