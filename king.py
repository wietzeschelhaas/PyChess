import piece
class King(piece.Piece):

    def __init__(self,img,x,y,isWhite,n):
        super().__init__(img,x,y,isWhite,n)

    
    def draw(self,win):
        self.drawPiece(win)
    
    def isQueen(self,p):
        return p.name == "q"
    
    def isRook(self,p):
        return p.name == "r"
    
    def isBish(self,p):
        return p.name == "b"

    def isBeingAttacked(self,board):
        counter = 1
        while self.prevXCor + counter < 8:
            if not board[self.prevXCor + counter][self.prevYCor] == 0:
                if not board[self.prevXCor + counter][self.prevYCor].isWhite:
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
                if not board[self.prevXCor - counter][self.prevYCor].isWhite:               
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
                if not board[self.prevXCor][self.prevYCor + counter].isWhite:
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
                if not board[self.prevXCor][self.prevYCor - counter].isWhite:
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
                if not board[self.prevXCor - counter][self.prevYCor - counter].isWhite:
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
                if not board[self.prevXCor - counter][self.prevYCor + counter].isWhite:
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
                if not board[self.prevXCor + counter][self.prevYCor + counter].isWhite:
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
                if not board[self.prevXCor + counter][self.prevYCor - counter].isWhite:
                    if self.isQueen(board[self.prevXCor + counter][self.prevYCor - counter]) or self.isBish(board[self.prevXCor + counter][self.prevYCor - counter]):
                        return True
                    else:
                        break
                else:
                    break                    
            counter = counter + 1
        return False

    def tilesMoveable(self,board):
        res = []
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

