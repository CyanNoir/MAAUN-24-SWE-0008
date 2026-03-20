from datetime import datetime
from flask import Flask, request

app = Flask(__name__)
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()

questions = [
    Question("What is the pinnacle of motorsport?", "Formula1"),
    Question("Who was the 2020 Formula1 World Champion?", "Lewis Hamilton"),
    Question("What language is used in Flask?", "Python")
]
@app.route("/")
def home():
    return """
    <h1>Welcome to the CBT App</h1>
    <a href='/quiz'>Start Quiz</a>
    """
if __name__ == "__main__":
    app.run(debug=True)
    @app.route("/quiz", methods=["GET", "POST"])
def quiz():
    score = 0

    if request.method == "POST":
        user_answers = [
            request.form.get("q1"),
            request.form.get("q2"),
            request.form.get("q3")
        ]

        for i in range(len(questions)):
            if questions[i].check_answer(user_answers[i]):
                score += 1

        time_submitted = datetime.now()

        return f"""
        <h2>Your Score: {score}/3</h2>
        <p>Submitted at: {time_submitted}</p>
        <a href='/'>Go Home</a>
        """

    return """
    <form method="post">
        <p>1. What is the pinnacle of motorsport?</p>
        <input name="q1">

        <p>2. Who was the 2020 Formula 1 World Champion?</p>
        <input name="q2">

        <p>3. What language is used in Flask?</p>
        <input name="q3">

        <br><br>
        <button type="submit">Submit</button>
    </form>
    """
    