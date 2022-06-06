import pygame
import sys
from gracz import *
from duszki import *
from pygame.math import Vector2

# inicjuje pygame
pygame.init()
# nazwa gry w oknie
pygame.display.set_caption("Twój stary Pacman")

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

# cała klasa  odpowiedzialna za grę
class Gra:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # to będzie potrzebne do poruszania się
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH//28
        self.cell_height = MAZE_HEIGHT//30
        self.gracz=Gracz(self, PLAYER_START_POS)
        self.sciany = []
        self.points = []
        self.duszki = []
# pozycja duszków
        self.d_pos = []
# pozycja gracza
        self.g_pos = None

        self.load()
        self.gracz=Gracz(self, self.g_pos)
        self.stworz_duszki()

# pętla dzięki której gra działa do momentu wyłączenia jej przez nas
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

############################ HELPER FUNCTIONS #################
# poniżej odpowiedzialne za wartości tekstu w naszej gierce, czcionka, wielkość
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    # tu trzeba dopracować ten ekran, wyśrodkować, dodać napisy, ustalić czcionkę itp ale to moze się tym ktoś pobawić
    # to zostawiłam tylko dlatego, bo bez teo nie działa mi program XD a jest bardzo późno

# załadowanie tła
    def load(self):
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

        # ściany, cyfra 1 to ściana, litera C punkty, P pozycja Pacmana, 2,3,4,5 pozycje duchów i E to wyjście z tego pokoiku duchów
        with open("sciany.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.sciany.append(Vector2(xidx, yidx))
                    elif char == "C":
                        self.points.append(Vector2(xidx, yidx))
                    elif char == "P":
                        self.g_pos = Vector2(xidx, yidx)
                    elif char in ["2", "3", "4", "5"]:
                        self.d_pos.append(Vector2(xidx, yidx))
                    elif char == "E":
                        pygame.draw.rect(self.background, BLACK, (xidx*self.cell_width, yidx*self.cell_height, self.cell_width, self.cell_height))
        # print(self.sciany)

    def stworz_duszki(self):
        for idx, pos in enumerate(self.d_pos):
            self.duszki.append(Duszek(self, pos, idx))

# grid to jest siatka dzięki której łatwiej się umieszcza rzeczy na ekranie i sprawdza czy coś porusza się w odpowiedniej płaszczyźnie
    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))
        for point in self.points:
            pygame.draw.rect(self.background,(112,55,163), (point.x*self.cell_width, point.y*self.cell_height, self.cell_width, self.cell_height))

# ################### INTRO FUNCTIONS ###############################
# okno startowe gry, odpalamy za pomocą spacji
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('NACIŚNIJ SPACJĘ', self.screen, [
                       WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
         # tu powinny znaleźć się komendy dotyczące napisów w intro itp. (przykład wyżej)
        pygame.display.update()

# ################### PLAYING FUNCTIONS ###########################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.gracz.ruch(Vector2(0,-1))
                if event.key==pygame.K_DOWN:
                    self.gracz.ruch(Vector2(0,1))
                if event.key==pygame.K_LEFT:
                    self.gracz.ruch(Vector2(-1,0))
                if event.key==pygame.K_RIGHT:
                    self.gracz.ruch(Vector2(1,0))

    def playing_update(self):
        self.gracz.update()
        for duszek in self.duszki:
            duszek.update()

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))

        self.draw_points()
        # grid włączamy i wyłączamy, ja zostawiłam wyłączony
        # self.draw_grid()

        self.gracz.draw()
        for duszek in self.duszki:
            duszek.draw()
        pygame.display.update()

# punkty też nie mają na razie grafiki, umieszczone na każdym polu jak na razie
    def draw_points(self):
        for point in self.points:
            pygame.draw.circle(self.screen, (82, 210, 149), (int(point.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_BUFFER//2, int(point.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_BUFFER//2), 5)

if __name__=='__main__':
    gra = Gra()
    gra.run()
