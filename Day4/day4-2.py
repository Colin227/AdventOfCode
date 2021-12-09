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
        
    def printBoard(self):
        for r in self.boardArray:
            print(r)
    # the above works :)

    def checkNumber(self, num_to_check):
        for i in range(0, 5):
            for j in range(0, 5):
                #print(num_to_check)
                if (self.boardArray[i][j] == num_to_check):
                    self.boardArray[i][j] = "X"
                    print("x is placed")
                    return True
        return False

    def checkHorizontal(self):
        for row in range(0, 5):
            
            #for col in range(0, 5):
                #print(board.boardArray[row][col])
            if self.boardArray[row] == [ "X", "X", "X", "X", "X"]:
                print("----------------------------------------------------------- horizontal winner -----------------------------------------------------------")
                # print("string comparison was successful - true")
                print(f'this is the winning row {row}')
                self.winner = True

    def checkVertical(self):
        for col in range(0, 5):
            tmpVertArray = []
            for row in range(0, 5):
                tmpVertArray.append(self.boardArray[row][col])
            
            if tmpVertArray == [ "X", "X", "X", "X", "X"]:
                print("----------------------------------------------------------- vertical winner -----------------------------------------------------------")
                
                #print('vertical winner')
                self.winner = True
                print(f'this is the last tmpVertArray {tmpVertArray}')
                
            print(f'this is the tmpVertArray {tmpVertArray}')



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


  # check rows in given board for win  
# def checkHorizontal(board):
#     for row in range(0, 5):
#         #for col in range(0, 5):
#             #print(board.boardArray[row][col])
#         if board.boardArray[row] == [ "X", "X", "X", "X", "X"]:
#             # print("string comparison was successful - true")
#             return True
#     return False

    # Check columns in given board for win

        
    # Only used for first part
# def getUnmarked(board, currentNum):
#     unmarkedList = []
#     for row in range(0, 5):
#         for col in range(0, 5):
#             if (board.boardArray[row][col] != 'X'):
#                 unmarkedList.append(board.boardArray[row][col])
#     print(f'The score is: {sum(unmarkedList) * currentNum}')

# def lookForCurrentNumber(listOfBoards, num):
#     for i in range(0, len(listOfBoards)):
#         # if this board has a value of winner true, skip this board
#         if listOfBoards[i].winner == True:
#             continue

#         # look for the current number on the board
#         isLocated = listOfBoards[i].checkNumber(num)
#         print(f'Number located on current board: {isLocated}')
#         #print(isLocated)
#         # look for next drawn number in the current board
        
#     return listOfBoards

                
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
    # look at each number that will be drawn
    for num in drawnNumbers:
        print(f'current search num: {num}')
        for brdObj in tempWorkingList:
            isNumLocated = brdObj.checkNumber(num)
            if bool(isNumLocated) == True:
                print("hey the number was located")
                brdObj.checkHorizontal()
                brdObj.checkVertical()
                print(f'checking is winner of brdObj: {brdObj.winner}')
        for brdObj in tempWorkingList:
            if brdObj.winner == True:
            # if board is a winner, check if it is the last board
            # if true, print out the board
                if ((brdObj.boardNumber == tempWorkingList[0].boardNumber) and (brdObj.boardNumber == tempWorkingList[-1].boardNumber)):
                    print(f'the last board is {tempWorkingList[0].boardNumber}')
                    print(f'the supposed last drawn number is: {num}')
                    brdObj.printBoard()
                    return getUnmarked(brdObj.boardArray, num)
                    
                # if it is not the last board, remove it
                else:
                    tempWorkingList.remove(brdObj)
                    print(f'the brd removed was {brdObj.boardNumber}')


        
        




    # indexOfDrawnNumbers = 5
    # winningBoards = []
    # notWonBoards = []
    # bList = listOfBoards[:]
    # print("main function called")
    # # while the number of drawn numbers is less than the number of total numbers
    # #while indexOfDrawnNumbers <= len(drawnNumbers):
    # # loop through each of the drawn numbers
    # # for each number in drawnNumbers
    # for counter in range(0, len(drawnNumbers)):
    #     print('draw number index is less than total draw numbers')
    #     print(indexOfDrawnNumbers)
    #     # if len(bList) == 1:
    #     #     print('bList is 1')
    #     #     break
    #     currentNumbers = drawnNumbers[:indexOfDrawnNumbers]
    #     print(f'current numbers: {currentNumbers}')
    #     for num in currentNumbers:
    #         boardCounter = len(bList)
    #         print(f'len of boardCounter list: {boardCounter}')
    #         #print(f'BoardCounter: {boardCounter}')

            

    #         while True:
    #             #





    #             print("in the len of list loop")
    #             updatedBoardList = lookForCurrentNumber(bList, num)
    #             for b in updatedBoardList:
    #                 print(f'b.winner is: {b.winner}')
    #                 if b.winner == True:
    #                     updatedBoardList.pop(b.boardNumber)
    #                     print('b.winner is True')
    #             notWonBoards = updatedBoardList
    #             print(f'the not won boards is: {notWonBoards[0].boardArray}')
    #             # return notWonBoards[0].boardNumber
    #             # TODO: this is where the loop is exiting
    #             #return notWonBoards

    #             #print(f'inside boardcounter loop {winBoardNum[0].boardNumber}')
    #             # if (winBoardNum) == True:
    #             #     print("wincheck not false")
    #             #     bList.pop(winBoardNum)
    #             #     print(f'length of blist after pop: {len(bList)}')
    #             #     boardCounter = len(bList)
    #             #         #getUnmarked(listOfBoards[i], num)
    #             #         # return True

    #         else:
    #             # this isn't being triggered
    #             print("hello")
    #             return
    #     indexOfDrawnNumbers += 1
        
    #     print(len(bList))
    #     print(bList[0].boardNumber)
    # return winningBoards

isWinner = False
# while isWinner == False:
#     isWinner = main()
# get all the boards that are in the input file
main()
# winners = main()
# for winner in winners:
#     if winner.winner == True:
#         print(f'helllloooooo {winner.boardNumber}')
# # print(winners)


# for win_board_number in winners:
#     if win_board_number in (listOfBoards)


# getUnmarked(notWonBoards, )


'''
function to check all boards for number of winners that are false?
if num of boards that are false is one, return that


for each board:
    if (board.winner == False):





'''