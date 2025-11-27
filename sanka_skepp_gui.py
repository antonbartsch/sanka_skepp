"""Hanterar gui versionen av sänka skepp"""
from tkinter import *
from tkinter import messagebox
from game_functions import *
from board import *

class start_menu(Frame):
    """Hantera gui versionen av startmenyn"""

    def __init__(self, master=None):
        """Initierar ett start_menu objekt"""
        Frame.__init__(self, master)
        self.pack()
        self.generate_menu()

    def generate_menu(self):
        """skapa startmenyn till gui spelet"""
        self.title = Label(self, text="Välkommen till Sänka Skepp")
        self.title.pack()

        self.new_game_button = create_button("Starta nytt spel", self.start_new_game)
        self.new_game_button.pack()

        self.top_list_button = create_button("Topplista", self.show_top_list)
        self.top_list_button.pack()

        self.rules_button = create_button("Regler", self.show_rules)
        self.rules_button.pack()

        self.quit_button = create_button("Avsluta", self.quit_game)
        self.quit_button.pack()

    def start_new_game(self):
        
        gui_board = Gui_board(master=self.master)
        gui_board.create_board(6,7)
        gui_board.generate_ship(5)
    def show_top_list(self):
        top_list = read_top_list()
        messagebox.showinfo("Toplista", format_top_list(top_list))
    def show_rules(self):
        pass  #todo: implementera visa regler funktionalitet
    def quit_game(self):
        self.master.destroy()

class Gui_board(Frame,Board):
    """Hantera gui versionen av spelbrädets utseende och funktionalitet
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
        hit_percentage, victury = self.analyze_hits()
        if victury:
            messagebox.showinfo("Grattis!", "Du har sänkt alla skepp!")
            #todo: victory
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

def format_top_list(top_list):
    """Formatera topplistan så att den kan skrivas ut i en messagebox
    
    Argument:
        toplist (List): lista med toppresultat
        
    Returnerar:
        formatted_list (str): formaterad sträng med topplistan
    """
    formated_list = "Topplista:\n"
    for player_score in top_list:
        formated_list += f"{player_score[1]}: {player_score[0]}%\n"
    return formated_list
            
def create_button(text, command):
    """Skapa knappar snabbt

    Argument:
        text (str): texten på knappen
        command (function): funktion som körs när knappen trycks
    Returnerar:
        button (Button): den skapade knappen
    """
    button = Button(text=text, command=command)
    return button

def main():
    """Huvudfunktion för gui applikationen"""
    root = Tk()
    #board = Gui_board(master=root)
    #root.board = board
    #board.create_board(6,7)
    #board.generate_ship(5)
    #board.generate_ship(3)
    #board.generate_ship(2)
    root.app = start_menu(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()