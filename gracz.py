import pygame
from pygame.math import Vector2

# ustawienia ekranu
SZEROKOSC, WYSOKOSC = 610, 670
FPS = 60
BUFOR = 50
SZEROKOSC_LABIRYNTU, WYSOKOSC_LABIRYNTU = SZEROKOSC-BUFOR, WYSOKOSC - BUFOR

# ustawienia kolorów
CZERN = (0, 0, 0)
CZERWIEN = (208, 22, 22)
SZAROSC = (107, 107, 107)
BIEL = (255,255,255)
KOLOR_GRACZA = (190,194,15)
# ustawienia czcionki
START_TEXT_SIZE = 16
FONT = 'arial black'
# ustawienia związane z graczem
PLAYER_START_POS = Vector2(1,1)
# avatar którego nie umiem jeszcze umieścić zamiast zółtej kropki
image= pygame.image.load('start.png')

class Gracz:
    def __init__(self, gra, pos):
        self.screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
        self.gra = gra
        self.starting_pos = [pos[0], pos[1]]
        self.grid_pos = Vector2(pos[0],pos[1])
        self.pix_pos = self.get_pix_pos()
        self.kierunek = Vector2(0,0)
        self.biezacy_kierunek = None
        self.ma_mozliwosc_ruchu = True
        self.predkosc=2
        self.wynik=0
        self.zycia=3

    def update(self):
        if self.ma_mozliwosc_ruchu:
            self.pix_pos += self.kierunek*self.predkosc
        if self.czas_na_ruch():
            if self.biezacy_kierunek != None:
                self.kierunek = self.biezacy_kierunek
            self.ma_mozliwosc_ruchu = self.moze_ruszyc()
        if self.dotknac_punkt():
            self.zjesc_punkt()

# pozycjonowanie na siatce
        self.grid_pos[0] = (self.pix_pos[0]-BUFOR+self.gra.szerokosc_komorki//2)//self.gra.szerokosc_komorki+1
        self.grid_pos[1] = (self.pix_pos[1]-BUFOR+self.gra.wysokosc_komorki//2)//self.gra.wysokosc_komorki+1

    def draw(self):
        self.gra.screen.blit(self.gra.pacman,(int(self.pix_pos.x)-8,  int(self.pix_pos.y)-8))


# pozycjonowanie w pikselach
    def get_pix_pos(self):
        return Vector2((self.grid_pos.x*self.gra.szerokosc_komorki)+BUFOR//2+self.gra.szerokosc_komorki//2, (self.grid_pos.y*self.gra.wysokosc_komorki)+ BUFOR//2+self.gra.wysokosc_komorki//2)
        print(self.grid_pos, self.pix_pos)

#ruszanie się pacmana
    def ruch(self, kierunek):
        self.biezacy_kierunek = kierunek

    def czas_na_ruch(self):
        if int(self.pix_pos.x+BUFOR//2) % self.gra.szerokosc_komorki == 0:
            if self.kierunek == Vector2(1,0) or self.kierunek == Vector2(-1,0) or self.kierunek == Vector2(0, 0):
                return True
        if int(self.pix_pos.y+BUFOR//2) % self.gra.wysokosc_komorki == 0:
            if self.kierunek == Vector2(0,1) or self.kierunek == Vector2(0,-1) or self.kierunek == Vector2(0, 0):
                return True
        return False

    def moze_ruszyc(self):
        for sciana in self.gra.sciany:
            if Vector2(self.grid_pos+self.kierunek)== sciana:
                return False
        return True

#zbieranie i zjadanie punkcików
    def dotknac_punkt(self):
        if self.grid_pos in self.gra.punkty:
            return True
        return False

    def zjesc_punkt(self):
        self.gra.punkty.remove(self.grid_pos)
        self.wynik+=1
