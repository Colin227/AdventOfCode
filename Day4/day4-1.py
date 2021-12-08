inputFile = open('testinput.txt', 'r')
drawNumbers = inputFile.readline()
lines = []
inp = open('E:/Programming/AdventOfCode/Day4/testinput.txt').read()
numbers = inp.splitlines()[0]
boards = inp.split('\n\n')[1:]
    

class board:
    def __init__(self, boardIndex, nums_in_board):
        self.boardNumber = boardIndex
        self.boardArray = [ [], [], [], [], [] ]
        self.setBoard(nums_in_board)
    # Parameter nums_in_row is the list of board numbers
    def setBoard(self, nums_in_board):
        boardNumber = self.boardNumber
        # for i in range(0, 5):
        #     self.boardArray[i] = [int(s) for s in nums_in_board.split(',')]

def printBoards():
    for brd in boards:
        print(brd)
        print("\n")
    






# get the total number of boards 
# print(len(boards))

def createBoard():
    workingList = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],]
    board_nums = " ".join(boards[0].split())

    row_values = [int(i) for i in board_nums.split()]

    current_board_num_index = 0
    for row in range(0, 5):
        for col in range(0, 5):
            workingList[row][col] = row_values[current_board_num_index]
            current_board_num_index += 1
    print(workingList)

    
createBoard()