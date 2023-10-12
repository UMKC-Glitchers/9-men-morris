import constants


class NineMensMorrisGame:
    def __init__(self):
        self.phase = constants.PHASE1
        self.turn = constants.PLAY1
        self.CURRENT_POSITION = constants.CURRENT_POSITION

    def change_turn(self):
        if self.turn == constants.PLAY1:
            self.turn = constants.PLAY2
        else:
            self.turn = constants.PLAY1

    def get_turn(self):
        return self.turn

    def place_piece(self, row, col, player):
        self.CURRENT_POSITION[row][col] = player

    def move_piece(self, start_row, start_col, end_row, end_col, player):
        self.CURRENT_POSITION[start_row][start_col] = constants.BLANK
        self.CURRENT_POSITION[end_row][end_col] = player

    def remove_piece(self, row, col):
        self.CURRENT_POSITION[row][col] = constants.BLANK

    def is_move_valid(self, row, col, new_row, new_col, moves):
        if (self.phase == constants.PHASE1) or (self.phase == constants.PHASE3):
            return [row, col] in self.get_valid_moves()
        elif self.phase == constants.PHASE2:
            for move in moves:
                newb1 = str(move[0]) + str(move[1])
                newb2 = str(new_row) + str(new_col)
                if newb1 == newb2:
                    return 1
            return 0

    def get_valid_moves(self):
        moves = []
        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                if (int(constants.VALID_POSITIONS[r][c]) == constants.VALID) and (
                        int(self.CURRENT_POSITION[r][c]) == constants.BLANK):
                    moves.append([r, c])
        return moves

    def is_game_over(self):
        # Logic to check if the game is over
        pass

        # Other methods for game rules, checking for a mill, etc.
