import pygame
from pawn import Pawn
from rook import Rook
from bish import Bish
from king import King
from queen import Queen
from knight import Knight

pygame.init()

win = pygame.display.set_mode((640,640))
pygame.display.set_caption("chess")

board  = [[0 for x in range(8)] for y in range(8)]

canCastle = True


pieces = []
for x in range(8):
    pieces.append(Pawn("WhitePawn.png",x,6,True))


for i in range(8):
    pieces.append(Pawn("BlackPawn.png",i,1,False))

pieces.append(Rook("WhiteRook.png",0,7,True))
pieces.append(Rook("WhiteRook.png",7,7,True))

pieces.append(Rook("BlackRook.png",0,0,False))
pieces.append(Rook("BlackRook.png",7,0,False))

pieces.append(Knight("WhiteKnight.png",1,7,True))
pieces.append(Knight("WhiteKnight.png",6,7,True))

pieces.append(Knight("BlackKnight.png",1,0,False))
pieces.append(Knight("BlackKnight.png",6,0,False))

pieces.append(Bish("WhiteBishop.png",2,7,True))
pieces.append(Bish("WhiteBishop.png",5,7,True))

pieces.append(Bish("BlackBishop.png",2,0,False))
pieces.append(Bish("BlackBishop.png",5,0,False))

pieces.append(King("WhiteKing.png",3,7,True))
pieces.append(King("BlackKing.png",3,0,False))

pieces.append(Queen("WhiteQueen.png",4,7,True))
pieces.append(Queen("BlackQueen.png",4,0,False))

#board to keep track of where the pieces are
for p in pieces:
    board[p.prevXCor][p.prevYCor] = p

print(board)

pressedPiece = False
run = True
mouseDown = False
toMove = None
while run: #main loop

    #update
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


                #if its allowed to move, move to that tile
                #TODO what if black piece is there?
                if (x,y) in res:

                    # TODO check if king isn't already in check.

                    # TODO check if moving the piece doesn't lead to check.

                    #TODO does player want to castle? make funciton that checks if casteling is still legal.
                    #do this here or in king.py?

                    toMove.moveToTile(x,y)
                    board[toMove.prevXCor][toMove.prevYCor] = 0

                    #this has to be a black piece? 
                    #TODO remove black piece from the board
                    if not board[x][y] == 0:
                        print("on black piece")

                    #update board and prevcors    
                    board[x][y] = toMove
                    toMove.prevXCor = x
                    toMove.prevYCor = y
                #else move (x,y) in back to previous
                else:
                    toMove.moveToTile(toMove.prevXCor,toMove.prevYCor)
            pressedPiece = False

    if mouseDown:
        x, y = pygame.mouse.get_pos()
        for p in pieces:
            if p.rect.collidepoint(x,y) and not pressedPiece:
                pressedPiece = True
                toMove = p
    if pressedPiece: 
        x, y = pygame.mouse.get_pos()
        toMove.updatePos(x,y)


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

    for p in pieces:
        p.draw(win)
    pygame.display.update()

