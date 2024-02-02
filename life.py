import pygame
from grid import Grid
from cell import *

size_x = 1280
size_y = 780

tilesize = 20



class newGame:
    def __init__(self, gameSpeed = 100) -> None:
        pygame.init()
        self.gameSpeed = gameSpeed
        self.running = True
        self.autoPlay = False
        self.grd = Grid(size_x, size_y, tilesize)
        self.CellGrid = cellGrid(size_x, size_y, tilesize)
        self.cell_list = self.CellGrid.returnList()
        self.run()

    def run(self):
        screen = pygame.display.set_mode((size_x, size_y))
        clock = pygame.time.Clock()
        next_move = 0

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        self.autoPlay = not self.autoPlay
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_click_coords = (pos[0]//tilesize,pos[1]//tilesize)
                    cell_key = str(str(mouse_click_coords[0]) + ',' + str(mouse_click_coords[1]))
                    self.cell_list[cell_key].changeStatus()

            
            if self.autoPlay:
                self.cell_color = '#111111'
                next_move += dt
                if next_move > 0:
                    self.CellGrid.UpdateAll()
                    next_move = -self.gameSpeed
            else:
                self.cell_color = '#999999'
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("white")
            self.grd.draw(screen)
            for key in self.cell_list:
                self.cell_list[key].draw(screen, tilesize, self.cell_color)

            # RENDER YOUR GAME HERE
            
                    

            # flip() the display to put your work on screen
            pygame.display.flip()

            dt = clock.tick(60)  # limits FPS to 60

        pygame.quit()

run = newGame()