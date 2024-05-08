import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Enter a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print("Please enter a valid number within the specified range.")
        except ValueError:
            print("Please enter a valid integer.")


def compare_results(secret_number, user_guess):
    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        return True
    else:
        print(f"Sorry, the correct number was {secret_number}. Better luck next time!")
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)


try:
    difficulty = int(input("Enter the difficulty level (maximum number to guess): "))
    result = play(difficulty)
    if result:
        print("You won!")
    else:
        print("You lost!")
except ValueError:
    print("Please enter a valid integer.")
