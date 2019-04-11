import Scanner
import Answer

class Question:
  def getAnswersAsList(self):
    # convert list of answers to list of dictionaries
    local_answers = []
    for a, val in self.question_answers.items():
      local_answers.append(val.get_answer_dictionary())
    return local_answers

  def __init__(self, file_lines, scan, x):
    self.question_answers = {}
    self.question_num = x
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
      self.question_answers[temp.letter] = temp
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
    print ("Question Num : " + str(self.question_num))
    print ("Possible Answers: ")
    for x, val in self.question_answers.items():
      print ("    " +  val.return_letter() + " " + val.return_text())
    print ("Correct Answer : ")
    print ("    " +  self.correct_answer.return_letter() + " "+ self.correct_answer.return_text())

  def checkAnswer(self, answer):
    if answer in self.question_answers:
      return self.question_answers[answer].is_correct_answer()
    else:
      return False
  def getQuestionDictionary(self):
      return {
        'id' : self.ID,
        'questionNum': self.question_num,
        'question': self.question,
        'answers' : self.getAnswersAsList()
      }
