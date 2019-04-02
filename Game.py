import Scanner
import Question

def create(game_data):
    allQuestions = []
    scan = Scanner.Scanner()

    # storing each line in the file into an array
    # and stripping away newline at the end
    file_lines = []
    for line in game_data.split("\n"):
      file_lines.append(line.rstrip())

	# removing all the comments from the testfile
    for x in range(len(file_lines)):
      file_lines[x] = file_lines[x].split("//", 1)[0]

    print (file_lines)
    scan.reset()

    while file_lines[scan.current()] == '' and scan.current() != len(file_lines):
      scan.iter()
    print (scan.current())

    game_info = file_lines[scan.current()].split()
    game_version = game_info[1]
    name_length = len(game_info) - 2
    game_name = "";
    for x in range(2, len(game_info)):
      game_name += game_info[x] + " "

    # checking out the information to make sure its right
    print ("Game Version : " + game_version)
    print ("Game Name: " + game_name)

    scan.iter()
    while file_lines[scan.current()] == '' and scan.current() != len(file_lines):
      scan.iter()

    # splitting the input into a new array
    temp_line = file_lines[scan.current()].split()
    if temp_line[0].upper() != "QUESTIONS" :
      print ("This file does not follow the required formatting rules. Please try again with an input that does.")
      return 0
    num_questions = int(temp_line[1])
    print ("There are " + str(num_questions) + " questions")

    for x in range(num_questions) :
      scan.iter()
      temp = Question.Question(file_lines, scan, (x+1))
      allQuestions.append(temp)

    for x in range(len(allQuestions)) :
      allQuestions[x].printQuestionInfo()

    return allQuestions
