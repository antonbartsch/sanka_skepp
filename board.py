""" modul som hanterar klasserna Square och Board """

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
            hit_percentage = total_hit_ship_squares / total_ship_squares*100
        if total_hit_ship_squares == total_ship_squares:
            victory = True
        else:
            victory = False
        return hit_percentage, victory

    def __str__(self):
        """ returnera en strängrepresentation av spelplanen 
        
        Returnerar:
            board_str (str): strängrepresentation av spelplanen
        """
        board_str = ""
        for row in self.squares:
            for square in row:
                board_str += str(square)
            board_str += "\n"
        return board_str
    
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
    board[2,1].hit = True
    board[3,4].ship = True
    print(board)
if __name__ == "__main__":
    test()
