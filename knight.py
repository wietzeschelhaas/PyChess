import piece
import rules
class Knight(piece.Piece):
    def __init__(self,img,x,y,isWhite,n):
        super().__init__(img,x,y,isWhite,n)

    
    def draw(self,win):
        self.drawPiece(win)

    def tilesMoveable(self,playerTurn,whiteKing,rookQueenSide,rookKingSide,board):
        res = []
        
        if not self.outOfBounds(self.prevXCor-2,self.prevYCor+1):
            if board[self.prevXCor -2][self.prevYCor +1] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor -2,self.prevYCor+1,board):
                    res.append((self.prevXCor -2,self.prevYCor+1)) 

        if not self.outOfBounds(self.prevXCor-2,self.prevYCor-1):
            if board[self.prevXCor -2][self.prevYCor-1] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor -2,self.prevYCor-1,board):
                    res.append((self.prevXCor -2,self.prevYCor-1))

        if not self.outOfBounds(self.prevXCor+2,self.prevYCor-1):
            if board[self.prevXCor +2][self.prevYCor-1] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor +2,self.prevYCor-1,board):
                    res.append((self.prevXCor +2,self.prevYCor-1))
        
        if not self.outOfBounds(self.prevXCor+2,self.prevYCor+1):
            if board[self.prevXCor +2][self.prevYCor+1] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor +2,self.prevYCor+1,board):
                    res.append((self.prevXCor +2,self.prevYCor+1))

        if not self.outOfBounds(self.prevXCor+1,self.prevYCor+2):
            if board[self.prevXCor +1][self.prevYCor+2] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor +1,self.prevYCor+2,board):
                    res.append((self.prevXCor +1,self.prevYCor+2))
        
        if not self.outOfBounds(self.prevXCor-1,self.prevYCor+2):
            if board[self.prevXCor -1][self.prevYCor+2] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor -1,self.prevYCor+2,board):
                    res.append((self.prevXCor -1,self.prevYCor+2))
        
        if not self.outOfBounds(self.prevXCor+1,self.prevYCor-2):
            if board[self.prevXCor +1][self.prevYCor-2] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor +1,self.prevYCor-2,board):
                    res.append((self.prevXCor +1,self.prevYCor-2))

        if not self.outOfBounds(self.prevXCor-1,self.prevYCor-2):
            if board[self.prevXCor -1][self.prevYCor-2] == 0:
                if rules.isLegalMove(playerTurn,self,whiteKing,self.prevXCor -1,self.prevYCor-2,board):
                    res.append((self.prevXCor -1,self.prevYCor-2))
        return res


       
      
     
