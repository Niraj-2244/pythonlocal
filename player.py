import math
import random


class player:
    def __init__(self, letter):
        #letter is c or o
        self.letter = letter


    


class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        valid_sqare = False
        val = None
        while not valid_sqare:
            square = input(self.letter + '\'s turn. Input move (0-8):')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_sqare = True
            except ValueError:
                print('Invalid square. Try again')

        return val