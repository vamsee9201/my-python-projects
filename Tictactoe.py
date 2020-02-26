def DisplayBoard(l):
    print('     |       |       ')
    print(' {}   |   {}   |  {}   '.format(l[0],l[1],l[2]))
    print('---------------------')
    print('     |       |       ')
    print(' {}   |   {}   |  {}   '.format(l[3],l[4],l[5]))
    print('---------------------')
    print('     |       |       ')
    print(' {}   |   {}   |  {}   '.format(l[6],l[7],l[8]))

def PlayerInput(player1):
        player1 = input("Please pick a marker 'X' or 'O'")
        while player1 not in 'XO':
            print('Invalid input')
            player1 = input("Please pick a marker 'X' or 'O'")
        return player1

def Place_Marker(pl,c,pos):
         pl[pos] = c


def win_check(pl,c):
     if(pl[0] == c and pl[1] == c and pl[2] == c):
         return True
     elif (pl[3] == c and pl[4] == c and pl[5] == c):
         return True
     elif (pl[6] == c and pl[7] == c and pl[8] == c):
         return True
     elif (pl[0] == c and pl[4] == c and pl[8] == c):
         return True
     elif (pl[2] == c and pl[4] == c and pl[6] == c):
         return True
     elif (pl[0] == c and pl[3] == c and pl[6] == c):
         return True
     elif (pl[1] == c and pl[4] == c and pl[7] == c):
         return True
     elif (pl[2] == c and pl[5] == c and pl[8] == c):
         return True
     else:
         return False



def space_check(board, position):
     if board[position] == '#':
         game_on = False
         return True
     else:
         return False

def full_board_check(board):
     if '#' in board:
         return False
     else:
         return True

def player_choice(board):
     pos = int(input('enter the next position'))
     while pos == '#':
         pos = int(input('enter valid next position'))
     return pos

def replay():
    inp = input('do you want to play or not yes/no')
    return inp



print("welcome to tictactoe")


while True:
    l = ['#', '#', '#', '#', '#', '#', '#', '#', '#']
    player1 = PlayerInput('')
    player2 = ''
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    game_on = True
    winner = 'notyet'
    while game_on :
        print('this is player1 turn')
        pos = player_choice(l)
        while  not space_check(l,pos):
           print('already filled')
           pos = player_choice(l)
        Place_Marker(l, 'X', pos)
        DisplayBoard(l)

        if win_check(l,'X'):
                print('player1 has won')
                gameOver = True
                break
        if full_board_check(l) and winner == 'notyet':
            print('match Drawn')


        print('this is player2 turn')
        pos = player_choice(l)
        while not space_check(l, pos):
            print('already filled')
            pos = player_choice(l)
        Place_Marker(l, 'O', pos)
        DisplayBoard(l)

        if win_check(l, 'O'):
                print('player2 has won')
                gameOver = True
                break
        if full_board_check(l) and winner == 'notyet':
            print('match Drawn')



    playAgain = replay()
    if playAgain == 'yes':
        continue
    else :
        break



         
