from Pieces import *
import os

myColor: bool = True  # variable that shows which color this player is
currentturn: bool = False  # variable for tracking whose turn it is, true means white and false means black
defaultPosition: Position = Position(0, 0, 0)  # the default position for pieces at the beginning of the game
defaultColor: bool = True  # a boolean value for the color of a piece for making the list creation easier
whiteHand: list = [Commander(defaultPosition, defaultColor, None), Captain(defaultPosition, defaultColor, Pistol(defaultPosition, not defaultColor, None)), Captain(defaultPosition, defaultColor, Pistol(defaultPosition, not defaultColor, None)), Samurai(defaultPosition, defaultColor, Pike(defaultPosition, not defaultColor, None)), Samurai(defaultPosition, defaultColor, Pike(defaultPosition, not defaultColor, None)), Spy(defaultPosition, defaultColor, Clandestinite(defaultPosition, not defaultColor, None)), Spy(defaultPosition, defaultColor, Clandestinite(defaultPosition, not defaultColor, None)), Spy(defaultPosition, defaultColor, Clandestinite(defaultPosition, not defaultColor, None)), Catapult(defaultPosition, defaultColor, Lance(defaultPosition, defaultColor, None)), Fortress(defaultPosition, defaultColor, Lance(defaultPosition, defaultColor, None)), HiddenDragon(defaultPosition, defaultColor, DragonKing(defaultPosition, defaultColor, None)), Prodigy(defaultPosition, defaultColor, Phoenix(defaultPosition, defaultColor, None)), Bow(defaultPosition, defaultColor, Arrow(defaultPosition, defaultColor, None)), Bow(defaultPosition, defaultColor, Arrow(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Silver(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Gold(defaultPosition, defaultColor, None))]  # the starting hand of the white team
defaultColor = not defaultColor
blackHand: list = [Commander(defaultPosition, defaultColor, None), Captain(defaultPosition, defaultColor, Pistol(defaultPosition, not defaultColor, None)), Captain(defaultPosition, defaultColor, Pistol(defaultPosition, not defaultColor, None)), Samurai(defaultPosition, defaultColor, Pike(defaultPosition, not defaultColor, None)), Samurai(defaultPosition, defaultColor, Pike(defaultPosition, not defaultColor, None)), Spy(defaultPosition, defaultColor, Clandestinite(defaultPosition, not defaultColor, None)), Spy(defaultPosition, defaultColor, Clandestinite(defaultPosition, not defaultColor, None)), Spy(defaultPosition, defaultColor, Clandestinite(defaultPosition, not defaultColor, None)), Catapult(defaultPosition, defaultColor, Lance(defaultPosition, defaultColor, None)), Fortress(defaultPosition, defaultColor, Lance(defaultPosition, defaultColor, None)), HiddenDragon(defaultPosition, defaultColor, DragonKing(defaultPosition, defaultColor, None)), Prodigy(defaultPosition, defaultColor, Phoenix(defaultPosition, defaultColor, None)), Bow(defaultPosition, defaultColor, Arrow(defaultPosition, defaultColor, None)), Bow(defaultPosition, defaultColor, Arrow(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Bronze(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Silver(defaultPosition, not defaultColor, None)), Pawn(defaultPosition, defaultColor, Gold(defaultPosition, defaultColor, None))]  # the starting hand of the black team
boardPieces: list = []  # the list of pieces that are currently on the board
moves: list = []  # list of all moves made so far
checkmate: bool = False  # set true if a checkmate occurs

def printscreen():  # prints the board and any other relevant information
    unusedvariable = os.system("cls")
    printlist: list = [[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]],[["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "],["  ","  ","  "]]]
    for p in boardPieces:
        piece: Piece = p
        printlist[piece.p.y][piece.p.x][piece.p.z] = piece.char
    for row in printlist:
        rowstring: str = "|"
        for cell in row:
            for tier in cell:
                rowstring += tier + ">"
        print(rowstring)
    print("")
    turnstring = "whites"
    if not currentturn:
        turnstring = "blacks"
    print("It is " + turnstring + " turn")
    hand: list = whiteHand
    if not myColor:
        hand = blackHand
    handstring: str = "Your hand:"
    for piece in hand:
        handstring += " " + piece.char
    print(handstring)

def getpiece(char: str, p: Position) -> Piece:  # searches the boardPieces list to find a piece which matches the char and position given
    for piece in boardPieces:
        if piece.char == char and piece.p == p:
            return piece
    return None

def getmove() -> str:

def sendmove(move: str):

def parsemove(move: str) -> bool:

def main():  # main function which uses a loop to execute other functions to actually play the game
    while not checkmate:
        nonlocal currentturn
        printscreen()
        if myColor == currentturn:
            print("Previous move: " + moves[-1])
            inp: str = input("Enter move: ")
            while not parsemove(inp):
                printscreen()
                inp = input("Enter move: ")
            sendmove(inp)
        else:
            parsemove(getmove())
        currentturn = not currentturn

main()  # calls the main function to begin and end the program