import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.question_number += 1
            self.current_question = self.question_list[self.question_number]
            return html.unescape(self.current_question.text)

    def check_answer(self, user_input):
        correct_answer = self.current_question.answer
        if correct_answer == user_input:
            self.score += 1
            return True
