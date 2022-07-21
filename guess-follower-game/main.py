# pick random account from data

# format account into printable format

# ask user for a guess

# check if user is correct
# get follower account

# feedback

# scorekeeping

# make b become the next a

import random
from data import data


def get_random_account():
    return random.choice(data)


def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"


def game():
    game_should_countinue = True
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_countinue:
        account_a = account_b
        acount_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print("vs")
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has the most followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You are correct. Your current score is {score}")
        else:
            game_should_countinue = False
            print(f"You are wrong. Your score is {score}")


game()
