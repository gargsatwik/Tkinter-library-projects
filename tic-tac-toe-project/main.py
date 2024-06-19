import tkinter
from tkinter import messagebox
from itertools import combinations


i = 0
X_list = []
O_list = []


def get_combinations_of_size(input_list, size):
    if size < 1 or size > len(input_list):
        return []
    return [list(combination) for combination in combinations(input_list, size)]


def check_winner(squares):
    # if len(squares) < 3:
    #     return 0
    # else:
    #     squares.sort()
    #     differences = []                         # This logic fails if the players dont place X's or O's consecutively
    #     for a in range(len(squares)-1):
    #         difference = squares[a+1] - squares[a]
    #         differences.append(difference)
    #     if all(element == differences[0] for element in differences):
    #         return 1
    if len(squares) < 3:
        return False
    else:
        winning_lists = [[1, 2, 3], [3, 6, 9], [7, 8, 9], [1, 4, 7], [1, 5, 9], [3, 5, 7], [2, 5, 8], [4, 5, 6]]
        squares.sort()
        smaller_lists = get_combinations_of_size(squares, 3)
        print(smaller_lists)
        for list_ in smaller_lists:
            list_.sort()
            print(list_)
            if list_ in winning_lists:
                return True
    return False


def get_coordinates(event):
    global i
    if i <= 8:
        x = event.x_root
        y = event.y_root
        if x < 140 and 65 < y < 190:
            x_center = 70
            y_center = 65
            square = 1
        elif 140 < x < 270 and 60 < y < 190:
            x_center = 205
            y_center = 65
            square = 2
        elif 270 < x < 400 and 60 < y < 190:
            x_center = 335
            y_center = 65
            square = 3
        elif x < 140 and 195 < y < 325:
            x_center = 70
            y_center = 200
            square = 4
        elif 140 < x < 270 and 195 < y < 325:
            x_center = 205
            y_center = 200
            square = 5
        elif 270 < x < 400 and 195 < y < 325:
            x_center = 335
            y_center = 200
            square = 6
        elif x < 140 and 325 < y < 460:
            x_center = 70
            y_center = 332
            square = 7
        elif 140 < x < 270 and 325 < y < 460:
            x_center = 205
            y_center = 332
            square = 8
        elif 270 < x < 400 and 325 < y < 460:
            x_center = 335
            y_center = 332
            square = 9
        if i % 2 == 0:
            canvas.create_image(x_center, y_center, image=x_image)
            X_list.append(square)
            print(X_list)
            i += 1
            if check_winner(X_list):
                messagebox.showinfo("Message", "X wins")
                window.destroy()
        else:
            canvas.create_image(x_center, y_center, image=o_image)
            O_list.append(square)
            print(O_list)
            i += 1
            if check_winner(O_list):
                messagebox.showinfo("Message", "O wins")
                window.destroy()
    else:
        messagebox.showinfo("Message", "Match Draw")
        window.destroy()


window = tkinter.Tk()
window.title('Tic Tac Toe')
bg_image = tkinter.PhotoImage(file="tic-tac-toe-grid.png")
x_image = tkinter.PhotoImage(file="x-tic-tac-toe (1).png")
o_image = tkinter.PhotoImage(file="O-tic-tac-toe (1).png")

canvas = tkinter.Canvas(window, width=bg_image.width(), height=bg_image.height())
canvas.pack()
canvas.create_image(0, 0, anchor=tkinter.NW, image=bg_image)


window.bind("<Button-1>", get_coordinates)

window.mainloop()
