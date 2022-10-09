#!/usr/bin/env python3
from random import randint
import prompt


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        num = randint(0, 100)
        print(f'Question: {num}\nYour answer: ', end="")
        ans = input()
        if num % 2 == 0:
            quest = 'yes'
        else:
            quest = 'no'
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
    even()


if __name__ == '__main__':
    main()
