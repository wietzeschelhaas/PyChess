import piece
class Pawn(piece.Piece):
    def __init__(self,img,x,y,isWhite):
        super().__init__(img,x,y,isWhite)

    
    def draw(self,win):
        self.drawPiece(win)


    #returns a list of tiles the piece can move to
    def tilesMoveable(self,board):
        res = []
        if self.prevYCor == 6:
            if board[self.prevXCor][5] == 0:
                res.append((self.prevXCor,5))
            if board[self.prevXCor][4] == 0:
                res.append((self.prevXCor,4))
        elif board[self.prevXCor][self.prevYCor-1] == 0:
            res.append((self.prevXCor,self.prevYCor-1))

        # if there is a black piece there.TODO if pawn moves here black
        # piece should be removed
        if not self.outOfBounds(self.prevXCor+1,self.prevYCor-1):
            if not board[self.prevXCor+1][self.prevYCor -1] == 0:
                if not board[self.prevXCor+1][self.prevYCor -1].isWhite:
                    res.append((self.prevXCor+1,self.prevYCor -1))
                        
        if not self.outOfBounds(self.prevXCor-1,self.prevYCor-1):
            if not board[self.prevXCor-1][self.prevYCor -1] == 0:
                if not board[self.prevXCor+1][self.prevYCor -1].isWhite:
                    res.append((self.prevXCor+1,self.prevYCor -1))

        #TODO En passant
        return res



