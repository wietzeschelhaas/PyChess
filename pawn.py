import piece
class Pawn(piece.Piece):
    def __init__(self,img,x,y,isWhite,n):
        super().__init__(img,x,y,isWhite,n)

    
    def draw(self,win):
        self.drawPiece(win)


    #returns a list of tiles the piece can move to
    def tilesMoveable(self,board):
        if self.isWhite:
            res = []
            if self.prevYCor == 6: #if pawn is still at first position it can move two steps forward
                if board[self.prevXCor][5] == 0:
                    res.append((self.prevXCor,5))
                if board[self.prevXCor][4] == 0:
                    res.append((self.prevXCor,4))
            elif board[self.prevXCor][self.prevYCor-1] == 0: #if its not at first position it can only move 1 step forward 
                res.append((self.prevXCor,self.prevYCor-1))

            # if there is a black piece diagonoly from pawn.TODO if pawn moves here blackpiece should be removed
            if not self.outOfBounds(self.prevXCor+1,self.prevYCor-1):
                if not board[self.prevXCor+1][self.prevYCor -1] == 0:
                    if not board[self.prevXCor+1][self.prevYCor -1].isWhite:
                        res.append((self.prevXCor+1,self.prevYCor -1))
                            
            if not self.outOfBounds(self.prevXCor-1,self.prevYCor-1):
                if not board[self.prevXCor-1][self.prevYCor -1] == 0:
                    if not board[self.prevXCor-1][self.prevYCor -1].isWhite:
                        res.append((self.prevXCor+1,self.prevYCor -1))

            #TODO En passant
            return res
        #black movement
        else:
            res = []
            if self.prevYCor == 1: #if pawn is still at first position it can move two steps forward
                if board[self.prevXCor][2] == 0:
                    res.append((self.prevXCor,2))
                if board[self.prevXCor][3] == 0:
                    res.append((self.prevXCor,3))
            elif board[self.prevXCor][self.prevYCor+1] == 0: #if its not at first position it can only move 1 step forward 
                res.append((self.prevXCor,self.prevYCor+1))

            # if there is a black piece diagonoly from pawn.TODO if pawn moves here blackpiece should be removed
            if not self.outOfBounds(self.prevXCor+1,self.prevYCor+1):
                if not board[self.prevXCor+1][self.prevYCor +1] == 0:
                    if board[self.prevXCor+1][self.prevYCor +1].isWhite:
                        res.append((self.prevXCor+1,self.prevYCor +1))
                            
            if not self.outOfBounds(self.prevXCor-1,self.prevYCor+1):
                if not board[self.prevXCor-1][self.prevYCor +1] == 0:
                    if board[self.prevXCor-1][self.prevYCor +1].isWhite:
                        res.append((self.prevXCor-1,self.prevYCor +1))
            return res





