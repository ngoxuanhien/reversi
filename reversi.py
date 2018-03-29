indexs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
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
 if player == 'B':
  for b in bchoices:
   for w in wchoices:
    if b[1] == w[1]:
     if w[0]>b[0]:
      m = w[0]-b[0]
      vchoices.append([w[0] + m,w[1] + m])
     else:
      m = b[0] - w[0]
      vchoices.append([w[0] - m,w[1] + m])
    if b[0] == w[0]:
     if w[1]>b[1]:
      m = w[1] - b[1]
      vchoices.append([w[0], w[1] + 1])
     else:
      m = b[1] - w[1]
      vchoices.append([w[0], w[1]])

 if player == 'W':
  for w in wchoices:
   for b in bchoices:
    if b[1] == w[1]:
     if b[0]>w[0]:
      vchoices.append([b[0] + 1,b[1] + 1])
     else:
      vchoices.append([b[0] - 1,b[1] + 1])
    if b[0] == w[0]:
     if w[1]>b[1]:
      vchoices.append([b[0], b[1] + 4])
     else:
      vchoices.append([b[0], b[1]])
 return vchoices

def convertValid(listValid):
 list = []
 for l in listValid:
  list.append([indexs[l[0]], l[1]])
 return list

mainBoard = getNewBoard()
resetBoard(mainBoard)
drawBoard(mainBoard)
listValidB = validChoices(listChoices(mainBoard), mainBoard, 'B')
listValidW = validChoices(listChoices(mainBoard), mainBoard, 'W')
print(convertValid(listValidB))
print(convertValid(listValidW))
