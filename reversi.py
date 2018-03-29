index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def drawBoard(board):
 print('  a  b  c  d  e  f  g  h  \n')
 for i in range(8):
  row = '  '.join(x for x in board[i])
  print(str(i) + ' ' + row + '\n')

def resetBoard(board):
 #starting pieces:
 board[3][3] = 'W'
 board[3][4] = 'B'
 board[4][3] = 'B'
 board[4][4] = 'W'

def getNewBoard():
 board = []
 for i in range(8):
  board.append(['.']*8)
 return board

def playerChoices(board, player):
 pchoices = []
 for x in range(8):
  for y in range(8):
   if str(board[x][y]) == player:
    pchoices.append([x,y])
 return pchoices

def listChoices(board):
 choices = []
 for x in range(8):
  for y in range(8):
   if str(board[x][y]) != 'B' and str(board[x][y]) != 'W':
    choices.append([x,y])
 return choices

def validChoices(choices, board, player):
 bchoices = playerChoices(board, 'B')
 wchoices = playerChoices(board, 'W')
 vchoices = []
 for b in bchoices:
   for w in wchoices:
    if b[0] == w[0]:
      if player == 'B':
       m = w[0] + 1
      print(m)
mainBoard = getNewBoard()
resetBoard(mainBoard)
drawBoard(mainBoard)
validChoices(listChoices(mainBoard), mainBoard, 'B')
