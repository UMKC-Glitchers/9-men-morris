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
        self.moves_made = []  # TODO - Make it a stack, Will be useful when using undo

    def change_turn(self):
        if self.phase == constants.PHASE1:
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
                self.message = "Pieces placed, Move pieces now\n" + constants.PLAY1_MOVE_MESSAGE

        elif self.phase == constants.PHASE2:
            if self.turn == constants.PLAY1:
                self.turn = constants.PLAY2
                self.message = constants.PLAY2_MOVE_MESSAGE
            else:
                self.turn = constants.PLAY1
                self.message = constants.PLAY1_MOVE_MESSAGE
        else:
            self.message = "Invalid phase"

    def get_turn(self):
        return self.turn

    def set_phase(self, phase):
        self.phase = phase

    def make_move(self, row, col, new_row, new_col):
        valid = self.is_move_valid(row, col, new_row, new_col, None)
        print("clicked:", row, col, valid)  # Debug message, Remove it later
        if valid:
            print("vaild move")
            move = self.get_move(row, col)
            self.move_made = move
            self.moves_made.append(move)
            self.counter = self.counter + 1
            if self.phase == constants.PHASE1:
                self.place_piece(row, col, self.get_turn())
                self.change_turn()
            elif self.phase == constants.PHASE2:
                self.move_piece(row, col, new_row, new_col, self.get_turn())
                if self.is_mill(self.get_turn()):
                    #TODO - Remove a piece from opponent
                    self.message = "Remove a piece from opponent"
                else:
                    self.change_turn()
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
            if self.CURRENT_POSITION[row][col] == self.get_turn():
                if (abs(new_row - row) == 1 and abs(new_col - col) == 0) or \
                   (abs(new_row - row) == 0 and abs(new_col - col) == 1) and \
                   self.CURRENT_POSITION[new_row][new_col] == constants.BLANK:
                    return True
                if constants.VALID_POSITIONS[new_row][new_col] == constants.VALID:
                    return True
            return False

    def get_valid_moves(self):
        moves = []
        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                if (int(constants.VALID_POSITIONS[r][c]) == constants.VALID) and (
                        int(self.CURRENT_POSITION[r][c]) == constants.BLANK):
                    moves.append([r, c])
        return moves

    def save_game(self):
        print("Saving moves:", self.moves_made)

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

    def is_mill(self, player):
        for line in constants.LINES:
            piece_count = 0
            for i in range(0, len(line), 2):
                row = int(line[i])
                col = int(line[i + 1])
                if self.CURRENT_POSITION[row][col] == player:
                    piece_count += 1

            if piece_count == 3:
                return True

        return False