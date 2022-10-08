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
        num_1 = randint(1, 99)
        num_2 = randint(1, 99)
        rand_oper = choice(oper)
        question = eval(f'{num_1} {rand_oper} {num_2}')
        answer = prompt.string(f'Question: {num_1} {rand_oper} {num_2}\nYour answer: ')
        if str(question) == answer:
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {name}')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{question}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1
        

def main():
    print('Welcom to the Brain Games!')
    welcome_user()
    calc()


if __name__ == '__main__':
    main()
    

    