# author: Jaisuraj Kaleeswaran
# date: March 17, 2023
# file: game.py creates a GUI for the fifteen puzzle game
# input: A number that is clickable on the puzzle board
# output: The game fifteen on a GUI that operates by the user inputs 

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen

def shuffle():  # shuffle the tiles
    tiles.shuffle()
    clickButton(i)

def clickButton(i): #Makes the buttons on the Fifteen puzzle GUI clickable
    
    #Update the tiles so that they won't stay in order all the time
    tiles.update(tiles.tiles[i])
    fifteen = 15
    for x in range(fifteen + 1):
        if tiles.tiles[x] != 0: #If a tile value is not 0
            buttons[x].config(text = tiles.tiles[x])
        else: #If a tile value is 0
            buttons[x].config(text = " ")
            
    if tiles.is_solved():  #If the game finishes
        
        #Green symbolizes that the game is a success
        gui.tk_setPalette(background = "green") 
        text.config(foreground = "black", text = "You solved it!")
        
        for x in range(fifteen + 1): #Update text for each button
            buttons[x].config(foreground = "black") 
    else: #If the game continues
        for x in range(fifteen + 1): #Update text for each button
            buttons[x].config(foreground = "black")  
    click_shf.config(foreground = "black", text = "Shuffle") #Update Shuffle text

if __name__ == '__main__':
    fifteen = 15
    # make tiles
    tiles = Fifteen()
    
    # make a window
    gui = Tk()
    gui.title("Fifteen")
    puzzle = Entry(gui)
    puzzle.grid(columnspan=4)
    
    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')
    # make buttons
    buttons = []
    for i in range(fifteen + 1):
        name = str(i)
        # set text to a space if the tile is 0
        if tiles.tiles[i] == 0:
            textvariable = ' '
        else: # else set text to the tile number 
            textvariable = str(tiles.tiles[i]) 
        # make buttons
        button=(Button(gui, text=textvariable, name=name, font=font, height=3, width=5, command=lambda i=i: clickButton(i)))
        
        # use .grid() or .pack() methods
        button.grid(row=i//4, column=i%4)
        button.configure(bg='black')
        
         # the key argument name is used to identify the button
        gui.nametowidget(button.winfo_name()).grid(row=i//4, column=i%4)
        # add buttons to the window
        buttons.append(button)
        
    click_shf = Button(gui, text='Shuffle', font=font, height=3, command=lambda: shuffle())  # make a button to shuffle the tiles
    click_shf.grid(row=4, columnspan=4)  # place the button
    text = Label(gui, text="Click 'Shuffle' to create a new puzzle. Click on the numbers to move them.")
    text.grid(row=5, columnspan=4)
    # update the window
    gui.mainloop()