# Tic Tac Toe game with GUI
# using tkinter
  
# importing all necessary libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
  
# sign variable to decide the turn of which player
sign = 0
  
# Creates an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]
  
# Check l(O/X) won the match or not
# according to the rules of the game
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
  
# Configure text on button while playing with another player
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")
  
# Check if the player can push the button or not
def isfree(i, j):
    return board[i][j] == " "
  
# Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
  

  
# main function
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)
      
    head = Button(menu, text = "---Welcome to tic-tac-toe---",
                  activeforeground = 'red',
                  activebackground = "yellow", bg = "red", 
                  fg = "yellow", width = 500, font = 'summer', bd = 5)
      
    B1 = Button(menu, text = "Single Player", command = wpc, 
                activeforeground = 'red',
                activebackground = "yellow", bg = "red", 
                fg = "yellow", width = 500, font = 'summer', bd = 5)
      
    B2 = Button(menu, text = "Multi Player", command = wpl, activeforeground = 'red',
                activebackground = "yellow", bg = "red", fg = "yellow",
                width = 500, font = 'summer', bd = 5)
      
    B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
                activebackground = "yellow", bg = "red", fg = "yellow",
                width = 500, font = 'summer', bd = 5)
    head.pack(side = 'top')
    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    menu.mainloop()
  
# Call main function
if __name__ == '__main__':
    play()
