import pygame
from Tiles import Tile
from Settings import tileSize

class Level:
    def __init__(self, levelData, surface):
        self.displaySurface = surface
        self.setupLevel(levelData)
    

    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        for rowIndex, row in enumerate(layout):
            for colIndex, cell in enumerate(row):
                if cell == 'X':
                    x = colIndex * tileSize
                    y = rowIndex * tileSize
                    tile = Tile((x,y), tileSize)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(-1)
        self.tiles.draw(self.displaySurface)