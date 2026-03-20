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