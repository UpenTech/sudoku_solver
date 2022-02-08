board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def printBoard(data: list) -> None:
    """
    Prints the 9 x 9 sudoku board
    Para: List
    Return Type: None
    """
    for row in range(0,9):
        for field in range(0,9):

            if field % 3 == 0 and field != 0:
                print("|",end="  ")
            print(data[row][field],end="  ")

            if field == 8:
                print()

        if row == 8:
            print()
        elif (row + 1) % 3 == 0 and row != 0:
            print("-" * 32)

