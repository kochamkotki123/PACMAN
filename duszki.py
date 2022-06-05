import pygame
from pygame.math import Vector2 as vec
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
vec = pygame.math.Vector2

# cała klasa duszków, ich ilość, pozycje
class Ghost:
    def __init__(self, app, pos, number):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = int(self.app.cell_width//2.3)
        self.number = number
        self.colour = self.set_colour()



    def update(self):
        pass
# umieszczenie duszków na ekranie
    def draw(self):
        pygame.draw.circle(self.app.screen, self.colour,(int(self.pix_pos.x), int(self.pix_pos.y)) ,self.radius)
# znowu pozycjonowanie duszków
    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+ TOP_BOTTOM_BUFFER//2+self.app.cell_height//2)
        print(self.grid_pos, self.pix_pos)
# każda cyfra to osobny duszek i jego kolor, jeszcze nie ogarnęłam jak wrzucić w to avatary
    def set_colour(self):
        if self.number == 0:
            return (43, 78, 203)
        if self.number == 1:
            return (255, 192, 203)
        if self.number == 2:
            return (189, 29, 29)
        if self.number == 3:
            return (255, 69, 0)
