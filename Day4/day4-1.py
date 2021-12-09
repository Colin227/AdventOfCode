inp = open('E:/Programming/AdventOfCode/Day4/input.txt').read()
numbers = inp.splitlines()[0]
boards = inp.split('\n\n')[1:]
    
'''
This is a programming challenge from the AdventOfCode project.
It takes an input file and formats and reads it to generate a 
bingo game based on the given rules and boards.
'''
class board:
    def __init__(self, boardIndex):
        self.boardNumber = boardIndex
        self.boardArray = createBoard(boardIndex)
        self.winner = False

        
    def createBoard(boardIndex):
        workingList = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],]
        # Remove all double spaces from the input file
        board_nums = " ".join(boards[boardIndex].split())
        # Parse each value to int and add to row
        row_values = [int(i) for i in board_nums.split()]

        current_board_num_index = 0
        for row in range(0, 5):
            for col in range(0, 5):
                workingList[row][col] = row_values[current_board_num_index]
                current_board_num_index += 1
        return workingList
    
    def printBoard(self):
        for r in self.boardArray:
            print(r)
    # the above works :)

    def checkNumber(self, num_to_check):
        for i in range(0, 5):
            for j in range(0, 5):
                if (self.boardArray[i][j] == num_to_check):
                    self.boardArray[i][j] = "X"
                    return True
        return False


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

def getAllBoards():
    listOfBoards = []
    for i in range(0, len(boards)):
        listOfBoards.append(board(i))
    return listOfBoards


    
def checkHorizontal(boardArray):
    for row in range(0, 5):
        for col in range(0, 5):
            #print(board.boardArray[row][col])

            if boardArray[row] == [ "X", "X", "X", "X", "X"]:
                # print("string comparison was successful - true")
                return True
    return False


def checkVertical(boardArray):
    for col in range(0, 5):
        tmpVertArray = []
        for row in range(0, 5):
            tmpVertArray.append(boardArray[row][col])
        if tmpVertArray == [ "X", "X", "X", "X", "X"]:
            print('vertical winner')
            return True
    return False
        

def getUnmarked(boardArray, currentNum):
    unmarkedList = []
    for row in range(0, 5):
        for col in range(0, 5):
            if (boardArray[row][col] != 'X'):
                unmarkedList.append(boardArray[row][col])
    print(f'The score is: {sum(unmarkedList) * currentNum}')

def main():
    drawnNumbers = [int(i) for i in numbers.split(",")]
    indexOfDrawnNumbers = 5
    listOfBoards = getAllBoards()    
    while indexOfDrawnNumbers <= len(drawnNumbers):
        currentNumbers = drawnNumbers[:indexOfDrawnNumbers]
        for num in currentNumbers:
            for i in range(0, len(listOfBoards)):
                isLocated = listOfBoards[i].checkNumber(num)
                if (isLocated == True):
                    if (checkVertical(listOfBoards[i].boardArray) == True) or (checkHorizontal(listOfBoards[i].boardArray) == True):
                        getUnmarked(listOfBoards[i].boardArray, num)
                        return True
                else:
                    continue
        indexOfDrawnNumbers += 1


isWinner = False
while isWinner == False:
    isWinner = main()



# def printAllBoards():
#     for item in listOfBoards:
#         print(f'Board number: {item.boardNumber}')
#         item.printBoard()
#         print("\n")





