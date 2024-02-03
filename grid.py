import pygame

class Grid:
    def __init__(self, X, Y) -> None:
        self.matrice = []
        self.sizeX = X
        self.sizeY = Y

    def draw(self, screen, tileSize, grid_color='#EFEFEF'):
        for i in range(1,self.sizeX):
            pygame.draw.line(screen,grid_color, (tileSize*i, 0), (tileSize*i, tileSize*self.sizeX))
        for i in range(0,self.sizeY):
            pygame.draw.line(screen,grid_color, (0, tileSize*i), (tileSize*self.sizeX, tileSize*i))