import constants



class NineMensMorrisGame:
    def __init__(self):
        self.phase = 1
        self.turn = constants.PLAY1

    def place_piece(self, row, col, player):
        # Logic for placing a piece on the board
        pass

    def modify_cb(self, action, r, c, nr, nc):
        # remove a token
        if (action == "remove") or (action == "move"):
            constants.CURRENT_POSITION[r][c] = constants.BLANK

        # add a token
        if (action == "add") or (action == "move"):
            if int(self.turn) == int(constants.PLAY1):
                constants.CURRENT_POSITION[nr][nc] = constants.PLAY1
            else:
                constants.CURRENT_POSITION[nr][nc] = constants.PLAY2
        return constants.CURRENT_POSITION

    def move_piece(self, start_row, start_col, end_row, end_col, player):
        # Logic for moving a piece on the board
        pass

    def remove_piece(self, row, col, player):
        # Logic for removing a piece from the board
        pass

    def is_move_valid(self, r, c, nr, nc, moves):
        if (self.phase == 1) or (self.phase == 3):
            return [r, c] in self.get_valid_moves()
        elif self.phase == 2:
            for itemof in moves:
                newb1 = str(itemof[0]) + str(itemof[1])
                newb2 = str(nr) + str(nc)
                if newb1 == newb2:
                    return 1
            return 0

    def get_valid_moves(self):
        moves = []
        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                if (int(constants.VALID_POSITIONS[r][c]) == constants.VALID) and (
                        int(constants.VALID_POSITIONS[r][c]) == constants.BLANK):
                    moves.append([r, c])
        return moves

    def is_game_over(self):
        # Logic to check if the game is over
        pass

        # Other methods for game rules, checking for a mill, etc.
