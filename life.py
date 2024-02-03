import pygame
from grid import Grid
from cell import *

"""
PYTHON GAME OF LIFE BY SCHARTHUR
CLICK -> place une cellule
SPACEBAR -> lance la simulation
A -> avance d'une frame
ZQSD/ARROWS -> deplacer la camera
"""

menu_width = 500

min_tilesize = 10
max_tilesize = 40

class newGame:
    def __init__(self, gameSpeed = 100) -> None:
        pygame.init()
        self.tilesize = max_tilesize
        self.grid_offset = [0,0]
        self.screen_width = pygame.display.get_desktop_sizes()[0][0]
        self.screen_height = pygame.display.get_desktop_sizes()[0][1]
        self.game_width = self.screen_width - menu_width
        self.gameSpeed = gameSpeed
        self.running = True
        self.autoPlay = False
        self.grd = Grid(self.game_width, self.screen_height)
        self.CellGrid = cellGrid()
        self.run()

    def run(self):
        screen = pygame.display.set_mode((self.screen_width, self.screen_height),pygame.NOFRAME)
        game_surface = pygame.Surface((self.game_width, self.screen_height))
        clock = pygame.time.Clock()
        next_move = 0

        while self.running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        self.autoPlay = not self.autoPlay
                    if event.key == pygame.K_r:
                        print(self.CellGrid.returnDict())
                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        self.grid_offset[1] += 1
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.grid_offset[1] -= 1
                    elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                        self.grid_offset[0] += 1
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.grid_offset[0] -= 1

                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_a) and not self.autoPlay:
                        self.CellGrid.UpdateAll()
                if event.type == pygame.MOUSEWHEEL:
                    self.tilesize += event.y
                    if self.tilesize < min_tilesize:
                        self.tilesize = min_tilesize
                    elif self.tilesize > max_tilesize:
                        self.tilesize = max_tilesize
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] :
                        pos = pygame.mouse.get_pos()
                        if game_surface.get_rect().collidepoint(pos):
                            self.autoPlay = False
                            mouse_click_coords = ((pos[0]//self.tilesize)-self.grid_offset[0],(pos[1]//self.tilesize)-self.grid_offset[1])
                            self.CellGrid.appendCell(mouse_click_coords)

            # AUTOPLAY
            if self.autoPlay:
                self.cell_color = '#111111'
                next_move += dt
                if next_move > 0:
                    self.CellGrid.UpdateAll()
                    next_move = -self.gameSpeed
            else:
                self.cell_color = '#999999'

            # GAME RENDER
            game_surface.fill("white")
            self.grd.draw(game_surface, self.tilesize)
            self.CellGrid.drawAll(game_surface, self.tilesize, self.grid_offset, self.cell_color)
                                
            # flip() the display to put your work on screen
            pygame.Surface.blit(screen,game_surface,(0,0),game_surface.get_rect())
            pygame.display.flip()

            dt = clock.tick(60)  # limits FPS to 60

        pygame.quit()

run = newGame()