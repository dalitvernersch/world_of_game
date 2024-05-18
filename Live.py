from Score import ScoreManager


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play")


# def load_game():
#     print("Please choose a game to play:")
#     print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
#     print("2. Guess Game - guess a number and see if you chose like the computer")
#     print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
#     # game_choice = int(input("Enter the number of the game you want to play:"))
#     while True:
#         try:
#             game_choice = int(input("Please Enter the number of the game you want to play: "))
#             if 1 <= game_choice <= 3:
#                 break
#             else:
#                 print("Please enter a Number between 1 and 3.")
#         except ValueError:
#             print("Invalid Number input. Please enter a Number between 1 and 3.")
#
#     while True:
#         try:
#             difficulty = int(input("Please choose game difficulty from 1 to 5:"))
#             if 1 <= difficulty <= 5:
#                 print("All Good :)")
#                 break
#             else:
#                 print("Please enter a Number between 1 and 5.")
#         except ValueError:
#             print("Invalid Number input. Please enter a Number between 1 and 5.")


def load_game():
    global score
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while True:
        try:
            game_choice = int(input("Please Enter the number of the game you want to play: "))
            if 1 <= game_choice <= 3:
                break
            else:
                print("Please enter a Number between 1 and 3.")
        except ValueError:
            print("Invalid Number input. Please enter a Number between 1 and 3.")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5:"))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Please enter a Number between 1 and 5.")
        except ValueError:
            print("Invalid Number input. Please enter a Number between 1 and 5.")

    if game_choice == 1:
        from MemoryGame import play
        score = play(difficulty)
    elif game_choice == 2:
        from GuessGame import play
        score = play(difficulty)
    elif game_choice == 3:
        from CurrencyRouletteGame import play
        score = play(difficulty)

    if score is not None:
        # If the user won the game, update the score
        score_manager = ScoreManager()
        score_manager.add_score(difficulty)
