from Tkinter import * #Need this
import thread #Need this
import random #Need this
import time #need this

root = Tk() #Need this
#size = 500?
root.title("Connect Four") #need this

#since Connect Four is 7x6, making padding 100/50 allows for a buffer of 2 pixels left/right/above/below Connect Four board

# Normally 7 and 6, but could make bigger board
cols = 7
rows = 6
square_size = 50
padding = 100
#xSize = ySize
width = square_size * cols + 2 * padding  # Add padding on each side
height = square_size * rows + 2 * padding  # Add padding on top and bottom

root.geometry("%sx%s" % (width, height))  # Why change from original "root.geometry("500x500")"
# I changed this because the new board doesn't fit well in 500 square

#create connect four board (not the graphics...just the
#logical board representation)
board = []  #  More rows & cols

#records whether it's X or O's turn
turn=0

canvas = Canvas(root, width=width, height=height)  # Need this

#Frame rate is how often canvas will be updated
# each second. For Connect four, 10 should be plenty.
FRAME_RATE = 10  # this is fine (SLEEP VS UPDATE)


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

        def draw_board():
                #counter variable
                i=0

                #board variable is what stores the X/O/- values.
                # It's a 2D list. We iterate over it, looking to see
                # if there is a value that is X or O. If so, we draw
                # text to the screen in the appropriate spot (based on
                # i and j.
                while i < len(board):
                        j=0
                        left = padding + i * square_size + 20
                        while j < len(board[i]):
                                top = padding + j * square_size + 20
                                if board[i][j] == 0:
                                        lst2.append(canvas.create_text(left, top, text="X", font=("helvetica","36")))
                                elif board[i][j] == 1:
                                        lst2.append(canvas.create_text(left, top, text="O", font=("helvetica","36")))
                                j+=1

                        i+=1

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
                
                draw_board()

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
                        draw_board()
                        canvas.create_text(width/2,height/2, text="X WINS!",font=("helvetica","18"))
                #if O wins, put appropriate message on screen
                elif winner == 1: 
                        over=True
                        draw_board()
                        canvas.create_text(width/2,height/2, text="O WINS!", font=("helvetica","18"))
                #if draw, put appropriate message on screen
                if draw() == True:
                        over=True
                        draw_board()
                        canvas.create_text(width/2,height/2, text="DRAW!", font=("helvetica","18"))
                        


