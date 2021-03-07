# Jeremy Pena
# 3/1/2021
# This program... #TODO

# from colorama import Fore  # TODO remove color printing before turned in


class JanggiGame:
    """Represents a Janggi Game and all of its pieces"""

    def __init__(self):
        self._turn = "blue"
        self._game_state = 'UNFINISHED'
        self._game_board = GameBoard()

    def get_game_state(self):
        """Returns the current game state"""
        return self._game_state

    def is_in_check(self, color):
        """Returns true if the given player is in check, this method will iterate through all of the opposing players
        active pieces get_active_pieces(color) and see if the generals location on the board is a valid move for any
        pieces, will return either True or False """

        pass

    def make_move(self, start_pos, dest_pos):
        """Moves the piece at the specified position to the destination position if allowed will return True or False"""

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
            dest_y = int(dest_pos[1] + dest_pos[2]) - 1
        if len(dest_pos) == 2:
            dest_y = int(dest_pos[1]) - 1

        piece_to_move = self._game_board.get_piece(start_x, start_y)

        print("make_move(", start_pos, ",", dest_pos, ")")

        if piece_to_move.valid_move(start_x, start_y, dest_x, dest_y) is True and \
                self._game_board.board_is_valid(start_x, start_y, dest_x, dest_y) is True:
            self._game_board.set_board(piece_to_move, dest_x, dest_y)
            self._game_board.set_board(0, start_x, start_y)
            return True
        else:
            return False

    def is_check_mate(self, color):
        """Determines if one color is in checkmate, will first se if is_in_check() returns true, then will
        check to see what available moves the general has and if its possible move coordinates are still valid
        moves for the opposing color, will return True or False"""
        pass

    def print_board(self):
        """prints the current game board"""
        return self._game_board.board_print()


class GameBoard:
    """Represents the gameboard in the Janggi Game, initializes all of the pieces as piece objects of specific
    subclasses, needs to communicate with all the Pieces classes in order to read their information and get info
    about their valid movement patterns"""

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

    def get_active_pieces(self, color):
        """Will return a list of piece objects that are active of the given color"""
        pass

    def get_piece(self, x_coord, y_coord):
        """Returns the piece object at the given coordinates"""
        return self._board[y_coord][x_coord]

    def set_board(self, piece, x_coord, y_coord):
        """Moves the specified piece to the specified coordinates, returns nothing"""
        self._board[y_coord][x_coord] = piece
        return

    def get_board(self):
        """Returns the game board"""
        return self._board

    def board_is_valid(self, start_x, start_y, dest_x, dest_y):
        """Determines if the piece at starting location is allowed to make the move, returns True or False"""
        start_piece = self._board[start_y][start_x]
        dest_piece = self._board[dest_y][dest_x]

        if dest_piece == 0:
            return True
        if dest_piece.get_color() == start_piece.get_color():
            return False
        else:
            return True


class Piece:
    """Represents a generic Janggi Piece, parameters are color and ID, data member self._active is used for keeping
    track of active pieces on the board, does not communicate with other classes"""

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
    """Represents a General piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        if self.get_color() == "blue":
            if end_y == (0 or 1 or 2 or 3 or 4 or 5 or 6):
                return False
            elif end_x == (0 or 1 or 2 or 6 or 7 or 8):
                return False
            elif (end_y == start_y) and (end_x == ((start_x + 1) or (start_x - 1))):
                return True
            elif (end_x == start_x) and (end_y == ((start_y + 1) or (start_y - 1))):
                return True
            else:
                return False
        elif self.get_color() == "red":
            if end_y == (3 or 4 or 5 or 6 or 7 or 8 or 9):
                return False
            elif end_x == (0 or 1 or 2 or 6 or 7 or 8):
                return False
            elif (end_y == start_y) and (end_x == ((start_x + 1) or (start_x - 1))):
                return True
            elif (end_x == start_x) and (end_y == ((start_y + 1) or (start_y - 1))):
                return True
            else:
                return False


class Guard(Piece):
    """Represents a Guard piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        if self.get_color() == "blue":
            if end_y == (0 or 1 or 2 or 3 or 4 or 5 or 6):
                return False
            elif end_x == (0 or 1 or 2 or 6 or 7 or 8):
                return False
            elif (end_y == start_y) and (end_x == ((start_x + 1) or (start_x - 1))):
                return True
            elif (end_x == start_x) and (end_y == ((start_y + 1) or (start_y - 1))):
                return True
            else:
                return False
        elif self.get_color() == "red":
            if end_y == (3 or 4 or 5 or 6 or 7 or 8 or 9):
                return False
            elif end_x == (0 or 1 or 2 or 6 or 7 or 8):
                return False
            elif (end_y == start_y) and (end_x == ((start_x + 1) or (start_x - 1))):
                return True
            elif (end_x == start_x) and (end_y == ((start_y + 1) or (start_y - 1))):
                return True
            else:
                return False


class Horse(Piece):
    """Represents a Horse piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Elephant(Piece):
    """Represents an Elephant piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Chariot(Piece):
    """Represents a Chariot piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Cannon(Piece):
    """Represents a Cannon piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        pass


class Soldier(Piece):  # TODO - This works
    """Represents a Soldier piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        if self.get_color() == "blue":
            if end_y == (start_y + 1):
                return False
            elif start_y == (0 or 1 or 2) and start_x == (3 or 4 or 5):  # palace conditions
                if end_y == (start_y - 1) and (end_x == (start_x + 1) or (start_x - 1)):
                    return True
            elif (start_y == end_y) and (end_x == (start_x + 1) or (start_x - 1)):  # Left or right move
                return True
            elif end_y == (start_y - 1) and end_x == start_x:  # Forward move
                return True
            else:
                return False
        elif self.get_color() == "red":
            if end_y == (start_y - 1):
                return False
            elif start_y == (7 or 8 or 9) and start_x == (3 or 4 or 5):  # palace conditions
                if end_y == (start_y + 1) and (end_x == (start_x + 1) or (start_x - 1)):
                    return True
            elif (start_y == end_y) and (end_x == (start_x + 1) or (start_x - 1)):  # Left or right move
                return True
            elif end_y == (start_y + 1) and end_x == start_x:  # Forward move
                return True
            else:
                return False
