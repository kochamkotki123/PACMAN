import pygame

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

vec = pygame.math.Vector2
# avatar którego nie umiem jeszcze umieścić zamiast zółtej kropki
image= pygame.image.load('start.png')

class Player:
    def __init__(self, app, pos):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
#         self.pix_pos = self.get_pix_pos()
        self.pix_pos = vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2,
        (self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2+self.app.cell_height//2)
        self.direction = vec(1,0)
        self.stored_direction = None
        self.able_to_move = True
        
        self.speed=1
        # size = self.app.screen.get_size()
        # self.pos = vec(size[0]/2,size[1]/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def add_force(self, force):
        self.acc+= force

    def tick(self):
        #input
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.add_force(vec(0,-self.speed))
        if pressed[pygame.K_DOWN]:
            self.add_force(vec(0,+self.speed))
        if pressed[pygame.K_LEFT]:
            self.add_force(vec(-self.speed,0))
        if pressed[pygame.K_RIGHT]:
            self.add_force(vec(self.speed,0))


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
