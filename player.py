from bet import Bet
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 100
        self.passed_rounds = 0
        self.bets = []
    
    def start_betting(self):
        while True:
            os.system('clear')
            print('Betted: {}'.format(self.get_betted()))
            print('Your Money: {}'.format(self.chips))
            print('Passed Rounds: {}'.format(self.passed_rounds))
            print('*****************************')
            print('What kind of bet do you want {}?'.format(self.name))
            print('0 - Next                     ')
            print('1 - Low or High              ')
            print('2 - Red or Black             ')
            print('3 - Even or Odd              ')
            print('4 - Dozen                    ')
            print('5 - Column                   ')
            print('6 - Single                   ')
            bet_type = int(input())

            if bet_type == 0 and self.bets == [] and self.passed_rounds >= 3:
                print('You exceeded your right to pass')
                input()
                continue
            elif bet_type == 0:
                if self.bets == []:
                    self.passed_rounds += 1
                break

            while True:
                os.system('clear')
                print('How much do you want to bet?')
                price = int(input())

                if price > self.chips:
                    print()
                    print('YOU HAVE NOT ENOUGHT MONEY')
                elif price < 0:
                    print()
                    print('Haha, Very funny')
                else:
                    self.chips -= price
                    self.bets.append(Bet(price, bet_type))
                    break

    def owned_money(self, number):
        owned = 0
        for bet in self.bets:
            if number in bet.range:
                owned += bet.winning_price()
        return owned

    def get_betted(self):
        betted = 0
        for bet in self.bets:
            betted += bet.price
        return betted

