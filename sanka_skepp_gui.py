"""Hanterar gui versionen av sänka skepp"""
from tkinter import *
from tkinter import messagebox
from game_functions import *
from board import *

class Gui_board(Frame,Board):
    """Hanterar gui versionen av spelbrädets utseende och funktionalitet
    Ärver från Frame och Board klasserna
    """
    def __init__(self, master=None):
        """Initierar ett Gui_board objekt"""
        Frame.__init__(self)
        Board.__init__(self)
        self.grid()
    
    def __getitem__(self, key):
        """Skickar __getitem__ till rätt klass (Bord eller Frame) beroende på key typen
        
        Argument:
            key (str/tuple): tuple hör till Board klassen, str hör till Frame klassen
        """
        if isinstance(key, tuple):
            return Board.__getitem__(self, key)
        else:
            return Frame.__getitem__(self, key)

    
    def create_board(self, HEIGHT, WIDTH):
        """Skapar spelbrädet i gui fönstret lik generate_board men med knappar

        Argument:
            height (int): höjden på brädet
            width (int): bredden på brädet
        """
        for row_index in range (HEIGHT):
            row = []
            for square_index in range (WIDTH):
                square = Button_square(master=self)
                square.grid(row=row_index, column=square_index)
                row.append(square)
            self.squares.append(row)

    def update_board(self):
        """Uppdaterar alla knappar på spelbrädet"""
        self.analyze_hits()
        for row in self.squares:
            for square in row:
                square.update_button()
        


class Button_square(Button, Square):
    """Hanterar gui versionen av varje ruta på spelbrädet
    Ärver från Button och Square klasserna
    """
    def __init__(self, master = None):
        """Initierar Button_square klassen"""
        Button.__init__(self, master=master, width=2, height=2, bg='lightblue')
        Square.__init__(self,)
        self.grid()
        self.config(command=self.on_click)

    def on_click(self):
        """Hanterar klick på knappen och markerar rutan som träff eller miss"""
        if not self.hit:
            self.master.fired_shots += 1
            self.hit = True
            if self.ship:
                self.config(bg='red')
                messagebox.showinfo("Träff!", "Du träffade ett skepp!")
            else:
                self.config(bg='blue')
                messagebox.showinfo("Miss!", "Du missade!")
            self.master.update_board()
    
    def update_button(self):
        """Uppdaterar knappens utseende baserat på des status"""
        if self.ship and self.hit:
            self.config(bg='red') # träffat skepp
        elif self.ship and not self.hidden:
            self.config(bg='grey') # synligt obeskjutet skepp
        elif self.ship and self.hidden:
            self.config(bg='lightblue') # dolt obeskjutet skepp
        elif not self.ship and self.hit:
            self.config(bg='darkblue')  #träff på tomm ruta
        else:
            self.config(bg='lightblue') #obeskjuten tom ruta
            

def main():
    """Huvudfunktion för gui applikationen"""
    root = Tk()
    gui_board = Gui_board(root)
    gui_board.create_board(6,7)
    gui_board.generate_ship(5)
    gui_board.generate_ship(3)
    gui_board.generate_ship(2)
    gui_board.hide_ships()
    root.mainloop()

if __name__ == "__main__":
    main()