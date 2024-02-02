import pygame

class cellGrid:
    def __init__(self, width, height,tilesize):
        self.cell_list = {}
        for i in range(width//tilesize):
            for j in range(height//tilesize):
                self.cell_list[str(str(i) + ',' + str(j))] = newCell((i,j), False)
    def returnList(self):
        return self.cell_list
    
    def UpdateAll(self):
        for key in self.cell_list:
            self.Update(self.cell_list[key])
        for key in self.cell_list:
            if self.cell_list[key].willDie:
                self.cell_list[key].isAlive = False
                self.cell_list[key].willDie = False
            if self.cell_list[key].willLive:
                self.cell_list[key].isAlive = True
                self.cell_list[key].willLive = False
        
    def Update(self, cell):
        neighboorsAlive = 0
        cell_pos = cell.getCoords()
        for i in range(-1,2):
            for j in range(-1,2):
                if ((i != 0) or (j != 0)):
                    try:
                        if self.cell_list[str(str(i + cell_pos[0]) + ',' + str(j + cell_pos[1]))].isAlive:
                            neighboorsAlive += 1
                    except:
                        neighboorsAlive +=0
        
        # LIFE RULES
        if cell.isAlive:
            if neighboorsAlive < 2:
                cell.willDie = True
            elif 2 <= neighboorsAlive <= 3:
                cell.willDie = False
            elif neighboorsAlive > 3:
                cell.willDie = True
        else:
            if neighboorsAlive == 3:
                cell.willLive = True

class newCell:
    def __init__(self, coords, isAlive):
        self.willDie = False
        self.willLive = False
        self.coords = coords
        self.isAlive = isAlive
        
    def draw(self, screen, tileSize, color = '#111111'):
        if self.isAlive:
            cell_rect = pygame.Rect(self.coords[0]*tileSize, self.coords[1]*tileSize, tileSize, tileSize)
            pygame.draw.rect(screen, color, cell_rect)

    def getCoords(self):
        return self.coords
    
    def getViaPos(self, pos):
        if pos == self.coords:
            return self

    def changeStatus(self) -> tuple:
        self.isAlive = not self.isAlive
