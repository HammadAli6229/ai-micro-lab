#!/usr/bin/env python
# coding: utf-8

# # TIC-TAC-TOE Game against AI
# 
# Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms.

# In[1]:


import numpy as np

# Constants
EMPTY = 0
AI_PLAYER = 1
HUMAN_PLAYER = -1

def print_board(board):
    """
    Print the Tic-Tac-Toe board.
    """
    symbols = {EMPTY: ' ', AI_PLAYER: 'X', HUMAN_PLAYER: 'O'}
    for row in board:
        print('|'.join([symbols[s] for s in row]))
        print('-'*5)

def check_winner(board):
    """
    Check if there is a winner or if the game is a draw.
    """
    # Check rows
    for row in board:
        if all([s == row[0] and s != EMPTY for s in row]):
            return True, row[0]

    # Check columns
    for col in range(3):
        if all([board[row][col] == board[0][col] and board[row][col] != EMPTY for row in range(3)]):
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True, board[0][2]

    # Check for draw
    if all([s != EMPTY for row in board for s in row]):
        return True, 0

    return False, None

def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm with Alpha-Beta Pruning.
    """
    winner_exists, winner = check_winner(board)
    
    if winner_exists:
        if winner == AI_PLAYER:
            return 10 - depth, None
        elif winner == HUMAN_PLAYER:
            return -10 + depth, None
        else:
            return 0, None
    
    if is_maximizing:
        best_score = -np.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI_PLAYER
                    score, _ = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move
    else:
        best_score = np.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN_PLAYER
                    score, _ = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move

def ai_turn(board):
    """
    AI's turn to make a move.
    """
    _, move = minimax(board, 0, True)
    board[move[0]][move[1]] = AI_PLAYER

def main():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[EMPTY]*3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's turn
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN_PLAYER
                    break
                else:
                    print("That cell is already occupied. Try again.")
            except ValueError:
                print("Invalid input. Please enter row and column as integers separated by space.")

        print_board(board)
        winner_exists, winner = check_winner(board)
        if winner_exists:
            if winner == AI_PLAYER:
                print("AI wins!")
            elif winner == HUMAN_PLAYER:
                print("You win!")
            else:
                print("It's a draw!")
            break

        # AI's turn
        ai_turn(board)
        print("AI's move:")
        print_board(board)
        winner_exists, winner = check_winner(board)
        if winner_exists:
            if winner == AI_PLAYER:
                print("AI wins!")
            elif winner == HUMAN_PLAYER:
                print("You win!")
            else:
                print("It's a draw!")
            break

if __name__ == "__main__":
    main()


# In[ ]:




