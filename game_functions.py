""" Modul som hanterar de logiska funktionerna i spelet"""
import random

def safe_input(user_input, type, max_value=None):
    """ Hantera inmatning av korrekt typ och format
    Argument:
        input (str): användarens inmatning
        type (type): förväntad typ av inmatning
        max_value (int): högsta tillåtna värde för heltal (behövs endast för int)

    Returnerar:
        input (type): den validerade inmatningen av förväntad typ
    """
    while True:
        if type == int:
            try:
                return int(user_input)
            except ValueError:
                print(f"input måste vara ett heltal mellan 1 och {max_value} ")
        elif type == str:
            user_input = user_input.lower()
            if len(user_input) == 1 and (user_input == 'j' or user_input == 'n'):
                return user_input
            else: 
                print("input måste vara 'j' eller 'n'")
        user_input = input("Försök igen:")


def coordinate_input():
    """ Hantera användarinmatning av koordinater 

    Argument:
        input (str): användarens inmatning i formatet "x,y"
    returns:
        matrix_position (tuple): positionen som matrisindex (rad, kolumn)
    """
    while True:
        try:

            x_str, y_str = input().split(',')
            x = int(x_str) -1
            y = int(y_str) -1
            return (y, x) # Returnerar som matrisposition (rad, kolumn)
        except (ValueError, IndexError):
            print("Ogiltig inmatning. Ange koordinater i formatet x,y där x och y är heltal.")
            print('Försök igen: ', end='')

def victory(hit_percentage):
    #todo: skapa victory funktion
    print(f"Grattis! Du har vunnit spelet! träffprocent: {hit_percentage}%")

def load_position_from_file(file_list):
    """ Ladda skeppspositioner från en fil

    Argument:
        file_list (List): lista med filnamn att välja från

    Returnerar:
        positions_list (List): Lista med skeppspositioner
    """
    filename = random.choice(file_list)
    positions_list = []
    with open (filename, 'r') as file:
        for line in file:
            x, y = line.strip().split(',')
            positions_list.append((int(x), int(y)))
    return positions_list

def start_menu():
    """ Visa startmenyn och returnera användarens val 
    
    Returnerar:
        choice (int): användarens val från menyn
    """
    print("=== VÄLKOMMEN TILL SÄNKA SKEPP ===")
    print("1. Starta nytt spel")
    print("2. Regler")
    print("3. Avsluta")
    choice = safe_input(input("Välj ett alternativ (1-3): "), int, 3)
    return choice

def game_menu(board):
    """ Visa spelmenyn och dirigera användaren till vald funktion """
    game_running = True
    while game_running:
        print("--- MENY ---")
        print("1. Beskjut skepp")
        print("2. Tjuvkika på spelplanen")
        print("3. Avsluta till huvudmenyn")
        choice = safe_input(input("Välj ett alternativ (1-3): "), int, 3)
        if choice == 1:
            print("Beskjuter skepp...")
            game_running = shoot(board)
        elif choice == 2:
            print("Tjuvkikar på spelplanen...")
            view_board(board)
        elif choice == 3:
            print("Avslutar spelet...")
            game_running = False

def validate_shot_input(shot_input, board):
    """ Validera användarens inmatning för beskjutning

    Argument:
        shot_input (tuple): användarens inmatning som sammansatt (rad, kolumn)
        board (Board): spelplanen för att kontrollera giltigt skott

    Returnerar:
        valid(bool): True om inmatningen är giltig
    """
    try:
        return not board[shot_input].hit
    except IndexError:
        return False

def shoot(board):
    """ Hantera beskjutning av spelplanen

    Argument:
        board (Board): spelplanen som ska beskjutas
    """
    board.hide_ships()
    shoot_menu_active = True
    while shoot_menu_active:
        print("### SPELPLAN ###")
        print(board)
        print('Ange koordinater för beskjutning "x,y:":', end='')
        matrix_position = coordinate_input()
        if validate_shot_input(matrix_position, board):
            board[matrix_position].hit = True
            hit_percentage, is_victory = board.analyze_hits()
            if is_victory:
                victory(hit_percentage)
                return False
            if board[matrix_position].ship:
                print("Träff!")
            else:
                print("Miss!")
            print(f"träffsäkerhet: {hit_percentage}%")
        else:
            print("Ogiltig inmatning, rutan är redan träffad eller utanför spelplanen")
        print("Vill du skjuta igen? (j/n):")
        user_choice = safe_input(input(), str)
        if user_choice != 'j':
            shoot_menu_active = False
    return True

def view_board(board):
    """ Visa spelplanen för tjuvkikning

    Argument:
        board (Board): spelplanen som ska visas
    """
    board.show_ships()
    print("### SPELPLAN ###")
    print(board)
    input("Tryck på Enter för att återgå till menyn...")

def print_rules():
    #todo: skapa print_rules funktion
    return print("regler:")

def test():
    """ Testfunktion för game_functions"""
    file_list = ['position_list1.txt', 'position_list2.txt']
    positions = load_position_from_file(file_list)
    print("Loaded positions:", positions)

    from board import Board, Square
    board = Board()
    board.generate_board(5, 5)
    for pos in positions:
        board[pos].ship = True
    print(board)
    game_menu(board)


if __name__ == "__main__":
    test()