import random

choice = input('Press "1" for multiplayer or press "2" for single player: ')
    
board = [1,2,3,4,5,6,7,8,9]

def displayboard():
    print('',board[0], '|', board[1], '|', board[2])
    print(' ---------')
    print('',board[3], '|', board[4], '|', board[5])
    print(' ---------')
    print('',board[6], '|', board[7], '|', board[8])

counter = 0

if choice == '1':
    while True :
        #PLAYER 1
        displayboard()
        num1 = int(input('Player 1:'))

        while board [num1-1] == 'X' or board [num1-1] == 'O':
            print('Illegal move! Please try again.')
            num1 = int(input('Player 1:'))

        board[num1-1]= 'O'
            
        displayboard()

        if board[1]== 'O' and board[4]==board[7]==board[1]:
            print('Player 1 wins!')
            break
        if board[0]== 'O' and board[3]== 'O' and  board[6] == 'O':
            print('Player 1 wins!')
            break
        if board[2]== 'O' and board[5]== 'O' and  board[8] == 'O':
            print('Player 1 wins!')
            break
        if board[0]== 'O' and board[1]== 'O' and  board[2] == 'O':
            print('Player 1 wins!')
            break
        if board[3]== 'O' and board[4]== 'O' and  board[5] == 'O':
            print('Player 1 wins!')
            break
        if board[6]== 'O' and board[7]== 'O' and  board[8] == 'O':
            print('Player 1 wins!')
            break
        if board[0]== 'O' and board[4]== 'O' and  board[8] == 'O':
            print('Player 1 wins!')
            break
        if board[6]== 'O' and board[4]== 'O' and  board[2] == 'O':
            print('Player 1 wins!')
            break

        counter +=1
        if counter == 9:
            print('Draw!')
            break

        #PLAYER 2
        num2 = int(input('Player 2:'))

        while board [num2-1] == 'O' or board [num2-1] == 'X':
                print('Illegal move! Please try again.')
                num2 = int(input('Player 2:'))

        board[num2-1]= 'X'

        if board[1]== 'X' and board[4]== 'X' and  board[7] == 'X':
            print('Player 2 wins!')
            break
        if board[0]== 'X' and board[3]== 'X' and  board[6] == 'X':
            print('Player 2 wins!')
            break
        if board[2]== 'X' and board[5]== 'X' and  board[8] == 'X':
            print('Player 2 wins!')
            break
        if board[0]== 'X' and board[1]== 'X' and  board[2] == 'X':
            print('Player 2 wins!')
            break
        if board[3]== 'X' and board[4]== 'X' and  board[5] == 'X':
            print('Player 2 wins!')
            break
        if board[6]== 'X' and board[7]== 'X' and  board[8] == 'X':
            print('Player 2 wins!')
            break
        if board[0]== 'X' and board[4]== 'X' and  board[8] == 'X':
            print('Player 2 wins!')
            break
        if board[6]== 'X' and board[4]== 'X' and  board[2] == 'X':
            print('Player 2 wins!')
            break
        counter +=1
        
if choice == '2':
    while True:
        #PLAYER 1
        displayboard()
        num1 = int(input('Choose a tile:'))

        while board [num1-1] == 'X' or board [num1-1] == 'O':
            print('Illegal move! Please try again.')
            num1 = int(input('Choose a tile:'))

        board[num1-1]= 'O'
        counter +=1
        
        if board[1]== 'O' and board[4]==board[7]==board[1]:
            displayboard()
            print('YOU WIN!')
            break
        if board[0]== 'O' and board[3]== 'O' and  board[6] == 'O':
            displayboard()
            print('YOU WIN!')
            break
        if board[2]== 'O' and board[5]== 'O' and  board[8] == 'O':
            displayboard()
            print('YOU WIN!')
            break
        if board[0]== 'O' and board[1]== 'O' and  board[2] == 'O':
            displayboard()
            print('YOU WIN!')
            break
        if board[3]== 'O' and board[4]== 'O' and  board[5] == 'O':
            displayboard()
            print('YOU WIN!')
            break
        if board[6]== 'O' and board[7]== 'O' and  board[8] == 'O':
            displayboard()
            print('YOU WIN!')
            break
        if board[0]== 'O' and board[4]== 'O' and  board[8] == 'O':
            displayboard()
            print('YOU WIN!')
            break
        if board[6]== 'O' and board[4]== 'O' and  board[2] == 'O':
            displayboard()
            print('YOU WIN!')
            break
        if counter == 9:
            print('Draw!')
            break

        #BOT
        num2 = random.randint(0,9)

        while board [num2-1] == 'O' or board [num2-1] == 'X':
                num2 = random.randint(0,9)

        board[num2-1]= 'X'
        counter+=1

        if board[1]== 'X' and board[4]== 'X' and  board[7] == 'X':
            print('YOU LOSE!')
            break
        if board[0]== 'X' and board[3]== 'X' and  board[6] == 'X':
            print('YOU LOSE!')
            break
        if board[2]== 'X' and board[5]== 'X' and  board[8] == 'X':
            print('YOU LOSE!')
            break
        if board[0]== 'X' and board[1]== 'X' and  board[2] == 'X':
            print('YOU LOSE!')
            break
        if board[3]== 'X' and board[4]== 'X' and  board[5] == 'X':
            print('YOU LOSE!')
            break
        if board[6]== 'X' and board[7]== 'X' and  board[8] == 'X':
            print('YOU LOSE!')
            break
        if board[0]== 'X' and board[4]== 'X' and  board[8] == 'X':
            print('YOU LOSE!')
            break
        if board[6]== 'X' and board[4]== 'X' and  board[2] == 'X':
            print('YOU LOSE!')
            break
        


