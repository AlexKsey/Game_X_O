import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    if all(cell != "" for row in board for cell in row):
        return "Draw"
    return None

def click_button(x, y):
    if board[x][y] == "" and not winner:
        board[x][y] = current_player[0]
        buttons[x][y].config(text=current_player[0])
        result = check_winner()
        if result:
            show_winner(result)
        else:
            current_player[0] = "O" if current_player[0] == "X" else "X"

def show_winner(result):
    global winner
    winner = True
    if result == "Draw":
        messagebox.showinfo("Игра окончена", "Ничья!")
    else:
        messagebox.showinfo("Игра окончена", f"Победитель: {result}")

# Создание окна
root = tk.Tk()
root.title("Крестики-нолики")

# Игровое поле
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = ["X"]
winner = False

# Создание кнопок
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda x=i, y=j: click_button(x, y))
        buttons[i][j].grid(row=i, column=j)

# Start
root.mainloop()
