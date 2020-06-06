#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

"""
Cell_base.py

This script modelise the behavior of the proteins inside the cell. 

"""

__authors__ = ("Benoit Aliaga")
__contact__ = ("aliaga.benoit@gmail.com")
__version__ = "0.1"
__date__ = "06/06/2020"

import math
from tkinter import *

#class Cell:
#    def __init__(self, length, width):
#        """
#           Initialisation d'un objet
#           Definition des attributs avec des valeurs par defauts.
#        """
#        self.x = length
#        self.y = width

#    def cell_area(self):
#        """
#           Methode qui calcule la surface de la cellule.
#        """
#        area = self.x * self.y
#        return area

#    def nuclear_(self):
#        """
#           Dessin d'un canvas
#        """

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

    def nuclear_area(self):
        pass
    
    def coordo(self):
        """
           Methode qui calcule les coordonnees de la proteine.
        """
        position = self.coordx + self.coordy
        return position

# Main section
if __name__ == "__main__":
    my_prot = Protein(2,1,4,5,10)
    print(my_prot)
    print(my_prot.init_position())
    
    #my_cell = Cell(2,1)
    #print("Width = ", my_cell.x, "Length = ", my_cell.y)
    #print("The cell area is:", my_cell.cell_area())
    #my_prot = Protein(4,6)
    #print("The coordinate of my protein is:", my_prot.prot_coord())

