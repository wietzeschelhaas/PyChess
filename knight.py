import piece
class Knight(piece.Piece):
    def __init__(self,img,x,y,isWhite):
        super().__init__(img,x,y,isWhite)

    
    def draw(self,win):
        self.drawPiece(win)

    def tilesMoveable(self,board):
        res = []
        
        if not self.outOfBounds(self.prevXCor-2,self.prevYCor+1):
            if board[self.prevXCor -2][self.prevYCor +1] == 0:
                res.append((self.prevXCor -2,self.prevYCor+1)) 

        if not self.outOfBounds(self.prevXCor-2,self.prevYCor-1):
            if board[self.prevXCor -2][self.prevYCor-1] == 0:
                res.append((self.prevXCor -2,self.prevYCor-1))

        if not self.outOfBounds(self.prevXCor+2,self.prevYCor-1):
            if board[self.prevXCor +2][self.prevYCor-1] == 0:
                res.append((self.prevXCor +2,self.prevYCor-1))
        
        if not self.outOfBounds(self.prevXCor+2,self.prevYCor+1):
            if board[self.prevXCor +2][self.prevYCor+1] == 0:
                res.append((self.prevXCor +2,self.prevYCor+1))

        if not self.outOfBounds(self.prevXCor+1,self.prevYCor+2):
            if board[self.prevXCor +1][self.prevYCor+2] == 0:
                res.append((self.prevXCor +1,self.prevYCor+2))
        
        if not self.outOfBounds(self.prevXCor-1,self.prevYCor+2):
            if board[self.prevXCor -1][self.prevYCor+2] == 0:
                res.append((self.prevXCor -1,self.prevYCor+2))
        
        if not self.outOfBounds(self.prevXCor+1,self.prevYCor-2):
            if board[self.prevXCor +1][self.prevYCor-2] == 0:
                res.append((self.prevXCor +1,self.prevYCor-2))

        if not self.outOfBounds(self.prevXCor-1,self.prevYCor-2):
            if board[self.prevXCor -1][self.prevYCor-2] == 0:
                res.append((self.prevXCor -1,self.prevYCor-2))
        return res


       
      
     
