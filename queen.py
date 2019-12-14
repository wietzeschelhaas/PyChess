import piece
class Queen(piece.Piece):
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
                res.append((self.prevXCor + counter,self.prevYCor))
                break
            counter = counter + 1

        counter = 1
        while self.prevXCor - counter >= 0:
            if board[self.prevXCor - counter][self.prevYCor] == 0:
                res.append((self.prevXCor - counter,self.prevYCor))
            else:
                res.append((self.prevXCor - counter,self.prevYCor))
                break
            counter = counter + 1
        
        counter = 1
        while self.prevYCor + counter < 8:
            if board[self.prevXCor][self.prevYCor + counter] == 0:
                res.append((self.prevXCor,self.prevYCor+counter))
            else:
                res.append((self.prevXCor,self.prevYCor+counter))
                break
            counter = counter + 1

        counter = 1
        while self.prevYCor - counter >= 0:
            if board[self.prevXCor][self.prevYCor - counter] == 0:
                res.append((self.prevXCor,self.prevYCor-counter))
            else:
                res.append((self.prevXCor,self.prevYCor-counter))
                break
            counter = counter + 1
        
        #left up
        counter = 1
        while not self.outOfBounds(self.prevXCor - counter,self.prevYCor
                - counter):
            if board[self.prevXCor - counter][self.prevYCor - counter] == 0:
                res.append((self.prevXCor - counter,self.prevYCor-counter))
            else:
                res.append((self.prevXCor - counter,self.prevYCor-counter))
                break
            counter = counter + 1

        #left down
        counter = 1
        while not self.outOfBounds(self.prevXCor - counter,self.prevYCor
                + counter):
            if board[self.prevXCor - counter][self.prevYCor + counter] == 0:
                res.append((self.prevXCor - counter,self.prevYCor+counter))
            else:
                res.append((self.prevXCor - counter,self.prevYCor+counter))
                break
            counter = counter + 1

        #right down
        counter = 1
        while not self.outOfBounds(self.prevXCor + counter,self.prevYCor
                + counter):
            if board[self.prevXCor + counter][self.prevYCor + counter] == 0:
                res.append((self.prevXCor + counter,self.prevYCor+counter))
            else:
                res.append((self.prevXCor + counter,self.prevYCor+counter))
                break
            counter = counter + 1

        #right up
        counter = 1
        while not self.outOfBounds(self.prevXCor + counter,self.prevYCor
                - counter):
            if board[self.prevXCor + counter][self.prevYCor - counter] == 0:
                res.append((self.prevXCor + counter,self.prevYCor-counter))
            else:
                res.append((self.prevXCor + counter,self.prevYCor-counter))
                break
            counter = counter + 1
        return res




