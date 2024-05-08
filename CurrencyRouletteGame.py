import random
import requests


def get_money_interval(difficulty):
    try:
        # Fetching the current exchange rate from USD to ILS using a free currency API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        rate = data['rates']['ILS']

        # Generating the interval based on difficulty
        total_value = random.randint(1, 100)
        interval = (total_value - (5 - difficulty), total_value + (5 - difficulty))
        interval_in_ils = tuple(round(val * rate, 2) for val in interval)
        return interval_in_ils
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Enter your guess for the value in ILS: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")


def play(difficulty):
    try:
        interval = get_money_interval(difficulty)
        if interval is None:
            print("Failed to retrieve currency data. Exiting game.")
            return False

        print(f"Guess the value of the generated number in ILS (between {interval[0]} and {interval[1]}):")
        user_guess = get_guess_from_user()

        if interval[0] <= user_guess <= interval[1]:
            print("Congratulations! Your guess is within the correct interval.")
            return True
        else:
            print("Sorry, your guess is outside the correct interval. You lost!")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# try:
#     difficulty = int(input("Enter the difficulty level (1-5): "))
#     if not 1 <= difficulty <= 5:
#         print("Invalid difficulty level. Please enter a number between 1 and 5.")
#     else:
#         result = play(difficulty)
#         if result:
#             print("You won!")
#         else:
#             print("Better luck next time!")
# except ValueError:
#     print("Please enter a valid integer for the difficulty level.")
