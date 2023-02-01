import sys
from asyncore import read

# This is a program that solves Sudoku puzzles
# the input for the puzzle should be provided in the input.txt file
# the outcome of the puzzle will be displayed in the console

def readInput():
    inputData = [['*' for i in range(9)] for j in range(9)]
    inputFile = open("input.txt", "r")

    for x in range(9):
        for y in range(9):
            c = inputFile.read(1)
            if c == ' ' or c == '\n':
                c = inputFile.read(1)
            inputData[y][x] = int(c)

    return inputData

def solveSudoku(board, y, x):
    if x > 8:
        x = 0
        y += 1
    if y == 9:
        return True

    if board[y][x] == 0:
        for i in range(1, 10):
            if checkInput(board, y, x, i):
                board[y][x] = i
                if solveSudoku(board, y, x + 1) == False:
                    board[y][x] = 0
                else:
                    return True
        return False
    else:
        return solveSudoku(board, y, x + 1)

def checkInput(board, _y, _x, value):
    x = _x - (_x % 3)
    y = int(_y / 3) * 3
    for i in range(9):
        if _x != i and board[_y][i] == value:
            return False
        if _y != i and board[i][_x] == value:
            return False
        if _x != x + i%3 and _y != y + int(i/3) and board[y + int(i/3)][x + i%3] == value:
            return False
    return True

def printBoard(board):
    for x in range(9):
        for y in range(9):
            print(board[y][x], end=" ")
        print()

sudokuBoard = readInput()
if solveSudoku(sudokuBoard, 0, 0) == False:
    print("The provided puzzle is not solvable!")
else:  
    printBoard(sudokuBoard)