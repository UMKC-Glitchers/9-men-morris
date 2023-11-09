import os

import constants


class NineMensMorrisGame:
    def __init__(self):
        self.phase = constants.PHASE1
        self.turn = constants.PLAY1
        self.CURRENT_POSITION = constants.CURRENT_POSITION
        self.is_remove_piece = False
        self.counter = 0
        self.play1_pieces = constants.TOTAL_MENS
        self.play2_pieces = constants.TOTAL_MENS
        self.play1_counter = 0
        self.play2_counter = 0
        self.message = constants.PLAYER1_MESSAGE
        self.move_made = ""
        self.over = False
        self.moves_made = []  # TODO - Make it a stack, Will be useful when using undo
        # TODO - Store the moves in a struct to save even the type of move i.e. place, move, remove, fly

    def update_pieces(self):
        if self.turn == constants.PLAY1:
            self.play2_pieces -= 1
        else:
            self.play1_pieces -= 1

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
                self.message = ("Pieces placed, Move pieces now\n" + constants.PLAY1_MOVE_MESSAGE)

        elif self.phase == constants.PHASE2:
            if self.turn == constants.PLAY1:
                self.turn = constants.PLAY2
                self.message = constants.PLAY2_MOVE_MESSAGE
            else:
                self.turn = constants.PLAY1
                self.message = constants.PLAY1_MOVE_MESSAGE
        else:
            self.message = "Invalid phase"

        # check for game over
        if self.is_game_over() is not None:
            self.message = self.get_player_from_const(self.is_game_over()) + " Wins the game!!"
            self.over = True

    def get_turn(self):
        return self.turn

    def get_opp(self):
        if self.turn == constants.PLAY1:
            return constants.PLAY2
        return constants.PLAY1

    def set_phase(self, phase):
        self.phase = phase

    def get_player_from_const(self, player):
        if player == constants.PLAY1:
            return "Player 1"
        return "Player 2"

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
                print("Is mill:", self.is_mill(row, col, self.get_turn()))

                if self.is_mill(row, col, self.get_turn()):
                    self.message = "Remove a piece from opponent"
                    self.is_remove_piece = True
                    return

                self.change_turn()
            elif self.phase == constants.PHASE2:
                self.move_piece(row, col, new_row, new_col, self.get_turn())
                print("Is mill:", self.is_mill(new_row, new_col, self.get_turn()))

                if self.is_mill(new_row, new_col, self.get_turn()):
                    self.message = "Remove a piece from opponent"
                    self.is_remove_piece = True
                    return
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
                            if constants.VALID_POSITIONS[row][col_index] == constants.VALID and self.CURRENT_POSITION[row][col_index] == constants.BLANK and col_index == new_col:
                                return True
                            elif constants.VALID_POSITIONS[row][col_index] == 0 and row != 3:
                                col_index += 1
                            else:
                                return False
                    else:
                        col_index -= 1
                        while col_index >= new_col:
                            if constants.VALID_POSITIONS[row][col_index] == constants.VALID and self.CURRENT_POSITION[row][col_index] == constants.BLANK and col_index == new_col:
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
                            if constants.VALID_POSITIONS[row_index][col] == constants.VALID and self.CURRENT_POSITION[row_index][col] == constants.BLANK and row_index == new_row:
                                return True
                            elif constants.VALID_POSITIONS[row_index][col] == 0 and col != 3:
                                row_index += 1
                            else:
                                return False
                    else:
                        row_index -= 1
                        while row_index >= new_row:
                            if constants.VALID_POSITIONS[row_index][col] == constants.VALID and self.CURRENT_POSITION[row_index][col] == constants.BLANK and row_index == new_row:
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
        if self.play1_pieces <= 2:
            return constants.PLAY2
        elif self.play2_pieces <= 2:
            return constants.PLAY1
        else:
            return None

    # def can_move(self, player):
    #     # Check if the player can make a move
    #     for start_row in range(constants.ROWS):
    #         for start_col in range(constants.COLS):
    #             if self.CURRENT_POSITION[start_row][start_col] == player:
    #                 for end_row in range(constants.ROWS):
    #                     for end_col in range(constants.COLS):
    #                         if self.is_move_valid(start_row, start_col, end_row, end_col):
    #                             return True
    #     return False

    def move_piece(self, start_row, start_col, end_row, end_col, player):
        if self.is_move_valid(start_row, start_col, end_row, end_col):
            self.CURRENT_POSITION[start_row][start_col] = constants.BLANK
            self.CURRENT_POSITION[end_row][end_col] = player
            return True
        return False

    # Fixme - Player can remove from a mill if no other pieces are available
    def remove_piece(self, row, col, player):
        if self.CURRENT_POSITION[row][col] != player and self.CURRENT_POSITION[row][col] != constants.BLANK:
            if not self.is_mill(row, col, self.CURRENT_POSITION[row][col]):
                self.CURRENT_POSITION[row][col] = constants.BLANK
                self.update_pieces()
                self.change_turn()
                return True
            if self.is_mill(row, col, self.CURRENT_POSITION[row][col]) and not self.has_free_pieces():
                self.CURRENT_POSITION[row][col] = constants.BLANK
                self.update_pieces()
                self.change_turn()
                return True

    def fly_piece(self, start_row, start_col, end_row, end_col, player):
        if self.is_move_valid(start_row, start_col, end_row, end_col):
            self.CURRENT_POSITION[start_row][start_col] = constants.BLANK
            self.CURRENT_POSITION[end_row][end_col] = player
            return True
        return False

    def is_mill(self, row, col, player):
        col_index = 0
        row_index = 0
        piece_count = 0

        if row == 3:
            if col > 3:
                col_index = 4
        if col == 3:
            if row > 3:
                row_index = 4

        while col_index < constants.COLS:
            if constants.VALID_POSITIONS[row][col_index] == constants.VALID and self.CURRENT_POSITION[row][col_index] == player:
                piece_count += 1
            elif constants.VALID_POSITIONS[row][col_index] == constants.VALID and constants.VALID_POSITIONS[row][col_index] != player:
                piece_count = 0
            if row == 3 and col_index == 3:
                break
            col_index += 1
            if piece_count == 3:
                return True

        if piece_count == 3:
            return True

        piece_count = 0
        while row_index < constants.ROWS:
            if constants.VALID_POSITIONS[row_index][col] == constants.VALID and self.CURRENT_POSITION[row_index][col] == player:
                piece_count += 1
            elif constants.VALID_POSITIONS[row_index][col] == constants.VALID and constants.VALID_POSITIONS[row_index][col] != player:
                piece_count = 0
            if row_index == 3 and col == 3:
                return False
            row_index += 1
            if piece_count == 3:
                return True

        if piece_count == 3:
            return True
        return False

    def has_free_pieces(self):
        for r in range(constants.ROWS):
            for c in range(constants.COLS):
                if self.CURRENT_POSITION[r][c] == self.get_opp() and not self.is_mill_at_position(r, c):
                    return True  # Found a free piece belonging to the player
        return False

    def is_mill_at_position(self, row, col):
        player = self.CURRENT_POSITION[row][col]
        if player == constants.BLANK:
            return False  # No mill possible if the position is empty

        # Check horizontal and vertical lines
        if self.check_line(row, col, 0, 1, player) or self.check_line(row, col, 1, 0, player):
            return True

        # Check diagonal lines
        if self.check_line(row, col, 1, 1, player) or self.check_line(row, col, 1, -1, player):
            return True

        return False

    def check_line(self, row, col, dr, dc, player):
        for i in range(1, 3):  # Check up to 2 positions in the line
            r, c = row + i * dr, col + i * dc
            if 0 <= r < constants.ROWS and 0 <= c < constants.COLS and self.CURRENT_POSITION[r][c] != player:
                return False  # The line is not valid if there is an opponent's piece
            elif 0 <= r < constants.ROWS and 0 <= c < constants.COLS and self.CURRENT_POSITION[r][c] == constants.BLANK:
                return False  # The line is not valid if there is a blank space
        return True  # The line is valid (contains only player's pieces)
