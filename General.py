class Position:
    def __init__(self, x: int, y: int, z: int):  # creates a new position instance with x,y and z values
        self.x = x  # x position on board or column
        self.y = y  # y position on board or row
        self.z = z  # z position on board or tier


class Piece:
    def __init__(self, p: Position, color: bool, alternate):
        self.p = p  # the position of the piece
        self.color = color  # the color of the piece
        self.alternate: Piece = alternate  # the piece class for the alternate piece if this piece is flipped
        alternate.color = not color  # setting alternate color to the opposite of this pieces color
        alternate.alternate = self  # setting the alternate of the alternate to this

    def superCheckMove(self, newP: Position) -> bool:  # checks if a move is generally valid without using rules specific to certain pieces and then returns true if the move is valid
        # should check for normal problems such as allied pieces in the way or moving to this location will cause check on the allied commander and so on

    def superCheckDrop(self, newP: Position) -> bool:  # checks if a drop is generally valid without using rules specific to certain pieces and then returns true if the drop is valid
        # should check for normal problems such as allied pieces in the way, but allow for rules like earth-link

    def superMove(self, newP: Position):  # moves the piece without requiring a validity check

    def superGetMREE(self) -> bool:  # checks if this piece is in range of allied Mobile Range Expansion Effect and returns true if it is
