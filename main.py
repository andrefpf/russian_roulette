import os
from game import Game
from player import Player

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
    game = Game(players, roulette_type)

players = []
print('WARNING!')
print('You might use a roulette picture to play this.')
print()
print('What kind of roulette do you want to play?')
print('0 - American')
print('1 - European')
print('2 - French  ')
roulette_type = int(input())

os.system('clear')
print('How many players are going to play?')
num_players = int(input())

for p in range(num_players):
    new_player()


start_game()