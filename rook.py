import piece
class Rook(piece.Piece):
    def __init__(self,img,x,y,isWhite,n):
        super().__init__(img,x,y,isWhite,n)

    
    def draw(self,win):
        self.drawPiece(win)


    def tilesMoveable(self,board):
        res = []
        
        counter = 1
        while self.prevXCor + counter < 8:
            if board[self.prevXCor + counter][self.prevYCor] == 0:
                res.append((self.prevXCor + counter,self.prevYCor))
            else:
                break
            counter = counter + 1

        counter = 1
        while self.prevXCor - counter >= 0:
            if board[self.prevXCor - counter][self.prevYCor] == 0:
                res.append((self.prevXCor - counter,self.prevYCor))
            else:
                break
            counter = counter + 1
        
        counter = 1
        while self.prevYCor + counter < 8:
            if board[self.prevXCor][self.prevYCor + counter] == 0:
                res.append((self.prevXCor,self.prevYCor+counter))
            else:
                break
            counter = counter + 1

        counter = 1
        while self.prevYCor - counter >= 0:
            if board[self.prevXCor][self.prevYCor - counter] == 0:
                res.append((self.prevXCor,self.prevYCor-counter))
            else:
                break
            counter = counter + 1

        return res
