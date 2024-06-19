import tkinter
import quiz_brain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: quiz_brain.QuizBrain):
        self.quiz_brain = quiz

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text=f"Score: {self.quiz_brain.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text=f"",
                                                     fill=THEME_COLOR,
                                                     font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = tkinter.PhotoImage(file="images/true.png")
        self.right_button = tkinter.Button(image=right_img, highlightthickness=0, command=self.right_pressed)
        self.right_button.grid(row=2, column=0)

        left_img = tkinter.PhotoImage(file="images/false.png")
        self.wrong_button = tkinter.Button(image=left_img, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def wrong_pressed(self):
        if self.quiz_brain.check_answer("False"):
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
