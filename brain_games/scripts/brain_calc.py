#!/usr/bin/env python3
from random import choice, randint
import prompt


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def calc():
    print('What is the result of the expression?')
    oper = ['+', '-', '*']
    i = 1
    while i <= 3:
        num_1 = randint(0, 99)
        num_2 = randint(0, 99)
        r_oper = choice(oper)
        quest = eval(f'{num_1} {r_oper} {num_2}')
        print(f'Question: {num_1} {r_oper} {num_2}')
        ans = prompt.string('Your answer: ')
        if str(quest) == ans:
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {name}')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{quest}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1


def main():
    print('Welcom to the Brain Games!')
    welcome_user()
    calc()


if __name__ == '__main__':
    main()
