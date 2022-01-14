from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>heyyyyy</h1>"

@app.route("/<my_name>")
def greet(my_name):
  return "<h2>{}, did you know about the recursion joke?</h2>".format(my_name) * 20

@app.route("/test")
def figure_out():
  return "do we get this or the dynamic route?"

if __name__ == "__main__":
  app.run(port=5000, debug=True)