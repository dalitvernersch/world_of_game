import os

# Points for winning a game based on difficulty
POINTS_OF_WINNING = {
    "EASY": (3 * 3) + 5,  # Difficulty X 3 + 5
    "MEDIUM": (5 * 3) + 5,
    "HARD": (7 * 3) + 5
}


class ScoreManager:
    def __init__(self, scores_file="Scores.txt"):
        self.scores_file = scores_file

    def add_score(self, difficulty):
        # Calculate points based on difficulty
        points = POINTS_OF_WINNING.get(difficulty, 0)

        # Check if scores file exists
        if not os.path.exists(self.scores_file):
            # Create a new scores file and write the initial score
            with open(self.scores_file, "w") as file:
                file.write(str(points))
        else:
            # Read current score from the scores file
            with open(self.scores_file, "r") as file:
                current_score = int(file.read())

            # Add points to the current score
            new_score = current_score + points

            # Write the new score back to the scores file
            with open(self.scores_file, "w") as file:
                file.write(str(new_score))

# Example usage:
# score_manager = ScoreManager()
# score_manager.add_score("EASY")
