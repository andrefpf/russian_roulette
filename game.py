from random import randint
import os

class Game:
    def __init__(self, players, roulette_type):
        self.players = players 
        self.roulette_type = roulette_type
        self.budget = 1000
        self.game_loop()

    def game_loop(self):
        while self.budget > 0 and self.players:
            self.make_bet()
            self.premiate(randint(0, 37))
            self.eliminate_players()
        self.game_over()

    def make_bet(self):
        for player in self.players:
            player.start_betting(self.roulette_type)
    
    def sort_number(self):
        roulette = list(range(0, 37))

        if self.roulette_type == 0:
            roulette.append['00']

        return random.choice(roulette)

    def premiate(self, number):
        os.system('clear')
        print('Number:', number)
        for player in self.players:
            owned = player.owned_money(number)
            print(player.name, owned)
            self.budget -= owned
            player.chips += owned
            player.bets = []
        print('Budget: ', self.budget)
        input()

    def eliminate_players(self):
        for index, player in enumerate(self.players):
            if player.chips <= 0:
                print('{} was eliminated!'.format(player.name))
                input()
                self.players.pop(index)

    def game_over(self):
        winner = ''
        for player in self.players:
            if winner == '':
                winner = player
            elif player.chips > winner.chips:
                winner = player 

        if self.players:
            print(winner.name, 'won!')
            input()