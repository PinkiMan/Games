__author__ = "Pinkas Matěj"
__copyright__ = ""
__credits__ = []
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Pinkas Matěj"
__email__ = "pinkas.matej@gmail.com"
__status__ = "Prototype"
__date__ = "14/08/2024"
__created__ = "14/08/2024"

"""
Filename: number_guessing.py

"""


import random
import math

def get_number(text):
    num = None
    while True:
        inp = input(text)
        try:
            num = int(inp)
            break
        except ValueError:
            print(f'Error: \'{inp}\' is not integer')

    return num


class NumberGuesserGame:
    def __init__(self):
        self.lower_limit = None
        self.upper_limit = None
        self.number = None
        self.difficulty = 1

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty


    def set_limits(self):
        self.lower_limit = get_number('Enter lower limit: ')
        self.upper_limit = get_number('Enter upper limit: ')

    def set_number(self):
        self.number = random.randint(self.lower_limit, self.upper_limit)

    def guess(self, max_range):
        count = 0
        while count < max_range:
            guess = get_number('Guess a number: ')
            count += 1

            if guess == self.number:
                print(f'Congratulations you did it in {count} try')
                break
            elif guess < self.number:
                print(f'Bigger than {guess}')
            elif guess > self.number:
                print(f'Smaller than {guess}')

        if count == max_range:
            print(f'Number was {self.number}, better luck next try')

    def set_max_tries(self):
        if self.difficulty == 0:
            return self.upper_limit - self.lower_limit + 1
        elif self.difficulty == 1:
            return self.upper_limit - self.lower_limit
        elif self.difficulty == 2:
            return round(math.log(self.upper_limit - self.lower_limit + 1, 2)) + 1
        elif self.difficulty == 3:
            return round(math.log(self.upper_limit - self.lower_limit + 1, 2))

    def main(self):
        self.set_limits()
        self.set_number()

        max_tries = self.set_max_tries()

        print('\nNumber was set')
        print(f'You have only {max_tries} tries')
        self.guess(max_tries)



if __name__ == "__main__":
    game = NumberGuesserGame()
    game.set_difficulty(2)
    game.main()
