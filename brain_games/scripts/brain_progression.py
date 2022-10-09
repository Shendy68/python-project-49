#!/usr/bin/env python3
import prompt
from random import randint, randrange


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def progression():
    print('What number is missing in the progression?')
    i = 1
    while i <= 3:
        begin = randint(0, 20)
        long = randint(5, 10)
        inter = randint(1, 10)
        end = long * inter + begin
        progr = list(range(begin, end, inter))
        random_index = randrange(len(progr))
        quest = progr[random_index]
        begin_progr = ' '.join(str(value) for value in progr[:random_index])
        end_progr = ' '.join(str(value) for value in progr[random_index + 1:])
        print(f'Question: {begin_progr} .. {end_progr}')
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
    progression()


if __name__ == '__main__':
    main()
