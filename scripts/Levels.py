import pygame
from Tiles import Tile
from Settings import tileSize, screenWidth
from Player import Player

class Level:
    def __init__(self, levelData, surface):
        self.displaySurface = surface
        self.setupLevel(levelData)
    
        self.worldShift = 0

    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for rowIndex, row in enumerate(layout):
            for colIndex, cell in enumerate(row):
                x = colIndex * tileSize
                y = rowIndex * tileSize
                if cell == 'X':
                    tile = Tile((x,y), tileSize)
                    self.tiles.add(tile)
                if cell == 'P':
                    playerSprite = Player((x,y))
                    self.player.add(playerSprite)
                
    def scrollHorizontal(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x

        if playerX < screenWidth // 4 and directionX < 0:
            self.worldShift = 10
            player.speed = 0
        elif playerX > screenWidth // 2 and directionX > 0:
            self.worldShift = -10
            player.speed = 0
        else:
            self.worldShift = 0
            player.speed = 10

    def run(self):
        # Level Tiles update
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        
        # Player update
        self.player.update()
        self.player.draw(self.displaySurface)
        self.scrollHorizontal()