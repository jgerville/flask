from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1>heyyyyy</h1>"

@app.route("/<my_name>")
def greet(my_name):
  return "<h2>sup {}</h2>".format(my_name)

if __name__ == "__main__":
  app.run(port=5000, debug=True)