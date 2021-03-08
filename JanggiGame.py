# Jeremy Pena
# 3/1/2021
# This program... #TODO

# from colorama import Fore  # TODO remove color printing before turned in


def alpha_translate(start_pos, dest_pos):
    """translates from alpha to numerical coordinates"""
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

    return [start_x, start_y, dest_x, dest_y]


class JanggiGame:
    """Represents a Janggi Game and all of its pieces"""

    def __init__(self):
        self._turn = "blue"
        self._game_state = 'UNFINISHED'
        self._game_board = GameBoard()
        self._turn_count = 0

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

        start_x = alpha_translate(start_pos, dest_pos)[0]
        dest_x = alpha_translate(start_pos, dest_pos)[2]
        dest_y = alpha_translate(start_pos, dest_pos)[3]
        start_y = alpha_translate(start_pos, dest_pos)[1]

        piece_to_move = self._game_board.get_piece(start_x, start_y)

        print("\nmake_move(", start_pos, ",", dest_pos, ")")

        print("piece = ", piece_to_move)
        if piece_to_move == 0:
            print("No Starting Piece Selected")
            return False
        if piece_to_move.valid_move(start_x, start_y, dest_x, dest_y) is True and \
                self._game_board.board_is_valid(start_x, start_y, dest_x, dest_y) is True:
            self._game_board.set_board(piece_to_move, dest_x, dest_y)
            self._game_board.set_board(0, start_x, start_y)
            return True
        else:
            print("\nmove not made\n")
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

        y_offset = (start_y - dest_y)
        x_offset = (start_x - dest_x)

        if start_piece == 0:
            print("false 1")
            return False
        if start_piece.get_id() == "Horse":  # Horse conditionals
            if (x_offset == 2) and abs(y_offset) == 1:
                if self._board[start_y][start_x - 1] == 0:
                    print("true 1")
                    return True
            if abs(x_offset) == 1 and (y_offset == 2):
                if self._board[start_y - 1][start_x] == 0:
                    print("true 2")
                    print(x_offset, y_offset)
                    print(self._board[start_y - 1][start_x])
                    return True
            if (x_offset == (- 2)) and abs(y_offset) == 1:
                if self._board[start_y][start_x + 1] == 0:
                    print("true 3")
                    return True
            if abs(x_offset) == 1 and (y_offset == (-2)):
                if self._board[start_y + 1][start_x] == 0:
                    print("true 4")
                    return True
            else:
                print("false 2")
                print([y_offset, x_offset])
                return False
        if dest_piece == 0:
            print("true 5")
            return True
        if dest_piece.get_color() == start_piece.get_color():
            print("false 3")
            return False
        else:
            print("true else")
            return True
        #   TODO - Work on this...


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
        blue_y_invalid = [0, 1, 2, 3, 4, 5, 6]
        red_y_invalid = [3, 4, 5, 6, 7, 8, 9]
        x_invalid = [0, 1, 2, 6, 7, 8]

        if self.get_color() == "blue":
            if end_y in blue_y_invalid:
                return False
            elif end_x in x_invalid:
                return False
            elif (end_y == start_y) and (abs(end_x - start_x) == 1):
                return True
            elif (end_x == start_x) and (abs(end_y - start_y) == 1):
                return True
            elif (abs(end_x - start_x)) == 1 and (abs(end_y - start_y) == 1):
                return True
            else:
                return False
        elif self.get_color() == "red":
            if end_y in red_y_invalid:
                return False
            elif end_x in x_invalid:
                return False
            elif (end_y == start_y) and (abs(end_x - start_x) == 1):
                return True
            elif (end_x == start_x) and (abs(end_y - start_y) == 1):
                return True
            elif (abs(end_x - start_x)) == 1 and (abs(end_y - start_y) == 1):
                return True
            else:
                return False


class Guard(Piece):
    """Represents a Guard piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        blue_y_invalid = [0, 1, 2, 3, 4, 5, 6]
        red_y_invalid = [3, 4, 5, 6, 7, 8, 9]
        x_invalid = [0, 1, 2, 6, 7, 8]

        if self.get_color() == "blue":
            if end_y in blue_y_invalid:
                return False
            elif end_x in x_invalid:
                return False
            elif (end_y == start_y) and (abs(end_x - start_x) == 1):
                return True
            elif (end_x == start_x) and (abs(end_y - start_y) == 1):
                return True
            elif (abs(end_x - start_x)) == 1 and (abs(end_y - start_y) == 1):
                return True
            else:
                return False
        elif self.get_color() == "red":
            if end_y in red_y_invalid:
                return False
            elif end_x in x_invalid:
                return False
            elif (end_y == start_y) and (abs(end_x - start_x) == 1):
                return True
            elif (end_x == start_x) and (abs(end_y - start_y) == 1):
                return True
            elif (abs(end_x - start_x)) == 1 and (abs(end_y - start_y) == 1):
                return True
            else:
                return False


class Horse(Piece):
    """Represents a Horse piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        if self.get_id() == "Horse":
            if (abs(end_y - start_y) == 2) and (abs(end_x - start_x) == 1):
                return True
            elif (abs(end_x - start_x) == 2) and (abs(end_y - start_y) == 1):
                return True
            else:
                return False


class Elephant(Piece):
    """Represents an Elephant piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        if self.get_id() == "Elephant":
            if (abs(end_y - start_y) == 3) and (abs(end_x - start_x) == 2):
                return True
            elif (abs(end_x - start_x) == 3) and (abs(end_y - start_y) == 2):
                return True
            else:
                return False


class Chariot(Piece):
    """Represents a Chariot piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        y_coords = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        x_coords = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        palace_y = [0, 1, 2, 7, 8, 9]
        palace_x = [3, 4, 5]

        if self.get_id() == "Chariot":
            if (end_x == start_x) and (end_y in y_coords):
                return True
            if (end_y == start_y) and (end_x in x_coords):
                return True
            if ((start_y in palace_y) and (end_y in palace_y)) and ((start_x in palace_x) and (end_x in palace_x)) \
                    and (abs(start_y - end_y) == abs(start_x - end_x)):  # diagonal okay in Palace
                return True
            else:
                return False


class Cannon(Piece):
    """Represents a Cannon piece, inherits from Piece class"""

    def __init__(self, color, ID):
        super().__init__(color, ID)

    def valid_move(self, start_x, start_y, end_x, end_y):
        """Returns true if the given destination coordinates are a valid move for this piece type"""
        y_coords = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        x_coords = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        palace_y = [0, 1, 2, 7, 8, 9]
        palace_x = [3, 4, 5]

        if self.get_id() == "Cannon":
            if (end_x == start_x) and (end_y in y_coords):
                return True
            if (end_y == start_y) and (end_x in x_coords):
                return True
            if ((start_y in palace_y) and (end_y in palace_y)) and ((start_x in palace_x) and (end_x in palace_x)) \
                    and (abs(start_y - end_y) == abs(start_x - end_x)):  # diagonal okay in Palace
                return True
            else:
                return False


class Soldier(Piece):
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



