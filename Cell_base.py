#!/usr/bin/python3

"""
Cell_base.py Version 1
Script qui va modeliser la diffusion d'une proteine dans une cellule
Benoît Aliaga, 2019
"""

class Cell:
    def __init__(self, length, width):
        """
        Test
        """
        self.x = width
        self.y = length

    def cell_area(self):
        area = self.x * self.y
        return area

# Main section
if __name__ == "__main__":
    my_cell = Cell(2,1)
    print("x = ", my_cell.x, "y = ", my_cell.y)
    print(my_cell.cell_area())
