import pygame

class newCell:
    def __init__(self, coords) -> None:
        self.coords = coords
        pass
    def draw(self, screen, tileSize, color = '#111111'):
        cell_rect = pygame.Rect(self.coords[0]*tileSize, self.coords[1]*tileSize, tileSize, tileSize)
        pygame.draw.rect(screen, color, cell_rect)