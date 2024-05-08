
from flask import Flask

app = Flask(__name__)

SCORES_FILE_NAME = "Scores.txt"


def read_score():
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            score = int(file.read())
        return score
    except Exception as e:
        return str(e)


@app.route("/")
def score_server():
    score = read_score()
    if isinstance(score, int):
        html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    else:
        html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{score}</div></h1>
        </body>
        </html>
        """
    return html


if __name__ == '__main__':
    # Bind to 0.0.0.0 to allow access from any IP address
    app.run(host='0.0.0.0', port=5010)
