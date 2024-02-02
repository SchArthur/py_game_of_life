import pygame
from grid import Grid
from cell import newCell

size_x = 1280
size_y = 720

tilesize = 20

cell_list = []

class newGame:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.grd = Grid(size_x, size_y, tilesize)
        self.cell = newCell((10,10))
        self.run()  

    def run(self):
        screen = pygame.display.set_mode((size_x, size_y))
        clock = pygame.time.Clock()

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print("mouse_pos:", pos)
                    mouse_click_coords = (pos[0]//tilesize,pos[1]//tilesize)
                    cell_list.append(newCell(mouse_click_coords))

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("white")
            self.grd.draw(screen)
            for elt in cell_list:
                elt.draw(screen,tilesize)
            self.cell.draw(screen, tilesize)

            # RENDER YOUR GAME HERE


            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()

run = newGame()