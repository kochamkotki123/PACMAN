import pygame
from ustawienia import *
vec = pygame.math.Vector2
# avatar którego nie umiem jeszcze umieścić zamiast zółtej kropki
image= pygame.image.load('start.png')

class Player:
    def __init__(self, app, pos):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.stored_direction = None
        self.able_to_move = True

    def update(self):



# pozycjonowanie troche skomplikowane średnio ogarniam więc jeżeli macie pomysły jak to ułatwić to będe wdzięczna

        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height+1

    def draw(self):
# żółte kółko ;-;
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x),  int(self.pix_pos.y)), self.app.cell_width//2-2)



# pozycjonowanie znowu

    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2, (self.grid_pos.y*self.app.cell_height)+ TOP_BOTTOM_BUFFER//2+self.app.cell_height//2)
        print(self.grid_pos, self.pix_pos)
