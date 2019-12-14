import pygame

from pawn import Pawn
from rook import Rook
from bish import Bish
from king import King
from queen import Queen
from knight import Knight
import rules

pygame.init()

win = pygame.display.set_mode((640,640))
pygame.display.set_caption("chess")

board  = [[0 for x in range(8)] for y in range(8)]

canCastle = True

playerTurn = True


blackPieces = []
whitePieces = []
for x in range(8):
    whitePieces.append(Pawn("WhitePawn.png",x,6,True,"p"))


for i in range(8):
    blackPieces.append(Pawn("BlackPawn.png",i,1,False,"p"))

whitePieces.append(Rook("WhiteRook.png",0,7,True,"r"))
whitePieces.append(Rook("WhiteRook.png",7,7,True,"r"))

blackPieces.append(Rook("BlackRook.png",0,0,False,"r"))
blackPieces.append(Rook("BlackRook.png",7,0,False,"r"))

whitePieces.append(Knight("WhiteKnight.png",1,7,True,"h"))
whitePieces.append(Knight("WhiteKnight.png",6,7,True,"h"))

blackPieces.append(Knight("BlackKnight.png",1,0,False,"h"))
blackPieces.append(Knight("BlackKnight.png",6,0,False,"h"))

whitePieces.append(Bish("WhiteBishop.png",2,7,True,"b"))
whitePieces.append(Bish("WhiteBishop.png",5,7,True,"b"))

blackPieces.append(Bish("BlackBishop.png",2,0,False,"b"))
blackPieces.append(Bish("BlackBishop.png",5,0,False,"b"))

whiteKing = King("WhiteKing.png",3,7,True,"k")
whitePieces.append(whiteKing)
blackPieces.append(King("BlackKing.png",3,0,False,"k"))

whitePieces.append(Queen("WhiteQueen.png",4,7,True,"q"))
blackPieces.append(Queen("BlackQueen.png",4,0,False,"q"))

#board to keep track of where the pieces are
for p in blackPieces:
    board[p.prevXCor][p.prevYCor] = p
for p in whitePieces:
    board[p.prevXCor][p.prevYCor] = p

#used for debugging so that you can also move the black pieces
allPieces = whitePieces + blackPieces


pressedPiece = False
run = True
mouseDown = False
toMove = None

whiteIncheck = False
blackIncheck = False


def blackRandomMove():
    playerTurn = True
while run: #main loop

    #update
    if playerTurn:



        #events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False
                if pressedPiece:
                    x,y = toMove.calcWhichTile()
                    res = toMove.tilesMoveable(board)
                    print(res)
                    
                    if not rules.isLegalMove(playerTurn,whiteIncheck,toMove,whiteKing,x,y,res,board):
                            #move to previous position
                        toMove.moveToTile(toMove.prevXCor,toMove.prevYCor)
                    else:
                        #TODO RIGHT NOW PLAYER CAN CAPTURE ITS OWN PIECES, THIS IS CLEANER IF ITS FIXED HERE INSTEAD OF IN ALL PIECE CLASSES
                        #TODO do all below by making the  move and then check to see all stuff below

                        # TODO check if moving the piece doesn't lead to check.

                        #TODO does player want to castle? make funciton that checks if casteling is still legal.
                        #do this here or in king.py?

                        toMove.moveToTile(x,y)
                        board[toMove.prevXCor][toMove.prevYCor] = 0

                        #update board and prevcors    
                        board[x][y] = toMove
                        toMove.prevXCor = x
                        toMove.prevYCor = y
                pressedPiece = False

        if mouseDown:
            x, y = pygame.mouse.get_pos()
            #TODO change this to whitePieces later
            for p in allPieces:
                if p.rect.collidepoint(x,y) and not pressedPiece:
                    pressedPiece = True
                    toMove = p
        if pressedPiece: 
            x, y = pygame.mouse.get_pos()
            toMove.updatePos(x,y)
    else:
        blackRandomMove()


    win.fill((0,0,0))
    white = True

    # draw board and pieces
    for x in range(8):
        if x%2 == 0:
            white = True
        else:
            white = False
        for y in range(8):
            if white:
                pygame.draw.rect(win,(255,255,255),(80*x,80*y,80,80))
                white = False
            else:
                pygame.draw.rect(win,(173, 131, 76),(80*x,80*y,80,80))
                white = True

    for p in whitePieces:
        p.draw(win)
    for p in blackPieces:
        p.draw(win)
    pygame.display.update()

