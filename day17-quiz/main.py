from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

new_quiz_brain = QuizBrain(question_bank)
while new_quiz_brain.still_has_question():
    new_quiz_brain.next_question()
    print(f"Your Score is {new_quiz_brain.score}/{new_quiz_brain.question_number}")
print(f"You got {new_quiz_brain.score} right")
