import random
gameBoard = [[1,2,3],[4,5,6],[7,8,9]]
possible_numbers = [1,2,3,4,5,6,7,8,9]
end_game = False
rows = 3
cols = 3
turn_counter = 0


print('Welcome to Tic-Tac-Toe')
print('-----------------------')

def game_board():
    for x in range(rows):
        print('\n*---*---*---*')
        print('|', end='')
        for y in range(cols):
            print("", gameBoard[x][y],'|',end="")
    print('\n*---*---*---*')

def update_board(number, player):
    number -= 1
    if number == 0:
        gameBoard[0][0] = player
    elif number == 1:
        gameBoard[0][1] = player
    elif number == 2:
        gameBoard[0][2] = player
    elif number == 3:
        gameBoard[1][0] = player
    elif number == 4:
        gameBoard[1][1] = player
    elif number == 5:
        gameBoard[1][2] = player
    elif number == 6:
        gameBoard[2][0] = player
    elif number == 7:
        gameBoard[2][1] = player
    elif number == 8:
        gameBoard[2][2] = player

def check_winner(board):
    #Horizontal
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        print('Computer is the winner!!')
        return 'O'
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        print('Computer is the winner!!')
        return 'O'
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        print('Computer is the winner!!')
        return 'O'

    #Vertical

    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        print('Computer is the winner!!')
        return 'O'
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        print('Computer is the winner!!')
        return 'O'
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        print('Computer is the winner!!')
        return 'O'

    #Diagional
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('Player is the winner!!')
        return 'X'
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print('Computer is the winner!!')
        return 'O'
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        print('Computer is the winner!!')
        return 'O'
    else:
        return 'N'

while not end_game:
    if turn_counter % 2 == 0:
        game_board()
        player_choice = int(input("Please select a number between 1 and 9: "))
        if player_choice in range(1,10) and player_choice in possible_numbers:
            update_board(player_choice, 'X')
            possible_numbers.remove(player_choice)
        else:
            player_choice = int(input("Sorry, your choice was invalid, please choose another number: "))
            update_board(player_choice, 'X')
            possible_numbers.remove(player_choice)
    else:
        cpu_choice =random.choice(possible_numbers)
        update_board(cpu_choice, 'O')
        possible_numbers.remove(cpu_choice)
    turn_counter +=1


    winner = check_winner(gameBoard)
    if winner != 'N':
        game_board()
        end_game = True
        print('Game Over. Thank you for playing!')

    if len(possible_numbers) == 0:
        print('The game has ended in a tie')
        end_game = True
