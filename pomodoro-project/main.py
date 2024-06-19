import tkinter


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


def reset_timer():
    global reps
    reps = 1
    window.after_cancel(timer)
    title_label.config(text="TIMER")
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


def timer_mechanism():
    global reps
    work_in_secs = WORK_MIN*60
    short_break_in_secs = SHORT_BREAK_MIN*60
    long_break_in_secs = LONG_BREAK_MIN*60
    if reps % 2 != 0:
        count_down(work_in_secs)
        title_label.config(text="WORK", fg=GREEN, font=(FONT_NAME, 24), bg=YELLOW)
    elif reps == 8:
        count_down(long_break_in_secs)
        title_label.config(text="BREAK", fg=RED, font=(FONT_NAME, 24), bg=YELLOW)
        reps = 1
    else:
        count_down(short_break_in_secs)
        title_label.config(text="BREAK", fg=PINK, font=(FONT_NAME, 24), bg=YELLOW)
    reps += 1


def count_down(count):
    global timer
    mins = int(count/60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        timer_mechanism()
        mark = ""
        for _ in range(int(reps/2)):
            mark += "✔"
        tick_label.config(text=mark)


window = tkinter.Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text=f"00:00", font=(FONT_NAME, 18))
canvas.grid(row=1, column=1)

title_label = tkinter.Label(fg=GREEN, text="TIMER", font=(FONT_NAME, 24), bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", command=timer_mechanism)
start_button.grid(row=2, column=0)

tick_label = tkinter.Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=2, column=1)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
