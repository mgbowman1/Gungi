class Position:

    def __init__(self, x: int, y: int, z: int):  # creates a new position instance with x,y and z values
        self.x = x  # x position on board [column]
        self.y = y  # y position on board [row]
        self.z = z  # z position on board [tier]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Piece:
    char: str  # the string that represents the piece on the board
    earthlink: int = 0  # 0=no EARTH-LINK ability, 1=full EARTH-LINK ability, 2=only front pieces, 3=only back pieces
    front: bool = True  # whether this piece is a front or back
    mree: int = 0  # 0=no MOBILE RANGE EXPANSION EFFECT, 1=Fortress, 2=Catapult

    def __init__(self, p: Position, color: bool, alternate):
        self.p = p  # the position of the piece
        self.color = color  # the color of the piece
        self.alternate: Piece = alternate  # the piece class for the alternate piece if this piece is flipped
        if alternate:
            alternate.color = not color  # setting alternate color to the opposite of this pieces color
            alternate.alternate = self  # setting the alternate of the alternate to this

    def supercheckjump(self, activelist: list, newp: Position) -> bool:  # checks if a move requires jumping
        xdiff: int = (newp.x - self.p.x) / abs(newp.x - self.p.x)
        ydiff: int = (newp.y - self.p.y) / abs(newp.y - self.p.y)
        tempp: Position = self.p
        while not (tempp.x == newp.x):
            tempp = Position(tempp.x + xdiff, tempp.y, 0)
            if not tempp.__eq__(newp) and self.superpieceat(activelist, tempp):
                return True
            if not (tempp.y == newp.y):
                tempp = Position(tempp.x, tempp.y + ydiff, 0)
                if not tempp.__eq__(newp) and self.superpieceat(activelist, tempp):
                    return True
        while not (tempp.y == newp.y):
            tempp = Position(tempp.x, tempp.y + ydiff, 0)
            if not tempp.__eq__(newp) and self.superpieceat(activelist, tempp):
                return True
        return False

    def supercheckmove(self, activelist: list, newp: Position) -> bool:  # checks if a move is generally valid
        if self.p.__eq__(newp):
            return False
        if not self.supervalidposition(newp):
            return False
        if self.superpieceat(activelist, newp):
            return False
        tempp: Position = Position(newp.x, newp.y, newp.z - 1)
        if tempp.z >= 0 and not self.superpieceat(activelist, tempp):
            return False
        if self.supercheckjump(activelist, newp):
            return False
        for piece in activelist:
            p: Piece = piece
            if p.p.__eq__(newp) and p.color == self.color:
                return False
        return True

    def supercheckdrop(self,  activelist: list, newp: Position) -> bool:  # checks if a drop is generally valid
        if not self.supervalidposition(self, newp):
            return False
        if self.superpieceat(activelist, newp):
            return False
        if newp.z > 0 and not self.supercheckearthlink(self, activelist, newp):
            return False
        return True

    def supermove(self, newp: Position):  # moves the piece without requiring a validity check
        self.p = newp

    def supergetmree(self, activelist: list) -> bool:  # checks if this piece is in allied Mobile Range Expansion Effect
        for piece in activelist:
            p: Piece = piece
            if p.mree == 1 and p.color == self.color and self.p.x == p.p.x and not self.superinfront(self, p.p):
                return True
            if p.mree == 2 and p.color == self.color and ((self.color and self.p.y < 3) or (not self.color and self.p.y > 5)) and self.superchecklocation(self, [3,7,8,9,11,12,13,14,15,17,18,19,23], p.p):
                return True
        return False

    def supercaptured(self, activelist: list, hand: list):  # execute normal procedures for a captured piece
        activelist.remove(self)
        hand.append(self.alternate)

    def superchecklocation(self, positions: list, newp: Position) -> bool:
        # positions is a list of integers from 1-25 where 1 represents two squares forward and to the left of the piece
        # 2 represents 2 squares forward and 1 square to the left of the position and so on
        # newp is a regular Position variable
        # should return whether newp is equal to one of the relative positions in the positions list
        x: int = newp.x - self.p.x + 3
        y: int = newp.y - self.p.y + 3
        relative: int = y * 5 + x
        if positions.count(relative) > 0:
            return True
        return False

    def supercheckearthlink(self, activelist: list, newp: Position) -> bool:
        # returns true if the desired drop is within EARTH-LINK special move
        if newp.z == 0:
            return False
        else:
            for piece in activelist:
                p: Piece = piece
                if p.p.x == newp.x and p.p.y == newp.y and p.p.z == newp.z - 1 and p.earthlink > 0:
                    if p.earthlink == 1:
                        return True
                    elif p.earthlink == 2 and self.front:
                        return True
                    elif p.earthlink == 3 and not self.front:
                        return True
            return False

    def superinfront(self, pos1: Position) -> bool:  # returns true if pos1 is considered "in front" of this piece
        return (self.color and pos1.y > self.p.y) or (not self.color and pos1.y < self.p.y)

    @staticmethod
    def supervalidposition(pos1: Position) -> bool:  # return true if pos1 is a valid position on the board
        return not pos1.x < 0 or pos1.x > 8 or pos1.y < 0 or pos1.y > 8 or pos1.z < 0 or pos1.z > 2

    @staticmethod
    def superpieceat(activelist: list, pos1: Position) -> bool:  # returns true if there is a piece at pos1
        for piece in activelist:
            p: Piece = piece
            if p.p.__eq__(pos1):
                return True
        return False
