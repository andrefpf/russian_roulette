from random import randint

class Game:
    def __init__(self, players, roulette_type=''):
        self.players = players 
        self.roulette_type = roulette_type
        self.budget = 1000
        self.game_loop()

    def game_loop(self):
        while self.budget > 0 and len(self.players) > 1:
            self.make_bet()
            self.premiate(randint(0, 37))
            self.eliminate_players()
        self.game_over()

    def make_bet(self):
        for player in self.players:
            player.start_betting()
    
    def sort_number(self):
        randint(0, 37)

    def premiate(self, number):
        print('Number:', number)
        for player in self.players:
            owned = player.owned_money(number)
            print(player.name, owned)
            self.budget -= owned
            player.chips += owned

    def eliminate_players(self):
        for index, player in enumerate(self.players):
            if player.chips <= 0:
                print('{} foi eliminado'.format(player.name))
                self.players.pop(index)

    def game_over(self):
        print(self.players[0].name, 'venceu')