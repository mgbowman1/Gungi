from Pieces import *

currentTurn: bool = True  # variable for tracking whose turn it is, true means white and false means black
whiteHand: list = []  # the starting hand of the white team
blackHand: list = []  # the starting hand of the black team
boardPieces: list = []  # the list of pieces that are currently on the board
moves: list = []  # list of all moves made so far

def getinput() -> str:  # gets user input as a string and returns it

def printscreen():  # prints the board and any other relevant information

def getpiece(type: Piece, p: Position) -> Piece:  # searches the boardPieces list to find a piece which matches the type and position given

def main():  # main function which uses a loop to execute other functions to actually play the game

main()  # calls the main function to begin and end the program