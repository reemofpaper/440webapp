import webapp2
import jinja2
import os
import Game

# we will iterate through this as
all_questions = []

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

def getQuestionDictionaryList(questions):
  local_questions = []
  for q in questions:
    local_questions.append(q.getQuestionDictionary())
  return local_questions

class MainPage(webapp2.RequestHandler):
  def get(self):
    values = {"name":"Siham"}
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.headers['Content-Type'] = 'text/html'
    self.response.write(template.render(values))

class UploadHandler(webapp2.RequestHandler):
  def post(self):
    global current_question
    global all_questions
    # this is where you need to write your game stuff
    print("User entered: " )
    print(self.request.get('game_data'))

    # the game returns a list of all the questions once it has finished parsing
    all_questions = []

    try:
      all_questions = Game.create(self.request.get('game_data'))
    except Exception as e:
      all_questions = Game.create(self.request.get('game_data'))
      template = JINJA_ENVIRONMENT.get_template('error.html')
      print(e)
      self.response.headers['Content-Type'] = 'text/html'
      self.response.write(template.render())
      return

    print(all_questions)

    template = JINJA_ENVIRONMENT.get_template('questions.html')
    values = {
      'question' : getQuestionDictionaryList(all_questions)[0],
      'num_wrong' : 0
    }
    self.response.write(template.render(values))

# inheriting from the request handler class
class QuestionAnswerHandler(webapp2.RequestHandler):
  def post(self):
    global all_questions
    current_question = int(self.request.get('current_question'))
    num_wrong = int(self.request.get('num_wrong'))

    print("current_question is " + str(current_question))
    #html page after we gather all the questions.
    answer = self.request.get('answer')
    print("The user entered " + answer)

    # do checking to see if thats not over bounds
    if(current_question <= 0 or current_question > len(all_questions)):
      # return the error page template
      return

    intro = ""
    text = "You defeated the zombie! Congratulations! Try some harder questions next time."

    # do checking to see if thats correct
    if all_questions[current_question-1].checkAnswer(answer):
      intro = "Woot we got the right answer!, onto the next question"
    else:
      num_wrong += 1
      if(num_wrong >= 4):
        text = "You got all the questions wrong and now you lost! The zombie will now eat your brain! Come back and try again!"
        print("all are wrong")
        # return you're done page
        template = JINJA_ENVIRONMENT.get_template('end_page.html')
        self.response.write(template.render({
          'message' : text,
          'num_wrong' : num_wrong,
          'total': current_question,
          'img_url': "/zombieparts/zombie" + str(num_wrong) + ".png"
        }))
        return
      else:
        intro = "wrong, try another question. You have " + str(num_wrong) + " wrong questions"

    # go to the next question - current_question is already off by 1 because the
    # form counting starts at 1
    next_question = current_question
    text = "You defeated the zombie! Congratulations! Try some harder questions next time."
    
    if(next_question >= len(all_questions)):
      # return you're done page
      template = JINJA_ENVIRONMENT.get_template('end_page.html')
      self.response.write(template.render({
        'message' : text,
        'num_wrong' : num_wrong,
        'total': len(all_questions),
        'img_url': "/zombieparts/zombie" + str(num_wrong) + ".png"
      }))
      return

    template = JINJA_ENVIRONMENT.get_template('questions.html')
    values = {
      'intro' : intro,
      'question' : getQuestionDictionaryList(all_questions)[next_question],
      'num_wrong' : num_wrong,
      'img_url': "/zombieparts/zombie" + str(num_wrong) + ".png"
    }
    self.response.write(template.render(values))

app = webapp2.WSGIApplication([
  ('/checkAnswer', QuestionAnswerHandler),
  ('/upload', UploadHandler),
  ('/', MainPage),
], debug=True)
