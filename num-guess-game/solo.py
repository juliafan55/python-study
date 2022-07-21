# things i did wrong
# -> repetitive code -- checking both easy and hard separately
# -> implementing turns locally
# -> need to break down the problem a bit more
# --> game start -> ask difficulty -> game logic



import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


random_number = random.randrange(1, 101)
# print(random_number)


def easy_game():
    easy_num_of_tries = 10
    easy_game_end = False

    while not easy_game_end:
        print(
            f"You have {easy_num_of_tries} attempts remaining to guess the number.")
        print(random_number)
        guess = int(input("Make a guess: "))

        if guess != random_number:
            easy_num_of_tries -= 1
            if guess > random_number:
                print("Too high.")
                print("Guess again.")
            elif guess < random_number:
                print("Too low.")
                print("Guess again.")
        elif guess == random_number:
            print(f"You got it the answer is {guess}!")
            easy_game_end = True

        if easy_num_of_tries == 0:
            print("You ran out of attempts. You lose.")
            easy_game_end = True


def hard_game():
    hard_num_of_tries = 5
    hard_game_end = False

    while not hard_game_end:
        print(
            f"You have {hard_num_of_tries} attempts remaining to guess the number.")
        print(random_number)
        guess = int(input("Make a guess: "))
        if guess != random_number:
            hard_num_of_tries -= 1
            if guess > random_number:
                print("Too high.")
                print("Guess again.")
            elif guess < random_number:
                print("Too low.")
                print("Guess again.")
        elif guess == random_number:
            print(f"You got it the number is {guess}!")
            hard_game_end = True

        if hard_num_of_tries == 0:
            print("You ran out of attempts. You lose.")
            hard_game_end = True


def game_start():
    correct = True

    while correct:
        if difficulty == "easy":
            easy_game()
        elif difficulty == "hard":
            hard_game()
        elif difficulty != "easy" or difficulty != "hard":
            print("Please try again!")
            correct = False


game_start()
