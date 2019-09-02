from player import Player
from game import Game
import os

def show_ready_players():
    os.system('clear')
    print('Ready players:')
    for p in players:
        print(p.name)
    print('*'*20)

def new_player():
    show_ready_players()
    print('what is your name?')
    name = input()
    players.append(Player(name))

def start_game():
    game = Game(players)

players = []
print('How many players are going to play?')
num_players = int(input())

for p in range(num_players):
    new_player()

start_game()