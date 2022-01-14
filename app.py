from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Learn to play Go"

@app.route("/about")
def about():
  return "This is a tiny little website that I'm creating in order to get familiar with Flask!"

@app.route("/<other>")
def catchall(other):
  return "Sorry, there isn't any page named {}!".format(other)

if __name__ == "__main__":
  app.run(port=5000, debug=True)