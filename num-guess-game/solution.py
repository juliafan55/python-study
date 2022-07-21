# choosing a random number between 1 and 100
# make functionality to set difficulty
# let user guess a number
# function to check user's guess against actual answer
# track the number of turns and reduce by 1 if they get it wrong
# repeat the guessing functionality if they get it wrong


from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks against answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)
    print(answer)

    # the number of turns will depend on what set_difficulty function returns
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
