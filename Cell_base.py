#!/usr/bin/python3

"""
Cell_base.py Version 1
Script qui va modeliser la diffusion d'une proteine dans une cellule
Benoît Aliaga, 2019
"""

class Cell:
    def __init__(self):
        """
        Test
        """
        self.x = 5
        self.y = 10

    def cell_area(self):
        area = self.x * self.y
        return area


# Main section
if __name__ == "__main__":
    my_cell = Cell()
    print("x = ", my_cell.x, "y = ", my_cell.y)
    dir(my_cell)
    my_cell.__doc__
    #print(my_cell.area())
