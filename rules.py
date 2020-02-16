    # TODO can we change back to 0 if the tile there is not empty????
def revertChanges(board, toMove, xTemp,yTemp):
    board[toMove.prevXCor][toMove.prevYCor] = 0
    toMove.prevXCor = xTemp
    toMove.prevYCor = yTemp
    board[toMove.prevXCor][toMove.prevYCor] = toMove



#this functrion given all arguemnts will check to see if the move the players wants to make is a legal one
def isLegalMove(playersTurn, toMove, whiteKing,x,y,board):

    #if its blacks turn and we try to move a white piece
    if not playersTurn and toMove.isWhite:
        print("tried to move white piece when its blacksturn")
        return False
        
    #white is in check before making a move
    whiteIncheckBeforeMove = whiteKing.isBeingAttacked(board)

    #make the move
    board[toMove.prevXCor][toMove.prevYCor] = 0
    board[x][y] = toMove
    xTemp = toMove.prevXCor 
    yTemp = toMove.prevYCor
    toMove.prevXCor = x
    toMove.prevYCor = y

    whiteIncheckAfterMove = whiteKing.isBeingAttacked(board)

    if not whiteIncheckBeforeMove and whiteIncheckAfterMove and playersTurn:
        #The piece is pinned
        print("king is in check!")
        revertChanges(board,toMove,xTemp,yTemp)
        return False
    
    if playersTurn and whiteIncheckAfterMove:
        print("king is in check!")
        print("test")
        revertChanges(board,toMove,xTemp,yTemp)
        return False

    #Must revert the changes either way
    revertChanges(board,toMove,xTemp,yTemp)
    return True
