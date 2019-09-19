import os

class Bet:
    def __init__(self, price, kind_of_bet):
        self.price = price 
        self.type = kind_of_bet
        self.range = []

    def low_high(self):
        options = [list(range(1, 19)), list(range(19, 37))]

        os.system('clear')
        print('Select the range')
        print('0 - Low')
        print('1 - High')
        
        selected = int(input())
        self.range = options[selected]

    def red_black(self):
        options = [[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36], 
                   [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35],]

        os.system('clear')
        print('Select the range')
        print('0 - Red')
        print('1 - Black')

        selected = int(input())
        self.range = options[selected]

    def even_odd(self):
        options = [[i for i in range(1, 37) if i%2 == 0],
                   [i for i in range(1, 37) if i%2 == 1],]

        os.system('clear')
        print('Select the range')
        print('0 - Even')
        print('1 - Odd')

        selected = int(input())
        self.range = options[selected]

    def dozen(self):
        options = [list(range(1, 13)), list(range(13, 25)), list(range(25, 37))]
        os.system('clear')
        print('Select the range')
        print('0 - 1 to 12')
        print('1 - 13 to 24')
        print('2 - 25 to 36')
        selected = int(input())
        self.range = options[selected]

    def column(self):
        options = [[3,6,9,12,15,18,21,24,27,30], 
                   [2,5,8,11,14,17,20,23,26,29], 
                   [1,4,7,10,13,16,19,22,25,28],]
        os.system('clear')
        print('Select the collumn')

        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        selected = int(input())
        self.range = options[selected]
        
    def single(self):
        os.system('clear')
        print('Select a number between 0 and 36')
        selected = int(input())
        self.range = [selected]

    def split(self):
        os.system('clear')
        print('Select a number between 0 and 36')
        first_number = int(input())
        options = self.__split_options__(first_number)
        
        print('Select the second number')
        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        selected = int(input())
        self.range = [first_number] + options[selected]
    
    def street(self):
        options = [[i+1, i+2, i+3] for i in range(0, 36, 3)]
        print('Select the range')

        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        selected = int(input())
        self.range = options[selected]

    def square(self):
        os.system('clear')
        print('Select a number between 1 and 36')
        first_number = int(input())
        options = self.__square_options__(first_number)
        
        print('Select the square you want')
        for num, row in enumerate(options):
            print('{} - {}'.format(num, row))

        selected = int(input())
        self.range = [first_number] + options[selected]

    def winning_price(self):
        return self.price * (36 // len(self.range))

    def __split_options__(self, first_number):
        options = []

        if first_number % 3 != 0:
            options.append(first_number - 1)

        if first_number % 3 != 1:
            options.append(first_number + 1)

        if first_number < 34:
            options.append(first_number - 3)

        if first_number > 3:
            options.append(first_number + 3)
            
        return options

    def __square_options__(self, first_number):
        options = []

        upper_left = (first_number % 3) != 1 and first_number > 3
        upper_right = (first_number % 3) != 0 and first_number > 3
        lower_left = (first_number % 3) != 1 and first_number < 34
        lower_right = (first_number % 3) != 1 and first_number < 34

        if upper_left:
            options = [first_number-4, first_number-3, first_number-1, first_number]

        if upper_right:
            options = [first_number-3, first_number-2, first_number, first_number+1]

        if lower_left:
            options = [first_number-1, first_number, first_number+2, first_number+3]

        if lower_right:
            options = [first_number, first_number+1, first_number+3, first_number+4]
        
        return options