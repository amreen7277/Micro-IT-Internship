import tkinter as tk
from tkinter import messagebox
import math

board = [" " for _ in range(9)]

def is_winner(board, player):
    wins = [[0,1,2], [3,4,5], [6,7,8], 
            [0,3,6], [1,4,7], [2,5,8], 
            [0,4,8], [2,4,6]]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_draw(board):
    return " " not in board

def minimax(board, is_max):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_draw(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                val = minimax(board, False)
                board[i] = " "
                best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                val = minimax(board, True)
                board[i] = " "
                best = min(best, val)
        return best

def ai_move():
    best = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best:
                best = score
                move = i
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")
    check_result()

def click(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")
        if not check_result():
            root.after(500, ai_move)

def check_result():
    if is_winner(board, "X"):
        messagebox.showinfo("Result", "You win!")
        root.quit()
        return True
    elif is_winner(board, "O"):
        messagebox.showinfo("Result", "AI wins!")
        root.quit()
        return True
    elif is_draw(board):
        messagebox.showinfo("Result", "It's a draw!")
        root.quit()
        return True
    return False

root = tk.Tk()
root.title("Tic-Tac-Toe AI")

buttons = []
for i in range(9):
    btn = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()