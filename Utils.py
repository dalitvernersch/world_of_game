import os

# Default file name for scores
SCORES_FILE_NAME = "Scores.txt"

# Bad return code
BAD_RETURN_CODE = -1


# Function to clear the screen
def screen_cleaner():
    # Clear the screen based on the operating system
    if os.name == 'posix':
        # For Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':
        # For Windows
        os.system('cls')
    else:
        # Unsupported operating system
        print("Unsupported operating system. Unable to clear the screen.")
