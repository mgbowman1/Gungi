class Position:
    def __init__(self, x: int, y: int, z: int):  # creates a new position instance with x,y and z values
        self.x = x  # x position on board [column]
        self.y = y  # y position on board [row]
        self.z = z  # z position on board [tier]


class Piece:
    char: str
    def __init__(self, p: Position, color: bool, alternate):
        self.p = p  # the position of the piece
        self.color = color  # the color of the piece
        self.alternate: Piece = alternate  # the piece class for the alternate piece if this piece is flipped
        if alternate:
            alternate.color = not color  # setting alternate color to the opposite of this pieces color
            alternate.alternate = self  # setting the alternate of the alternate to this

    def supercheckmove(self, newp: Position, activelist: list) -> bool:  # checks if a move is generally valid without using rules specific to certain pieces and then returns true if the move is valid
        # should check for normal problems such as allied pieces in the way or moving to this location will cause check on the allied commander and so on

    def supercheckdrop(self, newp: Position, activelist: list) -> bool:  # checks if a drop is generally valid without using rules specific to certain pieces and then returns true if the drop is valid
        # should check for normal problems such as allied pieces in the way, but allow for rules like earth-link

    def supermove(self, newp: Position):  # moves the piece without requiring a validity check
        self.p = newp

    def supergetmree(self, activelist: list) -> bool:  # checks if this piece is in range of allied Mobile Range Expansion Effect and returns true if it is

    def supercaptured(self, activelist: list, hand: list):  # execute normal procedures for a captured piece such as flipping the piece and adding it to the opponents hand
        activelist.remove(self)
        hand.append(self.alternate)

    def superchecklocation(self, positions: list, newp: Position) -> bool:  # positions is a list of integers from 1-25 where 1 represents two squares forward and to the left of the pieces position, 2 represents 2 squares forward and 1 square to the left of the position and so on.  newp is a regular Position variable
        # should return whether newp is equal to one of the relative positions in the positions list
        x: int = newp.x - self.p.x + 3
        y: int = newp.y - self.p.y + 3
        relative: int = y * 5 + x
        if positions.count(relative) > 0:
            return True
        return False