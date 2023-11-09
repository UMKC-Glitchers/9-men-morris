import os

import constants


class NineMensMorrisGame:
    def __init__(self):
        self.phase = constants.PHASE1
        self.turn = constants.PLAY1
        self.CURRENT_POSITION = constants.CURRENT_POSITION
        self.counter = 0
        self.max_pieces = 9
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

            if (
                self.play1_counter == constants.TOTAL_MENS
                and self.play2_counter == constants.TOTAL_MENS
            ):
                self.set_phase(constants.PHASE2)
                self.message = (
                    "Pieces placed, Move pieces now\n" + constants.PLAY1_MOVE_MESSAGE
                )

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
        valid = self.is_move_valid(row, col, new_row, new_col)
        print("clicked:", row, col, valid)  # Debug message, Remove it later
        if valid:
            print("vaild move")
            move = self.get_move(row, col)
            self.move_made = move
            self.moves_made.append(move)
            self.counter = self.counter + 1
            if self.phase == constants.PHASE1:
                self.place_piece(row, col, self.get_turn())
                # if mill is formed, do not change the player's turn, but ask him to remove an opponent piece
                print("Is mill:", self.is_mill(row, col))
                self.change_turn()
            elif self.phase == constants.PHASE2:
                self.move_piece(row, col, new_row, new_col, self.get_turn())
                print("Is mill:", self.is_mill(new_row, new_col))
                # if self.is_mill(self.get_turn()):
                #     # TODO - Remove a piece from opponent
                #     self.message = "Remove a piece from opponent"
                # else:
                self.change_turn()
            elif self.phase == constants.PHASE3:
                pass

    def get_move(self, row, col):
        return constants.POSITIONS[col] + str(abs(row - 7))

    def place_piece(self, row, col, player):
        self.CURRENT_POSITION[row][col] = player

    def is_move_valid(self, row, col, new_row, new_col):
        if (self.phase == constants.PHASE1) or (self.phase == constants.PHASE3):
            return [row, col] in self.get_valid_moves()
        elif self.phase == constants.PHASE2:
            if self.CURRENT_POSITION[row][col] == self.get_turn() and self.CURRENT_POSITION[new_row][new_col] == constants.BLANK:
                # Check the valid positions matrix, there should exist a 3 in it and a 0 in current position
                # Can skip 0 for a complete row or column, Should handle a special case
                if row == new_row:
                    col_index = col
                    if new_col > col:
                        col_index += 1
                        while col_index <= new_col:
                            if constants.VALID_POSITIONS[row][col_index] == constants.VALID and self.CURRENT_POSITION[row][col_index] == constants.BLANK:
                                return True
                            elif constants.VALID_POSITIONS[row][col_index] == 0 and row != 3:
                                col_index += 1
                            else:
                                return False
                    else:
                        col_index -= 1
                        while col_index >= new_col:
                            if constants.VALID_POSITIONS[row][col_index] == constants.VALID and self.CURRENT_POSITION[row][col_index] == constants.BLANK:
                                return True
                            elif constants.VALID_POSITIONS[row][col_index] == 0 and row != 3:
                                col_index -= 1
                            else:
                                return False
                if col == new_col:
                    row_index = row
                    if new_row > row:
                        row_index += 1
                        while row_index <= new_row:
                            if constants.VALID_POSITIONS[row_index][col] == constants.VALID and self.CURRENT_POSITION[row_index][col] == constants.BLANK:
                                return True
                            elif constants.VALID_POSITIONS[row_index][col] == 0 and col != 3:
                                row_index += 1
                            else:
                                return False
                    else:
                        row_index -= 1
                        while row_index >= new_row:
                            if constants.VALID_POSITIONS[row_index][col] == constants.VALID and self.CURRENT_POSITION[row_index][col] == constants.BLANK:
                                return True
                            elif constants.VALID_POSITIONS[row_index][col] == 0 and col != 3:
                                row_index -= 1
                            else:
                                return False

            return False

    def get_valid_moves(self):
        moves = []
        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                if (int(constants.VALID_POSITIONS[r][c]) == constants.VALID) and (
                    int(self.CURRENT_POSITION[r][c]) == constants.BLANK
                ):
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
        # Game is finished when a player loses
        if self.play1_counter <= 2 or not self.can_move(self.turn):
            return constants.PLAY2
        elif self.play2_counter <= 2 or not self.can_move(self.turn):
            return constants.PLAY1
        else:
            return None

    def can_move(self, player):
        # Check if the player can make a move
        for start_row in range(constants.ROWS):
            for start_col in range(constants.COLS):
                if self.CURRENT_POSITION[start_row][start_col] == player:
                    for end_row in range(constants.ROWS):
                        for end_col in range(constants.COLS):
                            if self.is_move_valid(start_row, start_col, end_row, end_col):
                                return True
        return False

    def move_piece(self, start_row, start_col, end_row, end_col, player):
        if self.is_move_valid(start_row, start_col, end_row, end_col):
            self.CURRENT_POSITION[start_row][start_col] = constants.BLANK
            self.CURRENT_POSITION[end_row][end_col] = player
            return True
        return False

    def remove_piece(self, player):
        # Player removes one piece belonging to the opponent that does not form part of a mill
        for row in range(constants.ROWS):
            for col in range(constants.COLS):
                if self.CURRENT_POSITION[row][col] != player and self.CURRENT_POSITION[row][col] != constants.BLANK:
                    if not self.is_part_of_mill(row, col, self.CURRENT_POSITION[row][col]):
                        self.CURRENT_POSITION[row][col] = constants.BLANK
                        return

    def fly_piece(self, start_row, start_col, end_row, end_col, player):
        if self.is_move_valid(start_row, start_col, end_row, end_col):
            self.CURRENT_POSITION[start_row][start_col] = constants.BLANK
            self.CURRENT_POSITION[end_row][end_col] = player
            return True
        return False

    # Update this
    def is_part_of_mill(self, row, col, player):
        for line in constants.LINES:
            if [row, col] in [(int(line[i]), int(line[i + 1])) for i in range(0, len(line), 2)]:
                piece_count = 0
                for i in range(0, len(line), 2):
                    r = int(line[i])
                    c = int(line[i + 1])
                    if self.CURRENT_POSITION[r][c] == player:
                        piece_count += 1
                if piece_count == 3:
                    return True
        return False

    def is_mill(self, row, col):
        col_index = 0
        piece_count = 0
        while col_index <= constants.COLS:
            if constants.VALID_POSITIONS[row][col_index] == constants.VALID and self.CURRENT_POSITION[row][col_index] == self.turn:
                piece_count += 1
            elif constants.VALID_POSITIONS[row][col_index] == 0 and (col < col_index == 3):
                return False
            col_index += 1
            if piece_count == 3:
                return True

        if piece_count == 3:
            return True

        row_index = 0
        piece_count = 0
        while row_index <= constants.ROWS:
            if constants.VALID_POSITIONS[row_index][col] == constants.VALID and self.CURRENT_POSITION[row_index][col] == self.turn:
                piece_count += 1
            elif constants.VALID_POSITIONS[row_index][col] == 0 and (row < row_index == 3):
                return False
            row_index += 1
            if piece_count == 3:
                return True

        if piece_count == 3:
            return True
        return False
