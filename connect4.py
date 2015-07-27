from Tkinter import * #Need this
import thread #Need this
import random #Need this
import time #need this


root = Tk() #Need this
root.title("Connect Four") #need this

# Normally 7 and 6, but could make bigger board
cols = 7
rows = 6
square_size = 50
padding = 100
width = square_size * cols + 2 * padding  # Add padding on each side
height = square_size * rows + 2 * padding  # Add padding on top and bottom

root.geometry("%sx%s" % (width, height))  # Need this

#create connect four board (not the graphics...just the
#logical board representation)
board = cols*[rows*[-1]]

#records whether it's X or O's turn
turn=0

canvas = Canvas(root, width=width, height=height)  # Need this

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

        global canvas, root, rows, cols, padding, square_size
        print 'in draw thread'
        over = False

        # Draw horizontal lines
        for i in range(rows + 1):
                canvas.create_line(padding, padding + i * square_size,
                                   padding + cols * square_size, padding + i * square_size)

        # Draw vertical lines
        for i in range(cols + 1):
                canvas.create_line(padding + i * square_size, padding,
                                   padding + i * square_size, padding + rows * square_size)

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
                        canvas.create_text(width/2,height/2, text="X WINS!",font=("helvetica","18"))
                #if O wins, put appropriate message on screen
                elif winner == 1: 
                        over=True
                        canvas.create_text(width/2,height/2, text="O WINS!", font=("helvetica","18"))
                #if draw, put appropriate message on screen
                if draw() == True:
                        over=True
                        canvas.create_text(width/2,height/2, text="DRAW!", font=("helvetica","18"))
                        


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
        

#Assuming the user has clicked cell i,j, this
#function checks to see if it's a valid move. If
#so, it places the appropriate X or O there.
def processMove(col, row):
        global board, turn

        print col, row
        #case 1 -- already been clicked
        if board[col][row] >= 0:
                return
        #case 2 -- if clicked cell is not already taken
        elif board[col][row] <0:
                board[col][row] = turn
                turn = (turn + 1) % 2


#Function that handles mouse clicks. From the x,y coordinate
# of the mouse click, it calculates the corresponding i,j
# of the board.
        
def buttonPressed(event):
        #will want to change turn so declare global 
        global padding, square_size, turn

        # Only process click if it is inside board
        if (event.x > padding and event.x < (width - padding) and
                            event.y > padding and event.y < (height - padding)):
                # Calculate col and row based on event x and y
                col = (event.x - padding) / square_size
                row = (event.y - padding) / square_size
                processMove(col, row)


#Bind left mouse button clicks to the buttonPressed function
root.bind("<Button-1>",buttonPressed)

#make the canvas visible on the root window
canvas.pack()

#start the drawing thread
startDrawing()

#show the main window
root.mainloop()
