Projektuppgift i programmeringsteknik DD1310
Sänka skepp

Det här programmet låter en spelare spela sänka skepp mot ett randomiserat spelbräde.
Spelarens träffsäkerhet sparas och anges som resultat.

🧮 Algoritm

Spelaren startar programmet

En spelplan läses in med slumpmässig placering av skeppen utifrån fil

Användaren möts av en meny med alternativen:

BESKJUT FIENDEFARTYG

En tabell som visar rutorna i ett koordinatsystem och vilka rutor som är (beskjutna träffar/tomma ser olika ut) skrivs ut

Frågar användaren om den vill skjuta eller återvända till menyn

Användaren anger vilken koordinat hen vill skjuta på

Programmet kontrollerar att den beskjutna rutan ligger i spelplanen och att den inte redan är beskjuten

Programmet registrerar rutan som träffad

Programmet jämför antalet träffade rutor som innehåller skepp med totala antalet träffade rutor och printar ut en träffprocent.
Om alla skepp är träffade anroppas victory()

Loopa från (1)

Vid victory() anges träffprocenten och användaren tillåts avsluta programmet eller så returneras break så att spelet återvänder till main-loopen.

TJUVKIKA PÅ SPELPLAN (FUSK)

En tabell som visar rutorna i ett koordinatsystem och vilka rutor som innehåller skepp skrivs ut

Låter användaren återvända till menyn

AVSLUTA

Avslutar programmet

💾 Datastrukturer

Varje ruta i programmet kommer att vara objekt av en klass Square.
Square kommer hålla koll på om rutan innehåller ett skepp och om spelaren har skjutit på den.
Rutorna kommer sedan att ingå i en spelplan av klassen Board där de lagras i en 2D-matris.

🧱 Klasser
klass Square()

Attribut:

self.ship (bool)

self.hit (bool)

self.hidden (bool)

Funktioner:

__str__(self):
    if self.ship and self.hit:
        return "X"
    elif self.ship and not self.hidden:
        return "#"
    elif self.ship and self.hidden:
        return " "
    elif self.hit:
        return "O"
    else:
        return " "


set/get(ship/hit/hidden) – sätter och hämtar bool-värden

klass Board()

Attribut:

HEIGHT

WIDTH

squares = []

Funktioner:

generate_board()

Skapar en 2D-lista som innehåller Square-objekt

analyze_hits()

Kollar statusen på alla rutor i brädet och returnerar en träffprocent (float) och en victory-flagga (bool)

place_ship(self, ship_size, origin)

Placerar ut ett skepp av storleken ship_size som utgår ifrån origin och breder ut sig åt vänster.
Returnerar success (bool)

clear_board()

Sätter alla värden i alla rutor till False

hide_ships()

Sätter alla skepp som gömda

un_hide_ships()

Avmarkerar alla skepp som gömda

__str__()

Ger en strängrepresentation av hela spelplanen

⚙️ Funktioner
pick_random_file()

Väljer en slumpmässig fil för positioner på skeppen

load_possitions_from_fromfile("exempelfil")

Läser in positioner från filen och returnerar en lista ship_cordinate_list med koordinater

for every coordinate in ship_cordinate_list:
    board.place_ship(coordinate)

game_menue()

Presenterar användaren med en meny och skickar användaren till respektive funktion.
Loopar under spelets gång.

shoot()
hide_ships()
while True:
    print(board)
    välj koordinat
    kontrollera giltigt skott
    registrera skott
    fortsätt skjuta eller återvänd?

sneak_peak()
show_ships()
print(board)
tryck enter för att återvända

victory()
print("Grattis du vann!")
print(träffprocent)
vill du generera ett nytt spel eller avsluta?