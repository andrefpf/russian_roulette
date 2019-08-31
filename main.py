from player import Player
from game import Game

def new_player():
    print('what is your name?')
    name = input()
    players.append(Player(name))

def start_game():
    game = Game(players)

players = []
new_player()
new_player()
start_game()