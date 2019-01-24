Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 

import random
import pdb
##Notes to go through the game 
##We need it seeded
##we need a list or dictionary to keep track of the spaces, x's, or o's,
##Its length will be nine
##
##We need to display the board using hardcoded separators and variables based on the dictionary or list
##
##We need to let the computer move
##
##the other computers player will move
##
##Loop until win or tie
##
##We need two random ints in the range 0 to 3, exclusive
##
##Is available function
##
##Has won
##Has tied

board=list()
random.seed(1)

for index in range(0, 9):
    board.append(" ")

def displayBoard():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-+-+-")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-+-+-")
    print(board[6]+"|"+board[7]+"|"+board[8])

def updateBoard(index, player):
    board[index]=player
    displayBoard()

def isAvailable(index):
    if (board[index]==" "):
        return True
    else:
        return False

def computerMakesMove(player):
    valid=False

    index=0
    while(not valid):
        index=random.randint(0,8)
        valid=isAvailable(index)
    updateBoard(index, player)

def isTie():
    for index in range(0, 9):
        if(isAvailable(index)):
            return False
    return True


def hasWon(player):

    if (board[0]==player and board[1]==player and board[2]==player):
        return True
    elif (board[3]==player and board[4]==player and board[5]==player):
        return True
    elif (board[6]==player and board[7]==player and board[8]==player):
        return True

    if (board[0]==player and board[3]==player and board[6]==player):
        return True
    elif (board[1]==player and board[4]==player and board[7]==player):
        return True
    elif (board[2]==player and board[5]==player and board[8]==player):
        return True

    if (board[0]==player and board[4]==player and board[8]==player):
        return True
    elif (board[2]==player and board[4]==player and board[6]==player):
        return True
    

def testWinCondition(first, second, third, player):
    board[first]=player
    board[second]=player
    board[third]=player
    displayBoard()

def gameHasEnded():
    return hasWon("X") or hasWon("O") or isTie()

def printEnding():
    if hasWon("X"):
        print("Player X has won!")
    elif hasWon("O"):
        print("Player O has won!")
    elif isTie():
        print("It's a tie")

def computerPlay():
    gameOver=False
    while(not gameOver):
        computerMakesMove("X")
        if (gameHasEnded()):
            break
        computerMakesMove("O")
        if (gameHasEnded()):
            break
        

displayBoard()
computerPlay()
printEnding()


