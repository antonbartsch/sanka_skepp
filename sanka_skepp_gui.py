"""Hanterar gui versionen av sänka skepp"""
from tkinter import *
from tkinter import messagebox
from game_functions import *
from board import *

HEIGHT = 6
WIDTH = 7
SHIPS = [5, 3, 2]

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

    
    def generate_menu(self, HEIGHT):
        """skapa menyknapparna till spelet
        
        Argument:
            HEIGHT (int): höjden på spelbrädet för att placera knapparna rätt
        """
        self.new_game_button = create_button("Restart Game", self.start_new_game, (HEIGHT+1, 0))
        self.top_list_button = create_button("Topplista", self.show_top_list, (HEIGHT+2, 0))
        self.rules_button = create_button("Växla synliga skepp", self.toggle_hidden_ships, (HEIGHT+3, 0))
        self.quit_button = create_button("Avsluta", self.quit_game, (HEIGHT+4, 0))

    def start_new_game(self):
        """starta ett nytt spel genom att återställa brädet och skapa nya skepp"""
        self.clear_board()
        for ship_size in SHIPS:
            self.generate_ship(ship_size)
        self.hide_ships()
        self.update_board()

    def show_top_list(self):
        """Visa topplistan i en messagebox"""
        top_list = read_top_list()
        messagebox.showinfo("Toplista", format_top_list(top_list))

    def toggle_hidden_ships(self):
        """växla mellan att visa och dölja skeppen på brädet"""
        for row in self.squares:
            for square in row:
                square.hidden = not square.hidden
        self.update_board()

    def quit_game(self):
        """Avsluta spelet och stäng fönstret"""
        self.master.destroy()

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

class Victory_popup(Toplevel):
    """Hantera popup fönstret för vinnst"""
    def __init__(self, master=None, hit_percentage=0):
        """initierar Highscore_popup"""
        Toplevel.__init__(self, master=master)
        generate_widgets(self)
        self.hit_percentage = hit_percentage
    
    def generate_widgets(self):
        """Skapa widgets i popup fönstret"""
        self.title("Grattis! Du vann!")
        self.label = Label(self, text=f"Du sänkte alla skepp med en träffsäkerhet på {self.hit_percentage}%!")
        if self.compare_score() and self.compare_score() <=10:
            self.name_label = Label(self, text=f"Du kom på plats {self.compare_score()} topplistan! Skriv in ditt namn:")
            self.name_entry = Entry(self)
            self.submit_button = Button(self, text="Skicka", command=self.submit_name)
            self.name_label.pack()
            self.name_entry.pack()
            self.submit_button.pack()
    
    def compare_score(self):
        """Jämför spelarens poäng med topplistan och hanterar inmatning av namn om nödvändigt
        
        Returnerar:
            placering (int): spelarens placering på topplistan, eller None om inte placerad
        """

        top_list =read_top_list()
        if len(top_list) == 0:
            return 1
        else:
            i=0
            for player_score in top_list:
                i+=1
                if self.hit_percentage > player_score[0]:
                    return i
            if len(top_list) <10:
                return i+1
        return None
    
    def submit_name(self):
        """Hantera inmatning av namn och spara poängen"""
        name = self.name_entry.get()

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
            
def create_button(text, command, grid_pos=None):
    """Skapa knappar snabbt

    Argument:
        text (str): texten på knappen
        command (function): funktion som körs när knappen trycks
        grid_pos (tuple): positionen i grid layouten (row, column)
    Returnerar:
        button (Button): den skapade knappen
    """
    button = Button(text=text, command=command)
    if grid_pos:
        button.grid(row=grid_pos[0], column=grid_pos[1])
    return button

def main():
    """Huvudfunktion för gui applikationen"""
    root = Tk()
    board = Gui_board(master=root)
    root.board = board
    board.create_board(6,7)
    board.generate_menu(6)
    board.generate_ship(5)
    board.generate_ship(3)
    board.generate_ship(2)
    board.hide_ships()
    #root.app = start_menu(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()