
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
# ustawienia czcionki
START_TEXT_SIZE = 16
START_FONT = 'arial black'


# ustawienia związane z graczem

PLAYER_START_POS = vec(1,1)
# ustawienia związane z duszkami
