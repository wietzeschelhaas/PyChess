import piece
class King(piece.Piece):

    def __init__(self,img,x,y,isWhite):
        super().__init__(img,x,y,isWhite)

    
    def draw(self,win):
        self.drawPiece(win)


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
