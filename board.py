""" modul som hanterar klasserna Square och Board """
import random

class Square:
    """ representerar en ruta på spelplanen
    
    Atribut:
    ship (bool): True om rutan innehåller ett skepp
    hit (bool): True om rutan har beskjutits
    hidden (bool): True om rutan är dold för spelaren
    """

    def __init__ (self):
        """ initiera en ruta med standardvärden"""
        self.ship = False
        self.hit = False
        self.hidden = False

    def __str__(self):
        """ returnera en strängrepresentation av rutan baserat på dess tillstånd """
        if self.ship and self.hit:
            return "¤" # träff på skepp
        elif self.ship and not self.hidden:
            return "=" # synligt obeskjutet skepp
        elif self.ship and self.hidden:
            return " " # dolt obeskjutet skepp
        elif not self.ship and self.hit:
            return "O" #träff på tomm ruta
        else:
            return " " #obeskjuten tom ruta
        
class Board:
    """ representerar spelplanen

    Atribut:
    squares (list): 2D-lista av Square-objekt som representerar spelplanen
    """
    def __init__ (self):
        """ initiera spelplanen"""
        self.squares = []

    def __getitem__ (self, index):
        """ hämta värdet från angiven ruta på spelplanen

        Argument:
            index (tuple): ett sammansatt värde med rad och kolumn för rutan
        Returnerar:
            Square: rutan på angiven position
        """
        row, col = index
        return self.squares[row][col]
    
    def generate_board (self, HEIGHT, WIDTH):
        """ generera en 2D-lista av Square-objekt baserat på angivna dimensioner 
        
        Argument:
            HEIGHT (int): höjden på spelplanen
            WIDTH (int): bredden på spelplanen
        """
        for row in range (HEIGHT):
            row = []
            for square in range (WIDTH):
                square = Square()
                row.append(square)
            self.squares.append(row)

    def analyze_hits (self):
        """
        analysera träffar på spelplanen och returnera träffprocent och om speler är vunnet

        Returnerar:
            hit_percentage (float): procentandel träffar på skepp
            victory (bool): True om alla skepp är träffade annars False
        """
        total_ship_squares = 0
        total_hit_ship_squares = 0
        total_hit_squares = 0

        for row in self.squares:
            for square in row:
                if square.ship:
                    total_ship_squares += 1
                    if square.hit:
                        total_hit_ship_squares += 1
                if square.hit:
                    total_hit_squares += 1
        
        if total_ship_squares == 0:
            hit_percentage = 0.0
        else:
            hit_percentage = total_hit_ship_squares / total_hit_squares*100
            hit_percentage=round(hit_percentage, 2)
        if total_hit_ship_squares == total_ship_squares:
            is_victory = True
        else:
            is_victory = False
        return hit_percentage, is_victory
    
    def clear_board(self):
        """ Återställ värdena på brädet"""
        for row in self.squares:
            for square in row:
                square.ship = False
                square.hit = False
                square.hidden = False

    def hide_ships(self):
        """Göm alla skepp"""
        for row in self.squares:
            for square in row:
                square.hidden = True

    def show_ships(self):
        """Visa alla skepp"""
        for row in self.squares:
            for square in row:
                square.hidden = False

    def __str__(self):
        """ returnera en strängrepresentation av spelplanen 
        
        Returnerar:
            board_str (str): strängrepresentation av spelplanen
        """
        board_str = ""
        board_str += self.string_top_rows()
        for row in self.squares:
            board_str +="——"*(len(self.squares[0])+2)+"\n"
            board_str += f"|{self.squares.index(row)+1}|#|"
            for square in row:
                board_str += str(square)+"|"
            board_str += "\n"
        board_str +="——"*(len(self.squares[0])+2)+"\n"
        return board_str
    
    def string_top_rows(self):
        """ returnera en strängrepresentation av de två översta raderna som kordinatsystemet
        
        Returnerar:
            top_rows_str (str): strängrepresentation av de två översta raderna
        """
        top_row_str =""
        for col in range(len(self.squares[0])+2):
            top_row_str +="__"
        top_row_str +="\n| |X|"
        for col in range(len(self.squares[0])):
            top_row_str += str(col+1)+"|"
        top_row_str +="\n|Y|"
        for col in range(len(self.squares[0])+1):
            top_row_str +="#|"
        top_row_str +="\n"
        return top_row_str

    def test_square_values(self):
        """ testfunktion för att skriva ut olika attributvärden för varje ruta på spelplanen """
        for row in self.squares:
            for square in row:
                square.ship=True
                square.hit=True
                square.hidden=False
        print(self)
        for row in self.squares:
            for square in row:
                square.ship=False
                square.hit=True
                square.hidden=False
        print(self)
        for row in self.squares:
            for square in row:
                square.ship=True
                square.hit=False
                square.hidden=False
        print(self)

class Ship:
    """ Representerar ett skepp på spelplanen

    Atribut:
    size (int): Storleken på skeppet
    rotation (str): Riktningen på skeppet, 'H' för horisontell, 'V' för vertikal
    ship_squares (list): Lista med kordinater för rutorna som skeppet ligger på
    """
    def __init__(self):
        """ initiera ett tomt skepp"""
        #self.size = None
        #self.rotation = None
        self.ship_squares = []
        self.ship_blocked_squares = []

    def is_sunk(self, board):
        """ kontrolera om skeppet är sänkt

        Argument:
            board (Board): spelplanen där skeppet finns
        """
        ship_sunk = True
        for square in self.ship_squares:
            if not board[square].hit:
                ship_sunk = False
        if ship_sunk:
            for square in self.ship_squares:
                try:
                    board[square].hit = True
                except IndexError:
                    pass

    def generate_ship(self, size, board):
        """ generera ett skepp baserat på storlek

        Argument:
            size (int): storleken på skeppet
        """
        start_x = random.randint(0, len(board.squares[0])-1) #-1 för att index börjar på 0
        start_y = random.randint(0, len(board.squares)-1)
        rotation = random.choice(['H', 'V'])
        self.ship_squares =[(start_x, start_y)]
        if rotation == 'H':
            for i in range(1, size):
                self.ship_squares.append((start_x + i, start_y))
        elif rotation == 'V':
            for i in range(1, size):
                self.ship_squares.append((start_x, start_y + i))


            
def test():
    """ testfunktion för att skapa och skriva ut en spelplan """
    board = Board()
    board.generate_board(5, 5)
    print(board)
    board[1,1].ship = True
    board[1,1].hit = True
    board[1,2].ship = True
    board[1,2].hit = True
    board[4,1].ship = True
    board[4,1].hit = True
    board[2,0].ship = True
    board[2,0].hit = True
    board[2,1].hit = True
    board[3,4].ship = True
    print(board)
    hit_percentage, victory = board.analyze_hits()
    print(f"Hit percentage: {hit_percentage}%")
    print(f"Victory: {victory}")
    board.hide_ships()
    print(board)
    board.show_ships()
    print(board)
    board.clear_board()
    print(board)
if __name__ == "__main__":
    test()
