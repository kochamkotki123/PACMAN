import pygame
import random
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

# cała klasa duszków, ich ilość, pozycje
class Duszek:
    def __init__(self, gra, pos, numer):
        self.gra = gra
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.radius = int(self.gra.szerokosc_komorki//2.3)
        self.numer = numer
        self.colour = self.set_colour()
        self.kierunek = Vector2(0,0)
        self.usposobienie = self.ustaw_usposobienie()
        self.predkosc = self.ustaw_predkosc()
        self.pozycja_poczatkowa=[pos[0],pos[1]]

#opcje związane z ruchem duszków i gonieniem pacmana
    def update(self):
        self.pix_pos += self.kierunek*self.predkosc
        if self.czas_na_ruch():
            self.ruch()
                        #pozycjonowako
        self.grid_pos[0] = (self.pix_pos[0]-BUFOR+self.gra.szerokosc_komorki//2)//self.gra.szerokosc_komorki+1
        self.grid_pos[1] = (self.pix_pos[1]-BUFOR+self.gra.wysokosc_komorki//2)//self.gra.wysokosc_komorki+1

    def czas_na_ruch(self):
        if int(self.pix_pos.x+BUFOR//2) % self.gra.szerokosc_komorki == 0:
            if self.kierunek == Vector2(1,0) or self.kierunek == Vector2(-1,0) or self.kierunek == Vector2(0, 0):
                return True
        if int(self.pix_pos.y+BUFOR//2) % self.gra.wysokosc_komorki == 0:
            if self.kierunek == Vector2(0,1) or self.kierunek == Vector2(0,-1) or self.kierunek == Vector2(0, 0):
                return True
        return False

    def ruch(self):
        if self.usposobienie == "losowy":
            self.kierunek = self.losowy_kierunek()
        if self.usposobienie == "szybki" or self.usposobienie == "normalny" or self.usposobienie == "wolny":
            self.kierunek = self.wyznacz_trase()

    def losowy_kierunek(self):
        while True:
            numer = random.randint(-2,1)
            if numer ==-2:
                x_kierunek, y_kierunek = 0,1
            elif numer ==-1:
                x_kierunek, y_kierunek = 0,-1
            elif numer ==0:
                x_kierunek, y_kierunek = -1,0
            else:
                x_kierunek, y_kierunek = 1,0
            next_pos=Vector2(self.grid_pos.x+x_kierunek, self.grid_pos.y+y_kierunek)
            if next_pos not in self.gra.sciany:
                break
        return Vector2(x_kierunek, y_kierunek)

    def wyznacz_trase(self):
        nastepna_komorka = self.wyznacz_nastepna_komorke()
        xkierunek = nastepna_komorka[0] - self.grid_pos[0]
        ykierunek = nastepna_komorka[1] - self.grid_pos[1]
        return Vector2(xkierunek, ykierunek)

    def wyznacz_nastepna_komorke(self):
        trasa = self.przeszukaj([int(self.grid_pos.x), int(self.grid_pos.y)], [int(self.gra.gracz.grid_pos.x), int(self.gra.gracz.grid_pos.y)])
        return trasa[1]

    def przeszukaj(self, start, ofiara):
        grid = [[0 for x in range(28)] for x in range(30)]
        for komorka in self.gra.sciany:
            if komorka.x <28 and komorka.y <30:
                grid[int(komorka.y)][int(komorka.x)] = 1
        w_kolejce = [start]
        trasa = []
        sprawdzone = []
        while w_kolejce:
            obecna = w_kolejce[0]
            w_kolejce.remove(w_kolejce[0])
            sprawdzone.append(obecna)
            if obecna == ofiara:
                break
            else:
                sasiadujace=[[1,0],[0,1],[-1,0],[0,-1]]
                for sasiad in sasiadujace:
                    if sasiad[0]+obecna[0] >=0 and sasiad[0]+obecna[0] < len(grid[0]):
                        if sasiad[1]+obecna[1] >=0 and sasiad[1]+obecna[1] < len(grid):
                            nastepna_komorka = [sasiad[0]+obecna[0], sasiad[1]+obecna[1]]
                            if nastepna_komorka not in sprawdzone:
                                if grid[nastepna_komorka[1]][nastepna_komorka[0]] != 1:
                                    w_kolejce.append(nastepna_komorka)
                                    trasa.append({"Obecna": obecna, "Następna": nastepna_komorka})

        najkrotsza=[ofiara]
        while ofiara != start:
            for krok in trasa:
                if krok["Następna"] == ofiara:
                    ofiara = krok["Obecna"]
                    najkrotsza.insert(0,krok["Obecna"])

        return najkrotsza

# umieszczenie duszków na ekranie
    def draw(self):
        if self.numer==0:
            self.gra.screen.blit(self.gra.duszek1, (int(self.pix_pos.x)-8, int(self.pix_pos.y)-8))
        if self.numer==1:
            self.gra.screen.blit(self.gra.duszek2, (int(self.pix_pos.x)-8, int(self.pix_pos.y)-8))
        if self.numer==2:
            self.gra.screen.blit(self.gra.duszek3, (int(self.pix_pos.x)-8, int(self.pix_pos.y)-8))
        if self.numer==3:
            self.gra.screen.blit(self.gra.duszek4, (int(self.pix_pos.x)-8, int(self.pix_pos.y)-8))

# znowu pozycjonowanie duszków
    def get_pix_pos(self):
        return Vector2((self.grid_pos.x*self.gra.szerokosc_komorki)+BUFOR//2+self.gra.szerokosc_komorki//2, (self.grid_pos.y*self.gra.wysokosc_komorki)+ BUFOR//2+self.gra.wysokosc_komorki//2)
        print(self.grid_pos, self.pix_pos)

#każda cyfra to osobny duszek i jego kolor
    def set_colour(self):
        if self.numer == 0:
            return (43, 78, 203)
        if self.numer == 1:
            return (255, 192, 203)
        if self.numer == 2:
            return (189, 29, 29)
        if self.numer == 3:
            return (255, 69, 0)

    def ustaw_usposobienie(self):
        if self.numer == 0:
            return "losowy"
        if self.numer == 1:
            return "szybki"
        if self.numer == 2:
            return "normalny"
        if self.numer ==3:
            return "wolny"

    def ustaw_predkosc(self):
        if self.usposobienie=="szybki":
            predkosc=3
        if self.usposobienie=="wolny":
            predkosc=1
        else:
            predkosc=2
        return predkosc

    def ustaw_ofiare(self):
        if self.usposobienie in ["wolny","szybki"]:
            return self.gra.gracz.grid_pos
        else:
            if self.gra.gracz.grid_pos[0]>14 and self.gra.gracz.grid_pos[1]>15:
                return Vector2(1,1)
            if self.gra.gracz.grid_pos[0]>14 and self.gra.gracz.grid_pos[1]<15:
                return Vector2(1,28)
            if self.gra.gracz.grid_pos[0]<14 and self.gra.gracz.grid_pos[1]>15:
                return Vector2(26,1)
            else:
                return Vector2(26,28)
