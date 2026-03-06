# Step 1: Setup the quiz questions
quiz = [
    {
        "question": "What is the largest planet in the solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "correct_answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs in Python?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "correct_answer": "C"
    },
    {
        "question": "Which keyword is used to create a loop in Python?",
        "options": ["A. repeat", "B. loop", "C. for", "D. iterate"],
        "correct_answer": "C"
    }
]

# Step 2: Initialize score
score = 0

# Step 3: Loop through the quiz questions
for q in quiz:
    print("\n" + q["question"])

    # Display options
    for option in q["options"]:
        print(option)

    # Step 4: Get user input
    answer = input("Enter your answer (A/B/C/D): ").upper()

    # Step 5: Check the answer
    if answer == q["correct_answer"]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        print("The correct answer is:", q["correct_answer"])

# Step 6: Show final score
print("\nQuiz Finished")
print("Your score:", score, "out of", len(quiz))