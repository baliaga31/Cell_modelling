#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

"""
Cell_base_simple.py

The aim of this script is the same than Cell_base.py. However, this script is not written in object oriented.
"""

from tkinter import *

def deplacement():
    global dx, dy
    if cell.coords(prot)[2]>500:
        dx = -1*dx
    # On deplace la balle :
    cell.move(prot, dx, dy)
    # On repete cette fonction
    root.after(1000,deplacement)

def cell():
    cell = canvas_create_
    
# Coordinate of the cell:

Pos_X = 60
Pos_Y = 10
dx = 10
dy = 0

# Create a windows and a canvas.

root = Tk()
cell = Canvas(root, width = 500, height = 400, background = "white")
cell.pack(padx = 10, pady = 10)

# Create a button "Quit".

Bouton_Quitter = Button(root, text ='Quitter', command = root.destroy)

# Add the button in the windows tk:

Bouton_Quitter.pack()

# On cree une balle:

prot = cell.create_oval(Pos_X, Pos_Y, Pos_X+20, Pos_Y+20, fill = 'red')

deplacement()

# Launch the loop for the window

root.mainloop()
