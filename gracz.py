import pygame
from pygame.math import Vector2

# ustawienia ekranu
WIDTH, HEIGHT = 610, 670
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER

# ustawienia kolorów
BLACK = (0, 0, 0)
RED = (208, 22, 22)
GREY = (107, 107, 107)
WHITE = (255,255,255)
PLAYER_COLOUR = (190,194,15)
# ustawienia czcionki
START_TEXT_SIZE = 16
START_FONT = 'arial black'
# ustawienia związane z graczem
PLAYER_START_POS = 0

# avatar którego nie umiem jeszcze umieścić zamiast zółtej kropki
image= pygame.image.load('start.png')

class Gracz:
    def __init__(self, gra, pos):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.gra = gra
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.kierunek = Vector2(1,0)
        self.biezacy_kierunek = None
        self.ma_mozliwosc_ruchu = True
        self.predkosc=2

    def update(self):
        if self.ma_mozliwosc_ruchu:
            self.pix_pos += self.kierunek*self.predkosc
        if self.czas_na_ruch():
            if self.biezacy_kierunek != None:
                self.kierunek = self.biezacy_kierunek
            self.ma_mozliwosc_ruchu = self.moze_ruszyc()

# pozycjonowanie troche skomplikowane średnio ogarniam więc jeżeli macie pomysły jak to ułatwić to będe wdzięczna

        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.gra.cell_width//2)//self.gra.cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.gra.cell_height//2)//self.gra.cell_height+1

    def draw(self):
# żółte kółko ;-;
        pygame.draw.circle(self.gra.screen, PLAYER_COLOUR, (int(self.pix_pos.x),  int(self.pix_pos.y)), self.gra.cell_width//2-2)



# pozycjonowanie znowu

    def get_pix_pos(self):
        return Vector2((self.grid_pos.x*self.gra.cell_width)+TOP_BOTTOM_BUFFER//2+self.gra.cell_width//2, (self.grid_pos.y*self.gra.cell_height)+ TOP_BOTTOM_BUFFER//2+self.gra.cell_height//2)
        print(self.grid_pos, self.pix_pos)

#ruszanie się

    def ruch(self, kierunek):
        self.biezacy_kierunek = kierunek

    def czas_na_ruch(self):
        if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.gra.cell_width == 0:
            if self.kierunek == Vector2(1,0) or self.kierunek == Vector2(-1,0) or self.kierunek == Vector2(0, 0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.gra.cell_height == 0:
            if self.kierunek == Vector2(0,1) or self.kierunek == Vector2(0,-1) or self.kierunek == Vector2(0, 0):
                return True
        return False

    def moze_ruszyc(self):
        for sciana in self.gra.sciany:
            if Vector2(self.grid_pos+self.kierunek)== sciana:
                return False
        return True
