#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def prime_num():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    while i <= 3:
        num = randint(0, 99)
        print(f'Question: {num}')
        ans = prompt.string('Your answer: ')
        for div in range(2, num):
            if num % div == 0:
                quest = 'no'
                break
        else:
            quest = 'yes'
        if str(quest) == ans:
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {name}')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{quest}'.")
            print(f"Let's try again, {name}!")
        i += 1


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    prime_num()


if __name__ == '__main__':
    main()
