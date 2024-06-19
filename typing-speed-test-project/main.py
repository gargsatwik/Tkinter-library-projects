import tkinter
import random
from tkinter import messagebox


timer = None
time = 30


paragraphs = []  # random paragraphs or text you want to test your speed on


def start_function():
    global time
    entry.config(state="normal")
    count_down(time)


def count_down(time):
    timer_label = tkinter.Label(window, text=time, font=("Arial", 20))
    timer_label.grid(row=0, column=1)
    if time > 0:
        window.after(1000, count_down, time-1)
    else:
        end_function()
    return 0


def reset_function():
    global time
    time = 30
    entry.delete(0, tkinter.END)
    start_function()


def check_accuracy():
    expected = paragraph_text.split(" ")
    user_input = entry.get().split(" ")
    common = 0
    print(expected)
    print(user_input)
    for i in range(min(len(expected), len(user_input))):
        if expected[i] == user_input[i]:
            common += 1
    if len(user_input) == 0:
        return 0, 0
    accuracy = (common/(len(user_input)))*100
    speed = common*2
    return accuracy, speed


def end_function():
    user_accuracy, user_speed = check_accuracy()
    messagebox.showinfo(title="Your result", message=f"Your accuracy is {user_accuracy}.\n"
                                                     f"Your speed is {user_speed} words per minute.")
    entry.config(state="disabled")


window = tkinter.Tk()

window.title("Typing Test")
window.geometry("600x450")

paragraph_text = random.choice(paragraphs)
paragraph = tkinter.Label(window, width=50, height=16, text=paragraph_text, wraplength=450)
paragraph.grid(row=1, column=0, columnspan=3, padx=40, pady=20)

entry = tkinter.Entry(window, width=40)
entry.config(state="disabled")
entry.grid(row=2, column=0, columnspan=3, padx=40)

start_button = tkinter.Button(window, text="Start", command=start_function)
start_button.grid(row=3, column=0, pady=40)

reset_button = tkinter.Button(window, text="Reset", command=reset_function)
reset_button.grid(row=3, column=2, pady=40)

window.mainloop()
