theBoard = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '}

boardKeys = []

for key in theBoard:
    boardKeys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    
def playerTurn():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("The first turn is for " + turn + " Please specify the cell where you want to place X")
        
        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("The cell is filled. Please choose different cell.")
            continue
            
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
            if theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
            if theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
            if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
            if theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print('\n Game Over \n')
                print("Player " + turn + "Won")
                break
                
        if count == 9:
            print('\n Game Over \n')
            print("Game Tied")
            
        if turn == 'X':
            turn = '0'
        else: 
            turn = 'X'

    restart = input("Do you want to restart the game? (y/n)")
    
    if restart == 'y' or restart == 'Y':
        for key in boardKeys:
            theboard[key] = ' '
        playerTurn()

if __name__ == "__main__":
    playerTurn()



