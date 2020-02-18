from random import random

GAME_STATE = True

while GAME_STATE:
    WIN_STATE = False

    while True:
        random_num = int(random() * 10000)

        if len(random_num) == 4:
            break

        if len(random_num) < 4:
            random_num = "0" * (4 - len(random_num)) + random_num
            break

    print(f'GENERATED NUMBER: {random_num}')

    print("Welcome to the Game!\n\n")

    for chance in range(1,9):
        number = input(f'Please input a 4 digit number({chance}/8): ')

        if number.isdigit():
            if len(number) == 4:
                if number == random_num:
                    WIN_STATE = True
                else:
                    print("WARNING: THE INPUT IS WRONG. TRY AGAIN!")
                    
                    digit1_valid = 'correct' if number[0] == random_num[0] else 'incorrect'
                    digit2_valid = 'correct' if number[1] == random_num[1] else 'incorrect'
                    digit3_valid = 'correct' if number[2] == random_num[2] else 'incorrect'
                    digit4_valid = 'correct' if number[3] == random_num[3] else 'incorrect'

                    # Output the feedback for the wrong result
                    print(f'1st digit: {digit1_valid}')
                    print(f'2st digit: {digit2_valid}')
                    print(f'3st digit: {digit3_valid}')
                    print(f'4st digit: {digit4_valid}')
            else:
                print("ERROR: THE LENGTH OF THE INPUT IS NOT 4")
        else:
            print("ERROR: THE INPUT CONSISTS OF NON-DIGIT INPUT")

        if WIN_STATE:
            print("Congratulations! You Win!")
            break

    # If all attempts failed
    if not(WIN_STATE):
        print("You lose!")