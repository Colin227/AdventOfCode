'''
This is a programming challenge from the AdventOfCode project.
It takes an input file and formats and reads it to generate a 
bingo game based on the given rules and boards. 

This is the second part of the challenge, where you are to find
the bingo card that will win last, based on given numbers.
'''

inp = open('E:/Programming/AdventOfCode/Day4/input.txt').read()
# Separate first line of input, these are the numbers drawn for the game
numbers = inp.splitlines()[0]
# Separate boards based on double line break
boards = inp.split('\n\n')[1:]
    
class board:
    def __init__(self, boardIndex):
        self.boardNumber = boardIndex
        self.boardArray = createBoard(boardIndex)
        self.winner = False

    # Print board - Used for testing and debugging process   
    def printBoard(self):
        for r in self.boardArray:
            print(r)

    # Look through each value in the board, and if it matches, replace it with "X"
    # Return true if value is found, else false
    def checkNumber(self, num_to_check):
        for i in range(0, 5):
            for j in range(0, 5):
                if (self.boardArray[i][j] == num_to_check):
                    self.boardArray[i][j] = "X"
                    return True
        return False

    # look through each row for a winner
    def checkHorizontal(self):
        for row in range(0, 5):
            if self.boardArray[row] == [ "X", "X", "X", "X", "X"]:
                self.winner = True

    # look at each column for winner
    def checkVertical(self):
        for col in range(0, 5):
            tmpVertArray = []
            for row in range(0, 5):
                tmpVertArray.append(self.boardArray[row][col])
            
            if tmpVertArray == [ "X", "X", "X", "X", "X"]:
                self.winner = True


# Function to create the list for each board object
# Format input to from string to int, remove whitespace
# and double spacing

def createBoard(boardIndex):
    workingList = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],]
    board_nums = " ".join(boards[boardIndex].split())
    row_values = [int(i) for i in board_nums.split()]
    current_board_num_index = 0

    for row in range(0, 5):
        for col in range(0, 5):
            workingList[row][col] = row_values[current_board_num_index]
            current_board_num_index += 1
    return workingList

# Instantiate all boards into list
def getAllBoards():
    listOfBoards = []
    for i in range(0, len(boards)):
        listOfBoards.append(board(i))
    return listOfBoards
    
# look for values in board that have not been drawn yet
# These are used for the challenge output
def getUnmarked(boardArray, currentNum):
    unmarkedList = []
    for row in range(0, 5):
        for col in range(0, 5):
            if (boardArray[row][col] != 'X'):
                unmarkedList.append(boardArray[row][col])
    print(f'unmarked list: {unmarkedList} and current num: {currentNum}')
    print(f'The score is: {sum(unmarkedList) * currentNum}')




def main():
    listOfBoards = getAllBoards()  
    drawnNumbers = [int(i) for i in numbers.split(",")]
    tempWorkingList = listOfBoards[:]
    for num in drawnNumbers:
        for brdObj in tempWorkingList:
            isNumLocated = brdObj.checkNumber(num)
            if bool(isNumLocated) == True:
                # TODO: likely can remove this if statement - check later
                brdObj.checkHorizontal()
                brdObj.checkVertical()

        # Separated these due to numbers not being checked when
        # a board wins from the current number value
        for brdObj in tempWorkingList:
            if brdObj.winner == True:
            # TODO: This can likely be cleaned up
                if ((brdObj.boardNumber == tempWorkingList[0].boardNumber) and (brdObj.boardNumber == tempWorkingList[-1].boardNumber)):
                    return getUnmarked(brdObj.boardArray, num)
                
                # if it is not the last board, remove it
                else:
                    tempWorkingList.remove(brdObj)

main()

