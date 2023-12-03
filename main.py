import constants
from GUI import NineMensMorrisGUI
from logic import NineMensMorrisGame
from menu import Menu


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

    if game is not None:
        gui = NineMensMorrisGUI(game)
        gui.main_loop()
