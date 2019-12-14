import copy

#this functrion given all arguemnts will check to see if the move the players wants to make is a legal one
def isLegalMove(playersTurn, whiteIncheck, toMove, whiteKing,x,y,reachableMoves,board):
    if playersTurn and whiteIncheck and toMove != whiteKing:
        return False
    if not (x,y) in reachableMoves:
        return False
        

    #TODO MAKE SURE TO REVERT CHANGES
    #make the move
    board[toMove.prevXCor][toMove.prevYCor] = 0
    board[x][y] = toMove
    #now check if king is attacked, if it is, the piece was pinned 
    if whiteKing.isBeingAttacked(board):
        print("test")
        board[x][y] = 0
        board[toMove.prevXCor][toMove.prevYCor] = toMove
        return False
    

    #Must revert the changes either way
    board[x][y] = 0
    board[toMove.prevXCor][toMove.prevYCor] = toMove
    return True