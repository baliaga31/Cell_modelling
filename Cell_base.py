#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

"""
Cell_base.py

This script modelise the behavior of the proteins inside the cell. 

"""

__authors__ = ("Benoit Aliaga")
__contact__ = ("aliaga.benoit@gmail.com")
__version__ = "0.1"
__date__ = "09/06/2020"

import math
from tkinter import *

class Cell:
    def __init__(self, length, width):
        """
           Initialisation d'un objet
           Definition des attributs avec des valeurs par defauts.
        """
        self.length = length 
        self.width = width

    def cell_size(self):
        """
           Give the cell size.
        """
        print("The cell has a {} length and {} width.".format(self.length, self.width))
        
    def cell_area(self):
        """
           This method give you the area of the cell.
        """
        area = self.length * self.width
        return area

class Nuclear():
    def __init(self):
        pass

class Protein():
    def __init__(self, pos_x, pos_y, vx, vy, mw):
        """
           Classe qui defini une proteine
        """
        self.coord_x = pos_x
        self.coord_y = pos_y
        self.vx = vx
        self.vy = vy
        self.mw = mw

    def init_position(self):
        """
           Position of the protein
        """
        return("The cell coordinates are: x = {} and y = {}".format(self.coord_x, self.coord_y)) 
    
    def coordo(self):
        """
           Methode qui calcule les coordonnees de la proteine.
        """
        position = self.coordx + self.coordy
        return position

def deplacement():
    global dx, dy
    canvas.move(my_prot, dx, dy)
    root.after(500, deplacement)

dx = 10
dy = 0
 
# Main section
if __name__ == "__main__":
    my_cell = Cell(500,100)
    my_cell.cell_size()
    my_protein = Protein(300, 100, 4, 5, 6)
    
    print("We will open the canvas.")
    root = Tk()
    canvas = Canvas(root, width = 800, height = 400, background = "white")
    canvas.pack(padx = 10, pady = 10)

    Quit_button = Button(root, text = "Quit Cell Modelling", command = root.destroy)
    Quit_button.pack()
    
    canvas.create_rectangle(10, 10, 10 + my_cell.length, 10 + my_cell.width, fill = "white", width = 3, outline = "black") # create a cell in Tkinter

    my_prot = canvas.create_oval(20, 20, 30, 30, width = 1, fill = "grey")

    deplacement()
    
    root.mainloop()

#    my_prot = Protein(2,1,4,5,10)
#    print(my_prot.init_position())
    
#    my_cell = Cell(2,1)
#    print("The cell area is:", my_cell.cell_area())
