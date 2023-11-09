from GUI import NineMensMorrisGUI
from logic import NineMensMorrisGame
from menu import Menu


if __name__ == '__main__':
    menu = Menu()
    menu.display_menu()
    selected_option = menu.get_selected_option()

    if selected_option == 'human_vs_human':
        game = NineMensMorrisGame()
    elif selected_option == 'human_vs_computer':
        # Initialize game for human vs computer mode
        game = NineMensMorrisGame()  # Replace with your computer player logic

    gui = NineMensMorrisGUI(game)
    gui.main_loop()
