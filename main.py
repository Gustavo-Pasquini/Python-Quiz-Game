import random

QUESTION = 4

corrects = 0

question_answer = {
    "Where does CPU stand for? ": "central processing unit",
    "Where does GPU stand for? ": "graphics processing unit",
    "Where does RAM stand for? ": "random acess memory",
    "Where does PSU stand for? ": "power supply"
}

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Lets Play!")

asked_questions = set()

for i in range(QUESTION):
    while True:
        question = random.choice(list(question_answer.keys()))
        if question not in asked_questions:
            asked_questions.add(question)
            correct_answer = question_answer[question]
            break
    user_answer = input(f"{i}. {question}")
    if user_answer.lower() == correct_answer:
        print("Correct!")
        corrects = corrects + 1
    else:
        print("Incorrect!")

print("Congratulations, you finished the quiz!!! 🥳")

if corrects == QUESTION:
    print("You answered correctly all the questions!")
else:
    print(f"You answered correctly {corrects}/{QUESTION} questions!")