#detect win condition in board 
# win is FOUR of the same vert/horiz/diag
# should return -1 for no win, 0 for x win, 1 for o win
def win():
        #Does a player have four in a row?
        if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == board[3][0] and board[0][0] != -1:
                return board[0][0]
        if board[1][0] == board[2][0] and board[2][0] == board[3][0] and board[3][0] == board[4][0] and board[1][0] != -1:
                return board[1][0]
        if board[2][0] == board[3][0] and board[3][0] == board[4][0] and board[4][0] == board[5][0] and board[2][0] != -1:
                return board[2][0]
        if board[3][0] == board[4][0] and board[4][0] == board[5][0] and board[5][0] == board[6][0] and board[3][0] != -1:
                return board[3][0] 
            
        if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == board[3][1] and board[0][1] != -1:
                return board[0][1]
        if board[1][1] == board[2][1] and board[2][1] == board[3][1] and board[3][1] == board[4][1] and board[1][1] != -1:
                return board[1][1]
        if board[2][1] == board[3][1] and board[3][1] == board[4][1] and board[4][1] == board[5][1] and board[2][1] != -1:
                return board[2][1]
        if board[3][1] == board[4][1] and board[4][1] == board[5][1] and board[5][1] == board[6][1] and board[3][1] != -1:
                return board[3][1]

        if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == board[3][2] and board[0][2] != -1:
                return board[0][2]
        if board[1][2] == board[2][2] and board[2][2] == board[3][2] and board[3][2] == board[4][2] and board[1][2] != -1:
                return board[1][2]
        if board[2][2] == board[3][2] and board[3][2] == board[4][2] and board[4][2] == board[5][2] and board[2][2] != -1:
                return board[2][2]
        if board[3][2] == board[4][2] and board[4][2] == board[5][2] and board[5][2] == board[6][2] and board[3][2] != -1:
                return board[3][2]

        if board[0][3] == board[1][3] and board[1][3] == board[2][3] and board[2][3] == board[3][3] and board[0][3] != -1:
                return board[0][3]
        if board[1][3] == board[2][3] and board[2][3] == board[3][3] and board[3][3] == board[4][3] and board[1][3] != -1:
                return board[1][3]
        if board[2][3] == board[3][3] and board[3][3] == board[4][3] and board[4][3] == board[5][3] and board[2][3] != -1:
                return board[2][3]
        if board[3][3] == board[4][3] and board[4][3] == board[5][3] and board[5][3] == board[6][3] and board[3][3] != -1:
                return board[3][3]

        if board[0][4] == board[1][4] and board[1][4] == board[2][4] and board[2][4] == board[3][4] and board[0][4] != -1:
                return board[0][4]
        if board[1][4] == board[2][4] and board[2][4] == board[3][4] and board[3][4] == board[4][4] and board[1][4] != -1:
                return board[1][4]
        if board[2][4] == board[3][4] and board[3][4] == board[4][4] and board[4][4] == board[5][4] and board[2][4] != -1:
                return board[2][4]
        if board[3][4] == board[4][4] and board[4][4] == board[5][4] and board[5][4] == board[6][4] and board[3][4] != -1:
                return board[3][4]

        if board[0][5] == board[1][5] and board[1][5] == board[2][5] and board[2][5] == board[3][5] and board[0][5] != -1:
                return board[0][5]
        if board[1][5] == board[2][5] and board[2][5] == board[3][5] and board[3][5] == board[4][5] and board[1][5] != -1:
                return board[1][5]
        if board[2][5] == board[3][5] and board[3][5] == board[4][5] and board[4][5] == board[5][5] and board[2][5] != -1:
                return board[2][5]
        if board[3][5] == board[4][5] and board[4][5] == board[5][5] and board[5][5] == board[6][5] and board[3][5] != -1:
                return board[3][5]
               
        #Does a player have four in a column?
        if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == board[0][3] and board[0][0] != -1:
                return board[0][0]
        if board[0][1] == board[0][2] and board[0][2] == board[0][3] and board[0][3] == board[0][4] and board[0][1] != -1:
                return board[0][1]
        if board[0][2] == board[0][3] and board[0][3] == board[0][4] and board[0][4] == board[0][5] and board[0][2] != -1:
                return board[0][2]
            
        if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == board[1][3] and board[1][0] != -1:
                return board[1][0]
        if board[1][1] == board[1][2] and board[1][2] == board[1][3] and board[1][3] == board[1][4] and board[1][1] != -1:
                return board[1][1]
        if board[1][2] == board[1][3] and board[1][3] == board[1][4] and board[1][4] == board[1][5] and board[1][2] != -1:
                return board[1][2]

        if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == board[2][3] and board[2][0] != -1:
                return board[2][0]
        if board[2][1] == board[2][2] and board[2][2] == board[2][3] and board[2][3] == board[2][4] and board[2][1] != -1:
                return board[2][1]
        if board[2][2] == board[2][3] and board[2][3] == board[2][4] and board[2][4] == board[2][5] and board[2][2] != -1:
                return board[2][2]

        if board[3][0] == board[3][1] and board[3][1] == board[3][2] and board[3][2] == board[3][3] and board[3][0] != -1:
                return board[3][0]
        if board[3][1] == board[3][2] and board[3][2] == board[3][3] and board[3][3] == board[3][4] and board[3][1] != -1:
                return board[3][1]
        if board[3][2] == board[3][3] and board[3][3] == board[3][4] and board[3][4] == board[3][5] and board[3][2] != -1:
                return board[3][2]

        if board[4][0] == board[4][1] and board[4][1] == board[4][2] and board[4][2] == board[4][3] and board[4][0] != -1:
                return board[4][0]
        if board[4][1] == board[4][2] and board[4][2] == board[4][3] and board[4][3] == board[4][4] and board[4][1] != -1:
                return board[4][1]
        if board[4][2] == board[4][3] and board[4][3] == board[4][4] and board[4][4] == board[4][5] and board[4][2] != -1:
                return board[4][2]

        if board[5][0] == board[5][1] and board[5][1] == board[5][2] and board[5][2] == board[5][3] and board[5][0] != -1:
                return board[5][0]
        if board[5][1] == board[5][2] and board[5][2] == board[5][3] and board[5][3] == board[5][4] and board[5][1] != -1:
                return board[5][1]
        if board[5][2] == board[5][3] and board[5][3] == board[5][4] and board[5][4] == board[5][5] and board[5][2] != -1:
                return board[5][2]

        if board[6][0] == board[6][1] and board[6][1] == board[6][2] and board[6][2] == board[6][3] and board[6][0] != -1:
                return board[6][0]
        if board[6][1] == board[6][2] and board[6][2] == board[6][3] and board[6][3] == board[6][4] and board[6][1] != -1:
                return board[6][1]
        if board[6][2] == board[6][3] and board[6][3] == board[6][4] and board[6][4] == board[6][5] and board[6][2] != -1:
                return board[6][2]
    
        #Does a player have a diagonal?
        if board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[2][1] == board[3][0] and board[0][3] != -1:
                return board[0][3]
        if board[0][4] == board[1][3] and board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[0][4] != -1:
                return board[0][4]
        if board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[3][1] == board[4][0] and board[1][3] != -1:
                return board[1][3]
        if board[0][5] == board[1][4] and board[1][4] == board[2][3] and board[2][3] == board[3][2] and board[0][5] != -1:
                return board[0][5]
        if board[1][4] == board[2][3] and board[2][3] == board[3][2] and board[3][2] == board[4][1] and board[1][4] != -1:
                return board[1][4]
        if board[2][3] == board[3][2] and board[3][2] == board[4][1] and board[4][1] == board[5][0] and board[2][3] != -1:
                return board[2][3]
        if board[1][5] == board[2][4] and board[2][4] == board[3][3] and board[3][3] == board[4][2] and board[1][5] != -1:
                return board[1][5]
        if board[2][4] == board[3][3] and board[3][3] == board[4][2] and board[4][2] == board[5][1] and board[2][4] != -1:
                return board[2][4]
        if board[3][3] == board[4][2] and board[4][2] == board[5][1] and board[5][1] == board[6][0] and board[3][3] != -1:
                return board[3][3]
        if board[2][5] == board[3][4] and board[3][4] == board[4][3] and board[4][3] == board[5][2] and board[2][5] != -1:
                return board[2][5]
        if board[3][4] == board[4][3] and board[4][3] == board[5][2] and board[5][2] == board[6][1] and board[3][4] != -1:
                return board[3][4]
        if board[3][5] == board[4][4] and board[4][4] == board[5][3] and board[5][3] == board[6][2] and board[3][5] != -1:
                return board[3][5]
            
        return -1

#If there is no winner but all the spaces are taken, then there must be a tie.
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
def grid(cols, rows):
        for col in range(cols):
                col_data = []
                for row in range(rows):
                        col_data.append(-1)
                board.append(col_data)


#Assuming the user has clicked cell i,j, this
#function checks to see if it's a valid move. If
#so, it places the appropriate X or O there.
def processMove(col, row):
        global board, rows, turn, padding, square_size

        #case 1 -- already been clicked
        if board[col][row] >= 0:
                print "Location %s, %s has already been taken" % (col, row)
                return
        #case 2 -- if clicked cell is not already taken
        else:
                row_index = row
                # Loop to find lowest empty row
                while row_index < rows - 1:
                        if board[col][row_index + 1] >= 0:
                                break
                        row_index += 1
                board[col][row_index] = turn
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


#create connect four board (not the graphics...just the
#logical board representation)
grid(cols, rows)

#Bind left mouse button clicks to the buttonPressed function
root.bind("<Button-1>",buttonPressed)

#make the canvas visible on the root window
canvas.pack()

#start the drawing thread
startDrawing()

#show the main window
root.mainloop()
