"""Huvudfil för konsolapplikationen"""
from game_functions import *
from board import *
HEIGHT = 5
WIDTH = 5

def main():
    """ Huvudfunktion för konsolapplikationen"""
    game_running = True
    while game_running:
        choice = start_menu()
        if choice == 1:
            board = Board()
            board.generate_board(HEIGHT, WIDTH)
            positions = load_position_from_file(['position_list1.txt', 'position_list2.txt'])
            for pos in positions:
                board[pos].ship = True
            game_menu(board)
        elif choice == 2:
            print_rules()
        elif choice == 3:
            print("Avslutar spelet. Tack för att du spelade!")
            input("Tryck på Enter för att avsluta...")
            game_running = False

if __name__ == "__main__":
    main()