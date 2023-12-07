import constants
from GUI import NineMensMorrisGUI
from logic import NineMensMorrisGame
from menu import Menu
from SixMenMorrisGame import SixMenMorrisGame
from SixMenMorrisBoard import SixMenMorrisBoard


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
    selected_option = menu.get_selected_option()
    game = None

    if selected_option == constants.H_VS_H:
        game = NineMensMorrisGame()
        game.game_mode = constants.H_VS_H
    elif selected_option == constants.H_VS_C:
        # Initialize game for human vs computer mode
        game = NineMensMorrisGame()  # Replace with your computer player logic
        game.game_mode = constants.H_VS_C
    elif selected_option == constants.SIX_MEN_MORRIS:
        # game = SixMenMorrisGame()
        game = NineMensMorrisGame()

    if game is not None:
        if selected_option == constants.SIX_MEN_MORRIS:
            gui = SixMenMorrisBoard(game)
        else:
            gui = NineMensMorrisGUI(game)
        gui.main_loop()
