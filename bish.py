import piece
class Bish(piece.Piece):
    def __init__(self,img,x,y,isWhite,n):
        super().__init__(img,x,y,isWhite,n)

    
    def draw(self,win):
        self.drawPiece(win)


    def tilesMoveable(self,board):
        res = []
        
        #left up
        counter = 1
        while not self.outOfBounds(self.prevXCor - counter,self.prevYCor
                - counter):
            if board[self.prevXCor - counter][self.prevYCor - counter] == 0:
                res.append((self.prevXCor - counter,self.prevYCor-counter))
            else:
                break
            counter = counter + 1

        #left down
        counter = 1
        while not self.outOfBounds(self.prevXCor - counter,self.prevYCor
                + counter):
            if board[self.prevXCor - counter][self.prevYCor + counter] == 0:
                res.append((self.prevXCor - counter,self.prevYCor+counter))
            else:
                break
            counter = counter + 1

        #right down
        counter = 1
        while not self.outOfBounds(self.prevXCor + counter,self.prevYCor
                + counter):
            if board[self.prevXCor + counter][self.prevYCor + counter] == 0:
                res.append((self.prevXCor + counter,self.prevYCor+counter))
            else:
                break
            counter = counter + 1

        #right up
        counter = 1
        while not self.outOfBounds(self.prevXCor + counter,self.prevYCor
                - counter):
            if board[self.prevXCor + counter][self.prevYCor - counter] == 0:
                res.append((self.prevXCor + counter,self.prevYCor-counter))
            else:
                break
            counter = counter + 1
        return res


