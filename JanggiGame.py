# Jeremy Pena
# 3/1/2021
# This program... #TODO

from colorama import Fore  # TODO remove color printing


class JanggiGame:
    """Represents a Janggi Game"""

    def __init__(self):
        self._turn = "red"
        self._game_state = 'UNFINISHED'
        self._game_board = GameBoard()

    def get_game_state(self):
        """Returns the current game state"""
        return self._game_state

    def is_in_check(self, color):
        """Returns true if the given player is in check, this method will iterate through all of the opposing
        players active pieces and see if the generals location on the board is a valid move for any pieces"""
        pass

    def make_move(self, start_pos, dest_pos):
        """Moves the piece at the specified position to the destination position if allowed"""

        alpha_to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8}

        start_x = int(alpha_to_num.get(start_pos[0]))
        dest_x = int(alpha_to_num.get(dest_pos[0]))
        start_y = 0
        dest_y = 0

        if len(start_pos) == 3:
            start_y = int(start_pos[1] + start_pos[2]) - 1
        if len(start_pos) == 2:
            start_y = int(start_pos[1]) - 1
        if len(dest_pos) == 3:
            dest_y = int(dest_pos[1] + dest_pos[2])
        if len(dest_pos) == 2:
            dest_y = int(dest_pos[1]) - 1

        piece_to_move = self._game_board.get_piece(start_x, start_y)

        if piece_to_move.valid_move(start_x, start_y, dest_x, dest_y) is True:      # TODO - add to this....
            self._game_board.set_board(piece_to_move, dest_x, dest_y)
            self._game_board.set_board(0, start_x, start_y)
            return True
        else:
            return False

    def print_board(self):
        """prints the current game board"""
        return self._game_board.board_print()


class GameBoard:
    """Represents the gameboard in the Janggi Game"""

    def __init__(self):
        rcr1 = Chariot("red", "Chariot")
        rel1 = Elephant("red", "Elephant")
        rh1 = Horse("red", "Horse")
        rgd1 = Guard("red", "Guard")
        rgd2 = Guard("red", "Guard")
        rel2 = Elephant("red", "Elephant")
        rh2 = Horse("red", "Horse")
        rcr2 = Chariot("red", "Chariot")
        rg = General("red", "General")
        rc1 = Cannon("red", "Cannon")
        rc2 = Cannon("red", "Cannon")
        rs1 = Soldier("red", "Soldier")
        rs2 = Soldier("red", "Soldier")
        rs3 = Soldier("red", "Soldier")
        rs4 = Soldier("red", "Soldier")
        rs5 = Soldier("red", "Soldier")
        bcr1 = Chariot("blue", "Chariot")
        bel1 = Elephant("blue", "Elephant")
        bh1 = Horse("blue", "Horse")
        bgd1 = Guard("blue", "Guard")
        bgd2 = Guard("blue", "Guard")
        bel2 = Elephant("blue", "Elephant")
        bh2 = Horse("blue", "Horse")
        bcr2 = Chariot("blue", "Chariot")
        bg = General("blue", "General")
        bc1 = Cannon("blue", "Cannon")
        bc2 = Cannon("blue", "Cannon")
        bs1 = Soldier("blue", "Soldier")
        bs2 = Soldier("blue", "Soldier")
        bs3 = Soldier("blue", "Soldier")
        bs4 = Soldier("blue", "Soldier")
        bs5 = Soldier("blue", "Soldier")
        self._board = [[rcr1, rel1, rh1, rgd1, 0, rgd2, rel2, rh2, rcr2],
                       [0, 0, 0, 0, rg, 0, 0, 0, 0],
                       [0, rc1, 0, 0, 0, 0, 0, rc2, 0],
                       [rs1, 0, rs2, 0, rs3, 0, rs4, 0, rs5],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [bs1, 0, bs2, 0, bs3, 0, bs4, 0, bs5],
                       [0, bc1, 0, 0, 0, 0, 0, bc2, 0],
                       [0, 0, 0, 0, bg, 0, 0, 0, 0],
                       [bcr1, bel1, bh1, bgd1, 0, bgd2, bel2, bh2, bcr2]]
        self._active_red_pieces = [rcr1, rel1, rh1, rgd1, rgd2, rel2, rh2, rcr2, rg, rc1, rc2, rs1, rs2, rs3, rs4, rs5]
        self._active_blue_pieces = [bcr1, bel1, bh1, bgd1, bgd2, bel2, bh2, bcr2, bg, bc1, bc2, bs1, bs2, bs3, bs4, bs5]
        # Create method to iterate through all opposing active pieces and call valid_move on general location

    def board_print(self):
        """Prints out the current state of the game board"""
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        for x in letters:
            print('{:^8}'.format(x), end=' ')
        for space in self._board:
            print("")
            for pos in space:
                if pos == 0:
                    print(Fore.WHITE + '{:^8}'.format(pos), end=' ')
                elif pos.get_color() == "red":
                    print(Fore.RED + '{:^8}'.format(pos.get_id()), end=' ')
                elif pos.get_color() == "blue":
                    print(Fore.BLUE + '{:^8}'.format(pos.get_id()), end=' ')

    def get_piece(self, x_coord, y_coord):
        """Returns the piece object at the given coordinates"""
        return self._board[y_coord][x_coord]

    def set_board(self, piece, x_coord, y_coord):
        """Moves the specified piece to the specified coordinates"""
        self._board[y_coord][x_coord] = piece
        return

    def get_board(self):
        """Returns the game board"""
        return self._board

    # TODO - create a second is_valid method, board_is_valid() to check for other possible hindrances...


class Piece:
    """Represents a Janggi Piece"""

    def __init__(self, color, ID):
        self._color = color
        self._ID = ID
        self._active = True

    def get_id(self):
        """Returns the Piece ID"""
        return self._ID

    def get_color(self):
        """Returns the piece color"""
        return self._color

    def is_active(self):
        """Returns true if piece is active"""
        return self._active


class General(Piece):
    """"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass
    # TODO - Can use starting position to determine if inside the palace, etc...


class Guard(Piece):
    """"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Horse(Piece):
    """"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Elephant(Piece):
    """"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Chariot(Piece):
    """"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Cannon(Piece):
    """"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Soldier(Piece):
    """"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""


game = JanggiGame()
print("Starting Board")
game.print_board()
print("")

game.make_move("e9", "e4")
print("\nMove Made")
print("***Updated Board***")
game.print_board()
print("")

game.make_move("e7", "e2")
print("\nMove Made")
print("***Updated Board***")
print("")
game.print_board()
