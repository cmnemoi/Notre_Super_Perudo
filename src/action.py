from abc import abstractmethod

class Action:
    """
    La classe Action sert de base aux autres Actions du jeu (Enchérir, Dudo, Paco, Palifico)
    Abstraite, il ne faut pas créer d'objets avec.
    """

    def __init__(self, joueur) -> None:
        self.name = type(self).__name__
        self.joueur = joueur
        pass

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def lancer(self) -> 'Action':
        pass

    @abstractmethod
    def verifier_validite(self, action_precedente, pari) -> bool:
        pass

    @abstractmethod
    def demander_pari(self, premiere_fois) -> tuple:
        pass