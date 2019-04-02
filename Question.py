import Scanner
import Answer

class Question:


  def __init__(self, file_lines, scan, x):
    self.question_answers = []
    self.question_num = 1
    self.ID = 0;
    self.question = ""
    self.explaination = ""
    self.correct_answer = None

    #self.scan = scan
    self.questionNum = x
    print file_lines[scan.current()]

    while file_lines[scan.current()] == '':
      scan.iter()

    #splitting the input line
    temp_array = file_lines[scan.current()].split()
    self.ID = temp_array[0]

    for x in range(1, len(temp_array)):
      self.question += temp_array[x] + " "


    #getting a new line of fresh input
    scan.iter()
    while file_lines[scan.current()] == '' and scan.current() != len(file_lines):
      scan.iter()

    # gets the line with how many answers and the corrent answer and
    # splits the input line
    temp_array = file_lines[scan.current()].split()
    num_answers = int(temp_array[0].rstrip())
    correct_answer = int(temp_array[1].rstrip())

    scan.iter()

    for z in range(num_answers):
      temp = Answer.Answer(file_lines, scan, z)
      self.question_answers.append(temp)
      if (z+1) == correct_answer :
        temp.mark_correct()
        self.correct_answer = temp


    while file_lines[scan.current()] == '' and scan.current() != len(file_lines):
      scan.iter()

    temp_array = file_lines[scan.current()].split()
    num_explaination = int(temp_array[0])

    for x in range(num_explaination):
      scan.iter()
      while file_lines[scan.current()] == '' and scan.current() != len(file_lines):
        scan.iter()
      line = file_lines[scan.current()]
      self.explaination += line + "\n"

  def printQuestionInfo(self):
    print ("Question : " + self.question)
    print ("Possible Answers: ")
    for x in range (len(self.question_answers)):
      print ("    " +  self.question_answers[x].return_letter() + " " +self.question_answers[x].return_text())
    print ("Correct Answer : ")
    print ("    " +  self.correct_answer.return_letter() + " "+ self.correct_answer.return_text())
