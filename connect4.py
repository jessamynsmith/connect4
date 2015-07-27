from Tkinter import * #Need this
import thread #Need this
import random #Need this
import time #need this


root = Tk() #Need this
size = 500
root.geometry("400x400") #Need this
root.title("Connect Four") #need this

#Since C4 is 6x7, making padding 400/4 allows
#for a buffer of 100 pixels left/right/above/below
#TicTacToe board

padding = size / 50 # LEAVE ALONE
#xSize = ySize = 0
board = []
#Normally 7 and 6, but could make bigger board
rows=0
cols=0
#records whether it's X or O's turn
turn=0

canvas = Canvas(root,width=size, height=size) #Need this

#Frame rate is how often canvas will be updated
# each second. For Connect four, 10 should be plenty.
FRAME_RATE = 10  # this is fine


#Function responsible for starting the drawing thread
def startDrawing():
        thread.start_new(drawThread,())


#Function where the drawing thread picks up.
# It runs independently of the mainloop(), but
# it can still access global variables if needed.
def drawThread():

        #Width and height of each 'block' on the screen.
        #This number is in pixels.
        width = size / 10  #At 5, board went off screen
        height = size / 10  #At 5, board went off screen

        #declare canvas and root as global since
        # we want to be able to interact with them.
        global canvas, root
        print 'in draw thread'
        over = False

        #five horizontal lines.  These lines won't be
        # deleted since they should always be there.
        #Why are the beginning and end points what they are?
        canvas.create_line(width,height*2,width*8,height*2)
        canvas.create_line(width,height*3,width*8,height*3)
        canvas.create_line(width,height*4,width*8,height*4) # ADDED
        canvas.create_line(width,height*5,width*8,height*5)  # ADDED
        canvas.create_line(width,height*6,width*8,height*6)  # ADDED
        
        #six vertical lines.  These lines won't be
        # deleted since they should always be there.
        #Why are the beginning and end points what they are?
        canvas.create_line(width*2,height,width*2,height*7)
        canvas.create_line(width*3,height,width*3,height*7)
        canvas.create_line(width*4,height,width*4,height*7)
        canvas.create_line(width*5,height,width*5,height*7)
        canvas.create_line(width*6,height,width*6,height*7)
        canvas.create_line(width*7,height,width*7,height*7)     

        #over becomes True when the game is over (win or draw)
        while over == False:
                #List variable to store the text objects from
                #when we draw X and O in different cells of the board
                #Not used to delete yet, but program could be extended
                #to "start new game". To do this, the X's and O's that
                #have been draw would need to be deleted.
                lst2 = []
                
                #counter variable
                i=0
                
                #board variable is what stores the X/O/- values.
                # It's a 2D list. We iterate over it, looking to see
                # if there is a value that is X or O. If so, we draw
                # text to the screen in the appropriate spot (based on
                # i and j.
                while i < len(board):
                        j=0
                        while j < len(board[i]):

                                if board[i][j] == 0:
                                        lst2.append(canvas.create_text((i+1)*width + width/2 + 1,(j+1)*height + height/2 +1 ,text="X"))
                                elif board[i][j] == 1:
                                        lst2.append(canvas.create_text((i+1)*width + width/2 + 1,(j+1)*height + height/2 +1 ,text="O"))
                                j+=1
                        
                        i+=1

                #like the bind() call, this updates the screen
                root.update_idletasks()

                #puts the program to sleep for 100 ms
                #(since frame rate is 10)
                time.sleep(1.0 / FRAME_RATE)

                #call win method to check to see if someone ones
                winner = win()

                #if X wins, put appropriate message on screen
                if winner == 0:
                        over=True
                        canvas.create_text(size/2,size/2, text="X WINS!",font=("helvetica","18"))
                #if O wins, put appropriate message on screen
                elif winner == 1: 
                        over=True
                        canvas.create_text(size/2,size/2, text="O WINS!", font=("helvetica","18"))
                #if draw, put appropriate message on screen
                if draw() == True:
                        over=True
                        canvas.create_text(size/2,size/2, text="DRAW!", font=("helvetica","18"))
                        


#detect win condition in board 
# win is FOUR of the same vert/horiz/diag
# should return -1 for no win, 0 for x win, 1 for o win
def win():
        #Does a player have four in a row?
        if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != -1:
                return board[0][0]
        if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != -1:
                return board[1][0]
        if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != -1:
                return board[2][0]
    
        #Does a player have four in a column?
        if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != -1:
                return board[0][0]
        if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != -1:
                return board[0][1]
        if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != -1:
                return board[0][2]
    
        #Does a player have a diagonal?
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != -1:
                return board[0][0]
        if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != -1:
                return board[2][0]

        return -1

#If there is no winner but all the spaces are taken,
#then there must be a tie.
def draw():
        for row in board:
                for cell in row:
                #if a cell is not taken, can't be a draw
                        if cell == -1:
                                return False
        #If there is a winner, then there can't be a draw
        if win()>=0:
                return False
        #Otherwise, there must be a draw
        else:
                return True




#This function is called to set up the board. 7 and 6
#are usually passed as arguments 
def grid(x,y):

        global cols,rows
        i=0
        #set number of columns and rows 
        cols=x
        rows=y

        #initialize board with 42 -1's
        while i<x:
                #remember, board is a 2D list
                board.append([])
                j=0
                while j < y:
                        #-1 means no move yet
                        board[i].append(-1)
                        j+=1
                i+=1
        

#Assuming the user has clicked cell i,j, this
#function checks to see if it's a valid move. If
#so, it places the appropriate X or O there.
def processMove(i,j):
        global board, turn

        #case 1 -- if i or j is off the board
        if i < 0 or i >= len(board) or j < 0 or j>=len(board[i]):
                return
        #case 2 -- already been clicked
        elif board[i][j]>=0:
                return
        #case 3 -- if clicked cell is not already taken
        elif board[i][j] <0:
                board[i][j] = turn
                turn = (turn + 1) % 2




#Function that handles mouse clicks. From the x,y coordinate
# of the mouse click, it calculates the corresponding i,j
# of the board.
        
def buttonPressed(event):
        #will want to change turn so declare global 
        global turn

        #padding is 100 (for a 500x500 board). This is the
        #size of each cell. Recall that / does integer math
        #so that 323 / 100 is actually 3. If someone clicks at
        #pixel 250,250, then i and j are both set to 2.
        i = event.x / padding
        j = event.y / padding
        #debug print so we can see what i,j it calculates
        print i, ' ' ,j
        #If they click 2,2, then we want to change board[1][1]
        processMove(i-1,j-1)


#create connect four board (not the graphics...just the
#logical board representation)
grid(6,7)

#Bind left mouse button clicks to the buttonPressed function
root.bind("<Button-1>",buttonPressed)

#make the canvas visible on the root window
canvas.pack()

#start the drawing thread
startDrawing()

#show the main window
root.mainloop()
