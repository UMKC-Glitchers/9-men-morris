import os

import constants


class NineMensMorrisGame:
    def __init__(self):
        self.phase = constants.PHASE1
        self.turn = constants.PLAY1
        self.CURRENT_POSITION = constants.CURRENT_POSITION
        self.counter = 0
        self.play1_counter = 0
        self.play2_counter = 0
        self.message = constants.PLAYER1_MESSAGE
        self.move_made = ""
        self.moves_made = []

    def change_turn(self):
        if self.turn == constants.PLAY1:
            self.play1_counter = self.play1_counter + 1
            self.turn = constants.PLAY2
            self.message = constants.PLAYER2_MESSAGE
        else:
            self.play2_counter = self.play2_counter + 1
            self.turn = constants.PLAY1
            self.message = constants.PLAYER1_MESSAGE

        if self.play1_counter == constants.TOTAL_MENS and self.play2_counter == constants.TOTAL_MENS:
            self.set_phase(constants.PHASE2)

        if self.phase == constants.PHASE2:
            self.message = "Piece placement is done, Should implement Phase 2 code"

    def get_turn(self):
        return self.turn

    def set_phase(self, phase):
        self.phase = phase

    def make_move(self, row, col, new_row, new_col):
        valid = self.is_move_valid(row, col, new_row, new_col, None)
        print("clicked:", row + 1, col + 1, valid)  # Debug message, Remove it later
        if valid:
            move = self.get_move(row, col)
            self.move_made = move
            self.moves_made.append(move)
            self.counter = self.counter + 1
            if self.phase == constants.PHASE1:
                self.place_piece(row, col, self.get_turn())
                self.change_turn()
            elif self.phase == constants.PHASE2:
                pass
            else:
                pass

    def get_move(self, row, col):
        return constants.POSITIONS[col] + str(abs(row - 7))

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
            # TODO - Implement me
            # for move in moves:
            #     newb1 = str(move[0]) + str(move[1])
            #     newb2 = str(new_row) + str(new_col)
            #     if newb1 == newb2:
            #         return 1
            return 0

    def get_valid_moves(self):
        moves = []
        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                if (int(constants.VALID_POSITIONS[r][c]) == constants.VALID) and (
                        int(self.CURRENT_POSITION[r][c]) == constants.BLANK):
                    moves.append([r, c])
        return moves

    def save_game(self):
        print("Saving moves:",self.moves_made)

        if os.path.exists(constants.GAME_STATE_FILE):
            os.remove(constants.GAME_STATE_FILE)

        state_file = open(constants.GAME_STATE_FILE, "w")
        data = ",".join(self.moves_made)
        state_file.write(data)
        state_file.close()

    def is_game_over(self):
        # Logic to check if the game is over
        pass

        # Other methods for game rules, checking for a mill, etc.
