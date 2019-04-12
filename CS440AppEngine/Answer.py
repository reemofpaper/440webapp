class Answer:

  def __init__(self, file_lines, scan, x):
    self.text = ""
    self.is_correct = False
    self.letter = chr( x + 65)

    while file_lines[scan.current()] == '' and scan.current() != len(file_lines):
      scan.iter()

    self.text += file_lines[scan.current()]
    scan.iter()

  def mark_correct(self):
    self.is_correct = True

  def is_correct_answer(self):
    return self.is_correct

  def return_text(self):
    return self.text

  def return_letter(self):
    return self.letter

  def get_answer_dictionary(self):
      # add all the things here
      return {'letter': self.letter, 'answer_text' : self.text}
