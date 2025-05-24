import os
import sys
import json
import time
import random

if os.path.exists("highscore_db.json"):
    with open("highscore_db.json", "r") as hd:
        highscore_db = json.load(hd)
else:
    highscore_db = {
        1: "No High Score",
        2: "No High Score",
        3: "No High Score"
    }
    with open("highscore_db.json", "w") as hd:
        json.dump(highscore_db, hd)

while True:
    print("Welcome to the Number Guessing Game! " \
    "\nI'm thinking of a number between 1 and 100. " \
    "\n")

    print("Please select the difficulty level: " \
    "\n 1. Easy (10 chances) " \
    "\n 2. Medium (5 chances) " \
    "\n 3. Hard (3 chances)" \
    "\n")

    while True:
        try: 
            difficulty = int(input())
            if difficulty > 3:
                print("Invalid Difficulty. Please select a number between 1 and 3")
            if difficulty < 4 and difficulty > 0:
                break
        except:
            print("Invalid Difficulty. Please select a number between 1 and 3")

    difficulty_dict = {
        1: ["easy", 10],
        2: ["medium", 5],
        3: ["hard", 3]
    }

    if highscore_db[str(difficulty)] == "No High Score":
        print(f"Great you have selected the {difficulty_dict[difficulty][0]} difficulty level. \nYou have {difficulty_dict[difficulty][1]} chances to guess the correct number." \
            "\nLet's start the game!" \
            "\n")
    else:
        print(f"Great you have selected the {difficulty_dict[difficulty][0]} difficulty level. \nYou have {difficulty_dict[difficulty][1]} chances to guess the correct number. \nThe high score is {highscore_db[str(difficulty)]} chances." \
            "\nLet's start the game!" \
            "\n")

    guesses = difficulty_dict[difficulty][1]
    correct_number = random.randint(1, 100)
    print(correct_number)

    start = time.time()
    for i in range(guesses):
        check = time.time()
        if check - start > 60:
            print("Do you want a hint? [Y/n]")
            hint = input()
            if hint == "Y" or hint == "y":
                if len(str(correct_number)) == 1:
                    print("The first character in the number is 0")
                else:
                    print(f"The first character in the number is {str(correct_number)[0]}.")
            elif hint not in ["n", "N", "y", "Y"]:
                while True:
                    print("That is not a valid answer. Please select 'Y' if you would like a hint or 'n' if not.")
                    hint = input()
                    if hint == "Y" or hint == "y":
                        if len(str(correct_number)) == 1:
                            print("The first character in the number is 0")
                            break
                        else:
                            print(f"The first character in the number is {str(correct_number)[0]}.")
                            break
        if i == difficulty_dict[difficulty][1] - 1:
            print("You have one guess left. Do you want a hint? [Y/n]")
            hint = input()
            if hint == "Y" or hint == "y":
                if len(str(correct_number)) == 1:
                    print("The first character in the number is 0")
                else:
                    print(f"The first character in the number is {str(correct_number)[0]}.")
            elif hint not in ["n", "N", "y", "Y"]:
                while True:
                    print("That is not a valid answer. Please select 'Y' if you would like a hint or 'n' if not.")
                    hint = input()
                    if hint == "Y" or hint == "y":
                        if len(str(correct_number)) == 1:
                            print("The first character in the number is 0")
                            break
                        else:
                            print(f"The first character in the number is {str(correct_number)[0]}.")
                            break
                
        print(f"Enter your guess:")
        guess = int(input())
        won = False
        if guess == correct_number:
            end = time.time()
            print(f"Congratulations! You guessed the correct number in {i + 1} attempt(s) and {round(end - start, 2)} seconds.")
            if highscore_db[str(difficulty)] == "No High Score":
                highscore_db[str(difficulty)] = i + 1
                print(f"New High Score for {difficulty_dict[difficulty][0]} difficulty: {i + 1}")
                with open("highscore_db.json", "w") as hd:
                    json.dump(highscore_db, hd)
            elif i < int(highscore_db[str(difficulty)]):
                highscore_db[str(difficulty)] = i + 1
                with open("highscore_db.json", "w") as hd:
                    json.dump(highscore_db, hd)
            won = True
            break
        elif guess > correct_number:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < correct_number:
            print(f"Incorrect! The number is greater than {guess}.")

    if won == False:
        end = time.time()
        print(f"Sorry you are out of guesses. The number was {correct_number}. \nYou played for {round(end - start, 2)} seconds. \nWould you like to play again? [Y/n]")
        restart = input()
        if restart == "n" or restart == "N":
            print("Game Over! Thank you for playing.")
            sys.exit()
        elif restart not in ["n", "N", "y", "Y"]:
            while True:
                print("That is not a valid answer. Please select 'Y' if you would like to play again or 'n' if not.")
                restart = input()
                if restart == "n" or restart == "N":
                    print("Game Over! Thank you for playing.")
                    sys.exit()
                elif restart == "Y" or restart == "y":
                    break
    else:
        print("Would you like to play again? [Y/n]")
        restart = input()
        if restart == "n" or restart == "N":
            print("Game Over! Thank you for playing.")
            sys.exit()
        elif restart not in ["n", "N", "y", "Y"]:
                    while True:
                        print("That is not a valid answer. Please select 'Y' if you would like to play again or 'n' if not.")
                        restart = input()
                        if restart == "n" or restart == "N":
                            print("Game Over! Thank you for playing.")
                            sys.exit()
                        elif restart == "Y" or restart == "y":
                            break