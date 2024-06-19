import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            content = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Error", message="This data does not exist")
    else:
        messagebox.showinfo(title=f"{website}", message=f"Email: {content[website]["email"]}\nPassword: "
                                                        f"{content[website]["password"]}")


def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


def add_entry():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        new_entry = {website_entry.get(): {"email": email_entry.get(), "password": password_entry.get()}}
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}

        data.update(new_entry)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, "end")
        password_entry.delete(0, "end")


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = tkinter.Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "satwikgarg2005@gmail.com")

password_entry = tkinter.Entry(width=20)
password_entry.grid(row=3, column=1)

generate_password_button = tkinter.Button(text="Generate Password", command=random_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=34, command=add_entry)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", command=search, width=13)
search_button.grid(row=1, column=2)

window.mainloop()
