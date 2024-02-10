import random 

min = 0
max = 0

while True:

    print('Hi friend do you want to play a guessing game?')

    answer = input()

    if answer == 'no':
        print('Goodbye. :(')
        break

    # yes we play the game

    print('What difficulty do you want to play on, 1, 2, or 3?')

    difficulty = int(input())

    if difficulty == 1:
        min = 1
        max = 10
    elif difficulty == 2:
        min = 1
        max = 100
    else:
        min = 1
        max = 1000
    
    print(f"I'm thinking of a number between {min} and {max}.")

    number = random.randint(min, max)

    while True:
        print('Take your guess!')

        guess = int(input())

        if guess == number:
            print('Yay you win!!!')
            break
        elif guess < number:
            print('Too low!')
        else:
            print('Too high')
