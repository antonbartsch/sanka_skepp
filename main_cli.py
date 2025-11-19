"""Huvudfil för konsolapplikationen"""
from game_functions import *
from board import *
HEIGHT = 6
WIDTH = 7

def main():
    """ Huvudfunktion för konsolapplikationen"""
    game_running = True
    while game_running:
        choice = start_menu()
        if choice == 1:
            board = Board()
            board.generate_board(HEIGHT, WIDTH)
            board.generate_ship(2, board)
            board.generate_ship(3, board)
            game_menu(board)
        elif choice == 2:
            print_rules()
        elif choice == 3:
            print("Avslutar spelet. Tack för att du spelade!")
            input("Tryck på Enter för att avsluta...")
            game_running = False

if __name__ == "__main__":
    main()