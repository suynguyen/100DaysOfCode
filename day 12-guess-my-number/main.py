import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
mode = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

random_number = random.randint(1, 100)


def choose_hard_mode():
    attempts_hard = 5
    print(f"random number is: {random_number}")
    while attempts_hard != 0:
        user_guess_number = int(input("Make a guess: "))
        if user_guess_number != random_number:
            attempts_hard -= 1
            print(f"Your have {attempts_hard - 1} remaining to guess the number")
            if user_guess_number > random_number:
                print("Too high")
            elif user_guess_number < random_number:
                print("Too low")
        elif user_guess_number == random_number:
            print(f"You won, the random number is {random_number}")
            return


def choose_easy_mode():
    attempts_easy = 10
    print(f"random number is: {random_number}")
    while attempts_easy != 0:
        user_guess_number = int(input("Make a guess: "))
        if user_guess_number != random_number:
            attempts_easy -= 1
            print(f"Your have {attempts_easy} remaining to guess the number")
            if user_guess_number > random_number:
                print("Too high")
            elif user_guess_number < random_number:
                print("Too low")
        elif user_guess_number == random_number:
            print(f"You won, the random number is {random_number}")
            return


if mode == "hard":
    choose_hard_mode()
elif mode == "easy":
    choose_easy_mode()
