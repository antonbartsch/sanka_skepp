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