#!/usr/bin/env python3
from random import randint
import prompt


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def even():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 1
    while i <= 3:
        num = randint(0, 100)
        print(f'Question: {num}\nYour answer: ', end="")
        answer = input()
        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            print('Correct!')
            if i == 3:
                print(f'Congratulations, {name}!')
            i += 1
        elif num % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'")
            break
        elif num % 2 != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
            break


def main():
    print('Welcom to the Brain Games!')
    welcome_user()
    even()


if __name__ == '__main__':
    main()
