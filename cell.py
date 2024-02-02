import pygame

class cellGrid:
    def __init__(self, width, height,tilesize, offgrid = 15):
        self.cell_dict = {}

    def returnDict(self):
        return self.cell_dict
    
    def appendCell(self, coords):
        key = str(str(coords[0]) + ',' + str(coords[1]))
        if key in self.cell_dict:
            del self.cell_dict[key]
        else:
            self.cell_dict[key] = newCell((coords[0],coords[1]), False)
            self.cell_dict[key].isAlive = True

    def drawAll(self, screen, tileSize, color = '#999999'):
        for key in self.cell_dict:
            self.cell_dict[key].draw(screen, tileSize, color)
    
    def UpdateAll(self):
        key_del = []
        affectedDict = self.returnAffectedDict()
        affectedDict.update(self.cell_dict)
        for key in affectedDict:
            self.Update(affectedDict[key])
        for key in affectedDict:
            if affectedDict[key].willDie:
                affectedDict[key].isAlive = False
                affectedDict[key].willDie = False
            if affectedDict[key].willLive:
                affectedDict[key].isAlive = True
                affectedDict[key].willLive = False
        self.cell_dict.update(affectedDict)
        for key in self.cell_dict:
            if not self.cell_dict[key].isAlive:
                key_del.append(key)
        for x in key_del:
            if x in self.cell_dict:
                del self.cell_dict[x]


    def returnAffectedDict(self) -> dict:
        # Renvoi le dict de toutes les cases affectées par le jeu lors de la prochaine frame
        deadCells = {}
        for key in self.cell_dict:
            cell_pos = self.cell_dict[key].getCoords()
            for i in range(-1,2):
                for j in range(-1,2):
                    neighboorKey = str(str(i + cell_pos[0]) + ',' + str(j + cell_pos[1]))
                    if neighboorKey not in self.cell_dict:
                        deadCells[neighboorKey] = newCell((i + cell_pos[0], j + cell_pos[1]), False)
        return deadCells
        
    def Update(self, cell):
        neighboorsAlive = 0
        cell_pos = cell.getCoords()
        for i in range(-1,2):
            for j in range(-1,2):
                if ((i != 0) or (j != 0)):
                    try:
                        if self.cell_dict[str(str(i + cell_pos[0]) + ',' + str(j + cell_pos[1]))].isAlive:
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
