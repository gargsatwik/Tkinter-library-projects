import tkinter
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
dict_to_learn = {}

try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dict_to_learn = original_data.to_dict(orient="records")
else:
    dict_to_learn = words.to_dict(orient="records")

r = random.randint(0, 100)


def new_word():
    global r, flip_timer
    window.after_cancel(flip_timer)
    r = random.randint(0, 100)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{dict_to_learn[r]["French"]}", fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{dict_to_learn[r]["English"]}", fill="white")
    canvas.itemconfig(card_image, image=card_back)


def is_known():
    dict_to_learn.remove(dict_to_learn[r])
    to_learn = pandas.DataFrame(dict_to_learn)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_word()


window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")

right_button = tkinter.Button(image=right_img, command=new_word)
right_button.grid(row=1, column=1)

wrong_button = tkinter.Button(image=wrong_img, command=is_known)
wrong_button.grid(row=1, column=0)

card_back = tkinter.PhotoImage(file="images/card_back.png")
card_front = tkinter.PhotoImage(file="images/card_front.png")

canvas = tkinter.Canvas(height=526, width=800)
card_image = canvas.create_image(400, 264, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 264, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

new_word()

window.mainloop()
