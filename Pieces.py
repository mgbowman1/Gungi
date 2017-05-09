from General import *

class Commander(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

    def checkchecker(self) -> bool:  # checks if this commander is currently in check or checkmate

class Captain(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Samurai(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Spy(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Catapult(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Fortress(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class HiddenDragon(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Prodigy(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Bow(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Pawn(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Pistol(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Pike(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Clandestinite(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Lance(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class DragonKing(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Phoenix(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Arrow(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Bronze(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Silver(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured

class Gold(Piece):
    def checkmove(self, newp: Position, activelist: list) -> bool:  # check supercheckmove as well as any piece specific movement rules and return whether a move is allowed

    def move(self, newp: Position, activelist: list, whitehand: list, blackhand: list, player: bool):  # use checkmove to see if a move is allowed, if so then execute the move with supermove and take care of any after effects

    def simmove(self, newp: Position, activelist: list):  # executes a normal move, including checking if it is legal and not moving if it is not, but saves all of the relevant data about the move so it can be fully undone

    def unmove(self, activelist: list):  # reverses a simmove

    def drop(self, newp: Position, activelist: list, hand: list):  # use supercheckdrop and any other necessary checks to check the validity of a drop, then use supermove to execute it

    def captured(self, activelist: list, hand: list):  # use supercaptured as well as executing any piece specific effects of being captured
