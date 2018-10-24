import pygame

class Piece(pygame.sprite.Sprite):

    def __init__(self,img,x,y,isWhite):
        super().__init__()

        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = pygame.Rect((x*80,y*80),[80,80])
        self.prevXCor = x
        self.prevYCor = y
        self.isWhite = isWhite
        self.isTouched = False



    def drawPiece(self, screen):

        if not self.isTouched:
            screen.blit(self.image,(self.rect[0],self.rect[1]))

    #this is used when the mouse drags the piece
    def updatePos(self,x,y):
        self.rect = pygame.Rect((x-40,y-40),[80,80])

    
    def moveToTile(self,xCor,yCor):
        self.rect = pygame.Rect((xCor*80,yCor*80),[80,80])

    #TODO this function should calculate which tile the user wants the piece on
    # based on coordinates
    def calcWhichTile(self):
       xCor = int(round(self.rect.x / 80))
       yCor = int(round(self.rect.y / 80))
       # only if allowed
       #self.moveToTile(xCor,yCor)
       return (xCor,yCor)


    def outOfBounds(self,x,y):
        if x < 0 or x >7:
            return True
        if y < 0 or y > 7:
            return True
        return False
            
    
