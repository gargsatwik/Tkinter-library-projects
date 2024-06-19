import question_model
import data
import quiz_brain
import ui

question_bank = []
for question in data.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)
quiz_ui = ui.QuizInterface(quiz)
