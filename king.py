import piece
import rules
class King(piece.Piece):

    def __init__(self,img,x,y,isWhite,n):
        super().__init__(img,x,y,isWhite,n)

        self.hasMoved = False

    # TODO this only works for white king, implement blackking later
    def canCastleQside(self,rookQueenSide,board):
        if not board[4][7] == 0:
            return False
        if not board[5][7] == 0:
            return False
        if self.isBeingAttacked(board):
            return False
        if self.hasMoved:
            return False
        if rookQueenSide.hasMoved:
            return False

        #move the king to the tile to the left of it and check again if its being attacked. You cannot castle into an attack
        board[self.prevXCor][self.prevYCor] = 0
        board[4][7] = self
        xTemp = self.prevXCor 
        yTemp = self.prevYCor
        self.prevXCor = 4
        self.prevYCor = 7

        if self.isBeingAttacked(board):
            rules.revertChanges(board,self,xTemp,yTemp)
            return False

        #same as above
        board[self.prevXCor][self.prevYCor] = 0
        board[5][7] = self
        self.prevXCor = 5
        self.prevYCor = 7

        if self.isBeingAttacked(board):
            rules.revertChanges(board,self,xTemp,yTemp)
            return False
        
        #revert everything
        rules.revertChanges(board,self,xTemp,yTemp)
        return True


    def canCastleKside(self,rookKingSide,board):
        if not board[2][7] == 0:
            return False
        if not board[1][7] == 0:
            return False

        if self.isBeingAttacked(board):
            return False
        if self.hasMoved:
            return False
        if rookKingSide.hasMoved:
            return False


        #move the king to the tile to the left of it and check again if its being attacked. You cannot castle into an attack
        board[self.prevXCor][self.prevYCor] = 0
        board[2][7] = self
        xTemp = self.prevXCor 
        yTemp = self.prevYCor
        self.prevXCor = 2
        self.prevYCor = 7

        if self.isBeingAttacked(board):
            rules.revertChanges(board,self,xTemp,yTemp)
            return False

        #same as above
        board[self.prevXCor][self.prevYCor] = 0
        board[1][7] = self
        self.prevXCor = 1
        self.prevYCor = 7

        if self.isBeingAttacked(board):
            rules.revertChanges(board,self,xTemp,yTemp)
            return False
        
        #revert everything
        rules.revertChanges(board,self,xTemp,yTemp)
        return True
        
    
    def draw(self,win):
        self.drawPiece(win)
    
    def isQueen(self,p):
        return p.name == "q"
    
    def isRook(self,p):
        return p.name == "r"
    
    def isBish(self,p):
        return p.name == "b"
    
    def isPawn(self,p):
        return p.name == "p"

    def isKnight(self,p):
        return p.name == "h"

    #checks if the king is being attacked by a piece that is not its own.
    def isBeingAttacked(self,board):

        #attacked by knight
        if not self.outOfBounds(self.prevXCor-2,self.prevYCor+1):
            if not board[self.prevXCor -2][self.prevYCor +1] == 0:
                if not (board[self.prevXCor -2][self.prevYCor +1].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor -2][self.prevYCor +1]):
                        return True 

        if not self.outOfBounds(self.prevXCor-2,self.prevYCor-1):
            if not board[self.prevXCor -2][self.prevYCor-1] == 0:
                if not (board[self.prevXCor -2][self.prevYCor-1].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor -2][self.prevYCor-1]):
                        return True

        if not self.outOfBounds(self.prevXCor+2,self.prevYCor-1):
            if not board[self.prevXCor +2][self.prevYCor-1] == 0:
                if not (board[self.prevXCor +2][self.prevYCor-1].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor +2][self.prevYCor-1]):
                        return True
        
        if not self.outOfBounds(self.prevXCor+2,self.prevYCor+1):
            if not board[self.prevXCor +2][self.prevYCor+1] == 0:
                if not (board[self.prevXCor +2][self.prevYCor+1].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor +2][self.prevYCor+1]):
                        return True

        if not self.outOfBounds(self.prevXCor+1,self.prevYCor+2):
            if not board[self.prevXCor +1][self.prevYCor+2] == 0:
                if not (board[self.prevXCor +1][self.prevYCor+2].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor +1][self.prevYCor+2]):
                        return True
        
        if not self.outOfBounds(self.prevXCor-1,self.prevYCor+2):
            if not board[self.prevXCor -1][self.prevYCor+2] == 0:
                if not (board[self.prevXCor -1][self.prevYCor+2].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor -1][self.prevYCor+2]):
                        return True
        
        if not self.outOfBounds(self.prevXCor+1,self.prevYCor-2):
            if not board[self.prevXCor +1][self.prevYCor-2] == 0:
                if not (board[self.prevXCor +1][self.prevYCor-2].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor +1][self.prevYCor-2]):
                        return True

        if not self.outOfBounds(self.prevXCor-1,self.prevYCor-2):
            if not board[self.prevXCor -1][self.prevYCor-2] == 0:
                if not (board[self.prevXCor -1][self.prevYCor-2].isWhite == self.isWhite):
                    if self.isKnight(board[self.prevXCor -1][self.prevYCor-2]):
                        return True

        #if attacked by topleft pawn
        if not self.outOfBounds(self.prevXCor-1,self.prevYCor-1):
            if not board[self.prevXCor-1][self.prevYCor-1] == 0:
                    if not (board[self.prevXCor-1][self.prevYCor-1].isWhite == self.isWhite):
                        if self.isPawn(board[self.prevXCor -1][self.prevYCor-1]):
                            return True

        #if attacked by topright pawn
        if not self.outOfBounds(self.prevXCor+1,self.prevYCor-1):
            if not board[self.prevXCor+1][self.prevYCor-1] == 0:
                    if not (board[self.prevXCor+1][self.prevYCor-1].isWhite == self.isWhite):
                        if self.isPawn(board[self.prevXCor +1][self.prevYCor-1]):
                            return True


        counter = 1
        while self.prevXCor + counter < 8:
            if not board[self.prevXCor + counter][self.prevYCor] == 0:
                if not (board[self.prevXCor + counter][self.prevYCor].isWhite == self.isWhite):
                    if self.isQueen(board[self.prevXCor + counter][self.prevYCor])  or self.isRook(board[self.prevXCor + counter][self.prevYCor]):
                        return True
                    else:
                        break
                else:
                    break
            counter = counter + 1

        counter = 1
        while self.prevXCor - counter >= 0:
            if not board[self.prevXCor - counter][self.prevYCor] == 0:
                if not (board[self.prevXCor - counter][self.prevYCor].isWhite == self.isWhite):               
                    if self.isQueen(board[self.prevXCor - counter][self.prevYCor]) or self.isRook(board[self.prevXCor - counter][self.prevYCor]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1
        
        counter = 1
        while self.prevYCor + counter < 8:
            if not board[self.prevXCor][self.prevYCor + counter] == 0:
                if (not board[self.prevXCor][self.prevYCor + counter].isWhite == self.isWhite):
                    if self.isQueen(board[self.prevXCor][self.prevYCor + counter]) or self.isRook(board[self.prevXCor][self.prevYCor + counter]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1

        counter = 1
        while self.prevYCor - counter >= 0:
            if not board[self.prevXCor][self.prevYCor - counter] == 0:
                if (not board[self.prevXCor][self.prevYCor - counter].isWhite == self.isWhite):
                    if self.isQueen(board[self.prevXCor][self.prevYCor - counter] ) or self.isRook(board[self.prevXCor][self.prevYCor - counter]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1
        
        #left up
        counter = 1
        while not self.outOfBounds(self.prevXCor - counter,self.prevYCor
                - counter):
            if not board[self.prevXCor - counter][self.prevYCor - counter] == 0:
                if not (board[self.prevXCor - counter][self.prevYCor - counter].isWhite == self.isWhite):
                    if self.isQueen(board[self.prevXCor - counter][self.prevYCor - counter] ) or self.isBish(board[self.prevXCor - counter][self.prevYCor - counter]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1

        #left down
        counter = 1
        while not self.outOfBounds(self.prevXCor - counter,self.prevYCor
                + counter):
            if not board[self.prevXCor - counter][self.prevYCor + counter] == 0:
                if not (board[self.prevXCor - counter][self.prevYCor + counter].isWhite == self.isWhite):
                    if self.isQueen(board[self.prevXCor - counter][self.prevYCor + counter]) or self.isBish(board[self.prevXCor - counter][self.prevYCor + counter]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1

        #right down
        counter = 1
        while not self.outOfBounds(self.prevXCor + counter,self.prevYCor
                + counter):
            if not board[self.prevXCor + counter][self.prevYCor + counter] == 0:
                if not (board[self.prevXCor + counter][self.prevYCor + counter].isWhite == self.isWhite):
                    if self.isQueen(board[self.prevXCor + counter][self.prevYCor + counter] ) or self.isBish(board[self.prevXCor + counter][self.prevYCor + counter]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1

        #right up
        counter = 1
        while not self.outOfBounds(self.prevXCor + counter,self.prevYCor
                - counter):
            if not board[self.prevXCor + counter][self.prevYCor - counter] == 0:
                if not (board[self.prevXCor + counter][self.prevYCor - counter].isWhite == self.isWhite):
                    if self.isQueen(board[self.prevXCor + counter][self.prevYCor - counter]) or self.isBish(board[self.prevXCor + counter][self.prevYCor - counter]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1
        return False

    def tilesMoveable(self,playerTurn,whiteKing,rookQueenSide,rookKingSide,board):
        res = []
        print(self.canCastleKside(rookKingSide,board))
        #left
        if not self.outOfBounds(self.prevXCor-1,self.prevYCor):
            if board[self.prevXCor -1][self.prevYCor] == 0:
                res.append((self.prevXCor -1,self.prevYCor))
        #left up

        if not self.outOfBounds(self.prevXCor-1,self.prevYCor-1):
            if board[self.prevXCor -1][self.prevYCor-1] == 0:
                res.append((self.prevXCor -1,self.prevYCor-1))

        #up

        if not self.outOfBounds(self.prevXCor,self.prevYCor-1):
            if board[self.prevXCor][self.prevYCor-1] == 0:
                res.append((self.prevXCor,self.prevYCor-1))

        #right up

        if not self.outOfBounds(self.prevXCor+1,self.prevYCor-1):
            if board[self.prevXCor + 1][self.prevYCor-1] == 0:
                res.append((self.prevXCor +1,self.prevYCor-1))

        #right

        if not self.outOfBounds(self.prevXCor+1,self.prevYCor):
            if board[self.prevXCor + 1][self.prevYCor] == 0:
                res.append((self.prevXCor +1,self.prevYCor))

        #right down
        if not self.outOfBounds(self.prevXCor+1,self.prevYCor+1):
            if board[self.prevXCor + 1][self.prevYCor+1] == 0:
                res.append((self.prevXCor +1,self.prevYCor+1))

        #down

        if not self.outOfBounds(self.prevXCor,self.prevYCor+1):
            if board[self.prevXCor][self.prevYCor+1] == 0:
                res.append((self.prevXCor,self.prevYCor+1))

        #left down

        if not self.outOfBounds(self.prevXCor-1,self.prevYCor+1):
            if board[self.prevXCor - 1][self.prevYCor+1] == 0:
                res.append((self.prevXCor -1,self.prevYCor+1))
        return res

