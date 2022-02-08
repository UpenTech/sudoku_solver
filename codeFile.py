from ctypes.wintypes import BOOL
from pickle import TUPLE

board = [
    [7,8,5,4,3,9,1,2,6],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


board2 = [
    [0,0,0,0,2,7,0,0,0],
    [0,4,2,0,1,5,0,0,0],
    [0,0,0,6,0,0,5,0,0],
    [6,0,0,0,0,0,0,9,4],
    [2,0,0,7,0,0,0,8,0],
    [0,3,0,0,0,0,0,0,0],
    [0,0,0,8,0,0,0,0,0],
    [0,7,0,2,0,0,9,0,0],
    [0,5,1,0,4,0,0,6,0]
]

bT= 0

def printBoard(boa: list) -> None:
    """
    Prints the 9 x 9 sudoku board
    Para: List
    Return Type: None
    """
    for row in range(len(boa)):
        for field in range(len(boa[0])):

            if field % 3 == 0 and field != 0:
                print("|",end="  ")
            print(boa[row][field],end="  ")

            if field == 8:
                print()

        if row == 8:
            print()
        elif (row + 1) % 3 == 0 and row != 0:
            print("-" * 32)

def checkEmpty(boa: list):
    """
    Check if the board has an empty element which are 
    represented by a 0

    :param boa: board data
    :type boa: list
    """

    for row in range(len(boa)):
        for column in range(len(boa[0])):
            #return the co-ordinates of empty space
            if boa[row][column] == 0:
                return (row,column)

    return None

def solver(boa: list) -> BOOL:
    """ Backtracking function
    i.e. recursively calls itself until the board is filled

    :param boa: sudoku board
    :type boa: list
    :rtype: BOOL
    """
    track = checkEmpty(boa)
    if not track:
        return True
    else:
        row, col = track

    for value in range(1,10):

        if checkData(boa, value, track):
            boa[row][col] = value

            # Recursive call
            if solver(boa):
                return True

            boa[row][col] = 0

    global bT
    bT += 1
    return False

def checkData(boa: list, test: int, pos: TUPLE) -> BOOL:
    """
    Function to check the uniques of elements in row, column and 3 x 3 square
    :param boa: sudoku board
    :type boa: list
    :param num: test value i.e [1-9]
    :type num: int
    :param pos: co-ordinates of the empty space
    :type pos: tuple
    :return: if/whether test value is allowed
    :rtype: BOOL
    """
    # Tests the uniqueness of the element in a row
    for i in range(len(boa[0])):
        if boa[pos[0]][i] == test and pos[1] != i:
            return False
    # Tests the uniqueness of the element in a column
    for i in range(len(boa)):
        if boa[i][pos[1]] == test and pos[0] != i:
            return False

    # Generation of 3 X 3 square grid
    sqaure_X = pos[1] // 3
    square_Y = pos[0] // 3

    # Tests the uniqueness of the element in a square grid
    for i in range(square_Y * 3, square_Y * 3 + 3):
        for j in range(sqaure_X * 3, sqaure_X * 3 + 3):
            if boa[i][j] == test and (i,j) != pos:
                return False

    return True


printBoard(board)

print("=" * 32)
print()
solver(board)

printBoard(board)
print("BackTracked: " + str(bT))
bT = 0

print("New Board ")
print("-"*70)
printBoard(board2)

print("=" * 32)
print()
solver(board2)

printBoard(board2)
print("BackTracked: " + str(bT))


