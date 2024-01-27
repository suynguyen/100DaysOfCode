class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number +1}: {current_question.text} (True/False)")
        self.question_number += 1
        if user_answer == current_question.answer:
            self.score += 1

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
