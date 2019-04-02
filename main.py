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

class MainPage(webapp2.RequestHandler):
  def get(self):
    values = {"name":"Siham"}
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.headers['Content-Type'] = 'text/html'
    self.response.write(template.render(values))

class UploadHandler(webapp2.RequestHandler):
  def post(self):
    # this is where you need to write your game stuff
    print("User entered: " )
    print(self.request.get('game_data'))

    # the game returns a list of all the questions once it has finished parsing
    all_questions = Game.create(self.request.get('game_data'))
    print(all_questions)

app = webapp2.WSGIApplication([
  ('/upload', UploadHandler),
  ('/', MainPage),
], debug=True)
