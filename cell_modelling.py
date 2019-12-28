class Cell():
  def __init__(self, x, y):
    self.x = 5 
    self.y = 10
    self.xnuc = None
    self.ynuc = None


  def get_nuclear(self):
#    if self.xnuc is None or self.ynuc is None:
#      raise Exception("You should have called obj.nuclear to set nuc value before trying to get Them.")
    return (self.xnuc, self.ynuc)

  def set_nuclear(self, x, y):
    self.xnuc = x
    self.ynuc = y

  def cell_area(self, x, y):
    self_area = x * y 
    return self_area

class Protein():
  def __init__(self):
    pass

class Diffusion():
  def __init__(self):
    pass

