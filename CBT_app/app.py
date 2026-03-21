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
    Question("How many qualifying sessions are there in a Formula1 weekend?", "Three"),
    Question("Who was the world champion in 2007?", "Kimi Raikkonen")
    
]
@app.route("/")
def home():
    return """
    <h1>Welcome to the CBT App</h1>
    <a href='/quiz'>Start Quiz</a>
    """
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    score = 0

    if request.method == "POST":
        user_answers = [
            request.form.get("q1"),
            request.form.get("q2"),
            request.form.get("q3"),
            request.form.get("q4")
        ]

        for i in range(len(questions)):
            if questions[i].check_answer(user_answers[i]):
                score += 1

        time_submitted = datetime.now()

        return f"""
        <h2>Your Score: {score}/{len(questions)}</h2>
        <p>Submitted at: {time_submitted}</p>
        <a href='/'>Go Home</a>
        """

    return """
    <h1>FORMULA1 CBT Quiz</h1>
    <body style="background-color: red; color: white; font-family: Arial; text-align: center;">
    <a href="/">Go Home</a>
    <form method="post">
        <p>1. What is the pinnacle of motorsport?</p>
        <input name="q1" placeholder="Enter answer">
    
        <p>2. Who was the 2020 Formula 1 World Champion?</p>
        <input name="q2" placeholder="Enter answer">

        <p>3. How many qualifying sessions are there in a Formula1 weekend?</p>
        <input name="q3" placeholder="Enter answer">

        <p>4. Who was the world champion in 2007?</p>
        <input name="q4" placeholder="Enter answer">

        <br><br>
        <button type="submit">Submit</button>
    </form>
    """
if __name__ == "__main__":
    app.run(debug=True)