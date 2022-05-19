#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
import random


# function to print the board!
def display_board(board):
    clear_output()
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('--- --- ---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('--- --- ---')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    pass


# function to take in a player input and assign their marker as 'X' or 'O'!
def player_input():
    marker = 'none'
    while not (marker == 'X' or marker == 'O'):
        marker = input('Enter player 1 marker : ').upper()
        
        if not (marker == 'X' or marker == 'O'):
            print('Wrong input!')
        elif marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
        pass

    
# function to assign marker to a board position!
def place_marker(board, marker, position):
    board[position] = marker
    pass



# function to check win!
def win_check(board, mark):
    return(
        board[1] == board[2] == board[3] == mark or
        board[4] == board[5] == board[6] == mark or
        board[7] == board[8] == board[9] == mark or
        
        board[7] == board[4] == board[1] == mark or
        board[8] == board[5] == board[2] == mark or
        board[9] == board[6] == board[3] == mark or
        
        board[3] == board[5] == board[7] == mark or
        board[1] == board[5] == board[9] == mark )
    
    pass



# function to randomly select a player to play first!
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    pass


# function to check for free space in the board!
def space_check(board, position):
    return board[position] == ' '


# function to check if the board is full or not!
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# function to ask for the players next position!
def player_choice(board):
    pos = int(input("Enter 1st/next position(1-9): "))
    if pos in range(1,10) and space_check(board,pos):
        return pos
    pass


# function to ask players if they wanna play again!
def replay():
    choice = input("Wanna replay?(Y/N)").upper()
    if choice == 'Y':
        return True
    else:
        return False
    pass



# main program!
print('Welcome to Tic Tac Toe!')

while True:
    board = [' ']*10
    player_marker_1, player_marker_2 = player_input()
    player = choose_first()
    print('player ' + player +  ' will go first!')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    
    while game_on:
        
        if player == 'Player 1':
            display_board(board)
            pos = player_choice(board)
            place_marker(board,player_marker_1,pos)
        
            if win_check(board,player_marker_1):
                display_board(board)
                print('Player 1 has won the game!')
                game_on = False
            
            else:
                if full_board_check(board):
                    print('The game is a tie!')
                    break
            
                else:
                    player = 'Player 2'
            
        else:
            display_board(board)
            pos = player_choice(board)
            place_marker(board,player_marker_2,pos)
        
            if win_check(board,player_marker_2):
                display_board(board)
                print('Player 2 has won the game!')
                game_on = False
                
            else:
                if full_board_check(board):
                    print('The game is a tie!')
                    break
            
                else:
                    player = 'Player 1'
            
    
    if not replay():
        break
    


# In[ ]:




