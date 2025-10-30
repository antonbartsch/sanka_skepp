Projektuppgift i programeringsteknik DD1310
Sänka skepp
Det här programet låter en spelare spela sänka skepp mot ett randomiserat spelbräde. Spelarens träffsäkerhet sparas och anges som resultat.
###Algoritm###
1.Spelaren startar programmet
2.En spelplan läses in med slumpmässig placering av skeppen utifrån fil
3. Användaren möts av en meny med alternativen
    #BESKJUT FIENDEFARTYG
        1.En tabell som visar rutorna i ett kordinatsystem och vilka rutor som är (beskjutna träffar/tomma ser olika ut) skrivs ut
        2.Frågar användaren om den vill skjuta eller återvända till menyn
        3.Användaren anger vilken kordinat han vill skjuta på
        4.Programet kontrollerar att den beskjutna rutan ligger i spelplanen och att den inte redan är beskjuten. 
        5.Programmet registrerar rutan som träffad
        6.Programmet jämför antalet träffade rutor som inehåller skepp med totala antalet träffade rutor och printar ut en träffprocent. Om alla skepp är träffade anroppas victory()
        7.Loopa från (1)
        8.Vid victory() anges träffprocenten och användaren tillåts avsluta programmet eller så returneras break så att spelet återvänder till main loopen. 
    #TJUVKIKA PÅ SPELPLAN(FUSK)
        1.En tabell som visar rutorna i ett kordinatsystem och vilka rutor som inehåller skepp skrivs ut
        2.Låter användaren återvända till menyn.
    #AVSLUTA
        1.Avslutar programmet.

###Datastrukturer###
klass Square()
    Attribut:
        self.ship(bool)
        self.hit(bool)
        self.hidden(bool)
    Funktioner:
        __str__(self)
            if self.ship and self.hit
                return X
            elif self.ship and self.hidden
                return " "
            elif self.hit
                return O
            else return " "
        set/get(ship/hit/hidden)
            sätter och hämtar bool-värden

klass Board()
    Atribut:
        HEIGHT
        WIDTH
        squares = []
    Funktioner: 
        generate_board
            skapar en 2D-lista som innehåller squares
        analyze_hits
            kollar statusen på alla rutor i brädet och returnerar en träffprocent=float och en victory = bool
        place_ships(self, amount, max_size,)
            Placerar ut ett skepp itaget i en loop kontrollerar så att skeppet inte placeras på en ruta där det redan finns ett skepp
        clear_board
            sätter alla värden i alla rutor till false
        hide_ships
            sätter alla ships som gömmda
        un_hide_ships

