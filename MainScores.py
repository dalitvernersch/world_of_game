from flask import Flask, render_template

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
        return render_template('score.html', score=score)
    else:
        return render_template('error.html', error=score)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
