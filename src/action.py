from abc import abstractmethod

class Action:
    """
    La classe Action sert de base aux autres Actions du jeu (Enchérir, Dudo, Paco, Palifico)
    Abstraite, il ne faut pas créer d'objets avec.
    """

    def __init__(self) -> None:
        self.name = type(self).__name__
        pass

    @abstractmethod
    def lancer(self) -> None:
        pass

    @abstractmethod
    def verifier_validite(self, action_precedente, pari) -> bool:
        pass

    @abstractmethod
    def demander_pari(self, premiere_fois) -> tuple:
        pass