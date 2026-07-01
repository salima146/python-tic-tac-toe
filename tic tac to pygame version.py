#libraries
import tkinter

def set_tile(row, column):
    global current_player

    if (Game_End):
        return

    if Main_Board[row][column]["text"] != "":
        return #this is for an already occupied spot, so cant overlap it

    Main_Board[row][column]["text"] = current_player # this will mark the board X or O
    if current_player == O_player: #switch between the players
        current_player = X_player
    else:
        current_player = O_player
    label["text"] = current_player + "'s turn"

    winner()

def winner():
    global player_turns, Game_End
    player_turns += 1
    #check horizontally the 3 rows
    for row in range(3):
        if (Main_Board[row][0]["text"] == Main_Board[row][1]["text"] == Main_Board[row][2]["text"]
            and Main_Board[row][0]["text"] != ""):
            label.config(text=Main_Board[row][0]["text"] +" is the winner!", foreground = Highlight_colour)
            for column in range(3):
                Main_Board[row][column].config(foreground = Highlight_colour, background = Lines_colour)
            Game_End = True
            return

    #check vertically the 3 columns
    for column in range(3):
        if (Main_Board[0][column]["text"] == Main_Board[1][column]["text"] == Main_Board[2][column]["text"]
            and Main_Board[0][column]["text"] != ""):
            label.config(text = Main_Board[0][column]["text"]+" is the winner!", foreground = Highlight_colour)
            for row in range(3):
                Main_Board[row][column].config(foreground = Highlight_colour, background = Lines_colour)
            Game_End = True
            return

    #check diagonal
    if (Main_Board[0][0]["text"] == Main_Board[1][1]["text"] == Main_Board[2][2]["text"]
        and Main_Board[0][0]["text"] != ""):
        label.config(text = Main_Board[0][0]["text"]+" is the winner!", foreground = Highlight_colour)
        for k in range(3):
            Main_Board[k][k].config(foreground = Highlight_colour, background = Lines_colour)
        Game_End = True
        return

    #other side of the diagonal
    if (Main_Board[0][2]["text"] == Main_Board[1][1]["text"] == Main_Board[2][0]["text"]
        and Main_Board[0][2]["text"] != ""):
        label.config(text = Main_Board[0][2]["text"]+" is the winner!", foreground = Highlight_colour)
        Main_Board[0][2].config(foreground = Highlight_colour, background = Lines_colour)
        Main_Board[1][1].config(foreground = Highlight_colour, background = Lines_colour)
        Main_Board[2][0].config(foreground = Highlight_colour, background = Lines_colour)
        Game_End = True
        return

    #now for the tie condition
    if (player_turns == 9):
        Game_End = True
        label.config(text = "Tie!", foreground = Highlight_colour)

def New_Game():
    global player_turns, Game_End

    player_turns = 0
    Game_End = False
    label.config(text = current_player+"'s turn", foreground = "white")
    for row in range(3):
        for column in range(3):
            Main_Board[row][column].config(text = "", foreground = Shape_colour, background = BG_colour)
    
 









#main variables
X_player = "X"
O_player = "O"
current_player = X_player
Main_Board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

#Colours
BG_colour = "#FC8EAC" #hexadecimal used for the specific colours
Lines_colour = "#FFB6C1"
Shape_colour = "#FFD1DC"
Highlight_colour = "#FFA6C9"

player_turns = 0
Game_End = False




#Window setup
Window = tkinter.Tk() #creates the game window
Window.title("Tic Tac Toe") #title for the window
Window.resizable(False, False) #this is so the window cant be resized


frame = tkinter.Frame(Window)
label = tkinter.Label(frame, text=current_player+"'s turn", font = ("Consolas", 20), background = BG_colour,
                      foreground = "white") # this is label where it will show the current matter of the game

label.grid(row = 0, column = 0, columnspan = 3, sticky = "we") #position of the label

for row in range(3):#this is for the button
    for column in range(3):
        Main_Board[row][column] = tkinter.Button(frame, text = "", font = ("Consolas", 50, "bold"),
                                                 background = BG_colour, foreground = Shape_colour, width = 4, height = 1,
                                                 command = lambda row=row, column=column: set_tile(row, column))
        Main_Board[row][column].grid(row=row+1, column=column) #shifting ecerything down by 1

button = tkinter.Button(frame, text = "Restart", font = ("Consolas", 20), background = BG_colour,
                        foreground = "white", command = New_Game)

button.grid(row=4, column=0, columnspan=3, sticky= "we")




frame.pack()

#to centre the window in the screen
Window.update()
Window_width = Window.winfo_width()   #this is the width for the widow
Window_height = Window.winfo_height() #this is the height for the window

screen_width = Window.winfo_screenwidth() #this is the width of the screen
screen_height = Window.winfo_screenheight() #this is the heiht of the screen

#the X and Y values to be calculated
window_X = int((screen_width/2) - (Window_width/2)) 
window_Y = int((screen_height/2) - (Window_height/2))

Window.geometry(f"{Window_width}x{Window_height}+{window_X}+{window_Y}")




Window.mainloop()#this will create a loop to keep the window open






















