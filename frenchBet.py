import os
import random
from bet import Bet

class FrenchBet(Bet):
    def __init__(self, price, kind_of_bet):
        Bet.__init__(self, price, kind_of_bet)

        bet_types = ['', self.low_high, self.red_black, self.even_odd, 
                    self.dozen, self.column, self.single, self.split, 
                    self.street, self.square, self.neighbors_of_zero]

        function = bet_types[self.type]
        function()

    def single(self):
        os.system('clear')
        print('Select a number between 0 and 36')
        selected = int(input())
        self.range = [selected]

    def neighbors_of_zero(self):
        options = [[0, 1], [0, 2], [0, 3],
                   [0,1,2], [0,2,3], [0,1,2,3]]
        os.system('clear')
        print('Select the collumn')

        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        selected = int(input())
        self.range = options[selected]
