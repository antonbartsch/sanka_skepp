""" Modul som hanterar de logiska funktionerna i spelet"""
import random

def safe_input(input):
    #todo: skapa safe_input funktion
    return input
def coordinate_input():
    #todo: skapa coordinate_input funktion
    return input
def victory(hit_percentage):
    #todo: skapa victory funktion
    print("Grattis! Du har vunnit spelet!")

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
    """ Visa startmenyn och dirigera användaren till vald funktion """
    game_running = True
    while game_running:
        print("=== VÄLKOMMEN TILL SÄNKA SKEPP ===")
        print("1. Starta nytt spel")
        print("2. Regler")
        print("3. Avsluta")
        #todo: implementera motagning av användarval

def game_menu():
    """ Visa spelmenyn och dirigera användaren till vald funktion """
    game_running = True
    while game_running:
        print("--- MENY ---")
        print("1. Beskjut skepp")
        print("2. Tjuvkika på spelplanen")
        print("3. Avsluta spelet")
        choice = safe_input()
        if choice == '1':
            print("Beskjuter skepp...")
            #todo: implementera beskjutningsfunktion
        elif choice == '2':
            print("Tjuvkikar på spelplanen...")
            #todo: implementera tjuvkikningsfunktion
        elif choice == '3':
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
    shoot_menu_active = True
    while shoot_menu_active:
        print("### SPELPLAN ###")
        print(board)
        print('Ange koordinater för beskjutning "x,y:":')
        matrix_position = coordinate_input()
        if validate_shot_input(matrix_position, board):
            board[matrix_position].hit = True
            victory, hitpercentage = board.analyze_hits()
            if victory:
                victory(hitpercentage)
            if board[matrix_position].ship:
                print("Träff!")
            else:
                print("Miss!")
            print(f"träffsäkerhet: {hitpercentage}%")
        else:
            print("Ogiltig inmatning, rutan är redan träffad eller utanför spelplanen")
        print("Vill du skjuta igen? (j/n):")
        user_choice = safe_input()
        if user_choice != 'j':
            shoot_menu_active = False


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


if __name__ == "__main__":
    test()