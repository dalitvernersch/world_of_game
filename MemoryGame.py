import random
import time


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    print("Memorize the following numbers:")
    sequence = generate_sequence(difficulty)
    print(sequence)
    time.sleep(0.7)  # Display the numbers for 0.7 seconds
    print("\nNow, enter the numbers you remember:")
    user_input = []
    for i in range(difficulty):
        while True:
            try:
                number = int(input(f"Number {i + 1}: "))
                if 1 <= number <= 101:
                    user_input.append(number)
                    break
                else:
                    print("Please enter a number between 1 and 101.")
            except ValueError:
                print("Please enter a valid integer.")
    return user_input


def is_list_equal(list1, list2):
    return list1 == list2


def play(difficulty):
    sequence = generate_sequence(difficulty)
    user_input = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_input)


try:
    difficulty = int(input("Enter the difficulty level: "))
    result = play(difficulty)
    if result:
        print("Congratulations! You remembered all the numbers. You won!")
    else:
        print("Sorry, you didn't remember all the numbers. You lost!")
except ValueError:
    print("Please enter a valid integer for the difficulty level.")
