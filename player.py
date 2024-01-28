from typing import Type

from card import Card
from hand import Hand

# define player class
class Player:

    def __init__(self):
        self.matrix = None # to define

    def sim(self, trials: int) -> None:
        # run random trials and update the matrix
        pass

    def hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool:
        # use the matrix to decide whether to hit
        pass

    def play(self, trials: int) -> float:
        # play out trials with the learned matrix 
        pass