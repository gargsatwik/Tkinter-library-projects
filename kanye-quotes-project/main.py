import tkinter
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    canvas.itemconfig(quote, text=response.json()["quote"])


window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title("Kanye Says......")

canvas = tkinter.Canvas(height=414, width=300)
bg_image = tkinter.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=bg_image)
quote = canvas.create_text(150, 207, text="", width=250, font=("ariel", 24, "normal"))
button_image = tkinter.PhotoImage(file="kanye.png")
button = tkinter.Button(image=button_image, command=get_quote)
button.grid(row=1, column=0)
canvas.grid(row=0, column=0)

window.mainloop()
