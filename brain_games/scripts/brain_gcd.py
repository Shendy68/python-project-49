#!/usr/bin/env python3
import prompt
from math import gcd
from random import randint


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def gcd_game():
    print('Find the greatest common divisor of given numbers.')
    i = 1
    while i <= 3:
        num_1 = randint(0, 25)
        num_2 = randint(0, 25)
        ans = prompt.string(f'Question: {num_1} {num_2}\nYour answer: ')
        quest = gcd(num_1, num_2)
        if str(quest) == ans:
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{quest}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    gcd_game()


if __name__ == '__main__':
    main()
