

import turtle
import os



print("Welcome! Please use arrows to move game pieace and space bar to drop")

#the game board
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    ]

# initializes screen
win = turtle.Screen()

#displays title
win.title("Connect 4: USE ARROW KEYS to move: SPACE to drop")

#screen setup
win.setup(700,700)

#background
win.bgcolor("black")

#traces gameboard
win.tracer(0)

win.listen()

#list used to game pieces
list_ = []


def player_turn(board,row,column,piece):
    board[row][column] = piece


def winning_move(board,piece):

    # Check all horizontal 
    for j in range(4): 
        for r in range(7):
            if board[r][j] == piece and board[r][j+1]==piece and board[r][j+2]==piece and board[r][j+3]==piece:
                return True

    # Vertical 
    for j in range(7): 
        for r in range(4):  
            if board[r][j] == piece and board[r+1][j]==piece and board[r+2][j]==piece and board[r+3][j]==piece:
                return True

    # Check positive diagonals
    for j in range(4): 
        for r in range(4):
            if board[r][j] == piece and board[r+1][j+1]==piece and board[r+2][j+2]==piece and board[r+3][j+3]==piece:
                return True

    # Check negative diagonals
    for j in range(7): 
        for r in range(3, 7):
            if board[r][j] == piece and board[r-1][j+1]==piece and board[r-2][j+2]==piece and board[r-3][j+3]==piece:
                return True
            



class Tile(turtle.Turtle):
    '''
    Class: Tile
    Attributes: self
    Does: creates a square object
    '''
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(5,5)
        self.up()
        self.color('blue')


class Piece(turtle.Turtle):
    '''
    Class: piece
    Atrributes: Color, State
    Methods move_left, move_right, drop

    '''
    def __init__(self,color,state):
        """
        Constructor -- creates a new circle
        parameters:
            Self -- curent object
            color-- color of object
            state -- where the object is 

        """
        super().__init__(shape='circle')
        self.shapesize(4.5,4.5)
        self.up()
        self.c = color
        self.color(self.c)
        self.state = state

    def move_left(self):
        """
        Method: move_left
        Does: moves piece left using left arrow key

        """
        if self.xcor()>-300 and self.state == 'move':
            self.goto(self.xcor()-100, self.ycor())


    def move_right(self):
        """
        Method: move_right
        Does: moves piece right using right arrow key

        """
        if self.xcor()<300 and self.state == 'move':
            self.goto(self.xcor()+100, self.ycor())


    def drop(self):
        """
        Method:drops
        Does: Drops piece into game and also acts as main loop
        """
        global message
        global list_
        global board
        global game_over

        dropped_piece = turtle.Turtle()
        dropped_piece.shape('circle')
        dropped_piece.shapesize(4.5,4.5)
        dropped_piece.color(self.c)
        dropped_piece.up()

        

        for i in y_values[::-1]:
            #adds piece if no pieace is in that place
            if (self.xcor(),i) not in list_:
                ypos = i
                break
            else: # protects against invalid move
                if (self.xcor(), 200) in list_:
                    ypos = 1000
                    print("unable to add")

                    
        #drops piece
        dropped_piece.goto(self.xcor(),ypos)
        #xcordinate
        xcord = dropped_piece.xcor()
        #ycordinate
        ycord = dropped_piece.ycor()

        #ensures user places pieace in correct place 
        if ycord != 1000:
            list_.append((xcord, ycord))
        # player 1 is red
        if self.c == 'red':
            piece = 1
            self.c = 'yellow'
            self.color(self.c)
        else:
            self.c = 'red'
            self.color(self.c)
            piece = 2

        player_turn(board,x_values.index(xcord), y_values.index(ycord),piece)
        
        #checks to see if move was a winning move for player 1
        if winning_move(board,1):
            win.update()
            game_over = True
            message = "Player 1 wins!!!"
        #checks to see if move was a winning move for player 1     
        if winning_move(board,2):
            win.update()
            game_over = True
            message = 'Player 2 wins!!!'


#possible values where the pieace can be dropped
x_values = [-300, -200, -100, -0, 100, 200, 300]
y_values = [200, 100, 0, -100, -200, -300]



for i in x_values:
    for j in y_values:
        tile = Tile()
        tile.goto(i,j)
        piece = Piece('black','still')
        piece.goto(i,j)


piece1 = Piece("red","move")
piece1.goto(0,300)

# uses onkey to move piece right
win.onkey(piece1.move_right, 'Right')
#uses onkey to move piece left
win.onkey(piece1.move_left, 'Left')
#uses spacebar to drop pieace
win.onkey(piece1.drop, 'space')

game_over = False
message = ''

#ensures the game will continue while the board isnt filled
while not game_over:
    if len(list_) >= 42:
        game_over = True
    win.update()

print("Game_OVER")
pen = turtle.Turtle()
pen.up()
pen.hideturtle()
#If player 1 has won, display text in red
if message == "Player 1 wins!!!":
    pen.color("red")
else:
    # if player 2 was, display text in yellow
    pen.color('yellow')

pen.goto(0, 280)
pen.write(f'GAME OVER, {message}', align='center', font=('Courier', 36, 'normal'))

        

    
    


    
