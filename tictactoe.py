# Tic-Tac-Toe Program using random number
  
# importing all libraries 
import numpy as np 
import random 
from time import sleep 
  
# Creates an empty board 
def create_board(): 
    return(np.array([[0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0]])) 
  
# Check for empty places on board 
def possibilities(board): 
    l = [] 
      
    for i in range(len(board)): 
        for j in range(len(board)): 
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l) 
  
# Select a random place for the player 
def random_place(board, player): 
    selection = possibilities(board) 
    current_loc = random.choice(selection) 
    board[current_loc] = player 
    return(board) 
  
# Checks whether the player has completed their marks in a horizontal row 
def rowwin(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[x, y] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
# Checks whether the player has completed their marks in a vertical row 
def colwin(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[y][x] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
# Checks whether the player has completed their marks in a diagonal row 
def diagwin(board, player): 
    win = True
      
    for x in range(len(board)): 
        if board[x, x] != player: 
            win = False
    return(win) 
  
# Check whether there is a winner or a tie  
def check(board): 
    winner = 0
      
    for player in [1, 9]: 
        if (rowwin(board, player) or
            colwin(board,player) or 
            diagwin(board,player)): 
                 
            winner = player 
              
    if np.all(board != 0) and winner == 0: 
        winner = -1
    return winner 
  
# Main function to start the game 
def play(): 
    board, winner, count = create_board(), 0, 1
    print(board) 
    sleep(2) 
      
    while winner == 0: 
        for player in [1, 9]: 
            board = random_place(board, player) 
            print("Board after " + str(count) + " move") 
            print(board) 
            sleep(2) 
            count+=1
            winner = check(board) 
            if winner != 0: 
                break
    return(winner) 
  
# Driver Code 
print("Winner is: " + str(play())) 
