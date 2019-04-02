class Scanner:
  index = 0
  
  def __init__(self):
    self.index = 0

  def iter(self):
    self.index += 1

  def reset(self):
    self.index = 0

  def current(self):
    return self.index
