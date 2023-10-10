from GUI import NineMensMorrisGUI
from logic import NineMensMorrisGame

if __name__ == '__main__':
    game = NineMensMorrisGame()
    gui = NineMensMorrisGUI(game)
    gui.main_loop()
